# founder-skill

Skills from [Jakeschincariol/founder-skill](https://github.com/Jakeschincariol/founder-skill) at commit [`fd9385b`](https://github.com/Jakeschincariol/founder-skill/tree/fd9385b0cfe1b96bebce3898fbd506d73eff5a9d), copied into SOYL Hub on 2026-10-29. Licence: MIT.

> Eleven free Claude skills that test a business before you launch it: a board trained on Hormozi, Thiel and Jobs, a marketing director, a CFO, and a consumer panel of 100 buyer agents. Free, MIT.

All credit goes to the authors of Jakeschincariol/founder-skill. Each folder is the upstream skill unchanged, with its licence file added when it had none; build caches and plugin manifests are left out.

| Skill | What it does | Licence |
|---|---|---|
| [founder-board](founder-board/) | Your board of directors. Puts a business idea in front of a three-member board, each a sub-agent reading the idea through one published framework: the Offers lens (from… | MIT |
| [founder-brand](founder-brand/) | Your brand designer. Names the business (with the trademark, domain and handle checks to run before falling in love with a name), writes the voice, a one-line promise… | MIT |
| [founder-cfo](founder-cfo/) | Your CFO. Builds the unit economics of a business before money is spent: what one unit earns after its direct costs, the real profit margin at the planned volume, the… | MIT |
| [founder-competitors](founder-competitors/) | Maps every competitor and the gap they leave. Finds the direct competitors, indirect ones and the substitutes a buyer would use instead, from public sources only, and… | MIT |
| [founder-consumer](founder-consumer/) | The consumer panel. Spins up a swarm of buyer sub-agents (default 100, --quick for 20) trained on the user's target customer, each with a different income, age, buying… | MIT |
| [founder-launch](founder-launch/) | Your launch lead. Builds a dated, step-by-step launch plan: a cheap real-world test first (a waitlist, a pre-sale or a pop-up with a real price, so real buyers confirm… | MIT |
| [founder-marketing](founder-marketing/) | Your marketing director. Turns the buyer panel and the competitor map into positioning, the channels the target customer actually uses, a 30-day launch campaign with… | MIT |
| [founder-offer](founder-offer/) | Builds an offer too good to refuse. Lists every problem the buyer hits on the way to the result they want, turns each into a solution, trims to what is cheap to deliver… | MIT |
| [founder-ops](founder-ops/) | Your operations manager. Works out how the business actually runs on day one: suppliers and what they cost, who works when, the step-by-step routines for opening… | MIT |
| [founder-plan](founder-plan/) | Your business planner. Compiles everything the other founder skills wrote (the board's verdict, the competitors, the buyer panel, pricing, the offer, the CFO's numbers… | MIT |
| [founder-pricing](founder-pricing/) | Finds the price buyers will actually pay. Reads the consumer panel's four price answers per buyer into a Van Westendorp price-sensitivity range (too cheap, a bargain… | MIT |

Install one with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/SOYL-AI/soyl-skills-hub/tree/main/skills/marketing-and-growth/founder-skill/founder-board -g -a claude-code
```

Back to [Marketing and growth](../../../catalog/marketing-and-growth.md)
