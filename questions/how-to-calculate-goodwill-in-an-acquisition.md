---
layout: "question"
title: "How do you calculate goodwill in an acquisition (purchase price allocation)?"
description: "Goodwill calculation in a purchase price allocation: equity purchase price, book value, asset write-ups, new deferred tax liability, with a worked $1,000M example."
permalink: "/questions/how-to-calculate-goodwill-in-an-acquisition/"
slug: "how-to-calculate-goodwill-in-an-acquisition"
tagline: "Investment banking interview question (Hard): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"How do you calculate goodwill in an acquisition (purchase price allocation)?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Purchase price allocation assigns the price paid to the target's assets and liabilities at fair value, and whatever is left over becomes goodwill. I start with the equity purchase price, then subtract the fair value of identifiable net assets. To get that fair value, I begin with the target's book equity and remove any goodwill already on its balance sheet, since that is replaced by the new calculation. Then I add write-ups: PP&E or inventory marked to fair value, and intangible assets that were not on the books, such as customer relationships, technology or brand names. In a stock deal those book write-ups do not change the tax basis, so they create a deferred tax liability equal to the write-up times the tax rate, which reduces net assets. For example, suppose the buyer pays $1,000M for a target with $600M of book equity and no existing goodwill. Asset write-ups total $200M, so at a 25% tax rate the new deferred tax liability is $50M. Identifiable net assets at fair value are $600M plus $200M minus $50M, or $750M, so goodwill is $1,000M minus $750M, or $250M. In an asset deal there would be no new deferred tax liability, because the tax basis steps up too.\"}}, {\"@type\": \"Question\", \"name\": \"Why do write-ups matter for the merger model?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"They create extra depreciation and amortization, which lowers pro forma earnings and affects accretion or dilution.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

**Practiced one out loud?** [Paste your answer into the free self-check and get a score in 30 seconds](https://johnnnmai.github.io/ai-engineer-interview-questions/answer-check/?track=ib)

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you can run a purchase price allocation step by step, including write-ups, existing goodwill and the deferred tax liability.

## Answer framework

1. Start with the equity purchase price paid for the target.
2. Subtract the target's book value of equity, after removing any existing goodwill.
3. Subtract write-ups of assets to fair value, including newly identified intangibles such as customer relationships.
4. Add back the new deferred tax liability on those write-ups in a stock deal (write-up x tax rate).
5. The remainder is new goodwill; it is tested for impairment, not amortized, for public companies under US GAAP.

## Sample answer

> Purchase price allocation assigns the price paid to the target's assets and liabilities at fair value, and whatever is left over becomes goodwill. I start with the equity purchase price, then subtract the fair value of identifiable net assets.
>
> To get that fair value, I begin with the target's book equity and remove any goodwill already on its balance sheet, since that is replaced by the new calculation. Then I add write-ups: PP&E or inventory marked to fair value, and intangible assets that were not on the books, such as customer relationships, technology or brand names. In a stock deal those book write-ups do not change the tax basis, so they create a deferred tax liability equal to the write-up times the tax rate, which reduces net assets.
>
> For example, suppose the buyer pays $1,000M for a target with $600M of book equity and no existing goodwill. Asset write-ups total $200M, so at a 25% tax rate the new deferred tax liability is $50M. Identifiable net assets at fair value are $600M plus $200M minus $50M, or $750M, so goodwill is $1,000M minus $750M, or $250M. In an asset deal there would be no new deferred tax liability, because the tax basis steps up too.

## Likely follow-ups

**Why do write-ups matter for the merger model?** They create extra depreciation and amortization, which lowers pro forma earnings and affects accretion or dilution.

## Common mistakes

- Forgetting to remove the target's existing goodwill.
- Leaving out the deferred tax liability on write-ups in a stock deal.
- Using book value instead of fair value for net assets.
- Forgetting identified intangibles, which inflates goodwill.

## Related questions

- [What is goodwill and how is it created?](../what-is-goodwill/)
- [What is the difference between an asset deal and a stock deal?](../asset-deal-vs-stock-deal/)
- [What is a deferred tax asset vs a deferred tax liability?](../deferred-tax-asset-vs-deferred-tax-liability/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on questions #68, #69 in the [full question bank](../../)._

{% include qpage-cta.html %}
