# Playbook / SOP: AI-Powered SEO Content Production for B2B SaaS

**Author:** Marcos Dodds  
**Topic:** AI-Powered SEO Content Production  
**Repository:** [100Hires-Junior-Marketing-Growth](https://github.com/Kitosdodds/100Hires-Junior-Marketing-Growth)  
**Date:** August 2026

---

## Overview

This playbook is a step-by-step operating procedure for producing SEO content using AI tools, designed for a small B2B SaaS marketing team (1–3 people). It draws on research from 10 practitioners who actively build, ship, and measure AI-assisted content systems.

The goal is not to replace human judgment but to compress the most time-consuming parts of content production — research, outlining, drafting — into a repeatable, AI-assisted workflow while keeping editorial quality high.

---

## Phase 1: Topic Selection and Keyword Research

**Step 1: Identify content gaps using SEO tools, not guesses.**

Use an SEO platform (Ahrefs, Semrush, or Clearscope) to run a content gap analysis: compare your domain against 3–5 direct competitors and export keywords they rank for that you don't. Prioritize keywords with clear commercial or mid-funnel intent over top-of-funnel informational queries.  
*(Source: Ryan Law, "How I Do Content Engineering with Claude Code," ahrefs.com/blog, 28.04.2026)*

**Step 2: Validate keyword viability by checking the SERP.**

Before producing content on any keyword, manually review the top 5 results. Ask: is the dominant intent informational or transactional? Can a new article realistically compete, or is the SERP dominated by aggregators and platforms? If the answer comes up in an AI Overview with no click incentive, deprioritize it.  
*(Source: Kevin Indig, "State of AI Search Optimization 2026," growth-memo.com, 09.02.2026)*

**Step 3: Prioritize middle-of-funnel content.**

Top-of-funnel keywords (e.g., "what is an ATS") are increasingly answered by AI directly, reducing click-through. Focus instead on comparison, use-case, and workflow content where users still need depth — for example, "best ATS for small recruiting teams" or "how to automate candidate screening."  
*(Source: Eli Schwartz, "How to do SEO right in 2025," GTMnow newsletter, 2025; also: SearchPilot webinar, "SEO's New Playbook," 23.05.2025)*

---

## Phase 2: Building an AI Content Workflow

**Step 4: Break your editorial process into discrete skill files.**

Document each step of your content creation process as a separate instruction file (Markdown format) that an LLM can follow. Ryan Law uses 23 skill files for the Ahrefs blog covering: topic analysis, briefing, structural outlining, drafting, product mentions, line editing, internal linking, and metadata creation. Each skill can run independently or be chained into a single pipeline.  
*(Source: Ryan Law, "How I Do Content Engineering with Claude Code," ahrefs.com/blog, 28.04.2026)*

**Step 5: Chain skills into an end-to-end pipeline.**

Use an agentic coding tool (Claude Code, Cursor with Claude, or OpenAI Codex) to trigger skill files sequentially. Ryan Law's pipeline runs from keyword to publish-ready draft in 6–12 minutes and has produced ~15 published articles and ~30 updates on the Ahrefs blog.  
*(Source: Ryan Law, same article + Tim Soulo on X, 13.05.2026, referencing youtube.com/watch?v=iVZrVeESnFQ)*

**Step 6: Save the output of every intermediate step.**

When the pipeline runs, each stage (outline, research brief, draft) should be saved to its own file. If the final article is bad, you can diagnose exactly which step failed, fix the corresponding skill file, and restart from the last good checkpoint — instead of re-running the entire workflow.  
*(Source: Ryan Law, "How I Do Content Engineering with Claude Code," ahrefs.com/blog, 28.04.2026)*

**Step 7: Front-load human direction at the start, not the end.**

Provide brief editorial direction before the pipeline runs — the target angle, key sub-topics to cover, and product features to mention. Small amounts of expert input at the beginning are far more effective than heavy editing of a bad draft at the end.  
*(Source: Ryan Law, "AI Content Wasn't Good Enough. Now It Is.," ahrefs.com/blog, 16.03.2026)*

---

## Phase 3: Content Quality and Optimization

**Step 8: Ground AI output in real data.**

LLMs default to producing confident-sounding text with no substance. Counter this by mandating specific data sources: competitor analysis from the SERP, product documentation, customer questions, and trusted research. Use MCP integrations or RAG pipelines to feed real data into the drafting process.  
*(Source: Ryan Law, "How I Do Content Engineering with Claude Code," ahrefs.com/blog, 28.04.2026; also Bernard Huang, Clearscope webinars on content optimization)*

**Step 9: Optimize for AI search citation, not just rankings.**

Structure content with clean, sequential heading hierarchies (H1 → H2 → H3). Pages with proper heading structure get cited 2.8x more by AI models. Use schema markup — pages with 3+ schema types see a 13% lift in citation odds. Keep pages updated: content refreshed within the last 3 months is cited 3x more than stale pages.  
*(Source: Eli Schwartz, LinkedIn post referencing AirOps State of AEO 2026 report, June 2026; also Kevin Indig, "State of AI Search Optimization 2026," growth-memo.com, 09.02.2026)*

**Step 10: Use AI for content optimization scoring.**

Run your draft through a content optimization tool (Clearscope, Surfer, or MarketMuse) to check topical coverage. AI-generated drafts often hit surface-level terms but miss the semantic depth that signals relevance to search engines. The optimization score gives you a concrete quality check beyond "does this read well."  
*(Source: Bernard Huang, Clearscope webinars on AI content quality, 2025–2026)*

---

## Phase 4: Distribution and Iteration

**Step 11: Distribution is not optional — budget time for it.**

Most teams spend 80% of effort on creation and 20% on distribution. Invert that. Every published article should be repurposed into at least 3 formats: a LinkedIn post summarizing the key insight, a short-form video or carousel, and a community post (Reddit, Slack groups, or industry forums).  
*(Source: Ross Simmonds, "Content Distribution in the Age of AI," Zero Click conference, youtube.com/watch?v=VXxFJAg7YJw, October 2025; also "Create Once, Distribute Forever" framework)*

**Step 12: Use AI to repurpose, not just to create.**

AI excels at format transformation. Feed a finished blog post into an LLM and prompt it to extract: 5 LinkedIn post variants, 3 tweet threads, a newsletter summary, and a video script. This lets a single piece of research serve multiple channels.  
*(Source: Ross Simmonds, HubSpot interview, blog.hubspot.com/marketing/ross-simmonds-on-ai-and-experimentation, January 2026)*

**Step 13: Measure citation, not just traffic.**

Traditional SEO tracks rankings and organic traffic. In 2026, also track whether AI assistants (ChatGPT, Perplexity, Gemini) cite your content. 85% of brand mentions in AI answers come from third-party pages, not the brand's own site — which means earning coverage and backlinks from authoritative sources matters more than ever.  
*(Source: Eli Schwartz, LinkedIn post referencing AirOps State of AEO 2026 report, June 2026)*

---

## Where Experts Disagree

### Disagreement 1: Full automation vs. human-in-the-loop

- **Ryan Law** argues that AI can now produce publish-ready content with no quality trade-off. His pipeline generates articles in 6–12 minutes using 23 chained skill files. He states: AI content wasn't good enough before, but now it is, and the trade-off between speed and quality has disappeared.  
  *(Source: "AI Content Wasn't Good Enough. Now It Is.," ahrefs.com/blog, 16.03.2026)*

- **Eli Schwartz** pushes back on this. He argues that the question is not whether AI can produce content, but whether the content is worth producing at all. Without a product-led strategy anchoring what you create, AI just accelerates the production of things nobody needs. AI is a copilot, not an autopilot.  
  *(Source: GTMnow interview, "How to do SEO right in 2025"; SearchPilot webinar, 23.05.2025)*

- **My position:** I side with a middle ground closer to Ryan Law for execution but informed by Eli Schwartz's strategic filter. Use full automation for well-understood informational topics where you already have expertise and data, but apply Eli's "is this worth producing?" test before anything enters the pipeline. Automating the wrong content faster is still a waste.

### Disagreement 2: Volume vs. depth

- **Nathan Gotch** publishes checklist-driven, high-frequency content. His approach is to cover many keywords systematically, using AI to produce and optimize at scale. He also runs Rankability, a tool built around this scaling philosophy.  
  *(Source: "The AI SEO Checklist I'd Use in 2026," youtube.com/watch?v=0FmEV0jE5TQ, July 2025)*

- **Kevin Indig** explicitly argues against this. His Growth Memo essays emphasize that fewer, deeper pieces grounded in original data outperform large volumes of keyword-targeted content. He points out that LLM referral traffic is fading as models improve, making commodity content increasingly worthless.  
  *(Source: "State of AI Search Optimization 2026," growth-memo.com, 09.02.2026; Search Engine Journal articles, 2025–2026)*

- **My position:** I side with Kevin Indig. For a small B2B SaaS team (which is 100Hires's context), you don't have the resources to produce at Nathan Gotch's scale, and the content landscape is already flooded with AI-generated commodity articles. Depth and originality win.

### Disagreement 3: Content-first vs. distribution-first

- **Ryan Law and Nathan Gotch** focus almost entirely on content creation quality and SEO optimization as the primary growth lever. If you create the best content and optimize it correctly, it will rank.

- **Ross Simmonds** argues this is dangerously incomplete. He says most teams stop at pressing "publish" and ignore distribution entirely. His framework — create once, distribute forever — treats every article as raw material to be repurposed across LinkedIn, Reddit, YouTube, newsletters, and community channels. He points out that discovery now happens across multiple platforms, not just Google.  
  *(Source: SEO Week 2026 talk, seoweek.org/ross-simmonds-2026; HubSpot interview, January 2026)*

- **My position:** I side with Ross Simmonds. Especially for B2B SaaS, buyers don't just Google — they browse LinkedIn, read Reddit threads, and ask AI assistants. A great article that nobody sees is worth nothing. Distribution should get at least equal effort to creation.

---

## What I Rejected and Why

### Rejected Idea 1: Koray Tuğberk Gübür's topical authority maps

Koray advocates building extensive topical authority structures — deep networks of semantically connected content that machines can parse. The methodology is intellectually rigorous, and his case studies show traffic gains.

**Why I rejected it:** The approach requires producing dozens of interconnected articles to cover a single topic cluster before seeing results. For a small B2B SaaS team with limited resources, this is impractical. You'd spend months building a content network before generating any measurable business impact. It's better suited to large publishers or agencies with dedicated SEO teams and long time horizons.

### Rejected Idea 2: Using AI to mass-produce programmatic SEO pages

Several practitioners discuss using AI to generate hundreds or thousands of templated pages targeting long-tail keyword variations — for example, "best ATS for [industry]" pages for every industry. The logic is that AI makes this cheap and fast.

**Why I rejected it:** Google has explicitly targeted thin, auto-generated content in recent algorithm updates. Even if the pages rank temporarily, the risk of a site-wide quality penalty outweighs the short-term traffic gain. For a B2B SaaS brand like 100Hires that depends on trust and credibility, a Google penalty would be devastating. The better approach is fewer, higher-quality pages that each justify their existence.

---

## My Original Ideas

### Bilingual AI content production for the Latin American B2B SaaS market

None of the 10 experts I researched address non-English markets in any meaningful way. Their frameworks assume English-language content targeting the US, UK, or global English-speaking audience. This leaves a significant gap: the Latin American B2B SaaS market.

**The idea:** Use the same AI-powered content pipeline described in this playbook, but produce content in both Spanish and English simultaneously. Here is how it could work:

1. **Keyword research in both languages.** Use Ahrefs or Semrush with region filters (Argentina, Mexico, Colombia, Chile) to find Spanish-language B2B SaaS keywords. Many have far lower competition than their English equivalents.

2. **Draft in English first, then adapt (not translate) to Spanish.** LLMs like Claude handle Spanish-language content well, especially Rioplatense and neutral Latin American Spanish. But direct translation produces awkward, stilted content. Instead, prompt the AI to rewrite the piece for a Latin American audience: different examples, local SaaS tools, regional buyer behavior, local pricing context (e.g., pricing in ARS or MXN, not just USD).

3. **Target Spanish-language AI search.** As ChatGPT, Perplexity, and Gemini expand their Spanish-language capabilities, Spanish content that is well-structured and authoritative has a significant first-mover advantage in AI citations. The pool of high-quality Spanish B2B SaaS content is much smaller than in English, making it easier to earn visibility.

4. **Distribute through Latin American channels.** LinkedIn is heavily used by B2B professionals in LatAm. Spanish-language LinkedIn posts, combined with presence in local Slack communities and industry WhatsApp groups, can drive discovery in ways that English-only strategies miss entirely.

**Why it could work:** The competitive landscape for B2B SaaS SEO in Spanish is far less crowded than in English. A company like 100Hires, which already operates globally, could capture significant organic traffic and AI citations in Latin America by being one of the first to apply these AI content production techniques to the Spanish-language market. The cost of producing bilingual content with AI is minimal compared to the potential reach.

---

## Weaknesses of This Playbook

1. **Tool dependency.** This playbook assumes access to paid tools (Ahrefs, Claude Pro, Clearscope). A team without budget for these would need to find free alternatives, which may degrade the quality of keyword research and content optimization.

2. **Tested in theory, not in practice.** I have not personally executed this full pipeline end-to-end on a live site. The recommendations are synthesized from practitioners who have, but I cannot confirm that every step works as described when combined into a single workflow by a junior marketer.

3. **English-centric sources.** All 10 experts operate primarily in English-language markets. The bilingual idea in "My Original Ideas" is promising but untested — I found no case studies of B2B SaaS teams using AI content pipelines for Spanish-language SEO.

4. **Rapidly changing landscape.** AI search (AI Overviews, ChatGPT search, Perplexity) is evolving weekly. Recommendations about heading structure, schema markup, and citation behavior may shift significantly within months. This playbook should be treated as a snapshot, not a permanent guide.

5. **No coverage of link building.** SEO content production is only one half of the equation. This playbook does not address backlink acquisition, digital PR, or domain authority — all of which significantly affect whether content ranks, regardless of quality.

6. **Assumes existing editorial judgment.** Ryan Law explicitly warns that his AI content process works because it mirrors an editorial process built from 14 years of experience. A junior marketer running the same pipeline may not catch quality issues that an experienced editor would flag. The skill files are only as good as the person who writes them.

---

## Who I Would NOT Recommend Following and Why

### Koray Tuğberk Gübür — Founder, Holistic SEO

Koray is clearly knowledgeable. His understanding of semantic SEO and topical authority is deep, and his case studies include real traffic data from client sites. I'm not questioning his expertise.

However, I would not recommend him to someone learning AI-powered SEO content production for three reasons:

1. **Accessibility.** His YouTube videos routinely run 1–3 hours. The information density is high but poorly structured for extraction — there are no timestamps, no summaries, and no written companions. Compared to Ryan Law or Nathan Gotch, who produce concise, structured, immediately actionable content, Koray's material demands a disproportionate time investment for the value extracted.

2. **Practicality.** The topical authority framework he advocates requires building large content networks before seeing results. This is viable for agencies with big teams and patient clients, but impractical for a small B2B SaaS team that needs to show results within a quarter.

3. **Overlap.** The most actionable parts of his semantic SEO approach — using proper heading hierarchies, building internal link structures, ensuring topical coverage — are covered more concisely by Mike King (iPullRank) and Bernard Huang (Clearscope), both of whom also provide tooling to implement the ideas.

For someone new to AI-powered SEO content, time is better spent with Ryan Law, Kevin Indig, or Eli Schwartz, who deliver higher signal per minute of attention.

---

## Sources Index

| # | Expert | Key Source | URL | Date |
|---|--------|-----------|-----|------|
| 1 | Ryan Law | How I Do Content Engineering with Claude Code | ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/ | 28.04.2026 |
| 2 | Ryan Law | AI Content Wasn't Good Enough. Now It Is. | ahrefs.com/blog/ai-content-wasnt-good-enough-now-it-is/ | 16.03.2026 |
| 3 | Ryan Law | 74% of New Webpages Include AI Content | ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/ | 28.05.2026 |
| 4 | Kevin Indig | State of AI Search Optimization 2026 | growth-memo.com/p/state-of-ai-search-optimization-2026 | 09.02.2026 |
| 5 | Kevin Indig | How to build an AI SEO strategy that outlasts tactics | growth-memo.com/p/how-to-build-an-ai-seo-strategy-that | 02.03.2026 |
| 6 | Eli Schwartz | SEO's New Playbook (SearchPilot webinar) | searchpilot.com/resources/blog/seo-playbook-survive-ai-product-led-growth-eli-schwartz | 23.05.2025 |
| 7 | Eli Schwartz | How to do SEO right in 2025 (GTMnow) | thegtmnewsletter.substack.com/p/how-to-do-seo-right-in-2025-hint | 2025 |
| 8 | Eli Schwartz | LinkedIn post: AirOps State of AEO 2026 | linkedin.com/in/schwartze | June 2026 |
| 9 | Nathan Gotch | The AI SEO Checklist I'd Use in 2026 | youtube.com/watch?v=0FmEV0jE5TQ | 14.07.2025 |
| 10 | Ross Simmonds | Content Distribution in the Age of AI | youtube.com/watch?v=VXxFJAg7YJw | October 2025 |
| 11 | Ross Simmonds | HubSpot interview: AI and experimentation | blog.hubspot.com/marketing/ross-simmonds-on-ai-and-experimentation | January 2026 |
| 12 | Ross Simmonds | SEO Week 2026 talk | seoweek.org/ross-simmonds-2026 | March 2026 |
| 13 | Bernard Huang | Clearscope webinars on AI content optimization | clearscope.io (YouTube channel) | 2025–2026 |
| 14 | Mike King | iPullRank: relevance engineering framework | ipullrank.com | 2025–2026 |
| 15 | Aleyda Solis | SEOFOMO newsletter + Crawling Mondays | learningseo.io / youtube.com | 2025–2026 |
| 16 | Lily Ray | LinkedIn posts on E-E-A-T and AI Overviews | linkedin.com/in/lily-ray | 2025–2026 |
