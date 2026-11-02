---
layout: "question"
title: "A company issues $100M of debt to buy back stock: walk me through the three statements"
description: "Debt-funded share buyback three statement walk-through: $100M of debt, financing cash flows, treasury stock, then 6% interest and the EPS accretion test."
permalink: "/questions/debt-funded-share-buyback-three-statements/"
slug: "debt-funded-share-buyback-three-statements"
tagline: "Investment banking interview question (Medium): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"A company issues $100M of debt to buy back stock: walk me through the three statements\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"On the day of the transaction, nothing hits the income statement. On the cash flow statement, both legs sit in financing activities: issuing debt brings in $100M and repurchasing shares uses $100M, so net change in cash is zero. On the balance sheet, assets are unchanged, debt rises by $100M, and shareholders' equity falls by $100M through treasury stock. Liabilities plus equity are unchanged, so it balances. Over the following year, the company pays interest. If the rate is 6%, interest expense is $6M, pre-tax income falls by $6M, and net income falls by $4.5M at a 25% tax rate. Cash falls by $4.5M through the cash flow statement, and retained earnings fall by $4.5M on the balance sheet. The interesting question is EPS. Net income is lower, but there are fewer shares. The buyback is accretive if the after-tax cost of debt, here 4.5%, is lower than the earnings yield on the shares repurchased, which is earnings per share divided by the share price. A company trading at 15 times earnings has an earnings yield of about 6.7%, so this buyback would raise EPS.\"}}, {\"@type\": \"Question\", \"name\": \"Does the buyback change enterprise value?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"In the simple view no: equity value falls by $100M and debt rises by $100M; in practice taxes, signaling and distress risk can shift it.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

**Practiced one out loud?** [Paste your answer into the free self-check and get a score in 30 seconds](https://johnnnmai.github.io/ai-engineer-interview-questions/answer-check/?track=ib)

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you can handle a pure financing transaction on day one, then trace the interest cost later and reason about EPS.

## Answer framework

1. Day one income statement: no change.
2. Cash flow statement: cash from financing +$100M from new debt and -$100M for the repurchase, so net cash is unchanged.
3. Balance sheet: debt up $100M; equity down $100M through treasury stock; assets unchanged.
4. Afterwards: at 6% interest, interest expense is $6M, net income falls $4.5M at 25% tax, and cash and retained earnings fall $4.5M.
5. EPS: accretive if the after-tax cost of debt (4.5%) is below the company's earnings yield (E/P), since the share count falls.

## Sample answer

> On the day of the transaction, nothing hits the income statement. On the cash flow statement, both legs sit in financing activities: issuing debt brings in $100M and repurchasing shares uses $100M, so net change in cash is zero. On the balance sheet, assets are unchanged, debt rises by $100M, and shareholders' equity falls by $100M through treasury stock. Liabilities plus equity are unchanged, so it balances.
>
> Over the following year, the company pays interest. If the rate is 6%, interest expense is $6M, pre-tax income falls by $6M, and net income falls by $4.5M at a 25% tax rate. Cash falls by $4.5M through the cash flow statement, and retained earnings fall by $4.5M on the balance sheet.
>
> The interesting question is EPS. Net income is lower, but there are fewer shares. The buyback is accretive if the after-tax cost of debt, here 4.5%, is lower than the earnings yield on the shares repurchased, which is earnings per share divided by the share price. A company trading at 15 times earnings has an earnings yield of about 6.7%, so this buyback would raise EPS.

## Likely follow-ups

**Does the buyback change enterprise value?** In the simple view no: equity value falls by $100M and debt rises by $100M; in practice taxes, signaling and distress risk can shift it.

## Common mistakes

- Showing the repurchase as an expense on the income statement.
- Putting the repurchase in investing activities.
- Forgetting the interest cost in later periods.
- Assuming every buyback raises EPS without comparing yields.

## Related questions

- [Walk me through the three financial statements](../walk-me-through-the-three-financial-statements/)
- [Enterprise value vs equity value: what is the difference?](../enterprise-value-vs-equity-value/)
- [What is accretion/dilution in M&A?](../what-is-accretion-dilution/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on question #17 in the [full question bank](../../)._

{% include qpage-cta.html %}
