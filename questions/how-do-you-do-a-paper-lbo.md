---
layout: "question"
title: "How do you do a paper LBO?"
description: "Paper LBO walkthrough for IB and PE interviews: 10x entry, $200M EBITDA, 6x debt, 5% growth, 10x exit in 5 years, with MOIC, IRR and rules of thumb."
permalink: "/questions/how-do-you-do-a-paper-lbo/"
slug: "how-do-you-do-a-paper-lbo"
tagline: "Investment banking interview question (Medium): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"How do you do a paper LBO?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Take 10x entry, $200M EBITDA, 6x debt, 5% growth and a 10x exit in 5 years. Entry enterprise value is 10 x $200M = $2,000M; debt at 6x is $1,200M, so equity is $800M, ignoring fees. Year-5 EBITDA is $200M x 1.05^5, about $255M. Exit at 10x is about $2,553M. If no debt is repaid, exit equity is $2,553M - $1,200M = $1,353M: MOIC about 1.7x, IRR about 11%. If, say, $300M of debt is repaid from free cash flow, exit equity is about $1,653M: MOIC about 2.1x, IRR about 15 to 16%.\"}}, {\"@type\": \"Question\", \"name\": \"What rules of thumb help estimate IRR?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"2x in 5 years is about 15% IRR; 2x in 3 years is about 26%; 3x in 5 years is about 25%. For a single entry and exit, IRR = MOIC^(1/years) - 1.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

{% include qpage-cta.html %}

## What the interviewer is testing

Speed and structure with mental math: entry value, debt and equity, exit value, exit equity, then MOIC and an approximate IRR, without a calculator.

## Answer framework

1. Entry: enterprise value = entry multiple x EBITDA; split into debt and equity (ignore fees unless told).
2. Exit EBITDA: grow EBITDA over the hold period.
3. Exit value: exit multiple x exit EBITDA.
4. Exit equity: exit value minus remaining debt (after any paydown).
5. Returns: MOIC = exit equity / entry equity; estimate IRR with rules of thumb.

## Sample answer

> Take 10x entry, $200M EBITDA, 6x debt, 5% growth and a 10x exit in 5 years. Entry enterprise value is 10 x $200M = $2,000M; debt at 6x is $1,200M, so equity is $800M, ignoring fees.
>
> Year-5 EBITDA is $200M x 1.05^5, about $255M. Exit at 10x is about $2,553M. If no debt is repaid, exit equity is $2,553M - $1,200M = $1,353M: MOIC about 1.7x, IRR about 11%.
>
> If, say, $300M of debt is repaid from free cash flow, exit equity is about $1,653M: MOIC about 2.1x, IRR about 15 to 16%.

## Likely follow-ups

**What rules of thumb help estimate IRR?** 2x in 5 years is about 15% IRR; 2x in 3 years is about 26%; 3x in 5 years is about 25%. For a single entry and exit, IRR = MOIC^(1/years) - 1.

## Common mistakes

- Forgetting to subtract remaining debt at exit.
- Computing MOIC on enterprise value instead of equity.
- Losing time on exact IRR math instead of using rules of thumb.
- Not stating simplifying assumptions such as ignoring fees.

## Related questions

- [Walk me through an LBO model](../walk-me-through-an-lbo-model/)
- [Walk me through a merger model](../walk-me-through-a-merger-model/)
- [What is terminal value and how do you calculate it?](../what-is-terminal-value-and-how-do-you-calculate-it/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on questions #74, #75 in the [full question bank](../../)._

{% include qpage-cta.html %}
