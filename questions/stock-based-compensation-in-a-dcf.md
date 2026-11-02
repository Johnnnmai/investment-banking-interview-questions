---
layout: "question"
title: "How should you treat stock-based compensation in free cash flow and a DCF?"
description: "Stock-based compensation in a DCF for IB interviews: why the add-back overstates cash flow, treating SBC as a real cost, and avoiding double counting dilution."
permalink: "/questions/stock-based-compensation-in-a-dcf/"
slug: "stock-based-compensation-in-a-dcf"
tagline: "Investment banking interview question (Hard): how to answer it"
faq_jsonld: "{\"@context\": \"https://schema.org\", \"@type\": \"FAQPage\", \"mainEntity\": [{\"@type\": \"Question\", \"name\": \"How should you treat stock-based compensation in free cash flow and a DCF?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Accounting treats stock-based compensation as an expense on the income statement, but because no cash leaves the company, it is added back on the cash flow statement. If I simply copy that add-back into a DCF, I am treating employee pay as free, which overstates free cash flow and value, especially for tech companies where SBC can be a large share of revenue. Economically, SBC is a real cost: the company is paying employees with shares instead of cash, and that dilutes existing shareholders. A company could issue shares to investors for cash and use the cash to pay salaries; the effect on existing owners would be similar. So I prefer to treat SBC as if it were a cash expense: I do not add it back when calculating unlevered free cash flow. The alternative is to add it back but then increase the share count for all the future grants it implies, which is much harder to estimate. Either way, I pick one approach and avoid double counting, meaning I would not both deduct SBC and dilute for future grants. Existing options and RSUs still go into the diluted share count using the treasury stock method.\"}}, {\"@type\": \"Question\", \"name\": \"Does this matter more for some sectors?\", \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Yes, it matters most for tech and other high-growth companies where SBC is large relative to revenue and cash flow.\"}}]}"
---

[100 IB Interview Questions](../../) › [Questions](../) › This question

{% include qpage-cta.html %}

## What the interviewer is testing

Whether you recognize SBC as a real economic cost despite being non-cash, and can pick a consistent treatment without double counting.

## Answer framework

1. Accounting: SBC is a non-cash expense, so it is added back in cash from operations.
2. Economics: it is still a real cost, paid in shares instead of cash, and it dilutes existing shareholders.
3. Preferred approach: treat SBC as a cash-like expense by not adding it back in unlevered FCF.
4. Alternative: add it back but reflect expected future dilution in the share count, which is hard to estimate.
5. Consistency: do one or the other, never both, and still use current diluted shares for existing awards.

## Sample answer

> Accounting treats stock-based compensation as an expense on the income statement, but because no cash leaves the company, it is added back on the cash flow statement. If I simply copy that add-back into a DCF, I am treating employee pay as free, which overstates free cash flow and value, especially for tech companies where SBC can be a large share of revenue.
>
> Economically, SBC is a real cost: the company is paying employees with shares instead of cash, and that dilutes existing shareholders. A company could issue shares to investors for cash and use the cash to pay salaries; the effect on existing owners would be similar.
>
> So I prefer to treat SBC as if it were a cash expense: I do not add it back when calculating unlevered free cash flow. The alternative is to add it back but then increase the share count for all the future grants it implies, which is much harder to estimate. Either way, I pick one approach and avoid double counting, meaning I would not both deduct SBC and dilute for future grants. Existing options and RSUs still go into the diluted share count using the treasury stock method.

## Likely follow-ups

**Does this matter more for some sectors?** Yes, it matters most for tech and other high-growth companies where SBC is large relative to revenue and cash flow.

## Common mistakes

- Adding back SBC as if it were a free non-cash item like D&A.
- Deducting SBC and also diluting for the same future grants.
- Ignoring existing options and RSUs in diluted shares.
- Saying SBC has no impact on shareholders because it is non-cash.

## Related questions

- [What is the difference between unlevered and levered free cash flow?](../unlevered-vs-levered-free-cash-flow/)
- [How do you calculate diluted shares with the treasury stock method?](../treasury-stock-method-diluted-shares/)
- [Walk me through a DCF](../walk-me-through-a-dcf/)
- [All question deep dives](../)
- [All 100 investment banking interview questions with answers](../../)

_Based on question #16 in the [full question bank](../../)._

{% include qpage-cta.html %}
