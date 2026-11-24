---
title: "Design and development of a news bulletin automatic generation system based on large models"
excerpt: "The system automatically crawls web pages related to the power grid every day, and after extraction and filtering by a large model, generates a daily HTML briefing report, which is sent out on DingTalk.<br/><img src='/sooophia520/images/generation system.png'>"
collection: portfolio
---

## Project background

Power-grid news arrives every day from a wide range of outlets, and analysts used to spend the first hour of each morning scanning sources by hand to assemble an industry briefing. The goal was to automate that routine: crawl the relevant pages on a fixed schedule, let a large model extract and filter what mattered, and publish one daily HTML report that the team could read in a single page.

## What I did

- **Requirements.** Gathered and consolidated business requirements, turning how analysts actually read the briefing into the sections, filters and daily cadence the system had to support.
- **Sample material.** Collected and curated industry brief-news samples that became the reference output for the model pipeline and the basis for judging whether a generated issue was good.
- **Technical research.** Researched large language model documentation on extraction, filtering and summarisation to support design decisions.
- **Feature development.** Defined the functional specifications for part of the system and implemented those functions, from the agreed design through to working features.
- **Testing and documentation.** Organised test materials and proofread the project documents.

## Outcome

Each issue is generated automatically and published as a single HTML page: around 35 items grouped into thematic sections, a keyword summary of the day, and key figures pulled from the source articles. Every item links straight through to its original article, so a reader can open the full source from the briefing instead of searching for it again. The briefing is pushed to DingTalk, so the morning scan is replaced by reading one page.

![Daily briefing page](/sooophia520/images/generation system.png)
