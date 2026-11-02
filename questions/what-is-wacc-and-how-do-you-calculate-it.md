---
layout: "question"
title: "What is WACC and how do you calculate it?"
description: "What is WACC and how do you calculate it? IB interview answer with the formula, cost of equity via CAPM, after-tax cost of debt and the beta follow-up."
permalink: "/questions/what-is-wacc-and-how-do-you-calculate-it/"
slug: "what-is-wacc-and-how-do-you-calculate-it"
tagline: "Investment banking interview question (Medium): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"What is WACC and how do you calculate it?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"WACC is the blended required return of all capital providers. WACC = E/(D+E) x cost of equity + D/(D+E) x cost of debt x (1 - tax rate), plus a preferred-stock term if relevant. I use market values or a target capital structure for the weights. Cost of equity comes from CAPM: risk-free rate + levered beta x equity risk premium. Some practitioners add a size or company-specific premium. The risk-free rate is usually a long-term government bond yield in the currency of the cash flows. Cost of debt is the current yield or borrowing rate, taken after tax because interest is tax-deductible.\"}}, {\"@type\": \"Question\", \"name\": \"What beta would you use for a private company?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Take comparable public companies' levered betas, unlever each (levered beta / (1 + (1 - tax rate) x debt/equity)), take the median, then relever at the private company's target capital structure.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you know the formula, can explain each input (weights, cost of equity, after-tax cost of debt), and can handle the private-company beta follow-up.

## Answer framework

1. Define it: the blended required return of all capital providers.
2. Formula: WACC = E/(D+E) x cost of equity + D/(D+E) x cost of debt x (1 - tax rate), plus a preferred term if relevant.
3. Weights: market values or a target capital structure.
4. Cost of equity: CAPM, risk-free rate + levered beta x equity risk premium.
5. Cost of debt: current yield or borrowing rate, after tax because interest is deductible.

## Sample answer

> WACC is the blended required return of all capital providers. WACC = E/(D+E) x cost of equity + D/(D+E) x cost of debt x (1 - tax rate), plus a preferred-stock term if relevant. I use market values or a target capital structure for the weights.
>
> Cost of equity comes from CAPM: risk-free rate + levered beta x equity risk premium. Some practitioners add a size or company-specific premium. The risk-free rate is usually a long-term government bond yield in the currency of the cash flows.
>
> Cost of debt is the current yield or borrowing rate, taken after tax because interest is tax-deductible.

## Likely follow-ups

**What beta would you use for a private company?** Take comparable public companies' levered betas, unlever each (levered beta / (1 + (1 - tax rate) x debt/equity)), take the median, then relever at the private company's target capital structure.

## Common mistakes

- Using book values for the weights without saying why.
- Forgetting to tax-effect the cost of debt.
- Using an unlevered beta in CAPM for the cost of equity.
- Using the private company's own (non-existent) beta instead of comparables.

## Related questions

- [Walk me through a DCF](../walk-me-through-a-dcf/)
- [What is terminal value and how do you calculate it?](../what-is-terminal-value-and-how-do-you-calculate-it/)
- [Enterprise value vs equity value: what is the difference?](../enterprise-value-vs-equity-value/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on questions #27, #28, #29 in the [full question bank](../../)._

{% include qpage-cta.html %}
