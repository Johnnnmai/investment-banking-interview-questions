---
layout: "question"
title: "What is the difference between IRR and MOIC?"
description: "IRR vs MOIC for IB and PE interviews: definitions, why timing matters, converting 2.0x into IRR over three and five years, and how dividend recaps affect each."
permalink: "/questions/irr-vs-moic/"
slug: "irr-vs-moic"
tagline: "Investment banking interview question (Easy): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"What is the difference between IRR and MOIC?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"MOIC tells you how many times your money you got back: if a fund invests $100M and receives $250M in total, MOIC is 2.5x. It says nothing about how long that took. IRR is the annualized return, the discount rate at which the present value of all cash outflows and inflows equals zero, so it captures timing. With one investment at the start and one exit at the end, the conversion is simple: IRR equals MOIC raised to the power of one over the number of years, minus one. Doubling your money over three years is about a 26% IRR, while doubling over five years is about 15%. Same multiple, very different annual return. Investors look at both because each can be flattering on its own. A quick flip can show a high IRR on a small multiple, which may not move the needle for a large fund. Returning cash early, for example through a dividend recap, raises IRR more than MOIC. A long hold can show a strong multiple with a mediocre IRR. Limited partners want a high IRR, but they also need real multiples of cash back, so funds report both.\"}}, {\"@type\": \"Question\", \"name\": \"Roughly what IRR is 3.0x over five years?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"About 25%, since 3 to the power of 0.2 is roughly 1.25.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

**Practiced one out loud?** [Paste your answer into the free self-check and get a score in 30 seconds](https://johnnnmai.github.io/ai-engineer-interview-questions/answer-check/?track=ib)

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you understand both return metrics, can convert between them for a simple case, and know why investors look at both.

## Answer framework

1. MOIC (multiple on invested capital): total value returned divided by equity invested; ignores time.
2. IRR (internal rate of return): the annualized discount rate that makes the net present value of all cash flows zero; reflects timing.
3. Single entry and exit shortcut: IRR = MOIC^(1 / years) - 1.
4. Example: 2.0x over 3 years is about 26% IRR; over 5 years about 15%.
5. Use both: IRR can be boosted by early cash returns, while MOIC shows how much money was actually made.

## Sample answer

> MOIC tells you how many times your money you got back: if a fund invests $100M and receives $250M in total, MOIC is 2.5x. It says nothing about how long that took. IRR is the annualized return, the discount rate at which the present value of all cash outflows and inflows equals zero, so it captures timing.
>
> With one investment at the start and one exit at the end, the conversion is simple: IRR equals MOIC raised to the power of one over the number of years, minus one. Doubling your money over three years is about a 26% IRR, while doubling over five years is about 15%. Same multiple, very different annual return.
>
> Investors look at both because each can be flattering on its own. A quick flip can show a high IRR on a small multiple, which may not move the needle for a large fund. Returning cash early, for example through a dividend recap, raises IRR more than MOIC. A long hold can show a strong multiple with a mediocre IRR. Limited partners want a high IRR, but they also need real multiples of cash back, so funds report both.

## Likely follow-ups

**Roughly what IRR is 3.0x over five years?** About 25%, since 3 to the power of 0.2 is roughly 1.25.

## Common mistakes

- Saying MOIC accounts for time.
- Converting 2.0x over five years as 20% a year by simple division.
- Ignoring interim cash flows such as dividends in IRR.
- Judging a deal on IRR alone.

## Related questions

- [Walk me through an LBO model](../walk-me-through-an-lbo-model/)
- [What is a dividend recapitalization?](../what-is-a-dividend-recapitalization/)
- [How do you do a paper LBO?](../how-do-you-do-a-paper-lbo/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on question #75 in the [full question bank](../../)._

{% include qpage-cta.html %}
