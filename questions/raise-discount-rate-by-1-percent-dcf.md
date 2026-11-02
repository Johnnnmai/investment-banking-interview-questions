---
layout: "question"
title: "If you raise the discount rate by 1%, what happens to DCF value?"
description: "Raising the discount rate by 1% in a DCF: value falls, a worked terminal value example with 2% growth, the exit multiple case and sensitivity tables."
permalink: "/questions/raise-discount-rate-by-1-percent-dcf/"
slug: "raise-discount-rate-by-1-percent-dcf"
tagline: "Investment banking interview question (Medium): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"If you raise the discount rate by 1%, what happens to DCF value?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"The value goes down. A higher discount rate means each future cash flow is worth less today, and cash flows further in the future lose more value because the discounting compounds over more years. The size depends mostly on terminal value, which often makes up the majority of a DCF. With the Gordon Growth method and a 2% long-term growth rate, raising the discount rate from 10% to 11% changes the denominator from 8% to 9%. Terminal value as a multiple of next year's cash flow drops from 12.5 to about 11.1, roughly 11% lower, and then that smaller number is discounted at a higher rate too. Adding the smaller hit on the projected cash flows, a typical company might lose somewhere around 10% to 15% of its value, more if growth is high and the spread between discount rate and growth is narrow. If terminal value comes from an exit multiple, the terminal value itself does not change; only the present value factor falls, so the decline is smaller. Over five years, discounting at 11% instead of 10% lowers the present value of terminal value by roughly 4%. That is why I always show a sensitivity table across discount rates and growth rates or multiples.\"}}, {\"@type\": \"Question\", \"name\": \"Why does the effect get larger when growth is high?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"The Gordon denominator is the spread between discount rate and growth; a 1% change matters more when that spread is small.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you can reason about the direction and rough size of the change, and explain why terminal value drives most of it.

## Answer framework

1. Direction: value falls, because every future cash flow is discounted more heavily.
2. Terminal value usually dominates, so the effect is driven by it.
3. Gordon Growth: with g = 2%, going from 10% to 11% changes the terminal multiple of next-year cash flow from 1 / 8% = 12.5x to 1 / 9% = 11.1x, about 11% lower before discounting.
4. Discounting: higher rates also shrink the present value of all projected cash flows; the overall drop is often around 10-15% for a typical company.
5. Exit multiple method: terminal value itself does not change, only its present value, so the decline is smaller.

## Sample answer

> The value goes down. A higher discount rate means each future cash flow is worth less today, and cash flows further in the future lose more value because the discounting compounds over more years.
>
> The size depends mostly on terminal value, which often makes up the majority of a DCF. With the Gordon Growth method and a 2% long-term growth rate, raising the discount rate from 10% to 11% changes the denominator from 8% to 9%. Terminal value as a multiple of next year's cash flow drops from 12.5 to about 11.1, roughly 11% lower, and then that smaller number is discounted at a higher rate too. Adding the smaller hit on the projected cash flows, a typical company might lose somewhere around 10% to 15% of its value, more if growth is high and the spread between discount rate and growth is narrow.
>
> If terminal value comes from an exit multiple, the terminal value itself does not change; only the present value factor falls, so the decline is smaller. Over five years, discounting at 11% instead of 10% lowers the present value of terminal value by roughly 4%. That is why I always show a sensitivity table across discount rates and growth rates or multiples.

## Likely follow-ups

**Why does the effect get larger when growth is high?** The Gordon denominator is the spread between discount rate and growth; a 1% change matters more when that spread is small.

## Common mistakes

- Saying value rises.
- Claiming a 1% rate change gives a 1% value change.
- Ignoring that terminal value drives most of the change.
- Treating the exit multiple and Gordon Growth methods as equally sensitive.

## Related questions

- [Gordon Growth vs exit multiple: which terminal value method should you use?](../gordon-growth-vs-exit-multiple/)
- [What is WACC and how do you calculate it?](../what-is-wacc-and-how-do-you-calculate-it/)
- [Walk me through a DCF](../walk-me-through-a-dcf/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on questions #50, #41 in the [full question bank](../../)._

{% include qpage-cta.html %}
