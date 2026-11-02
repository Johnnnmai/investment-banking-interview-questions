---
layout: "question"
title: "How do you calculate diluted shares with the treasury stock method?"
description: "Treasury stock method for IB interviews: in-the-money options, exercise proceeds used to buy back shares, a worked 105M diluted share example, RSUs and convertibles."
permalink: "/questions/treasury-stock-method-diluted-shares/"
slug: "treasury-stock-method-diluted-shares"
tagline: "Investment banking interview question (Medium): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"How do you calculate diluted shares with the treasury stock method?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"The treasury stock method estimates how many extra shares options would create. I start by listing options and warrants and keep only those that are in the money, meaning their strike price is below the current share price, because no one would exercise an option to buy at a price above the market. Then I assume those options are exercised and the company uses the cash it receives to repurchase shares at the current price. Say a company has 100M basic shares, 10M options with a $10 strike, and a $20 share price. Exercise brings in $100M, which buys back 5M shares at $20. So the net new shares are 10M minus 5M, or 5M, and diluted shares are 105M. Beyond options, RSUs have no strike price, so I add them in full. Convertible bonds use the if-converted method: if the share price is above the conversion price, I add the shares from conversion and remove the bond from debt. For equity value, I multiply diluted shares by the share price. In an acquisition, I would use the offer price instead of the market price, which can bring more options into the money.\"}}, {\"@type\": \"Question\", \"name\": \"Why use the offer price in an M&A context?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Options are valued at the price the buyer pays, so more options may be in the money and more shares created.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you can compute diluted shares correctly and know which securities are included and how.

## Answer framework

1. Include only in-the-money options and warrants: strike price below the current share price.
2. Assume they are exercised; the company receives strike price times number of options.
3. Assume the proceeds buy back shares at the current share price.
4. Net new shares = options exercised - shares repurchased; add to basic shares.
5. Other items: RSUs are added in full; convertibles use the if-converted method when in the money.

## Sample answer

> The treasury stock method estimates how many extra shares options would create. I start by listing options and warrants and keep only those that are in the money, meaning their strike price is below the current share price, because no one would exercise an option to buy at a price above the market.
>
> Then I assume those options are exercised and the company uses the cash it receives to repurchase shares at the current price. Say a company has 100M basic shares, 10M options with a $10 strike, and a $20 share price. Exercise brings in $100M, which buys back 5M shares at $20. So the net new shares are 10M minus 5M, or 5M, and diluted shares are 105M.
>
> Beyond options, RSUs have no strike price, so I add them in full. Convertible bonds use the if-converted method: if the share price is above the conversion price, I add the shares from conversion and remove the bond from debt. For equity value, I multiply diluted shares by the share price. In an acquisition, I would use the offer price instead of the market price, which can bring more options into the money.

## Likely follow-ups

**Why use the offer price in an M&A context?** Options are valued at the price the buyer pays, so more options may be in the money and more shares created.

## Common mistakes

- Including out-of-the-money options.
- Forgetting the buyback step and adding all options.
- Applying the treasury stock method to RSUs, which have no proceeds.
- Using basic shares to calculate equity value.

## Related questions

- [Walk me through the enterprise value bridge](../walk-me-through-the-enterprise-value-bridge/)
- [Enterprise value vs equity value: what is the difference?](../enterprise-value-vs-equity-value/)
- [How should you treat stock-based compensation in free cash flow and a DCF?](../stock-based-compensation-in-a-dcf/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on question #25 in the [full question bank](../../)._

{% include qpage-cta.html %}
