---
layout: "question"
title: "What is terminal value and how do you calculate it?"
description: "Terminal value in a DCF: the Gordon Growth and exit multiple formulas, when to use each, how to cross-check them and why sensitivity tables matter."
permalink: "/questions/what-is-terminal-value-and-how-do-you-calculate-it/"
slug: "what-is-terminal-value-and-how-do-you-calculate-it"
tagline: "Investment banking interview question (Medium): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"What is terminal value and how do you calculate it?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Terminal value captures the value of cash flows beyond the projection period. With Gordon Growth it is final-year free cash flow x (1 + long-term growth rate) / (discount rate - growth rate). With an exit multiple it is final-year EBITDA, or another metric, x an exit multiple from comparable companies. Either way I discount it back to today from the end of the projection period. Exit multiple is common in banking because it ties to market valuations and to how buyers think about exits. Gordon Growth suits mature, stable businesses and is preferred when there are few good comparables or market multiples are distorted. Best practice is to cross-check: compute the growth rate implied by the exit multiple and the multiple implied by the growth rate. Terminal value is often the majority of a DCF's value, so sensitivity tables on its inputs matter. The long-term growth rate should not exceed long-run nominal GDP growth.\"}}, {\"@type\": \"Question\", \"name\": \"If you raise the discount rate by 1%, how much does value change?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Example with Gordon Growth only: at a 10% discount rate and 2% growth, terminal value is proportional to 1/0.08; at 11% it is 1/0.09, about 11% lower.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you know both methods and their formulas, when each fits, how to cross-check them, and why terminal value assumptions drive so much of a DCF.

## Answer framework

1. Define it: the value of cash flows beyond the projection period.
2. Gordon Growth: final-year FCF x (1 + g) / (discount rate - g).
3. Exit multiple: final-year EBITDA (or another metric) x a multiple from comparable companies.
4. Discount it back to today from the end of the projection period.
5. Cross-check the two methods and show sensitivity tables.

## Sample answer

> Terminal value captures the value of cash flows beyond the projection period. With Gordon Growth it is final-year free cash flow x (1 + long-term growth rate) / (discount rate - growth rate). With an exit multiple it is final-year EBITDA, or another metric, x an exit multiple from comparable companies. Either way I discount it back to today from the end of the projection period.
>
> Exit multiple is common in banking because it ties to market valuations and to how buyers think about exits. Gordon Growth suits mature, stable businesses and is preferred when there are few good comparables or market multiples are distorted. Best practice is to cross-check: compute the growth rate implied by the exit multiple and the multiple implied by the growth rate.
>
> Terminal value is often the majority of a DCF's value, so sensitivity tables on its inputs matter. The long-term growth rate should not exceed long-run nominal GDP growth.

## Likely follow-ups

**If you raise the discount rate by 1%, how much does value change?** Example with Gordon Growth only: at a 10% discount rate and 2% growth, terminal value is proportional to 1/0.08; at 11% it is 1/0.09, about 11% lower.

## Common mistakes

- Forgetting to discount the terminal value back to today.
- Using a growth rate above long-run nominal GDP growth.
- Applying an exit multiple without checking the growth rate it implies.
- Treating the output as precise when most of the value sits in the terminal value.

## Related questions

- [Walk me through a DCF](../walk-me-through-a-dcf/)
- [What is WACC and how do you calculate it?](../what-is-wacc-and-how-do-you-calculate-it/)
- [Walk me through an LBO model](../walk-me-through-an-lbo-model/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on questions #30, #31, #50 in the [full question bank](../../)._

{% include qpage-cta.html %}
