---
layout: "question"
title: "Gordon Growth vs exit multiple: which terminal value method should you use?"
description: "Gordon Growth vs exit multiple terminal value for IB interviews: choosing a method, cross-checking implied multiples and growth rates, and a worked example."
permalink: "/questions/gordon-growth-vs-exit-multiple/"
slug: "gordon-growth-vs-exit-multiple"
tagline: "Investment banking interview question (Medium): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"Gordon Growth vs exit multiple: which terminal value method should you use?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"I would use both and let each check the other. The exit multiple method applies a multiple, usually EV/EBITDA from comparable companies, to the final projected year's EBITDA. Bankers like it because it reflects how the market values similar businesses and it matches how buyers think about exit values. Its weakness is that it imports today's market mood into a value years out. The Gordon Growth method assumes free cash flow grows at a constant rate forever: terminal value equals final-year FCF times one plus g, divided by the discount rate minus g. It ties value to fundamentals but is very sensitive to the growth and discount rate assumptions. So I cross-check. Say final-year free cash flow is $100M, EBITDA is $150M, WACC is 10% and long-term growth is 2%. Gordon Growth gives $102M divided by 8%, or about $1,275M, which implies roughly 8.5 times EBITDA. If comps trade at 8 to 10 times, that is reasonable. If an exit multiple of 14 times implied a perpetual growth rate of 5% or more, I would question the multiple, since a mature company cannot outgrow the economy forever.\"}}, {\"@type\": \"Question\", \"name\": \"Which method is more common on the sell side?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Exit multiples are very common in banking, usually shown with a Gordon Growth cross-check.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

**Practiced one out loud?** [Paste your answer into the free self-check and get a score in 30 seconds](https://johnnnmai.github.io/ai-engineer-interview-questions/answer-check/?track=ib)

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you can choose between terminal value methods for a situation and use each to sanity-check the other.

## Answer framework

1. Exit multiple: terminal year EBITDA x a multiple from comps or precedents; common in banking and tied to market pricing.
2. Gordon Growth: final-year FCF x (1 + g) / (discount rate - g); grounded in long-run cash flow fundamentals.
3. Choose by context: exit multiple when good comps exist and for deal or LBO work; Gordon Growth for stable companies or when market multiples look distorted.
4. Cross-check: compute the multiple implied by the Gordon value and the growth rate implied by the exit multiple.
5. Red flags: implied growth above long-run economic growth, or an implied multiple far from current trading ranges.

## Sample answer

> I would use both and let each check the other. The exit multiple method applies a multiple, usually EV/EBITDA from comparable companies, to the final projected year's EBITDA. Bankers like it because it reflects how the market values similar businesses and it matches how buyers think about exit values. Its weakness is that it imports today's market mood into a value years out.
>
> The Gordon Growth method assumes free cash flow grows at a constant rate forever: terminal value equals final-year FCF times one plus g, divided by the discount rate minus g. It ties value to fundamentals but is very sensitive to the growth and discount rate assumptions.
>
> So I cross-check. Say final-year free cash flow is $100M, EBITDA is $150M, WACC is 10% and long-term growth is 2%. Gordon Growth gives $102M divided by 8%, or about $1,275M, which implies roughly 8.5 times EBITDA. If comps trade at 8 to 10 times, that is reasonable. If an exit multiple of 14 times implied a perpetual growth rate of 5% or more, I would question the multiple, since a mature company cannot outgrow the economy forever.

## Likely follow-ups

**Which method is more common on the sell side?** Exit multiples are very common in banking, usually shown with a Gordon Growth cross-check.

## Common mistakes

- Picking one method without checking it against the other.
- Using a perpetual growth rate above long-run GDP growth.
- Applying an exit multiple to the wrong year's metric.
- Forgetting to discount the terminal value back to today.

## Related questions

- [What is terminal value and how do you calculate it?](../what-is-terminal-value-and-how-do-you-calculate-it/)
- [Walk me through a DCF](../walk-me-through-a-dcf/)
- [If you raise the discount rate by 1%, what happens to DCF value?](../raise-discount-rate-by-1-percent-dcf/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on question #31 in the [full question bank](../../)._

{% include qpage-cta.html %}
