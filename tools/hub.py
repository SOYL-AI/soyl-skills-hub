"""SOYL Hub: mirror a skills archive into this repo, keep each skill's licence and credit, rebuild the catalog.

usage:
  python -I tools/hub.py sync [--archive DIR] [--only CATEGORY/REPO ...] [--push] [--message TEXT] [--no-github]
  python -I tools/hub.py catalog    rebuild CATALOG.md, catalog/ and the source READMEs from catalog/skills.json
  python -I tools/hub.py check      scan skills/ and the docs for keys, tokens and private details

The archive is a folder of <category>/<repo> clones. For every SKILL.md in it, sync either copies the skill
folder to skills/<category>/<repo>/<skill>/ (open-source licence, small enough, no compiled programs, nothing
that looks like a key) or lists it in the catalog with a link to its source. It never changes the archive.
Without --push it only changes files here, so look at `git status` first; with --push it commits and pushes.
The archive path comes from --archive, else $SOYL_HUB_ARCHIVE, else "archive" in hub.local.json, which is
never committed and can also hold "private_words": strings that must never be published.
Python 3.9+, standard library only. `gh` (GitHub CLI), when installed, adds repo descriptions and stars.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

HUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(HUB, "tools", "hub.json")
LOCAL_FILE = os.path.join(HUB, "hub.local.json")
INDEX_FILE = os.path.join(HUB, "catalog", "skills.json")
OVERRIDES_FILE = os.path.join(HUB, "tools", "licence-overrides.json")
EXCLUDE_FILE = os.path.join(HUB, "tools", "exclude.txt")
ALLOW_FILE = os.path.join(HUB, "tools", "check-allow.txt")
LICENCE_TEXTS = os.path.join(HUB, "tools", "licences")

# Folders never searched for skills (build output, dependencies, test fixtures).
DISCOVER_SKIP = {".git", "node_modules", "__pycache__", ".venv", "venv", ".next", ".turbo", ".cache", "dist",
                 "build", "tests", "test", "__tests__", "fixtures", "__fixtures__", "snapshots", "__snapshots__",
                 "testdata", "e2e"}
# Left out of every copy. Plugin manifests would make Claude Code load a copied skill a second time as a plugin.
COPY_SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", ".pytest_cache", ".next", ".turbo",
                  ".cache", ".claude-plugin", ".codex-plugin"}
COPY_SKIP_FILES = {".gitignore", ".gitattributes", ".gitmodules", ".DS_Store", "Thumbs.db", "desktop.ini"}
ENV_OK = {".env.example", ".env.sample", ".env.template", ".env.dist"}
BINARY_EXT = {".exe", ".dll", ".so", ".dylib", ".msi", ".bin", ".jar", ".class", ".pyd", ".o", ".a", ".lib",
              ".apk", ".dmg", ".pkg", ".deb", ".rpm", ".appimage", ".node", ".scr"}
TEXT_EXT = {".md", ".txt", ".py", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".json", ".yaml", ".yml", ".toml",
            ".sh", ".html", ".css", ".scss", ".xml", ".svg", ".csv", ".ini", ".cfg", ".conf", ".rb", ".go", ".rs",
            ".java", ".kt", ".swift", ".php", ".sql", ".r", ".lua", ".vue", ".svelte", ".astro", ".env", ".example",
            ".sample", ".template", ".tex", ".rst", ".ipynb", ".mdx", ".jsonl", ".lock", ""}
LICENSE_NAME = re.compile(r"^(licen[cs]e|copying|unlicen[cs]e)([-_.](mit|apache|apache-2\.0|bsd|isc|gpl|agpl|lgpl|"
                          r"mpl|cc0|cc-by[a-z0-9.-]*|enterprise|ee|commercial|docs|code))?(\.(md|txt|rst|markdown))?$",
                          re.I)
TRANSLATION = re.compile(r"(^|/)(translations?|i18n|locales?|[a-z]{2}-[A-Z]{2}|[a-z]{2}_[A-Z]{2}|zh|ja|ko|es|fr|de|"
                         r"pt|ru|it|tr|vi|ar|hi|id)(/|$)")
SECRET_PATTERNS = [
    ("AWS access key", r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    ("GitHub token", r"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{60,})\b"),
    ("Anthropic key", r"\bsk-ant-(?:api|admin)\d{2}-[A-Za-z0-9_\-]{60,}"),
    ("OpenAI key", r"\bsk-(?:proj-|svcacct-|admin-)?[A-Za-z0-9_\-]{20,}T3BlbkFJ[A-Za-z0-9_\-]{20,}|\bsk-proj-[A-Za-z0-9_\-]{60,}"),
    ("Google API key", r"\bAIza[0-9A-Za-z_\-]{35}\b"),
    ("Slack token", r"\bxox[baprs]-[0-9]{6,}-[A-Za-z0-9-]{10,}"),
    ("Slack webhook", r"https://hooks\.slack\.com/services/T[A-Z0-9]{6,}/B[A-Z0-9]{6,}/[A-Za-z0-9]{20,}"),
    ("Stripe live key", r"\b(?:sk|rk)_live_[0-9A-Za-z]{20,}"),
    ("Private key", r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP |ENCRYPTED )?PRIVATE KEY-----"),
    ("Hugging Face token", r"\bhf_[A-Za-z0-9]{34,}\b"),
    ("SendGrid key", r"\bSG\.[A-Za-z0-9_\-]{22}\.[A-Za-z0-9_\-]{43}\b"),
    ("npm token", r"\bnpm_[A-Za-z0-9]{36}\b"),
    ("Groq key", r"\bgsk_[A-Za-z0-9]{48,}\b"),
    ("Replicate token", r"\br8_[A-Za-z0-9]{37}\b"),
    ("Telegram bot token", r"\b\d{8,10}:AA[0-9A-Za-z_\-]{33}\b"),
]
PLACEHOLDER = re.compile(r"x{4,}|X{4,}|0{6,}|1234|abcd|your|example|dummy|fake|placeholder|redacted|sample|\.\.\.|<|\*{3,}", re.I)


# ── Small helpers ──────────────────────────────────────────────────────────────────────────────────────────────
def lp(path):
    """Extended-length path on Windows, so deep third-party trees don't hit the 260-character limit."""
    path = os.path.abspath(path)
    if os.name != "nt" or path.startswith("\\\\?\\"):
        return path
    return "\\\\?\\" + path


def read(path, limit=400000):
    try:
        with open(lp(path), encoding="utf-8", errors="replace") as f:
            return f.read(limit)
    except OSError:
        return ""


def load_json(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def write_text(path, text):
    os.makedirs(os.path.dirname(lp(path)), exist_ok=True)
    with open(lp(path), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def rel_posix(path, start):
    return os.path.relpath(path, start).replace("\\", "/")


def today():
    return datetime.date.today().isoformat()


def slug(text):
    s = re.sub(r"[^a-z0-9._-]+", "-", text.strip().lower()).strip("-.")
    return s or "skill"


def cell(text, limit=170):
    text = re.sub(r"\s+", " ", text or "").strip().replace("|", "\\|")
    text = re.sub(r"<", "&lt;", text)
    if len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0].rstrip(",.;:") + "…"
    return text


def frontmatter(text):
    m = re.match(r"^﻿?---\s*\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        return {}
    out, key = {}, None
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if km and not line.startswith((" ", "\t")):
            key = km.group(1).lower()
            val = km.group(2).strip()
            out[key] = "" if val in (">", "|", ">-", "|-", ">+", "|+") else val.strip("\"'")
        elif key and line.startswith((" ", "\t")):
            out[key] = (out[key] + " " + line.strip()).strip()
    return out


# ── Licences ───────────────────────────────────────────────────────────────────────────────────────────────────
# Each result is (licence id, kind): "ok" can be copied here, "link" is listed with a link to its source,
# "review" needs a person to decide (and is listed with a link until someone adds an override).
def classify_text(text):
    t = re.sub(r"\s+", " ", text.lower()).strip()
    if not t:
        return None
    head = t[:1500]
    if "polyform noncommercial" in t or "polyform-noncommercial" in t:
        return ("PolyForm-Noncommercial", "link")
    if "polyform" in head:
        return ("PolyForm", "link")
    if re.search(r"attribution-noncommercial|creativecommons\.org/licenses/by-nc|cc[ -]by[ -]nc|non-commercial use only|"
                 r"for non-commercial purposes only|noncommercial purposes only", t):
        return ("Non-commercial", "link")
    if "noderivatives" in t or "creativecommons.org/licenses/by-nd" in t:
        return ("CC-BY-ND", "link")
    if "business source license" in head:
        return ("BUSL", "link")
    if "elastic license" in head:
        return ("Elastic", "link")
    if "server side public license" in head:
        return ("SSPL", "link")
    if "commons clause" in t:
        return ("Commons-Clause", "review")
    if re.search(r"modified version of the (apache|mit)|with the following additional (conditions|terms)", head):
        return ("Modified licence", "review")
    if "gnu affero general public license" in head:
        return ("AGPL-3.0", "ok")
    if "gnu lesser general public license" in head or "gnu library general public license" in head:
        return ("LGPL", "ok")
    if "gnu general public license" in head:
        return ("GPL-3.0" if "version 3" in head else "GPL-2.0" if "version 2" in head else "GPL", "ok")
    if "mozilla public license" in head:
        return ("MPL-2.0", "ok")
    if "eclipse public license" in head:
        return ("EPL-2.0", "ok")
    if "european union public licen" in head:
        return ("EUPL-1.2", "ok")
    if "cc0" in t and ("creative commons" in t or "public domain" in t):
        return ("CC0-1.0", "ok")
    if "free and unencumbered software released into the public domain" in t:
        return ("Unlicense", "ok")
    if "attribution-sharealike" in t or "creativecommons.org/licenses/by-sa" in t:
        return ("CC-BY-SA-4.0", "ok")
    if "attribution 4.0 international" in t or "creativecommons.org/licenses/by/" in t:
        return ("CC-BY-4.0", "ok")
    # Permissive texts: when a file holds several (a project licence plus bundled components), the first one wins.
    marks = [
        ("MIT", t.find("permission is hereby granted, free of charge")),
        ("Apache-2.0", t.find("apache license") if ("version 2.0" in t or "license-2.0" in t) else -1),
        ("ISC", max(t.find("permission to use, copy, modify, and/or distribute this software for any purpose"),
                    t.find("permission to use, copy, modify, and distribute this software for any purpose"))),
        ("BSD", t.find("redistribution and use in source and binary forms")),
        ("BSL-1.0", t.find("boost software license")),
        ("Zlib", t.find("altered source versions must be plainly marked")),
        ("WTFPL", t.find("do what the fuck you want")),
        ("Artistic-2.0", t.find("artistic license")),
        ("PSF-2.0", t.find("python software foundation license")),
    ]
    marks = [(name, pos) for name, pos in marks if pos >= 0]
    if marks:
        name = min(marks, key=lambda m: m[1])[0]
        if name == "BSD":
            name = "BSD-3-Clause" if ("neither the name" in t or "endorse or promote" in t) else "BSD-2-Clause"
        return (name, "ok")
    if re.match(r"^(the )?mit license\b", t) or t == "mit":
        return ("MIT", "ok")
    if "all rights reserved" in t or "proprietary" in head:
        return ("Proprietary", "link")
    return ("Unknown", "review")


DECLARED = [
    (r"^mit(-0)?( license)?$", "MIT", "ok"), (r"^apache[- ]?(license[- ]?)?(v|version )?2(\.0)?$", "Apache-2.0", "ok"),
    (r"^bsd-?2(-clause)?$", "BSD-2-Clause", "ok"), (r"^bsd-?3(-clause)?$", "BSD-3-Clause", "ok"),
    (r"^isc$", "ISC", "ok"), (r"^0bsd$", "0BSD", "ok"), (r"^unlicen[cs]e$", "Unlicense", "ok"),
    (r"^cc0(-1\.0)?$", "CC0-1.0", "ok"), (r"^cc[- ]by[- ]4\.0$", "CC-BY-4.0", "ok"),
    (r"^cc[- ]by[- ]sa[- ]4\.0$", "CC-BY-SA-4.0", "ok"), (r"^mpl-?2\.0$", "MPL-2.0", "ok"),
    (r"^agpl-?3(\.0)?(-only|-or-later)?$", "AGPL-3.0", "ok"), (r"^lgpl-?[23](\.[01])?(-only|-or-later)?$", "LGPL", "ok"),
    (r"^gpl-?3(\.0)?(-only|-or-later)?$", "GPL-3.0", "ok"), (r"^gpl-?2(\.0)?(-only|-or-later)?$", "GPL-2.0", "ok"),
    (r"nc\b|non-?commercial", "Non-commercial", "link"), (r"proprietary|all rights reserved", "Proprietary", "link"),
    (r"elastic", "Elastic", "link"), (r"busl|business source", "BUSL", "link"),
]


def classify_declared(value):
    v = re.sub(r"\s+", " ", (value or "").strip().lower())
    if not v:
        return None
    for pat, ident, kind in DECLARED:
        if re.search(pat, v):
            return (ident, kind)
    return None


def licence_files(folder):
    try:
        names = os.listdir(lp(folder))
    except OSError:
        return []
    return sorted(n for n in names if LICENSE_NAME.match(n) and os.path.isfile(lp(os.path.join(folder, n))))


def classify_folder(folder):
    """The licence files in one folder, classified together: (id, kind, [file names]) or None."""
    files = licence_files(folder)
    results = [classify_text(read(os.path.join(folder, n))) for n in files]
    pairs = [(n, r) for n, r in zip(files, results) if r]
    if not pairs:
        return None
    kinds = {r[1] for _, r in pairs}
    ident = "+".join(sorted({r[0] for _, r in pairs}))
    kind = "link" if "link" in kinds else "review" if "review" in kinds else "ok"
    return (ident, kind, [n for n, _ in pairs])


def manifest_licence(repo):
    pkg = read(os.path.join(repo, "package.json"), 100000)
    if pkg:
        try:
            lic = json.loads(pkg).get("license")
            if isinstance(lic, str):
                return lic
        except ValueError:
            pass
    py = read(os.path.join(repo, "pyproject.toml"), 100000)
    m = re.search(r'^license\s*=\s*(?:\{\s*text\s*=\s*)?"([^"]+)"', py, re.M)
    return m.group(1) if m else ""


def find_override(overrides, source, rel, own_file):
    """The person's decision for this skill. One with a "path" names the skill and always applies; one for a whole
    source skips the paths in "except" and never overrules a licence file the skill carries itself."""
    for o in overrides:
        if o.get("source") != source:
            continue
        if o.get("path"):
            if rel == o["path"] or rel.startswith(o["path"].rstrip("/") + "/"):
                return o
        elif not own_file and not any((rel + "/").startswith(p) for p in o.get("except", [])):
            return o
    return None


# ── The archive ────────────────────────────────────────────────────────────────────────────────────────────────
def git_info(repo, non_git):
    cfg = read(os.path.join(repo, ".git", "config"), 20000)
    m = re.search(r'\[remote "origin"\][^\[]*?url\s*=\s*(\S+)', cfg, re.S)
    url = re.sub(r"\.git$", "", m.group(1)) if m else non_git.get(os.path.basename(repo), "")
    head = read(os.path.join(repo, ".git", "HEAD"), 1000).strip()
    branch, sha = "", ""
    if head.startswith("ref:"):
        ref = head[4:].strip()
        if ref.startswith("refs/heads/"):
            branch = ref[len("refs/heads/"):]
        sha = read(os.path.join(repo, ".git", *ref.split("/")), 200).strip()
        if not sha:
            for line in read(os.path.join(repo, ".git", "packed-refs")).splitlines():
                if line.endswith(" " + ref):
                    sha = line.split()[0]
    elif re.match(r"^[0-9a-f]{40}$", head):
        sha = head
    return url, branch, sha


def walk_files(folder):
    """Every file a copy of this skill folder would hold: (absolute path, path relative to the folder)."""
    for base, dirs, files in os.walk(lp(folder)):
        dirs[:] = sorted(d for d in dirs if d not in COPY_SKIP_DIRS)
        for name in sorted(files):
            if name in COPY_SKIP_FILES or name.endswith((".pyc", ".log")):
                continue
            if name.startswith(".env") and name not in ENV_OK:
                continue
            full = os.path.join(base, name)
            if os.path.islink(full):
                continue
            yield full, rel_posix(full, lp(folder))


def scan_text(path, rel, private_words, allow):
    """Secret-looking strings and private words in one file: a list of (rel, what, excerpt)."""
    ext = os.path.splitext(rel)[1].lower()
    if ext not in TEXT_EXT:
        return []
    try:
        if os.path.getsize(path) > 2_000_000:
            return []
    except OSError:
        return []
    text = read(path, 2_000_000)
    hits = []
    for what, pat in SECRET_PATTERNS:
        for m in re.finditer(pat, text):
            token = m.group(0)
            if PLACEHOLDER.search(token):
                continue
            hits.append((rel, what, token[:12] + "…"))
    low = text.lower()
    for word in private_words:
        w = word.lower()
        # Whole words only, so a short name doesn't fire inside a longer word that happens to contain it.
        pat = ("(?<![a-z0-9])" if w[:1].isalnum() else "") + re.escape(w) + ("(?![a-z0-9])" if w[-1:].isalnum() else "")
        if re.search(pat, low):
            hits.append((rel, "private word", word))
    return [h for h in hits if f"{h[0]}|{h[1]}" not in allow]


def skill_record(repo, source, folder, overrides, mlic):
    text = read(os.path.join(folder, "SKILL.md"))
    fm = frontmatter(text)
    rel = rel_posix(folder, repo)
    rel = "." if rel in ("", ".") else rel
    name = (fm.get("name") or os.path.basename(folder)).strip()
    desc = re.sub(r"\s+", " ", fm.get("description", "")).strip()
    declared = fm.get("license", "")
    # Licence: the skill's own file, then its frontmatter, then the nearest folder above it, then the repo's manifest.
    lic, origin, lic_dir, lic_files = None, "", None, []
    own = classify_folder(folder)
    if own:
        lic, origin, lic_dir, lic_files = (own[0], own[1]), "skill", rel, own[2]
    if not lic and declared:
        c = classify_declared(declared)
        if c:
            lic, origin = c, "frontmatter"
        elif re.search(r"licen[cs]e\.(txt|md)|complete terms", declared, re.I):
            lic, origin = ("Unknown", "review"), "frontmatter"
    if not lic:
        cur = os.path.dirname(folder)
        while os.path.normcase(cur).startswith(os.path.normcase(repo)):
            anc = classify_folder(cur)
            if anc:
                lic, origin, lic_dir, lic_files = (anc[0], anc[1]), "folder", rel_posix(cur, repo), anc[2]
                break
            if os.path.normcase(cur) == os.path.normcase(repo):
                break
            cur = os.path.dirname(cur)
    if not lic and mlic:
        c = classify_declared(mlic)
        if c:
            lic, origin = c, "manifest"
    if not lic:
        lic, origin = ("None", "link"), "none"
    # A person's decision in licence-overrides.json beats detection.
    o = find_override(overrides, source, rel, origin == "skill" and rel != ".")
    if o:
        lic, origin = (o["license"], o["kind"]), "override"
        if o.get("files"):
            lic_dir, lic_files = ".", o["files"]
    files, total, binaries = 0, 0, []
    for full, frel in walk_files(folder):
        try:
            total += os.path.getsize(full)
        except OSError:
            continue
        files += 1
        if os.path.splitext(frel)[1].lower() in BINARY_EXT:
            binaries.append(frel)
    if lic_dir == ".":
        lic_dir = ""
    return {
        "source": source, "upstream_path": rel, "name": name, "description": desc,
        "license": lic[0], "kind": lic[1], "license_from": origin,
        "license_dir": lic_dir, "license_files": lic_files,
        "bytes": total, "files": files, "binaries": binaries[:5],
        "hash": hashlib.sha1(re.sub(r"\s+", " ", text).strip().encode("utf-8", "replace")).hexdigest(),
        "translation": bool(TRANSLATION.search(rel)), "hidden": rel.startswith(".") or "/." in "/" + rel,
        "_folder": folder,
    }


def scan_archive(archive, settings, overrides, only=None):
    sources, skills = {}, []
    skip = set(settings["skip_top"])
    for cat in sorted(os.listdir(archive)):
        if cat.startswith(("_", ".")) or cat in skip or not os.path.isdir(os.path.join(archive, cat)):
            continue
        for repo_name in sorted(os.listdir(os.path.join(archive, cat)), key=str.lower):
            source = f"{cat}/{repo_name}"
            repo = os.path.join(archive, cat, repo_name)
            if not os.path.isdir(repo) or (only and source not in only):
                continue
            url, branch, sha = git_info(repo, settings["non_git_sources"])
            root = classify_folder(repo)
            mlic = manifest_licence(repo)
            sources[source] = {"category": cat, "repo": repo_name, "url": url, "branch": branch, "commit": sha,
                               "license": root[0] if root else (mlic or "None"), "skills": 0, "_path": repo}
            for base, dirs, files in os.walk(lp(repo)):
                dirs[:] = sorted(d for d in dirs if d not in DISCOVER_SKIP)
                if "SKILL.md" in files:
                    plain = base[4:] if base.startswith("\\\\?\\") else base
                    skills.append(skill_record(repo, source, plain, overrides, mlic))
    return sources, skills


# ── Deciding what to copy ──────────────────────────────────────────────────────────────────────────────────────
def public_reason(s, settings):
    lic, kind = s["license"], s["kind"]
    if kind == "ok":
        if s["bytes"] > settings["max_skill_mb"] * 1_000_000:
            return f"Too big to copy here ({s['bytes'] / 1e6:.0f} MB)"
        if s["binaries"]:
            return "Includes compiled programs"
        return ""
    if lic == "None":
        return "No licence"
    if lic in ("Non-commercial", "PolyForm-Noncommercial", "Custom non-commercial") or "non-commercial" in lic.lower():
        return "Non-commercial licence"
    if lic == "Proprietary":
        return "Proprietary licence"
    if kind == "link":
        return "Source-available licence"
    return "Licence unclear"


def decide(skills, settings, exclude, allow, private_words):
    for s in skills:
        s["reason"] = public_reason(s, settings)
        s["status"] = "mirrored" if not s["reason"] else "link"
        s["excluded"] = any(s["source"] == e or f"{s['source']}/{s['upstream_path']}".startswith(e + "/") or
                            f"{s['source']}/{s['upstream_path']}" == e for e in exclude)
    kept = [s for s in skills if not s["excluded"]]
    # One copy per name inside a source: translations and per-agent copies (.claude/, .agents/) give way.
    best = {}
    for s in kept:
        key = (s["source"], s["name"].lower())
        rank = (s["status"] != "mirrored", s["translation"], s["hidden"], s["upstream_path"].count("/"), s["upstream_path"])
        if key not in best or rank < best[key][0]:
            best[key] = (rank, s)
    kept = [s for _, s in best.values()]
    # The same SKILL.md in several sources: keep the original. Known originals (hub.json) come first; after them,
    # per-agent folders (.claude/, .agents/) and big collections usually hold copies. A copy's licence doesn't cover
    # what it copied, so an original we can only link to still wins over a copy we could mirror.
    originals = set(settings.get("originals", []))
    groups = {}
    for s in kept:
        groups.setdefault(s["hash"], []).append(s)
    kept = []
    for items in groups.values():
        items.sort(key=lambda s: (s["source"] not in originals, s["hidden"], s["source"].startswith("skill-collections/"),
                                  s["status"] != "mirrored", s["source"]))
        if len(items) > 1:
            items[0]["also_in"] = sorted({s["source"] for s in items[1:]} - {items[0]["source"]})
        kept.append(items[0])
    # Last gate before anything is copied: nothing that looks like a key or a private detail.
    hits = []
    for s in kept:
        if s["status"] != "mirrored":
            continue
        found = []
        for full, frel in walk_files(s["_folder"]):
            found += scan_text(full, f"{s['source']}/{s['upstream_path']}/{frel}".replace("/./", "/"), private_words, allow)
        if found:
            s["status"], s["reason"] = "link", "Held back for a check"
            hits += found
    return kept, hits


def assign_paths(skills):
    """skills/<category>/<repo>/<skill>/ for each copied skill; a skill inside another copied skill stays inside it."""
    by_source = {}
    for s in skills:
        by_source.setdefault(s["source"], []).append(s)
    for source, items in by_source.items():
        mirrored = sorted((s for s in items if s["status"] == "mirrored"), key=lambda s: s["upstream_path"].count("/"))
        used, placed = set(), []
        for s in mirrored:
            parent = next((p for p in placed if p["upstream_path"] == "." or
                           s["upstream_path"].startswith(p["upstream_path"] + "/")), None)
            if parent:
                inner = s["upstream_path"] if parent["upstream_path"] == "." else s["upstream_path"][len(parent["upstream_path"]) + 1:]
                s["hub_path"] = f"{parent['hub_path']}/{inner}"
                s["inside"] = parent["name"]
                continue
            # Folder names must not clash with each other or with the README and licence files beside them.
            base = slug(s["name"])
            name, n = base, 2
            while name in used or name == "readme.md" or LICENSE_NAME.match(name):
                name, n = f"{base}-{n}", n + 1
            used.add(name)
            s["hub_path"] = f"skills/{source}/{name}"
            placed.append(s)


# ── Copying ────────────────────────────────────────────────────────────────────────────────────────────────────
MIT_TEXT = """MIT License

Copyright (c) the authors of {project}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
ISC_TEXT = """ISC License

Copyright (c) the authors of {project}

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""


def declared_licence_text(ident, project, where):
    head = f"The authors of {project} declare this skill's licence as {ident} ({where}).\n\n"
    if ident == "MIT":
        return head + MIT_TEXT.format(project=project)
    if ident == "ISC":
        return head + ISC_TEXT.format(project=project)
    path = os.path.join(LICENCE_TEXTS, f"{ident}.txt")
    if os.path.isfile(path):
        return head + read(path)
    return head + f"Full text: https://spdx.org/licenses/{ident}.html\n"


def has_licence_file(folder):
    return bool(licence_files(folder))


def copy_tree(src, dst):
    os.makedirs(lp(dst), exist_ok=True)
    for full, frel in walk_files(src):
        target = os.path.join(dst, *frel.split("/"))
        os.makedirs(os.path.dirname(lp(target)), exist_ok=True)
        shutil.copyfile(full, lp(target))


def project_name(src):
    m = re.match(r"https://github\.com/([^/]+/[^/]+)", src.get("url", ""))
    return m.group(1) if m else src["repo"]


def build_source(source, src, skills, settings):
    """Rebuild skills/<category>/<repo>/ from the archive: every copied skill plus the licence files."""
    target = os.path.join(HUB, "skills", *source.split("/"))
    if os.path.isdir(lp(target)):
        shutil.rmtree(lp(target))
    copied = [s for s in skills if s["status"] == "mirrored" and "inside" not in s]
    if not copied:
        return
    repo = src["_path"]
    root_files = set()
    for s in copied:
        dst = os.path.join(HUB, *s["hub_path"].split("/"))
        copy_tree(s["_folder"], dst)
        if s["license_from"] == "override" and s["license_files"]:
            # The licence a person picked travels with the skill, next to any licence notes it already has.
            for name in s["license_files"]:
                if not os.path.exists(lp(os.path.join(dst, name))):
                    shutil.copyfile(lp(os.path.join(repo, name)), lp(os.path.join(dst, name)))
                root_files.add(name)
            continue
        if has_licence_file(dst):
            continue
        if s["license_files"] and s["license_dir"] is not None:
            for name in s["license_files"]:
                shutil.copyfile(lp(os.path.join(repo, *s["license_dir"].split("/"), name)) if s["license_dir"] else
                                lp(os.path.join(repo, name)), lp(os.path.join(dst, name)))
                if not s["license_dir"]:
                    root_files.add(name)
        else:
            where = {"frontmatter": "in SKILL.md", "manifest": "in the project's package manifest"}.get(s["license_from"], "upstream")
            write_text(os.path.join(dst, "LICENSE"), declared_licence_text(s["license"], project_name(src), where))
    for name in sorted(root_files):
        shutil.copyfile(lp(os.path.join(repo, name)), lp(os.path.join(target, name)))


# ── GitHub details (optional) ──────────────────────────────────────────────────────────────────────────────────
def github_details(url):
    m = re.match(r"https://github\.com/([^/]+/[^/]+?)/?$", url or "")
    if not m or not shutil.which("gh"):
        return {}
    try:
        out = subprocess.run(["gh", "api", f"repos/{m.group(1)}", "--jq",
                              "{full_name, description, stars: .stargazers_count, license: (.license.spdx_id // null), archived}"],
                             capture_output=True, text=True, encoding="utf-8", timeout=30, stdin=subprocess.DEVNULL)
        return json.loads(out.stdout) if out.returncode == 0 else {}
    except (OSError, ValueError, subprocess.TimeoutExpired):
        return {}


# ── Catalog ────────────────────────────────────────────────────────────────────────────────────────────────────
def tree_url(src, path):
    url = src.get("url", "")
    if not url.startswith("https://github.com/"):
        return url
    if path in (".", ""):
        return url
    return f"{url}/tree/{src.get('branch') or 'main'}/{path}"


def stars(n):
    if not n:
        return ""
    return f"★ {n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else f"★ {n}"


def source_line(src, n_here, n_link):
    bits = [f"[{project_name(src)}]({src['url']})" if src.get("url") else src["repo"]]
    if src.get("license") and src["license"] != "None":
        bits.append(src["license"])
    if src.get("stars"):
        bits.append(stars(src["stars"]))
    counts = []
    if n_here:
        counts.append(f"{n_here} here")
    if n_link:
        counts.append(f"{n_link} linked")
    bits.append(", ".join(counts))
    return " · ".join(bits)


def skill_rows(items, src, prefix):
    rows = ["| Skill | What it does |", "|---|---|"]
    for s in items:
        if s["status"] == "mirrored":
            link = f"[{cell(s['name'], 60)}]({prefix}{s['hub_path']}/)"
        else:
            link = f"[{cell(s['name'], 60)} ↗]({tree_url(src, s['upstream_path'])})"
        desc = cell(s["description"]) or "—"
        if s["status"] != "mirrored":
            desc += f" *({s['reason']}: install it from the source.)*"
        rows.append(f"| {link} | {desc} |")
    return "\n".join(rows)


def install_hint(prefix):
    return ("**To install a skill**, open it, copy the address from your browser and run "
            "`npx skills add <that address> -g -a claude-code`. "
            f"More ways in [How to install]({prefix}README.md#install-a-skill). "
            "Skills marked ↗ live in their own repos: install them from there.")


def write_catalog(index, settings):
    sources, skills = index["sources"], index["skills"]
    cats = settings["categories"]
    cat_title = {c["id"]: c["title"] for c in cats}
    by_cat = {}
    for s in skills:
        by_cat.setdefault(sources[s["source"]]["category"], {}).setdefault(s["source"], []).append(s)
    catalog_dir = os.path.join(HUB, "catalog")
    for old in os.listdir(catalog_dir) if os.path.isdir(catalog_dir) else []:
        if old.endswith(".md"):
            os.remove(os.path.join(catalog_dir, old))
    rows = []
    for c in cats:
        groups = by_cat.get(c["id"], {})
        if not groups:
            continue
        n_here = sum(1 for items in groups.values() for s in items if s["status"] == "mirrored")
        n_link = sum(1 for items in groups.values() for s in items if s["status"] != "mirrored")
        out = [f"# {c['title']}", "", c["blurb"], "",
               f"{n_here} skills here and {n_link} linked to their source, from {len(groups)} projects. "
               "[All categories](../CATALOG.md)", "", install_hint("../"), ""]
        for source in sorted(groups, key=lambda k: (-sum(1 for s in groups[k] if s["status"] == "mirrored"), k.lower())):
            items = sorted(groups[source], key=lambda s: (s["status"] != "mirrored", s["name"].lower()))
            src = sources[source]
            here = sum(1 for s in items if s["status"] == "mirrored")
            out += [f"## {src['repo']}", "", source_line(src, here, len(items) - here), ""]
            if src.get("description"):
                out += [cell(src["description"], 300), ""]
            if len(items) > settings["big_source"]:
                page = f"{c['id']}--{slug(src['repo'])}.md"
                write_text(os.path.join(catalog_dir, page),
                           "\n".join([f"# {src['repo']}", "", source_line(src, here, len(items) - here), "",
                                      f"Part of [{c['title']}]({c['id']}.md). " + install_hint("../"), "",
                                      skill_rows(items, src, "../"), ""]))
                out += [f"{len(items)} skills: see [the full list]({page}).", ""]
            else:
                out += [skill_rows(items, src, "../"), ""]
        write_text(os.path.join(catalog_dir, f"{c['id']}.md"), "\n".join(out))
        rows.append(f"| [{c['title']}](catalog/{c['id']}.md) | {n_here} | {n_link} | {c['blurb']} |")
    # Libraries, lists and apps from the archive that hold no skills.
    res = [f"# Libraries and resources", "", "Projects we keep next to the skills: libraries, lists and tools with no "
           "SKILL.md of their own. Each link goes to the project. [All categories](../CATALOG.md)", ""]
    n_res = 0
    for c in cats:
        items = sorted((s for s in sources.values() if s["category"] == c["id"] and not s.get("skills")),
                       key=lambda s: s["repo"].lower())
        if not items:
            continue
        res += [f"## {c['title']}", "", "| Project | What it is | Licence |", "|---|---|---|"]
        for s in items:
            name = f"[{s['repo']}]({s['url']})" if s.get("url") else s["repo"]
            res.append(f"| {name} | {cell(s.get('description', ''), 200) or '—'} | {s.get('license') if s.get('license') not in (None, 'None') else 'none'} |")
            n_res += 1
        res.append("")
    write_text(os.path.join(catalog_dir, "resources.md"), "\n".join(res))
    total_here = sum(1 for s in skills if s["status"] == "mirrored")
    total_link = len(skills) - total_here
    used_sources = len({s["source"] for s in skills})
    newest = sorted({s["added"] for s in skills}, reverse=True)
    out = ["# Catalog", "",
           f"{total_here} skills you can install from this repo, and {total_link} more listed with a link to "
           f"their source, from {used_sources} projects. Updated {index['updated']}.", "",
           "| Category | Here | Linked | What's in it |", "|---|---:|---:|---|"] + rows + [""]
    out += ["## Made by SOYL Academy", "",
            "| Skill | What it does |", "|---|---|",
            "| [soyl-academy-design](design-language/) | The SOYL Academy design language: calm, Apple-like pages "
            "with one typeface, one action colour and motion that only explains. |", ""]
    if len(newest) > 1:
        recent = [s for s in skills if s["added"] in newest[:3]]
        recent.sort(key=lambda s: (s["added"], s["source"], s["name"].lower()), reverse=True)
        out += ["## Newest", "", "| Skill | Category | Added |", "|---|---|---|"]
        for s in recent[:40]:
            src = sources[s["source"]]
            link = f"[{cell(s['name'], 60)}]({s['hub_path']}/)" if s["status"] == "mirrored" else \
                f"[{cell(s['name'], 60)} ↗]({tree_url(src, s['upstream_path'])})"
            out.append(f"| {link} | {cat_title.get(src['category'], src['category'])} | {s['added']} |")
        out.append("")
    out += ["## More", "",
            f"- [Libraries and resources](catalog/resources.md): {n_res} libraries, lists and tools that aren't skills.",
            "- [catalog/skills.json](catalog/skills.json): everything above as data.", ""]
    write_text(os.path.join(HUB, "CATALOG.md"), "\n".join(out))
    # Each source folder gets a README with credit, licence and its skills.
    for source, src in sources.items():
        items = sorted((s for s in skills if s["source"] == source and s["status"] == "mirrored" and "inside" not in s),
                       key=lambda s: s["name"].lower())
        if not items:
            continue
        cat = src["category"]
        commit = src.get("commit", "")
        when = f" at commit [`{commit[:7]}`]({src['url']}/tree/{commit})" if commit and src["url"].startswith("https://github.com/") else ""
        lines = [f"# {src['repo']}", "",
                 f"Skills from [{project_name(src)}]({src['url']}){when}, copied into SOYL Hub on {src.get('added', index['updated'])}. "
                 f"Licence: {src.get('license') or 'see each skill'}.", ""]
        if src.get("description"):
            lines += [f"> {cell(src['description'], 300)}", ""]
        lines += [f"All credit goes to the authors of {project_name(src)}. Each folder is the upstream skill unchanged, "
                  "with its licence file added when it had none; build caches and plugin manifests are left out.", "",
                  "| Skill | What it does | Licence |", "|---|---|---|"]
        for s in items:
            lines.append(f"| [{cell(s['name'], 60)}]({s['hub_path'].rsplit('/', 1)[1]}/) | {cell(s['description']) or '—'} | {s['license']} |")
        example = items[0]["hub_path"]
        lines += ["", "Install one with the [skills CLI](https://github.com/vercel-labs/skills):", "", "```bash",
                  f"npx skills add https://github.com/{settings['repo']}/tree/{settings['branch']}/{example} -g -a claude-code",
                  "```", "", f"Back to [{cat_title.get(cat, cat)}](../../../catalog/{cat}.md)", ""]
        write_text(os.path.join(HUB, "skills", *source.split("/"), "README.md"), "\n".join(lines))
    # The README's numbers.
    readme = os.path.join(HUB, "README.md")
    text = read(readme)
    stats = (f"<!-- stats -->**{total_here:,} skills** you can install from here, **{total_link:,} more** listed with a link "
             f"to their source, from **{used_sources} projects**. Updated {index['updated']}.<!-- /stats -->")
    if "<!-- stats -->" in text:
        write_text(readme, re.sub(r"<!-- stats -->.*?<!-- /stats -->", stats, text, flags=re.S))
    return total_here, total_link, used_sources


# ── Checks over what is about to be published ──────────────────────────────────────────────────────────────────
def check_tree(private_words, allow, roots=None):
    hits = []
    roots = roots or [HUB]
    for root in roots:
        for base, dirs, files in os.walk(lp(root)):
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
            for name in files:
                full = os.path.join(base, name)
                rel = rel_posix(full, lp(HUB))
                if rel == "hub.local.json":
                    continue
                hits += scan_text(full, rel, private_words, allow)
    return hits


# ── Git ────────────────────────────────────────────────────────────────────────────────────────────────────────
def git(*args, check=True):
    out = subprocess.run(["git", "-C", HUB, "-c", "core.longpaths=true", *args], capture_output=True, text=True,
                         encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
    if check and out.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed:\n{out.stderr.strip()}")
    return out.stdout


def publish(message):
    git("add", "-A")
    git("add", "-A", "-f", "--", "skills")
    if not git("status", "--porcelain").strip():
        print("Nothing changed: nothing to publish.")
        return
    git("commit", "-q", "-m", message)
    if not git("remote", check=False).strip():
        print("Committed. There is no remote yet, so nothing was pushed.")
        return
    git("push", "-q", "origin", "HEAD")
    print("Committed and pushed.")


# ── Commands ───────────────────────────────────────────────────────────────────────────────────────────────────
def settings_and_local():
    settings = load_json(CONFIG_FILE, None)
    if not settings:
        sys.exit(f"missing or broken {CONFIG_FILE}")
    local = load_json(LOCAL_FILE, {})
    return settings, local


def read_list(path):
    out = []
    for line in read(path).splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            out.append(line.rstrip("/"))
    return out


def cmd_sync(args):
    settings, local = settings_and_local()
    archive = args.archive or os.environ.get("SOYL_HUB_ARCHIVE") or local.get("archive")
    if not archive or not os.path.isdir(archive):
        sys.exit("Say where the archive is: --archive DIR, $SOYL_HUB_ARCHIVE, or \"archive\" in hub.local.json.")
    archive = os.path.abspath(archive)
    only = set(o.strip("/").replace("\\", "/") for o in args.only or [])
    overrides = load_json(OVERRIDES_FILE, [])
    exclude = read_list(EXCLUDE_FILE)
    allow = set(read_list(ALLOW_FILE))
    private_words = [w for w in local.get("private_words", []) if w.strip()]
    print(f"Scanning {'all of the archive' if not only else ', '.join(sorted(only))} ...")
    sources, found = scan_archive(archive, settings, overrides, only)
    if only and not sources:
        sys.exit(f"Not in the archive: {', '.join(sorted(only))} (use <category>/<repo> folder names)")
    kept, hits = decide(found, settings, exclude, allow, private_words)
    # A project left out in exclude.txt, or whose every skill is, isn't listed at all, not even as a resource.
    for key in [k for k in sources if k in exclude or (any(s["source"] == k for s in found) and
                                                       all(s["excluded"] for s in found if s["source"] == k))]:
        del sources[key]
    assign_paths(kept)
    index = load_json(INDEX_FILE, {"sources": {}, "skills": []})
    old_sources, old_skills = index.get("sources", {}), index.get("skills", [])
    stamp = today()
    old_added = {(s["source"], s["name"].lower()): s.get("added", stamp) for s in old_skills}
    for s in kept:
        s["added"] = old_added.get((s["source"], s["name"].lower()), stamp)
    # Descriptions and stars from GitHub, at most once a day per project.
    todo = [k for k in sources if not args.no_github and old_sources.get(k, {}).get("github_checked") != stamp]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        fetched = dict(zip(todo, pool.map(lambda k: github_details(sources[k]["url"]), todo)))
    for key, src in sources.items():
        src["skills"] = sum(1 for s in kept if s["source"] == key)
        prev = old_sources.get(key, {})
        src["added"] = prev.get("added", stamp)
        details = fetched.get(key, {})
        for field in ("description", "stars"):
            if details.get(field) is not None:
                src[field] = details[field]
            elif prev.get(field) is not None:
                src[field] = prev[field]
        # Link to where the project lives now (some have moved since they were cloned).
        if details.get("full_name"):
            src["url"] = f"https://github.com/{details['full_name']}"
        elif prev.get("url", "").startswith("https://github.com/"):
            src["url"] = prev["url"]
        if details.get("license") and src["license"] in ("None", "") and src["skills"]:
            print(f"  note: {key} has no licence in the archive copy, but GitHub now says {details['license']}. "
                  f"Update the archive copy (git pull) and sync again to copy its skills.")
        src["github_checked"] = stamp if details else prev.get("github_checked", "")
    # Rebuild the scanned sources' folders; with --only, everything else stays as it was.
    scanned = set(sources)
    gone = {k for k in old_sources if (k in only if only else True) and k not in sources}
    for key in gone | scanned:
        folder = os.path.join(HUB, "skills", *key.split("/"))
        if os.path.isdir(lp(folder)):
            shutil.rmtree(lp(folder))
    for key, src in sources.items():
        build_source(key, src, [s for s in kept if s["source"] == key], settings)
    new_sources = {k: v for k, v in old_sources.items() if k not in scanned and k not in gone}
    for key, src in sources.items():
        new_sources[key] = {k: v for k, v in src.items() if not k.startswith("_")}
    keep_old = [s for s in old_skills if s["source"] not in scanned and s["source"] not in gone]
    fields = ("name", "description", "source", "upstream_path", "status", "reason", "license", "hub_path", "inside",
              "added", "bytes")
    new_skills = keep_old + [{k: s[k] for k in fields if k in s} for s in kept]
    new_skills.sort(key=lambda s: (s["source"].lower(), s["name"].lower()))
    for s in new_skills:
        if s["status"] != "mirrored":
            s.pop("hub_path", None)
    index = {"updated": stamp, "hub": settings["repo"], "sources": dict(sorted(new_sources.items())), "skills": new_skills}
    write_text(INDEX_FILE, json.dumps(index, indent=1, ensure_ascii=False) + "\n")
    here, linked, n_src = write_catalog(index, settings)
    # What changed, for the person and the commit message.
    before = {(s["source"], s["name"].lower(), s["status"]) for s in old_skills if s["source"] in scanned or not only}
    after = {(s["source"], s["name"].lower(), s["status"]) for s in new_skills if s["source"] in scanned or not only}
    added = sorted({(k[0], k[1]) for k in after - before if k[2] == "mirrored"})
    removed = sorted({(k[0], k[1]) for k in before - after if k[2] == "mirrored"})
    print(f"Catalog: {here} skills here, {linked} linked, {n_src} projects.")
    print(f"This run: {len(added)} copied in, {len(removed)} taken out.")
    for src_key, name in added[:30]:
        print(f"  + {name}  ({src_key})")
    if len(added) > 30:
        print(f"  ... and {len(added) - 30} more")
    for src_key, name in removed[:30]:
        print(f"  - {name}  ({src_key})")
    if hits:
        print(f"\nHeld back {len({h[0].rsplit('/', 1)[0] for h in hits})} skill(s) for a check. Look at these lines; if one is harmless, "
              "add '<path>|<what>' to tools/check-allow.txt and sync again:")
        for rel, what, excerpt in hits[:40]:
            print(f"  {what}: {rel} ({excerpt})")
    problems = check_tree(private_words, allow, [os.path.join(HUB, p) for p in ("README.md", "CATALOG.md", "CONTRIBUTING.md", "catalog", "design-language", "tools")])
    if problems:
        print("\nThe docs mention something private. Fix these before publishing:")
        for rel, what, excerpt in problems:
            print(f"  {what}: {rel} ({excerpt})")
        if args.push:
            sys.exit("Not pushed.")
    if args.push:
        if args.message:
            message = args.message
        elif only and len(added) and not removed:
            names = ", ".join(n for _, n in added[:3]) + (" and more" if len(added) > 3 else "")
            message = f"Add {names} ({', '.join(project_name(sources[k]) for k in sorted(only) if k in sources)})"
        elif only:
            message = f"Update {', '.join(project_name(sources[k]) for k in sorted(only) if k in sources)}"
        else:
            message = f"Sync from the archive: {here} skills here, {linked} linked ({len(added)} in, {len(removed)} out)"
        publish(message)
    else:
        print("\nDry run: files here changed, nothing committed. Check `git status`, then run again with --push.")


def cmd_catalog(args):
    settings, _ = settings_and_local()
    index = load_json(INDEX_FILE, None)
    if not index:
        sys.exit("No catalog/skills.json yet: run sync first.")
    here, linked, n_src = write_catalog(index, settings)
    print(f"Catalog: {here} skills here, {linked} linked, {n_src} projects.")


def cmd_check(args):
    _, local = settings_and_local()
    hits = check_tree([w for w in local.get("private_words", []) if w.strip()], set(read_list(ALLOW_FILE)))
    for rel, what, excerpt in hits:
        print(f"{what}: {rel} ({excerpt})")
    print(f"{len(hits)} finding(s).")
    sys.exit(1 if hits else 0)


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(description="SOYL Hub: mirror the skills archive and rebuild the catalog.")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sync", help="copy skills in from the archive and rebuild the catalog")
    s.add_argument("--archive", help="the archive folder (holds <category>/<repo> clones)")
    s.add_argument("--only", nargs="+", metavar="CATEGORY/REPO", help="sync just these archive folders")
    s.add_argument("--push", action="store_true", help="commit and push when done")
    s.add_argument("--message", help="commit message to use with --push")
    s.add_argument("--no-github", action="store_true", help="don't ask GitHub for descriptions and stars")
    sub.add_parser("catalog", help="rebuild the catalog pages from catalog/skills.json")
    sub.add_parser("check", help="scan everything for keys and private details")
    args = p.parse_args()
    {"sync": cmd_sync, "catalog": cmd_catalog, "check": cmd_check}[args.cmd](args)


if __name__ == "__main__":
    main()
