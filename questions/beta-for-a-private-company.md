---
layout: "question"
title: "What beta would you use for a private company?"
description: "Beta for a private company in IB interviews: unlever comparable company betas, take the median, relever at the target's capital structure, plus a worked example."
permalink: "/questions/beta-for-a-private-company/"
slug: "beta-for-a-private-company"
tagline: "Investment banking interview question (Medium): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"What beta would you use for a private company?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Since a private company has no stock price, I estimate beta from comparable public companies. Their observed betas reflect two things: business risk and financial risk from leverage. I want only the business risk, so I unlever each peer's beta with the formula: unlevered beta equals levered beta divided by one plus one minus the tax rate times debt-to-equity. For example, a peer with a levered beta of 1.3, a 25% tax rate and a debt-to-equity ratio of 0.4 has an unlevered beta of 1.3 divided by 1.3, which is 1.0. I do this for each peer and take the median, which is less sensitive to outliers. Then I relever at the capital structure I expect for the target, either its own or a typical structure for its industry. If the target's debt-to-equity ratio is 0.6, its levered beta is 1.0 times one plus 0.75 times 0.6, or 1.45. That beta goes into CAPM to get cost of equity. Because the target is private and often smaller, I may also add a size premium, and in some contexts a discount for lack of marketability is applied to the final value rather than the discount rate.\"}}, {\"@type\": \"Question\", \"name\": \"Why unlever and relever rather than just averaging peer betas?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Peers have different leverage, which changes equity risk; unlevering isolates business risk so it can be applied to the target's own leverage.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

**Practiced one out loud?** [Paste your answer into the free self-check and get a score in 30 seconds](https://johnnnmai.github.io/ai-engineer-interview-questions/answer-check/?track=ib)

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you can estimate beta when there is no stock price, and can apply the unlevering and relevering formulas correctly.

## Answer framework

1. A private company has no traded stock, so you cannot regress its returns against the market.
2. Pick comparable public companies with similar business risk.
3. Unlever each beta: unlevered beta = levered beta / (1 + (1 - t) x D/E).
4. Take the median or mean unlevered beta to remove the effect of each peer's capital structure.
5. Relever at the target's or target industry's D/E: levered beta = unlevered beta x (1 + (1 - t) x D/E); consider a size premium in cost of equity.

## Sample answer

> Since a private company has no stock price, I estimate beta from comparable public companies. Their observed betas reflect two things: business risk and financial risk from leverage. I want only the business risk, so I unlever each peer's beta with the formula: unlevered beta equals levered beta divided by one plus one minus the tax rate times debt-to-equity.
>
> For example, a peer with a levered beta of 1.3, a 25% tax rate and a debt-to-equity ratio of 0.4 has an unlevered beta of 1.3 divided by 1.3, which is 1.0. I do this for each peer and take the median, which is less sensitive to outliers.
>
> Then I relever at the capital structure I expect for the target, either its own or a typical structure for its industry. If the target's debt-to-equity ratio is 0.6, its levered beta is 1.0 times one plus 0.75 times 0.6, or 1.45. That beta goes into CAPM to get cost of equity. Because the target is private and often smaller, I may also add a size premium, and in some contexts a discount for lack of marketability is applied to the final value rather than the discount rate.

## Likely follow-ups

**Why unlever and relever rather than just averaging peer betas?** Peers have different leverage, which changes equity risk; unlevering isolates business risk so it can be applied to the target's own leverage.

## Common mistakes

- Averaging levered peer betas without adjusting for leverage.
- Relevering at the peers' capital structure instead of the target's.
- Getting the unlevering formula upside down.
- Choosing comps with different business risk.

## Related questions

- [How do you calculate cost of equity?](../how-do-you-calculate-cost-of-equity/)
- [What is WACC and how do you calculate it?](../what-is-wacc-and-how-do-you-calculate-it/)
- [Walk me through how you would build a comparable companies analysis](../how-to-build-a-comparable-companies-analysis/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on question #29 in the [full question bank](../../)._

{% include qpage-cta.html %}
