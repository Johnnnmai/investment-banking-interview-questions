---
layout: "question"
title: "What is the difference between unlevered and levered free cash flow?"
description: "Unlevered vs levered free cash flow for IB interviews: formulas, why interest and debt repayment matter, matching discount rates, and which value each gives."
permalink: "/questions/unlevered-vs-levered-free-cash-flow/"
slug: "unlevered-vs-levered-free-cash-flow"
tagline: "Investment banking interview question (Medium): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"What is the difference between unlevered and levered free cash flow?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Unlevered free cash flow is the cash the business generates before any payments to lenders, so it belongs to all capital providers. I calculate it as EBIT times one minus the tax rate, plus D&A, minus capex, minus the increase in net working capital. Starting from EBIT means interest expense, and the tax shield it creates, are excluded, so the result does not depend on how the company is financed. Levered free cash flow is what is left for equity holders after the company services its debt. It starts from net income, which is already after interest, then adds D&A, subtracts capex and the increase in working capital, and subtracts mandatory debt repayments. If the company is borrowing new debt, net borrowing is added. The key is matching. Unlevered free cash flow goes with WACC, because it belongs to debt and equity holders together, and the DCF gives enterprise value. Levered free cash flow goes with cost of equity and gives equity value directly. Bankers usually use unlevered DCFs because capital structure can change and the result is easier to compare across companies; levered cash flow matters more in LBOs and for banks.\"}}, {\"@type\": \"Question\", \"name\": \"Why is unlevered FCF more common in DCFs?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"It separates operating value from financing choices, which can change, and avoids forecasting the debt schedule in detail.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you can write both formulas, explain what capital providers each one belongs to, and match each to the correct discount rate and valuation output.

## Answer framework

1. Unlevered FCF: cash flow available to all capital providers, before interest.
2. Formula: EBIT x (1 - tax rate) + D&A - capex - increase in net working capital.
3. Levered FCF: cash flow available to equity holders after interest and required debt repayments.
4. Formula: net income + D&A - capex - increase in NWC - mandatory debt repayments (plus net new borrowing if modeled).
5. Matching: unlevered FCF discounted at WACC gives enterprise value; levered FCF at cost of equity gives equity value.

## Sample answer

> Unlevered free cash flow is the cash the business generates before any payments to lenders, so it belongs to all capital providers. I calculate it as EBIT times one minus the tax rate, plus D&A, minus capex, minus the increase in net working capital. Starting from EBIT means interest expense, and the tax shield it creates, are excluded, so the result does not depend on how the company is financed.
>
> Levered free cash flow is what is left for equity holders after the company services its debt. It starts from net income, which is already after interest, then adds D&A, subtracts capex and the increase in working capital, and subtracts mandatory debt repayments. If the company is borrowing new debt, net borrowing is added.
>
> The key is matching. Unlevered free cash flow goes with WACC, because it belongs to debt and equity holders together, and the DCF gives enterprise value. Levered free cash flow goes with cost of equity and gives equity value directly. Bankers usually use unlevered DCFs because capital structure can change and the result is easier to compare across companies; levered cash flow matters more in LBOs and for banks.

## Likely follow-ups

**Why is unlevered FCF more common in DCFs?** It separates operating value from financing choices, which can change, and avoids forecasting the debt schedule in detail.

## Common mistakes

- Discounting levered FCF at WACC.
- Subtracting interest when calculating unlevered FCF.
- Getting the sign of the working capital change wrong.
- Forgetting mandatory debt repayments in levered FCF.

## Related questions

- [Walk me through a DCF](../walk-me-through-a-dcf/)
- [What is WACC and how do you calculate it?](../what-is-wacc-and-how-do-you-calculate-it/)
- [How do you calculate cost of equity?](../how-do-you-calculate-cost-of-equity/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on questions #49, #14, #15 in the [full question bank](../../)._

{% include qpage-cta.html %}
