---
layout: "question"
title: "How do you calculate cost of equity?"
description: "How to calculate cost of equity for IB interviews: CAPM with risk-free rate, beta and equity risk premium, a worked example, and when to add a size premium."
permalink: "/questions/how-do-you-calculate-cost-of-equity/"
slug: "how-do-you-calculate-cost-of-equity"
tagline: "Investment banking interview question (Easy): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"How do you calculate cost of equity?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"I would use the capital asset pricing model. Cost of equity equals the risk-free rate plus beta times the equity risk premium. It represents the return equity investors require, given how risky the stock is relative to the market. For the risk-free rate, I use the yield on a long-term government bond in the currency of the cash flows, typically the 10-year Treasury for a US company. Beta measures how much the stock moves relative to the market; because a single company's historical beta is noisy, bankers often unlever the betas of comparable companies, take the median and relever it at the target's capital structure. The equity risk premium is the extra return investors expect from stocks over government bonds; banks usually take it from a standard data provider or internal guidance. As an example, with a 4% risk-free rate, a beta of 1.2 and a 5% equity risk premium, cost of equity is 4% plus 6%, or 10%. For a small or unusually risky company I might add a size premium. Cost of equity then feeds into WACC alongside the after-tax cost of debt.\"}}, {\"@type\": \"Question\", \"name\": \"Why is cost of equity higher than cost of debt?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Equity holders are paid last and have no fixed return, and interest on debt is tax-deductible, so debt is cheaper.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you can apply CAPM, explain each input and where it comes from, and know common adjustments.

## Answer framework

1. Use CAPM: cost of equity = risk-free rate + beta x equity risk premium.
2. Risk-free rate: usually the yield on a long-term government bond, such as the 10-year Treasury, in the same currency as the cash flows.
3. Beta: sensitivity to the market; for a public company use its own or a peer-based relevered beta.
4. Equity risk premium: the extra return investors expect from stocks over the risk-free rate, from a chosen source.
5. Adjustments: add a size or company-specific premium for small or risky companies when justified.

## Sample answer

> I would use the capital asset pricing model. Cost of equity equals the risk-free rate plus beta times the equity risk premium. It represents the return equity investors require, given how risky the stock is relative to the market.
>
> For the risk-free rate, I use the yield on a long-term government bond in the currency of the cash flows, typically the 10-year Treasury for a US company. Beta measures how much the stock moves relative to the market; because a single company's historical beta is noisy, bankers often unlever the betas of comparable companies, take the median and relever it at the target's capital structure. The equity risk premium is the extra return investors expect from stocks over government bonds; banks usually take it from a standard data provider or internal guidance.
>
> As an example, with a 4% risk-free rate, a beta of 1.2 and a 5% equity risk premium, cost of equity is 4% plus 6%, or 10%. For a small or unusually risky company I might add a size premium. Cost of equity then feeds into WACC alongside the after-tax cost of debt.

## Likely follow-ups

**Why is cost of equity higher than cost of debt?** Equity holders are paid last and have no fixed return, and interest on debt is tax-deductible, so debt is cheaper.

## Common mistakes

- Adding beta and the risk premium instead of multiplying.
- Using a short-term bill rate for long-duration cash flows without reason.
- Relying on a single noisy historical beta.
- Mixing currencies between the risk-free rate and the cash flows.

## Related questions

- [What is WACC and how do you calculate it?](../what-is-wacc-and-how-do-you-calculate-it/)
- [What beta would you use for a private company?](../beta-for-a-private-company/)
- [Walk me through a DCF](../walk-me-through-a-dcf/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on questions #28, #42 in the [full question bank](../../)._

{% include qpage-cta.html %}
