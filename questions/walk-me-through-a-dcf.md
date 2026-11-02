---
layout: "question"
title: "Walk me through a DCF"
description: "How to answer \"walk me through a DCF\" in an investment banking interview: a five-step framework, a sample answer, likely follow-ups and common mistakes."
permalink: "/questions/walk-me-through-a-dcf/"
slug: "walk-me-through-a-dcf"
tagline: "Investment banking interview question (Easy): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"Walk me through a DCF\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"I would project the company's unlevered free cash flows, usually for 5 to 10 years, from revenue, margins, taxes, capex and working capital. Unlevered free cash flow is EBIT x (1 - tax rate) + D&A - capex - increase in net working capital. Then I calculate a terminal value at the end of the projection period, using either the Gordon Growth method or an exit multiple. I discount the projected cash flows and the terminal value back to today at WACC. The sum is enterprise value. I subtract net debt and other claims to get equity value and divide by diluted shares to get value per share. Because the terminal value is often the majority of the value, I would show the result with sensitivity tables on WACC and the terminal assumptions.\"}}, {\"@type\": \"Question\", \"name\": \"Why use unlevered free cash flow?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Because the discount rate (WACC) reflects all capital providers, so the cash flow must be before debt payments too.\"}}, {\"@type\": \"Question\", \"name\": \"If you raise the discount rate by 1%, what happens?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Value goes down. A one-point change commonly moves DCF value by roughly 10% to 15%, depending on the gap between the discount rate and the terminal growth rate.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

**Practiced one out loud?** [Paste your answer into the free self-check and get a score in 30 seconds](https://johnnnmai.github.io/ai-engineer-interview-questions/answer-check/?track=ib&q=walk-me-through-a-dcf)

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you can give a clean, ordered walk-through in about a minute, and whether you understand the logic behind each step: why unlevered free cash flow, why WACC, and why the terminal value deserves a sensitivity table.

## Answer framework

1. Project unlevered free cash flow for 5 to 10 years from revenue, margins, taxes, capex and working capital.
2. Calculate a terminal value at the end of the projection period with the Gordon Growth method or an exit multiple.
3. Discount the cash flows and the terminal value to today at the weighted average cost of capital (WACC).
4. Sum them to get enterprise value.
5. Subtract net debt and other claims to get equity value, then divide by diluted shares to get value per share.

## Sample answer

> I would project the company's unlevered free cash flows, usually for 5 to 10 years, from revenue, margins, taxes, capex and working capital. Unlevered free cash flow is EBIT x (1 - tax rate) + D&A - capex - increase in net working capital.
>
> Then I calculate a terminal value at the end of the projection period, using either the Gordon Growth method or an exit multiple. I discount the projected cash flows and the terminal value back to today at WACC.
>
> The sum is enterprise value. I subtract net debt and other claims to get equity value and divide by diluted shares to get value per share. Because the terminal value is often the majority of the value, I would show the result with sensitivity tables on WACC and the terminal assumptions.

## Likely follow-ups

**Why use unlevered free cash flow?** Because the discount rate (WACC) reflects all capital providers, so the cash flow must be before debt payments too.

**If you raise the discount rate by 1%, what happens?** Value goes down. A one-point change commonly moves DCF value by roughly 10% to 15%, depending on the gap between the discount rate and the terminal growth rate.

## Common mistakes

- Discounting levered free cash flow at WACC; levered FCF goes with the cost of equity and gives equity value.
- Stopping at enterprise value and forgetting the bridge to equity value and per-share value.
- Using a terminal growth rate above long-run nominal GDP growth.
- Presenting a single point estimate with no sensitivity on WACC and terminal assumptions.
- Rambling through formulas before giving the five steps in order.

## Related questions

- [What is WACC and how do you calculate it?](../what-is-wacc-and-how-do-you-calculate-it/)
- [What is terminal value and how do you calculate it?](../what-is-terminal-value-and-how-do-you-calculate-it/)
- [Enterprise value vs equity value: what is the difference?](../enterprise-value-vs-equity-value/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on questions #26, #49, #14, #30, #50 in the [full question bank](../../)._

{% include qpage-cta.html %}
