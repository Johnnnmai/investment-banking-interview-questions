# Batch 2 question pages (generated from seo_pages/batch2 drafts by merge_and_check.py). Same schema as question_pages_data.py.
PAGES = [
 {
  "slug": "cash-vs-accrual-accounting",
  "q": "What is the difference between cash and accrual accounting?",
  "desc": "Cash vs accrual accounting for investment banking interviews: when revenue and expenses are recorded, a worked example, and why the cash flow statement exists.",
  "level": "Easy",
  "src": [
   4
  ],
  "testing": "Whether you understand the basic recognition principle behind the income statement and can connect it to why cash flow and net income differ.",
  "steps": [
   "Cash accounting: record revenue when cash is received and expenses when cash is paid.",
   "Accrual accounting: record revenue when it is earned and expenses when they are incurred, matched to the period they relate to.",
   "Public companies report under accrual accounting (US GAAP or IFRS); cash accounting is mostly for very small businesses.",
   "Give an example: a sale on credit creates revenue and accounts receivable, but no cash yet.",
   "Link to the statements: because net income is on an accrual basis, the cash flow statement reconciles it to actual cash."
  ],
  "sample": [
   "Under cash accounting, you record revenue when the customer pays you and expenses when you pay a supplier. Under accrual accounting, you record revenue when you have earned it, meaning you delivered the product or service, and you record expenses in the period they help generate revenue, even if no cash has moved yet.",
   "For example, if a company delivers $100 of services in December and the client pays in February, accrual accounting shows $100 of December revenue and a $100 accounts receivable on the balance sheet. Cash accounting would show nothing until February. Likewise, wages earned by employees in December but paid in January are a December expense with an accrued liability under accrual accounting.",
   "Public companies use accrual accounting under US GAAP or IFRS because it matches revenue and costs to the right period. The trade-off is that net income no longer equals cash generated, which is exactly why we need the cash flow statement: it begins from net income, then reverses non-cash charges and reflects working capital movements to arrive at actual cash."
  ],
  "followups": [
   [
    "Can a profitable company run out of cash?",
    "Yes. Under accrual accounting it can book profits while cash is tied up in receivables, inventory or capex, so it can still miss payments."
   ]
  ],
  "mistakes": [
   "Saying accrual accounting records revenue when the invoice is paid.",
   "Forgetting the matching of expenses to the revenue they generate.",
   "Not connecting the difference to the cash flow statement.",
   "Claiming large companies can choose cash accounting for reporting."
  ],
  "related": [
   "walk-me-through-the-three-financial-statements",
   "what-is-working-capital",
   "what-is-deferred-revenue"
  ]
 },
 {
  "slug": "prepaid-expense-three-statements",
  "q": "A company prepays $12M of rent for the year: walk me through the three statements",
  "desc": "Prepaid rent three statement walk-through for IB interviews: the $12M payment, the expense over the year, net income, cash flow and balance sheet at 25% tax.",
  "level": "Medium",
  "src": [
   5
  ],
  "testing": "Whether you can separate the cash payment from the expense recognition, move working capital correctly through the cash flow statement and keep the balance sheet balanced.",
  "steps": [
   "At payment: no income statement effect.",
   "Cash flow statement: the increase in prepaid expenses reduces cash from operations by $12M.",
   "Balance sheet: cash down $12M, prepaid expenses up $12M; assets unchanged in total.",
   "Over the year: $12M rent expense, so pre-tax income falls $12M and net income falls $9M at a 25% tax rate.",
   "Cash flow: net income down $9M, plus the $12M decrease in prepaid, so cash from operations is up $3M; balance sheet: cash up $3M, prepaid down $12M, retained earnings down $9M."
  ],
  "sample": [
   "I would split it into the payment and the expense. When the company pays $12M upfront, nothing hits the income statement, because the rent has not been used yet. On the cash flow statement, prepaid expenses increase by $12M, which is a use of cash in operating activities, so cash falls by $12M. On the balance sheet, cash is down $12M and prepaid expenses are up $12M, so total assets do not change and it balances.",
   "Over the year the rent is used up. The income statement shows $12M of rent expense, so pre-tax income falls by $12M and, at a 25% tax rate, net income falls by $9M. On the cash flow statement, net income is down $9M, but the prepaid asset decreases by $12M, which is added back as a source of cash, so operating cash flow is up $3M. That $3M is the tax saving.",
   "On the balance sheet, cash is up $3M and prepaid expenses are down $12M, so assets are down $9M; retained earnings fall by $9M, so equity is down $9M and it balances. Looking at the full year combined, cash is down $9M and retained earnings are down $9M."
  ],
  "followups": [
   [
    "Why does cash go up by $3M when the expense is recognized?",
    "The expense lowers taxes by $3M, while the $12M itself was already paid earlier, so the non-cash expense is reversed through the prepaid change."
   ]
  ],
  "mistakes": [
   "Putting the $12M rent expense on the income statement at the time of payment.",
   "Forgetting the tax effect when the expense is recognized.",
   "Recording the payment in investing activities instead of operating.",
   "Showing cash falling by $12M again when the expense is recognized."
  ],
  "related": [
   "walk-me-through-the-three-financial-statements",
   "what-is-working-capital",
   "if-depreciation-goes-up-by-10-walk-me-through-the-three-statements"
  ]
 },
 {
  "slug": "what-is-goodwill",
  "q": "What is goodwill and how is it created?",
  "desc": "What is goodwill for IB interviews: purchase price above fair value of identifiable net assets, what it represents, impairment testing and bargain purchases.",
  "level": "Easy",
  "src": [
   6,
   68
  ],
  "testing": "Whether you know goodwill only comes from acquisitions, what drives it, and how it is treated after the deal.",
  "steps": [
   "Define it: the excess of the purchase price over the fair value of the target's identifiable net assets.",
   "It is created only in an acquisition; a company cannot record internally generated goodwill.",
   "It represents things not separately identifiable: expected synergies, workforce, market position, future growth.",
   "After the deal: not amortized under US GAAP for public companies or under IFRS; tested for impairment at least annually.",
   "Edge case: paying less than fair value of net assets creates a bargain purchase gain, not negative goodwill on the balance sheet."
  ],
  "sample": [
   "Goodwill is an intangible asset that appears only when one company acquires another. It equals the purchase price minus the fair value of the target's identifiable net assets. Identifiable means assets you can separate and value, such as PP&E, inventory, customer relationships, patents and brand names, less the liabilities you assume.",
   "For example, if a buyer pays $1,000M for a company whose identifiable net assets are worth $750M at fair value, after writing up assets and recognizing new intangibles, goodwill is $250M. That residual reflects what the buyer is paying for that cannot be recorded separately: expected synergies, an assembled workforce, market position and growth prospects.",
   "After the acquisition, goodwill stays on the balance sheet. Under US GAAP for public companies and under IFRS it is not amortized; instead it is tested for impairment at least once a year, and if the acquired business is worth less than its carrying value, it is written down. In the rare case where the price is below the fair value of net assets, the buyer records a bargain purchase gain on the income statement."
  ],
  "followups": [
   [
    "Can a company create goodwill by growing its own brand?",
    "No. Internally generated goodwill is not recorded; goodwill only arises from an acquisition."
   ]
  ],
  "mistakes": [
   "Calculating goodwill against book value instead of fair value of net assets.",
   "Saying goodwill is amortized for public companies under US GAAP.",
   "Forgetting identified intangibles, which reduce goodwill.",
   "Suggesting a company can record goodwill without an acquisition."
  ],
  "related": [
   "how-to-calculate-goodwill-in-an-acquisition",
   "goodwill-impairment-three-statements",
   "walk-me-through-a-merger-model"
  ]
 },
 {
  "slug": "goodwill-impairment-three-statements",
  "q": "How does a goodwill impairment affect the three statements?",
  "desc": "Goodwill impairment three statement walk-through: a $100M non-cash write-down, tax-deductible vs not, cash flow add-back and balance sheet effects.",
  "level": "Medium",
  "src": [
   7
  ],
  "testing": "Whether you treat impairment as a non-cash charge, handle the tax treatment correctly and balance the statements.",
  "steps": [
   "Income statement: $100M impairment charge reduces pre-tax income by $100M.",
   "Tax: goodwill impairment is usually not tax-deductible, so net income falls by the full $100M.",
   "Cash flow statement: add back the $100M non-cash charge, so cash is unchanged.",
   "Balance sheet: goodwill down $100M, retained earnings down $100M.",
   "If the interviewer says it is deductible at 25%: net income down $75M, cash up $25M, goodwill down $100M, equity down $75M."
  ],
  "sample": [
   "Say the company records a $100M goodwill impairment. On the income statement, it is a non-cash charge that reduces pre-tax income by $100M. In most cases goodwill impairment is not deductible for tax purposes, so there is no tax saving and net income falls by $100M.",
   "On the cash flow statement, net income is down $100M, but we add back the $100M impairment because it is non-cash, so cash from operations and total cash are unchanged. On the balance sheet, goodwill falls by $100M on the asset side, and retained earnings fall by $100M on the equity side, so it balances.",
   "If the interviewer tells me to assume the impairment is tax-deductible at a 25% rate, pre-tax income falls by $100M and net income by $75M. The cash flow statement starts with net income down $75M, adds back $100M, so cash is up $25M from lower taxes. On the balance sheet, cash is up $25M and goodwill is down $100M, so assets are down $75M, and retained earnings are down $75M. It balances."
  ],
  "followups": [
   [
    "Does an impairment change enterprise value?",
    "Not directly; it is a non-cash accounting write-down that recognizes value already lost, although it can signal weaker expected cash flows."
   ]
  ],
  "mistakes": [
   "Treating the impairment as a cash outflow.",
   "Applying a tax benefit by default without stating the assumption.",
   "Forgetting to add back the charge on the cash flow statement.",
   "Reducing cash on the balance sheet when it is non-deductible."
  ],
  "related": [
   "what-is-goodwill",
   "if-depreciation-goes-up-by-10-walk-me-through-the-three-statements",
   "how-to-calculate-goodwill-in-an-acquisition"
  ]
 },
 {
  "slug": "walk-me-through-the-enterprise-value-bridge",
  "q": "Walk me through the enterprise value bridge",
  "desc": "Enterprise value bridge for IB interviews: from diluted equity value to EV, adding debt, preferred stock and minority interest, subtracting cash and investments.",
  "level": "Medium",
  "src": [
   9,
   48,
   47
  ],
  "testing": "Whether you can build EV item by item and explain each adjustment with the consistency principle, beyond reciting the basic formula.",
  "steps": [
   "Start with equity value: diluted shares times share price.",
   "Add debt (including capital or finance leases) and preferred stock: other capital providers' claims on operations.",
   "Add noncontrolling (minority) interest, because 100% of the subsidiary's results are consolidated.",
   "Subtract cash and non-operating assets such as equity-method investments.",
   "Mention judgment items: unfunded pension liabilities and, depending on the metric, operating leases."
  ],
  "sample": [
   "Enterprise value measures what the operating business is worth to debt and equity holders together, so the bridge starts from equity value and adds or subtracts items to reach that. I start with diluted equity value: share price times diluted shares, using the treasury stock method for options and adding RSUs and in-the-money convertibles.",
   "Then I add the claims of other capital providers. Debt, including finance leases, and preferred stock both sit ahead of common equity, so a buyer of the whole business has to take them on. I add noncontrolling interest because if the company owns, say, 80% of a subsidiary, it consolidates 100% of that subsidiary's revenue and EBITDA, so EV must include the 20% it does not own to stay consistent with those metrics.",
   "Next I subtract cash and other non-operating assets, such as equity-method investments, because they are not part of operations and their income is not in EBITDA. Finally there are judgment items, such as unfunded pensions, which many bankers treat as debt-like. The test for every item is consistency: if the related earnings are in the metric I divide by, the claim belongs in EV."
  ],
  "followups": [
   [
    "Why subtract equity-method investments?",
    "Their EBITDA is not consolidated, so including their value in EV would mismatch EV/EBITDA."
   ]
  ],
  "mistakes": [
   "Using basic instead of diluted shares.",
   "Forgetting noncontrolling interest or preferred stock.",
   "Not explaining why items are added or subtracted.",
   "Subtracting all cash without considering minimum operating cash, if asked."
  ],
  "related": [
   "enterprise-value-vs-equity-value",
   "why-add-minority-interest-to-enterprise-value",
   "treasury-stock-method-diluted-shares"
  ]
 },
 {
  "slug": "why-add-minority-interest-to-enterprise-value",
  "q": "Why do you add minority interest (noncontrolling interest) to enterprise value?",
  "desc": "Why add minority interest to enterprise value: consolidation of 100% of a subsidiary's EBITDA, the consistency rule for multiples, and the equity investment mirror.",
  "level": "Medium",
  "src": [
   10
  ],
  "testing": "Whether you understand consolidation accounting and the consistency principle behind valuation multiples, not just the formula.",
  "steps": [
   "When a parent owns more than 50% of a subsidiary, it consolidates 100% of the subsidiary's revenue, EBITDA and assets.",
   "The portion it does not own is shown as noncontrolling interest.",
   "EV/EBITDA must match numerator and denominator: EBITDA includes 100% of the subsidiary, so EV must too.",
   "Adding noncontrolling interest captures the value belonging to the outside owners.",
   "Mirror case: equity-method investments (often 20-50% ownership) are subtracted, because their EBITDA is not consolidated."
  ],
  "sample": [
   "It comes down to consolidation and consistency. If a company owns more than 50% of a subsidiary, say 70%, accounting rules require it to consolidate 100% of the subsidiary's revenue, EBITDA and balance sheet. The 30% owned by outside shareholders is shown as noncontrolling interest in equity, and their share of earnings is subtracted near the bottom of the income statement.",
   "So the parent's reported EBITDA includes all of the subsidiary's EBITDA, including the 30% that belongs to someone else. The parent's market capitalization, though, only reflects the parent's own 70% stake. If I divided equity value plus debt minus cash by that EBITDA, the numerator would be too small for the denominator and the multiple would look artificially low. Adding noncontrolling interest puts the outside owners' 30% into EV, so both sides cover 100% of the subsidiary.",
   "The mirror case is an equity-method investment, where the company owns a minority stake without control. Its revenue and EBITDA are not consolidated, only its share of net income, so I subtract the value of the investment from EV for the same reason."
  ],
  "followups": [
   [
    "Should you use the book or market value of noncontrolling interest?",
    "Market value is better in theory, but book value is usually used because the subsidiary is rarely listed separately."
   ]
  ],
  "mistakes": [
   "Saying minority interest is added because it is a liability like debt.",
   "Mixing up the treatment of noncontrolling interest and equity investments.",
   "Not linking the answer to the EV/EBITDA consistency rule.",
   "Forgetting the more-than-50% consolidation threshold."
  ],
  "related": [
   "walk-me-through-the-enterprise-value-bridge",
   "enterprise-value-vs-equity-value",
   "how-to-build-a-comparable-companies-analysis"
  ]
 },
 {
  "slug": "what-is-deferred-revenue",
  "q": "What is deferred revenue and is it a source or use of cash?",
  "desc": "Deferred revenue for IB interviews: cash collected before delivery, why it is a liability, its three statement impact, and why an increase is a source of cash.",
  "level": "Easy",
  "src": [
   11,
   12
  ],
  "testing": "Whether you can explain deferred revenue as an obligation, move it correctly through working capital, and know which businesses depend on it.",
  "steps": [
   "Define it: cash received from customers for products or services not yet delivered.",
   "It is a liability because the company owes the customer delivery or a refund.",
   "When cash is collected: cash up, deferred revenue up; no revenue yet.",
   "When the service is delivered: revenue up, deferred revenue down; no cash movement.",
   "An increase in deferred revenue is a source of cash in operating cash flow, common for subscription software."
  ],
  "sample": [
   "Deferred revenue, also called unearned revenue, is cash a company has collected for goods or services it has not delivered yet. A software company that bills a customer $120 upfront for a one-year subscription has received the cash but has not earned the revenue, so it records a $120 liability. It is a liability because the company owes either the service or a refund.",
   "When the cash arrives, cash goes up by $120 and deferred revenue goes up by $120, with no revenue on the income statement. Each month, $10 is recognized as revenue and deferred revenue falls by $10. On the cash flow statement, the recognized revenue is in net income, but the decrease in deferred revenue is subtracted, because that revenue brought in no new cash.",
   "So an increase in deferred revenue is a source of cash: the company collected cash before recognizing the revenue, and the cash flow statement adds the increase back in operating activities. That is why fast-growing subscription businesses can generate operating cash flow well above net income. In an acquisition model, deferred revenue matters because the buyer takes on the obligation to deliver."
  ],
  "followups": [
   [
    "What happens to cash flow if a subscription business switches from annual to monthly billing?",
    "Deferred revenue shrinks, so operating cash flow falls in the transition even if revenue is unchanged."
   ]
  ],
  "mistakes": [
   "Calling deferred revenue an asset.",
   "Recording revenue when the cash is collected.",
   "Saying an increase in deferred revenue is a use of cash.",
   "Confusing deferred revenue with accounts receivable."
  ],
  "related": [
   "cash-vs-accrual-accounting",
   "what-is-working-capital",
   "walk-me-through-the-three-financial-statements"
  ]
 },
 {
  "slug": "lifo-vs-fifo",
  "q": "LIFO vs FIFO: how does each affect the financial statements when prices rise?",
  "desc": "LIFO vs FIFO with rising prices for IB interviews: COGS, net income, taxes, cash flow and inventory under each method, plus IFRS rules and the LIFO reserve.",
  "level": "Medium",
  "src": [
   13
  ],
  "testing": "Whether you can reason through the inventory flow assumption and its effects on all three statements, including taxes and cash.",
  "steps": [
   "Definitions: FIFO expenses the oldest inventory costs first; LIFO expenses the newest costs first.",
   "Rising prices under LIFO: higher COGS, lower gross profit, lower net income.",
   "Taxes and cash: lower taxable income, so lower taxes and higher cash flow under LIFO.",
   "Balance sheet: LIFO leaves older, cheaper costs in inventory, so inventory is lower.",
   "Context: LIFO is not allowed under IFRS; US LIFO users disclose a LIFO reserve to compare with FIFO companies."
  ],
  "sample": [
   "FIFO, first in first out, assumes the oldest inventory is sold first, so cost of goods sold uses older costs. LIFO, last in first out, assumes the newest inventory is sold first, so COGS uses the most recent costs.",
   "When prices are rising, the newest costs are the highest. Under LIFO, COGS is higher, so gross profit, operating income and net income are lower than under FIFO. Because taxable income is lower, the company pays less tax, which means operating cash flow is higher under LIFO, even though reported profit is lower. On the balance sheet, LIFO leaves the older, cheaper layers in inventory, so the inventory balance is lower and can be well below current replacement cost. FIFO is the reverse: higher profit and inventory, higher taxes and lower cash flow.",
   "Two practical points. LIFO is not permitted under IFRS, so it is mainly a US issue. And US companies using LIFO disclose a LIFO reserve, the difference between FIFO and LIFO inventory, which analysts use to put LIFO and FIFO companies on the same basis before comparing margins or multiples."
  ],
  "followups": [
   [
    "What happens if prices are falling?",
    "The effects reverse: LIFO gives lower COGS and higher net income and taxes than FIFO."
   ]
  ],
  "mistakes": [
   "Saying LIFO gives higher net income when prices rise.",
   "Forgetting the cash flow effect through taxes.",
   "Mixing up which costs stay in ending inventory.",
   "Not knowing LIFO is banned under IFRS."
  ],
  "related": [
   "walk-me-through-the-three-financial-statements",
   "how-to-build-a-comparable-companies-analysis",
   "what-is-working-capital"
  ]
 },
 {
  "slug": "unlevered-vs-levered-free-cash-flow",
  "q": "What is the difference between unlevered and levered free cash flow?",
  "desc": "Unlevered vs levered free cash flow for IB interviews: formulas, why interest and debt repayment matter, matching discount rates, and which value each gives.",
  "level": "Medium",
  "src": [
   49,
   14,
   15
  ],
  "testing": "Whether you can write both formulas, explain what capital providers each one belongs to, and match each to the correct discount rate and valuation output.",
  "steps": [
   "Unlevered FCF: cash flow available to all capital providers, before interest.",
   "Formula: EBIT x (1 - tax rate) + D&A - capex - increase in net working capital.",
   "Levered FCF: cash flow available to equity holders after interest and required debt repayments.",
   "Formula: net income + D&A - capex - increase in NWC - mandatory debt repayments (plus net new borrowing if modeled).",
   "Matching: unlevered FCF discounted at WACC gives enterprise value; levered FCF at cost of equity gives equity value."
  ],
  "sample": [
   "Unlevered free cash flow is the cash the business generates before any payments to lenders, so it belongs to all capital providers. I calculate it as EBIT times one minus the tax rate, plus D&A, minus capex, minus the increase in net working capital. Starting from EBIT means interest expense, and the tax shield it creates, are excluded, so the result does not depend on how the company is financed.",
   "Levered free cash flow is what is left for equity holders after the company services its debt. It starts from net income, which is already after interest, then adds D&A, subtracts capex and the increase in working capital, and subtracts mandatory debt repayments. If the company is borrowing new debt, net borrowing is added.",
   "The key is matching. Unlevered free cash flow goes with WACC, because it belongs to debt and equity holders together, and the DCF gives enterprise value. Levered free cash flow goes with cost of equity and gives equity value directly. Bankers usually use unlevered DCFs because capital structure can change and the result is easier to compare across companies; levered cash flow matters more in LBOs and for banks."
  ],
  "followups": [
   [
    "Why is unlevered FCF more common in DCFs?",
    "It separates operating value from financing choices, which can change, and avoids forecasting the debt schedule in detail."
   ]
  ],
  "mistakes": [
   "Discounting levered FCF at WACC.",
   "Subtracting interest when calculating unlevered FCF.",
   "Getting the sign of the working capital change wrong.",
   "Forgetting mandatory debt repayments in levered FCF."
  ],
  "related": [
   "walk-me-through-a-dcf",
   "what-is-wacc-and-how-do-you-calculate-it",
   "how-do-you-calculate-cost-of-equity"
  ]
 },
 {
  "slug": "stock-based-compensation-in-a-dcf",
  "q": "How should you treat stock-based compensation in free cash flow and a DCF?",
  "desc": "Stock-based compensation in a DCF for IB interviews: why the add-back overstates cash flow, treating SBC as a real cost, and avoiding double counting dilution.",
  "level": "Hard",
  "src": [
   16
  ],
  "testing": "Whether you recognize SBC as a real economic cost despite being non-cash, and can pick a consistent treatment without double counting.",
  "steps": [
   "Accounting: SBC is a non-cash expense, so it is added back in cash from operations.",
   "Economics: it is still a real cost, paid in shares instead of cash, and it dilutes existing shareholders.",
   "Preferred approach: treat SBC as a cash-like expense by not adding it back in unlevered FCF.",
   "Alternative: add it back but reflect expected future dilution in the share count, which is hard to estimate.",
   "Consistency: do one or the other, never both, and still use current diluted shares for existing awards."
  ],
  "sample": [
   "Accounting treats stock-based compensation as an expense on the income statement, but because no cash leaves the company, it is added back on the cash flow statement. If I simply copy that add-back into a DCF, I am treating employee pay as free, which overstates free cash flow and value, especially for tech companies where SBC can be a large share of revenue.",
   "Economically, SBC is a real cost: the company is paying employees with shares instead of cash, and that dilutes existing shareholders. A company could issue shares to investors for cash and use the cash to pay salaries; the effect on existing owners would be similar.",
   "So I prefer to treat SBC as if it were a cash expense: I do not add it back when calculating unlevered free cash flow. The alternative is to add it back but then increase the share count for all the future grants it implies, which is much harder to estimate. Either way, I pick one approach and avoid double counting, meaning I would not both deduct SBC and dilute for future grants. Existing options and RSUs still go into the diluted share count using the treasury stock method."
  ],
  "followups": [
   [
    "Does this matter more for some sectors?",
    "Yes, it matters most for tech and other high-growth companies where SBC is large relative to revenue and cash flow."
   ]
  ],
  "mistakes": [
   "Adding back SBC as if it were a free non-cash item like D&A.",
   "Deducting SBC and also diluting for the same future grants.",
   "Ignoring existing options and RSUs in diluted shares.",
   "Saying SBC has no impact on shareholders because it is non-cash."
  ],
  "related": [
   "unlevered-vs-levered-free-cash-flow",
   "treasury-stock-method-diluted-shares",
   "walk-me-through-a-dcf"
  ]
 },
 {
  "slug": "debt-funded-share-buyback-three-statements",
  "q": "A company issues $100M of debt to buy back stock: walk me through the three statements",
  "desc": "Debt-funded share buyback three statement walk-through: $100M of debt, financing cash flows, treasury stock, then 6% interest and the EPS accretion test.",
  "level": "Medium",
  "src": [
   17
  ],
  "testing": "Whether you can handle a pure financing transaction on day one, then trace the interest cost later and reason about EPS.",
  "steps": [
   "Day one income statement: no change.",
   "Cash flow statement: cash from financing +$100M from new debt and -$100M for the repurchase, so net cash is unchanged.",
   "Balance sheet: debt up $100M; equity down $100M through treasury stock; assets unchanged.",
   "Afterwards: at 6% interest, interest expense is $6M, net income falls $4.5M at 25% tax, and cash and retained earnings fall $4.5M.",
   "EPS: accretive if the after-tax cost of debt (4.5%) is below the company's earnings yield (E/P), since the share count falls."
  ],
  "sample": [
   "On the day of the transaction, nothing hits the income statement. On the cash flow statement, both legs sit in financing activities: issuing debt brings in $100M and repurchasing shares uses $100M, so net change in cash is zero. On the balance sheet, assets are unchanged, debt rises by $100M, and shareholders' equity falls by $100M through treasury stock. Liabilities plus equity are unchanged, so it balances.",
   "Over the following year, the company pays interest. If the rate is 6%, interest expense is $6M, pre-tax income falls by $6M, and net income falls by $4.5M at a 25% tax rate. Cash falls by $4.5M through the cash flow statement, and retained earnings fall by $4.5M on the balance sheet.",
   "The interesting question is EPS. Net income is lower, but there are fewer shares. The buyback is accretive if the after-tax cost of debt, here 4.5%, is lower than the earnings yield on the shares repurchased, which is earnings per share divided by the share price. A company trading at 15 times earnings has an earnings yield of about 6.7%, so this buyback would raise EPS."
  ],
  "followups": [
   [
    "Does the buyback change enterprise value?",
    "In the simple view no: equity value falls by $100M and debt rises by $100M; in practice taxes, signaling and distress risk can shift it."
   ]
  ],
  "mistakes": [
   "Showing the repurchase as an expense on the income statement.",
   "Putting the repurchase in investing activities.",
   "Forgetting the interest cost in later periods.",
   "Assuming every buyback raises EPS without comparing yields."
  ],
  "related": [
   "walk-me-through-the-three-financial-statements",
   "enterprise-value-vs-equity-value",
   "what-is-accretion-dilution"
  ]
 },
 {
  "slug": "deferred-tax-asset-vs-deferred-tax-liability",
  "q": "What is a deferred tax asset vs a deferred tax liability?",
  "desc": "Deferred tax asset vs deferred tax liability for IB interviews: book vs tax timing differences, accelerated depreciation, NOLs, valuation allowances, M&A write-ups.",
  "level": "Medium",
  "src": [
   18
  ],
  "testing": "Whether you understand that deferred taxes come from timing differences between book and tax accounting, and can give correct examples of each.",
  "steps": [
   "Source: book (GAAP) income and taxable income differ in timing.",
   "Deferred tax liability: lower taxes now, higher later, for example accelerated tax depreciation.",
   "Deferred tax asset: higher taxes now or future deductions, for example net operating losses or expenses recognized for books before they are deductible.",
   "Valuation allowance: reduces a DTA if it is unlikely to be used.",
   "M&A link: writing up assets in a stock deal creates a new DTL, because book basis rises but tax basis does not."
  ],
  "sample": [
   "Deferred taxes exist because companies keep two sets of rules: book accounting for reported financials and tax accounting for the tax authority. When income or expenses are recognized at different times under the two, the company records a deferred tax item to reflect taxes it will pay or save later.",
   "A deferred tax liability means the company has paid less tax so far than its book tax expense implies and will pay more later. The classic example is accelerated depreciation for tax purposes: tax depreciation is higher than book depreciation in the early years, so cash taxes are lower now and the difference reverses later. On the cash flow statement, an increase in a DTL is added back, since book tax expense exceeded cash tax.",
   "A deferred tax asset is the opposite: a future tax saving. Common sources are net operating losses that can offset future taxable income, and expenses such as warranty reserves that hit book income before they are deductible. If it is more likely than not that the company cannot use a DTA, it records a valuation allowance. In M&A, writing up a target's assets in a stock deal creates a new DTL, because book basis rises while tax basis stays the same."
  ],
  "followups": [
   [
    "How do NOLs affect valuation?",
    "They reduce future cash taxes, so their present value adds to value, subject to usage limits after an ownership change."
   ]
  ],
  "mistakes": [
   "Describing deferred taxes as taxes the company forgot to pay.",
   "Reversing the accelerated depreciation example.",
   "Forgetting valuation allowances on DTAs.",
   "Missing the DTL created by asset write-ups in stock deals."
  ],
  "related": [
   "how-to-calculate-goodwill-in-an-acquisition",
   "asset-deal-vs-stock-deal",
   "walk-me-through-the-three-financial-statements"
  ]
 },
 {
  "slug": "what-is-working-capital",
  "q": "What is working capital and how does an increase affect cash flow?",
  "desc": "Working capital for IB interviews: current assets minus current liabilities, operating NWC in models, why an increase uses cash, and when negative NWC is good.",
  "level": "Easy",
  "src": [
   20
  ],
  "testing": "Whether you know the definition used in models, can get the direction of the cash flow effect right, and understand what working capital says about a business.",
  "steps": [
   "Basic definition: current assets minus current liabilities.",
   "In models: operating working capital excludes cash and debt; mainly receivables, inventory and prepaids minus payables, accrued expenses and deferred revenue.",
   "An increase in net working capital is a use of cash and reduces operating cash flow.",
   "Examples: higher receivables or inventory tie up cash; higher payables or deferred revenue free it up.",
   "Negative working capital can be healthy, as in retailers or subscription businesses paid upfront."
  ],
  "sample": [
   "Working capital is current assets minus current liabilities. In valuation and modeling I use operating working capital, which excludes cash and debt because those are financing items. So it is mostly accounts receivable, inventory and prepaid expenses, minus accounts payable, accrued expenses and deferred revenue.",
   "An increase in net working capital is a use of cash. If receivables grow by $10M, the company booked revenue but has not collected that cash, so operating cash flow is $10M lower than net income would suggest. If inventory grows, cash went into stock sitting on shelves. Going the other way, if accounts payable grow, the company is holding onto cash longer before paying suppliers, which is a source of cash.",
   "Working capital also tells you about the business model. A growing manufacturer with long customer payment terms needs more working capital every year, which eats into free cash flow. A retailer that collects cash at the register but pays suppliers in 60 days, or a software company billing annually upfront, can run negative working capital, so growth actually releases cash. In a DCF, I subtract the increase in NWC each year."
  ],
  "followups": [
   [
    "Why exclude cash from operating working capital?",
    "Cash is treated separately in the EV bridge and as a financing item, so including it would double count."
   ]
  ],
  "mistakes": [
   "Saying an increase in working capital adds to cash flow.",
   "Including cash and short-term debt in operating working capital.",
   "Assuming negative working capital always signals distress.",
   "Forgetting deferred revenue as a working capital liability."
  ],
  "related": [
   "unlevered-vs-levered-free-cash-flow",
   "what-is-deferred-revenue",
   "walk-me-through-the-three-financial-statements"
  ]
 },
 {
  "slug": "capitalizing-vs-expensing",
  "q": "What is the difference between capitalizing and expensing a cost?",
  "desc": "Capitalizing vs expensing for IB interviews: the useful life test, effects on EBITDA, net income and cash flow sections, with a $10M machine worked example.",
  "level": "Easy",
  "src": [
   21
  ],
  "testing": "Whether you know when a cost is capitalized and how the choice moves EBITDA, net income and the cash flow statement, even though the cash paid is the same.",
  "steps": [
   "Expense: costs that benefit only the current period hit the income statement immediately.",
   "Capitalize: costs that benefit more than one year become an asset, such as PP&E or capitalized software, then are depreciated or amortized.",
   "Income statement: capitalizing raises current EBITDA and net income, then spreads the cost over time.",
   "Cash flow: capitalized costs appear as capex in investing; expensed costs reduce cash from operations.",
   "Total cash spent is the same; timing of expense and tax deductions differs."
  ],
  "sample": [
   "The test is how long the benefit lasts. A cost that is used up in the period, such as salaries or rent, is expensed. A cost that will benefit several years, such as a machine or a building, is capitalized: it goes on the balance sheet as an asset and is depreciated over its useful life.",
   "Take a $10M machine with a five-year life and a 25% tax rate. If it is capitalized, the first year shows $2M of depreciation, so EBITDA is unchanged and net income falls by $1.5M. On the cash flow statement, net income is down $1.5M, depreciation adds back $2M, so operating cash flow is up $0.5M, and capex in investing is $10M, giving net cash down $9.5M. If it were expensed, EBITDA would fall by $10M and net income by $7.5M, all in operating cash flow, so cash would fall by $7.5M, since the full deduction saves more tax in year one.",
   "That is why analysts watch capitalization choices. Aggressively capitalizing costs, such as software development, makes EBITDA and operating cash flow look stronger, so comparing companies may require adjusting EBITDA or looking at free cash flow after capex."
  ],
  "followups": [
   [
    "Which choice gives higher EBITDA?",
    "Capitalizing, because depreciation and amortization sit below EBITDA while expensed costs reduce it directly."
   ]
  ],
  "mistakes": [
   "Saying capitalizing saves cash; the cash paid is the same.",
   "Putting capex in operating cash flow.",
   "Forgetting the tax timing difference.",
   "Ignoring capitalization differences when comparing EBITDA across companies."
  ],
  "related": [
   "if-depreciation-goes-up-by-10-walk-me-through-the-three-statements",
   "unlevered-vs-levered-free-cash-flow",
   "walk-me-through-the-three-financial-statements"
  ]
 },
 {
  "slug": "operating-leases-asc-842",
  "q": "How do operating leases appear on the financial statements under ASC 842?",
  "desc": "Operating leases under ASC 842 for IB interviews: right-of-use asset and lease liability, straight-line lease cost, cash flow treatment, IFRS 16 and EV consistency.",
  "level": "Hard",
  "src": [
   23
  ],
  "testing": "Whether you know the current lease rules, can contrast operating and finance leases and IFRS 16, and apply the consistency rule for EV and EBITDA.",
  "steps": [
   "Balance sheet: a right-of-use (ROU) asset and a lease liability equal to the present value of lease payments.",
   "Income statement (US GAAP operating lease): a single straight-line lease cost within operating expenses, so it reduces EBITDA.",
   "Cash flow: operating lease payments are in cash from operations.",
   "Finance leases and IFRS 16: depreciation plus interest expense, so EBITDA excludes the lease cost; principal payments are financing cash flows.",
   "Valuation: under US GAAP operating leases, usually do not add lease liabilities to EV; with IFRS 16 EBITDA, add them for consistency."
  ],
  "sample": [
   "Since ASC 842 took effect, US companies put almost all leases longer than 12 months on the balance sheet. For an operating lease, the company records a right-of-use asset and a lease liability, both based on the present value of future lease payments.",
   "The income statement still looks like old rent expense: one straight-line lease cost inside operating expenses, so it reduces EBITDA. The payments are in cash from operations. A finance lease is different: the company records amortization of the asset and interest on the liability, so the cost sits below EBITDA, and principal repayments are financing cash flows. IFRS 16 treats almost all leases like finance leases.",
   "For valuation, the rule is consistency between EV and the metric. If I use US GAAP EBITDA for a company with operating leases, the lease cost has already reduced EBITDA, so I normally do not add operating lease liabilities to enterprise value; adding them would count the leases twice. If I am using IFRS EBITDA, which excludes lease costs, I add lease liabilities to EV. When comparing US and IFRS peers, I adjust them to the same basis first."
  ],
  "followups": [
   [
    "Why does IFRS 16 make EBITDA higher for retailers?",
    "Rent is replaced by depreciation and interest, both below EBITDA, so EBITDA rises even though the business has not changed."
   ]
  ],
  "mistakes": [
   "Saying operating leases are still off balance sheet.",
   "Adding operating lease liabilities to EV while using US GAAP EBITDA.",
   "Confusing operating and finance lease income statement treatment.",
   "Comparing US GAAP and IFRS companies' EBITDA without adjustment."
  ],
  "related": [
   "walk-me-through-the-enterprise-value-bridge",
   "how-to-build-a-comparable-companies-analysis",
   "enterprise-value-vs-equity-value"
  ]
 },
 {
  "slug": "treasury-stock-method-diluted-shares",
  "q": "How do you calculate diluted shares with the treasury stock method?",
  "desc": "Treasury stock method for IB interviews: in-the-money options, exercise proceeds used to buy back shares, a worked 105M diluted share example, RSUs and convertibles.",
  "level": "Medium",
  "src": [
   25
  ],
  "testing": "Whether you can compute diluted shares correctly and know which securities are included and how.",
  "steps": [
   "Include only in-the-money options and warrants: strike price below the current share price.",
   "Assume they are exercised; the company receives strike price times number of options.",
   "Assume the proceeds buy back shares at the current share price.",
   "Net new shares = options exercised - shares repurchased; add to basic shares.",
   "Other items: RSUs are added in full; convertibles use the if-converted method when in the money."
  ],
  "sample": [
   "The treasury stock method estimates how many extra shares options would create. I start by listing options and warrants and keep only those that are in the money, meaning their strike price is below the current share price, because no one would exercise an option to buy at a price above the market.",
   "Then I assume those options are exercised and the company uses the cash it receives to repurchase shares at the current price. Say a company has 100M basic shares, 10M options with a $10 strike, and a $20 share price. Exercise brings in $100M, which buys back 5M shares at $20. So the net new shares are 10M minus 5M, or 5M, and diluted shares are 105M.",
   "Beyond options, RSUs have no strike price, so I add them in full. Convertible bonds use the if-converted method: if the share price is above the conversion price, I add the shares from conversion and remove the bond from debt. For equity value, I multiply diluted shares by the share price. In an acquisition, I would use the offer price instead of the market price, which can bring more options into the money."
  ],
  "followups": [
   [
    "Why use the offer price in an M&A context?",
    "Options are valued at the price the buyer pays, so more options may be in the money and more shares created."
   ]
  ],
  "mistakes": [
   "Including out-of-the-money options.",
   "Forgetting the buyback step and adding all options.",
   "Applying the treasury stock method to RSUs, which have no proceeds.",
   "Using basic shares to calculate equity value."
  ],
  "related": [
   "walk-me-through-the-enterprise-value-bridge",
   "enterprise-value-vs-equity-value",
   "stock-based-compensation-in-a-dcf"
  ]
 },
 {
  "slug": "how-do-you-calculate-cost-of-equity",
  "q": "How do you calculate cost of equity?",
  "desc": "How to calculate cost of equity for IB interviews: CAPM with risk-free rate, beta and equity risk premium, a worked example, and when to add a size premium.",
  "level": "Easy",
  "src": [
   28,
   42
  ],
  "testing": "Whether you can apply CAPM, explain each input and where it comes from, and know common adjustments.",
  "steps": [
   "Use CAPM: cost of equity = risk-free rate + beta x equity risk premium.",
   "Risk-free rate: usually the yield on a long-term government bond, such as the 10-year Treasury, in the same currency as the cash flows.",
   "Beta: sensitivity to the market; for a public company use its own or a peer-based relevered beta.",
   "Equity risk premium: the extra return investors expect from stocks over the risk-free rate, from a chosen source.",
   "Adjustments: add a size or company-specific premium for small or risky companies when justified."
  ],
  "sample": [
   "I would use the capital asset pricing model. Cost of equity equals the risk-free rate plus beta times the equity risk premium. It represents the return equity investors require, given how risky the stock is relative to the market.",
   "For the risk-free rate, I use the yield on a long-term government bond in the currency of the cash flows, typically the 10-year Treasury for a US company. Beta measures how much the stock moves relative to the market; because a single company's historical beta is noisy, bankers often unlever the betas of comparable companies, take the median and relever it at the target's capital structure. The equity risk premium is the extra return investors expect from stocks over government bonds; banks usually take it from a standard data provider or internal guidance.",
   "As an example, with a 4% risk-free rate, a beta of 1.2 and a 5% equity risk premium, cost of equity is 4% plus 6%, or 10%. For a small or unusually risky company I might add a size premium. Cost of equity then feeds into WACC alongside the after-tax cost of debt."
  ],
  "followups": [
   [
    "Why is cost of equity higher than cost of debt?",
    "Equity holders are paid last and have no fixed return, and interest on debt is tax-deductible, so debt is cheaper."
   ]
  ],
  "mistakes": [
   "Adding beta and the risk premium instead of multiplying.",
   "Using a short-term bill rate for long-duration cash flows without reason.",
   "Relying on a single noisy historical beta.",
   "Mixing currencies between the risk-free rate and the cash flows."
  ],
  "related": [
   "what-is-wacc-and-how-do-you-calculate-it",
   "beta-for-a-private-company",
   "walk-me-through-a-dcf"
  ]
 },
 {
  "slug": "beta-for-a-private-company",
  "q": "What beta would you use for a private company?",
  "desc": "Beta for a private company in IB interviews: unlever comparable company betas, take the median, relever at the target's capital structure, plus a worked example.",
  "level": "Medium",
  "src": [
   29
  ],
  "testing": "Whether you can estimate beta when there is no stock price, and can apply the unlevering and relevering formulas correctly.",
  "steps": [
   "A private company has no traded stock, so you cannot regress its returns against the market.",
   "Pick comparable public companies with similar business risk.",
   "Unlever each beta: unlevered beta = levered beta / (1 + (1 - t) x D/E).",
   "Take the median or mean unlevered beta to remove the effect of each peer's capital structure.",
   "Relever at the target's or target industry's D/E: levered beta = unlevered beta x (1 + (1 - t) x D/E); consider a size premium in cost of equity."
  ],
  "sample": [
   "Since a private company has no stock price, I estimate beta from comparable public companies. Their observed betas reflect two things: business risk and financial risk from leverage. I want only the business risk, so I unlever each peer's beta with the formula: unlevered beta equals levered beta divided by one plus one minus the tax rate times debt-to-equity.",
   "For example, a peer with a levered beta of 1.3, a 25% tax rate and a debt-to-equity ratio of 0.4 has an unlevered beta of 1.3 divided by 1.3, which is 1.0. I do this for each peer and take the median, which is less sensitive to outliers.",
   "Then I relever at the capital structure I expect for the target, either its own or a typical structure for its industry. If the target's debt-to-equity ratio is 0.6, its levered beta is 1.0 times one plus 0.75 times 0.6, or 1.45. That beta goes into CAPM to get cost of equity. Because the target is private and often smaller, I may also add a size premium, and in some contexts a discount for lack of marketability is applied to the final value rather than the discount rate."
  ],
  "followups": [
   [
    "Why unlever and relever rather than just averaging peer betas?",
    "Peers have different leverage, which changes equity risk; unlevering isolates business risk so it can be applied to the target's own leverage."
   ]
  ],
  "mistakes": [
   "Averaging levered peer betas without adjusting for leverage.",
   "Relevering at the peers' capital structure instead of the target's.",
   "Getting the unlevering formula upside down.",
   "Choosing comps with different business risk."
  ],
  "related": [
   "how-do-you-calculate-cost-of-equity",
   "what-is-wacc-and-how-do-you-calculate-it",
   "how-to-build-a-comparable-companies-analysis"
  ]
 },
 {
  "slug": "gordon-growth-vs-exit-multiple",
  "q": "Gordon Growth vs exit multiple: which terminal value method should you use?",
  "desc": "Gordon Growth vs exit multiple terminal value for IB interviews: choosing a method, cross-checking implied multiples and growth rates, and a worked example.",
  "level": "Medium",
  "src": [
   31
  ],
  "testing": "Whether you can choose between terminal value methods for a situation and use each to sanity-check the other.",
  "steps": [
   "Exit multiple: terminal year EBITDA x a multiple from comps or precedents; common in banking and tied to market pricing.",
   "Gordon Growth: final-year FCF x (1 + g) / (discount rate - g); grounded in long-run cash flow fundamentals.",
   "Choose by context: exit multiple when good comps exist and for deal or LBO work; Gordon Growth for stable companies or when market multiples look distorted.",
   "Cross-check: compute the multiple implied by the Gordon value and the growth rate implied by the exit multiple.",
   "Red flags: implied growth above long-run economic growth, or an implied multiple far from current trading ranges."
  ],
  "sample": [
   "I would use both and let each check the other. The exit multiple method applies a multiple, usually EV/EBITDA from comparable companies, to the final projected year's EBITDA. Bankers like it because it reflects how the market values similar businesses and it matches how buyers think about exit values. Its weakness is that it imports today's market mood into a value years out.",
   "The Gordon Growth method assumes free cash flow grows at a constant rate forever: terminal value equals final-year FCF times one plus g, divided by the discount rate minus g. It ties value to fundamentals but is very sensitive to the growth and discount rate assumptions.",
   "So I cross-check. Say final-year free cash flow is $100M, EBITDA is $150M, WACC is 10% and long-term growth is 2%. Gordon Growth gives $102M divided by 8%, or about $1,275M, which implies roughly 8.5 times EBITDA. If comps trade at 8 to 10 times, that is reasonable. If an exit multiple of 14 times implied a perpetual growth rate of 5% or more, I would question the multiple, since a mature company cannot outgrow the economy forever."
  ],
  "followups": [
   [
    "Which method is more common on the sell side?",
    "Exit multiples are very common in banking, usually shown with a Gordon Growth cross-check."
   ]
  ],
  "mistakes": [
   "Picking one method without checking it against the other.",
   "Using a perpetual growth rate above long-run GDP growth.",
   "Applying an exit multiple to the wrong year's metric.",
   "Forgetting to discount the terminal value back to today."
  ],
  "related": [
   "what-is-terminal-value-and-how-do-you-calculate-it",
   "walk-me-through-a-dcf",
   "raise-discount-rate-by-1-percent-dcf"
  ]
 },
 {
  "slug": "dcf-with-negative-free-cash-flow",
  "q": "Can you do a DCF for a company with negative free cash flow?",
  "desc": "DCF with negative free cash flow for IB interviews: extend the projection period, model the path to profitability, use scenarios, cross-check with revenue multiples.",
  "level": "Hard",
  "src": [
   32,
   39
  ],
  "testing": "Whether you can adapt the DCF to early-stage or turnaround companies and recognize its limits, instead of saying it cannot be done.",
  "steps": [
   "Yes: a DCF values future cash flows, so negative near-term cash flow is fine if it turns positive later.",
   "Extend the projection period, often to 10 years or more, until cash flows reach a steady state.",
   "Model the drivers of the turn: revenue growth, gross margin, operating leverage and capex intensity.",
   "Calculate terminal value only once the business is mature; most value will sit in terminal value.",
   "Manage uncertainty: scenarios, sensitivity tables, a higher discount rate where justified, and cross-checks such as EV/revenue comps."
  ],
  "sample": [
   "Yes. A DCF values the cash flows a business will generate over its life, so negative cash flow today is not a problem as long as there is a credible path to positive cash flow. The negative years simply reduce value.",
   "The main change is the projection period. For a high-growth company burning cash, a five-year forecast might end while it is still losing money, and a terminal value based on that year would be meaningless. So I extend the forecast, often to ten years or more, until margins and growth reach something like a mature steady state, and only then calculate terminal value. I build the forecast from drivers: customer or revenue growth, gross margin, how operating expenses scale, and capex and working capital needs.",
   "The result is very sensitive, with most of the value in terminal value, so I would show scenarios, such as base, upside and downside, plus sensitivity tables on growth, margins and discount rate. I would also check whether the company has enough funding to reach profitability, since future dilution matters to equity value, and cross-check against EV/revenue or EV/gross profit multiples for similar companies."
  ],
  "followups": [
   [
    "What if the company may never become profitable?",
    "Then a DCF is not reliable; use liquidation value, comparable deals or option-style thinking, and say so."
   ]
  ],
  "mistakes": [
   "Saying a DCF cannot be used at all.",
   "Calculating terminal value while cash flows are still negative.",
   "Ignoring funding needs and future dilution.",
   "Presenting a single-point value without scenarios."
  ],
  "related": [
   "walk-me-through-a-dcf",
   "what-is-terminal-value-and-how-do-you-calculate-it",
   "ntm-vs-ltm-multiples"
  ]
 },
 {
  "slug": "how-to-build-a-comparable-companies-analysis",
  "q": "Walk me through how you would build a comparable companies analysis",
  "desc": "How to build a comparable companies analysis for IB interviews: picking peers, spreading financials, calendarizing, choosing multiples and applying a range.",
  "level": "Easy",
  "src": [
   33,
   34,
   46
  ],
  "testing": "Whether you know the full comps process end to end, including the cleanup steps that make multiples comparable.",
  "steps": [
   "Select peers: similar industry and business model, then size, growth, margins and geography.",
   "Gather data: filings for historicals, consensus estimates for projections, current share prices.",
   "Calculate equity value with diluted shares, then enterprise value with the EV bridge.",
   "Normalize: remove non-recurring items, calendarize to the same fiscal period and align accounting.",
   "Compute multiples (EV/Revenue, EV/EBITDA, P/E), look at the quartiles and median, and apply a justified range to the target's metrics."
  ],
  "sample": [
   "First I pick the peer set. The most important criterion is a similar business: same industry, products and customers. Then I narrow by size, growth, margins and geography, aiming for roughly five to fifteen companies. If the list is thin, I widen it and note which peers are the closest.",
   "Next I spread the financials. I pull historical figures from annual and quarterly filings and projections from consensus estimates, along with current share prices. For each company I calculate diluted equity value using the treasury stock method, then enterprise value by adding debt, preferred stock and noncontrolling interest and subtracting cash.",
   "Then I clean the numbers so they are comparable. I strip out one-time items such as restructuring charges or asset sale gains, calendarize everyone to the same period if fiscal years differ, and adjust for accounting differences such as lease treatment under IFRS. Only then do I calculate multiples, usually EV/Revenue, EV/EBITDA and P/E for the last twelve months and forward years. I look at the 25th percentile, median and 75th percentile, pick a range based on where the target fits on growth and margins, and apply it to the target's metrics to get an implied value range."
  ],
  "followups": [
   [
    "Why look at a range instead of the median alone?",
    "The target may deserve a premium or discount for growth, margins or risk, so a range shows judgment and uncertainty."
   ]
  ],
  "mistakes": [
   "Choosing peers by size alone rather than business similarity.",
   "Using basic shares or skipping the EV bridge.",
   "Mixing reported and adjusted EBITDA across peers.",
   "Comparing companies with different fiscal year-ends without calendarizing."
  ],
  "related": [
   "why-precedent-transactions-are-higher-than-comps",
   "ntm-vs-ltm-multiples",
   "walk-me-through-the-enterprise-value-bridge"
  ]
 },
 {
  "slug": "why-precedent-transactions-are-higher-than-comps",
  "q": "Why do precedent transactions usually give higher valuations than comps?",
  "desc": "Why precedent transactions usually exceed trading comps: control premiums, synergies and competitive auctions, plus when the pattern reverses and data limits.",
  "level": "Easy",
  "src": [
   36,
   38
  ],
  "testing": "Whether you understand the difference between a minority trading price and a price paid for control, and the limits of precedent data.",
  "steps": [
   "Comps reflect trading prices for small minority stakes; precedents reflect prices paid for control of whole companies.",
   "Control premium: buyers pay above the market price to gain control.",
   "Synergies: strategic buyers can pay part of expected synergies to the seller.",
   "Competitive processes: auctions push prices up.",
   "Caveats: market timing can reverse the pattern, and precedent data is often older and less complete."
  ],
  "sample": [
   "The main reason is control. A share price in the public market reflects what investors pay for a small minority stake. In an acquisition, the buyer is purchasing the entire company and gains control of its strategy, cash flows and assets, so it has to pay a premium over the current share price to convince shareholders to sell.",
   "Two other factors push the price higher. Strategic buyers often expect synergies, such as cost savings from combining operations, and in a competitive deal they end up paying part of that value to the seller. And sell-side processes are often auctions, where several bidders compete for the asset.",
   "There are exceptions. Precedent transactions happened at different points in the market cycle, so deals done in a weak market can show lower multiples than today's trading comps. Precedent data is also harder to work with: deals may be years old, private targets disclose limited financials, and each deal has its own circumstances. That is why I treat precedents as one input in a valuation and explain which deals are most relevant rather than taking a simple median."
  ],
  "followups": [
   [
    "When might precedents be lower than comps?",
    "When the deals happened in a weaker market or were distressed sales, while today's trading multiples are elevated."
   ]
  ],
  "mistakes": [
   "Saying precedents are higher because they are more accurate.",
   "Forgetting the role of synergies.",
   "Ignoring market timing differences between deals.",
   "Treating every precedent deal as equally relevant."
  ],
  "related": [
   "how-to-build-a-comparable-companies-analysis",
   "what-are-synergies",
   "walk-me-through-a-sell-side-m-and-a-process"
  ]
 },
 {
  "slug": "raise-discount-rate-by-1-percent-dcf",
  "q": "If you raise the discount rate by 1%, what happens to DCF value?",
  "desc": "Raising the discount rate by 1% in a DCF: value falls, a worked terminal value example with 2% growth, the exit multiple case and sensitivity tables.",
  "level": "Medium",
  "src": [
   50,
   41
  ],
  "testing": "Whether you can reason about the direction and rough size of the change, and explain why terminal value drives most of it.",
  "steps": [
   "Direction: value falls, because every future cash flow is discounted more heavily.",
   "Terminal value usually dominates, so the effect is driven by it.",
   "Gordon Growth: with g = 2%, going from 10% to 11% changes the terminal multiple of next-year cash flow from 1 / 8% = 12.5x to 1 / 9% = 11.1x, about 11% lower before discounting.",
   "Discounting: higher rates also shrink the present value of all projected cash flows; the overall drop is often around 10-15% for a typical company.",
   "Exit multiple method: terminal value itself does not change, only its present value, so the decline is smaller."
  ],
  "sample": [
   "The value goes down. A higher discount rate means each future cash flow is worth less today, and cash flows further in the future lose more value because the discounting compounds over more years.",
   "The size depends mostly on terminal value, which often makes up the majority of a DCF. With the Gordon Growth method and a 2% long-term growth rate, raising the discount rate from 10% to 11% changes the denominator from 8% to 9%. Terminal value as a multiple of next year's cash flow drops from 12.5 to about 11.1, roughly 11% lower, and then that smaller number is discounted at a higher rate too. Adding the smaller hit on the projected cash flows, a typical company might lose somewhere around 10% to 15% of its value, more if growth is high and the spread between discount rate and growth is narrow.",
   "If terminal value comes from an exit multiple, the terminal value itself does not change; only the present value factor falls, so the decline is smaller. Over five years, discounting at 11% instead of 10% lowers the present value of terminal value by roughly 4%. That is why I always show a sensitivity table across discount rates and growth rates or multiples."
  ],
  "followups": [
   [
    "Why does the effect get larger when growth is high?",
    "The Gordon denominator is the spread between discount rate and growth; a 1% change matters more when that spread is small."
   ]
  ],
  "mistakes": [
   "Saying value rises.",
   "Claiming a 1% rate change gives a 1% value change.",
   "Ignoring that terminal value drives most of the change.",
   "Treating the exit multiple and Gordon Growth methods as equally sensitive."
  ],
  "related": [
   "gordon-growth-vs-exit-multiple",
   "what-is-wacc-and-how-do-you-calculate-it",
   "walk-me-through-a-dcf"
  ]
 },
 {
  "slug": "ntm-vs-ltm-multiples",
  "q": "Why use NTM multiples instead of LTM multiples?",
  "desc": "NTM vs LTM multiples for IB interviews: why forward multiples reflect what markets price, when LTM is better, calendarizing and comparing high-growth companies.",
  "level": "Easy",
  "src": [
   35
  ],
  "testing": "Whether you understand which period to use for multiples in different situations and why.",
  "steps": [
   "LTM (last twelve months) uses actual reported results; NTM (next twelve months) uses projected results.",
   "Markets price stocks on future expectations, so NTM often aligns better with valuations.",
   "NTM helps for fast-growing companies, where LTM multiples look inflated, and after one-time events that distort LTM.",
   "LTM is objective and audited, useful when estimates are unreliable or unavailable, and standard for precedent transactions.",
   "Best practice: show both and calendarize so all companies use the same period."
  ],
  "sample": [
   "LTM multiples divide current value by the last twelve months of actual results, while NTM multiples use projections for the next twelve months. Both are useful, but they answer slightly different questions.",
   "I lean on NTM multiples because share prices reflect expectations about the future, not the past. That matters most for companies growing quickly: a software company growing 40% a year may look extremely expensive on LTM revenue but more reasonable on NTM revenue, and comparing it to slower peers on LTM would mislead. NTM numbers also smooth over one-time events, such as a year hit by a plant shutdown, that distort trailing results.",
   "LTM has advantages too. It is based on reported, audited figures rather than analyst estimates, which can be optimistic or unavailable for smaller and private companies. For precedent transactions, LTM at the time of the deal is standard because forward estimates at that point are often not disclosed. So in practice I show both, make sure every company is calendarized to the same period, and explain any big gap between them."
  ],
  "followups": [
   [
    "What does it mean if a company's NTM multiple is much lower than its LTM multiple?",
    "The market expects strong growth in the metric over the next year."
   ]
  ],
  "mistakes": [
   "Mixing LTM and NTM multiples in the same comparison.",
   "Forgetting to calendarize different fiscal years.",
   "Trusting consensus estimates without checking how many analysts cover the company.",
   "Using forward multiples for precedents when forward data at deal time is unavailable."
  ],
  "related": [
   "how-to-build-a-comparable-companies-analysis",
   "why-precedent-transactions-are-higher-than-comps",
   "dcf-with-negative-free-cash-flow"
  ]
 },
 {
  "slug": "what-is-accretion-dilution",
  "q": "What is accretion/dilution in M&A?",
  "desc": "Accretion/dilution in M&A for IB interviews: pro forma EPS vs standalone EPS, the adjustments that move it, the cost of funding shortcut and what it misses.",
  "level": "Medium",
  "src": [
   52
  ],
  "testing": "Whether you can explain the EPS test behind deals, list the pro forma adjustments and use the shortcut, while knowing its limits.",
  "steps": [
   "Definition: compare the buyer's pro forma EPS after the deal with its standalone EPS; higher is accretive, lower is dilutive.",
   "Pro forma net income: buyer + target net income + after-tax synergies - after-tax interest on new debt - lost after-tax interest on cash used - after-tax D&A from asset write-ups.",
   "Pro forma shares: buyer shares + new shares issued.",
   "Shortcut: compare the target's earnings yield at the purchase price with the weighted after-tax cost of the funding.",
   "Limits: EPS accretion does not mean the deal creates value."
  ],
  "sample": [
   "Accretion or dilution measures whether an acquisition raises or lowers the buyer's earnings per share. I calculate pro forma EPS for the combined company and compare it to the buyer's standalone EPS. If it goes up, the deal is accretive; if it goes down, dilutive.",
   "Pro forma net income starts with both companies' net income, adds after-tax synergies, then subtracts the after-tax cost of financing: interest on new debt, interest income lost on cash used, and extra depreciation and amortization from writing up the target's assets. The share count increases by any new shares issued to the target's shareholders.",
   "A quick shortcut is to compare yields. The target's earnings yield is its net income divided by the purchase price. The cost of each funding source is after-tax interest for debt, the lost after-tax interest yield for cash, and the buyer's earnings yield, the inverse of its P/E, for stock. If the target's yield is above the weighted cost, the deal is accretive before synergies and write-ups. Accretion is not the same as value creation, though: a buyer can overpay and still show accretion by using cheap debt, so I also look at return on invested capital and intrinsic value."
  ],
  "followups": [
   [
    "Can a deal be dilutive and still make sense?",
    "Yes, if it adds strategic value or growth that a short-term EPS test misses, for example buying a fast-growing but low-earning target."
   ]
  ],
  "mistakes": [
   "Forgetting the lost interest on cash used.",
   "Ignoring D&A from asset write-ups.",
   "Treating accretion as proof the deal creates value.",
   "Using pre-tax instead of after-tax financing costs."
  ],
  "related": [
   "walk-me-through-a-merger-model",
   "all-stock-deal-accretive-or-dilutive",
   "cash-vs-stock-consideration"
  ]
 },
 {
  "slug": "all-stock-deal-accretive-or-dilutive",
  "q": "In an all-stock deal, what determines if it is accretive or dilutive?",
  "desc": "All-stock deal accretion or dilution for IB interviews: buyer P/E vs purchase P/E, a worked example, and why synergies and write-ups can change the answer.",
  "level": "Medium",
  "src": [
   53
  ],
  "testing": "Whether you know the P/E rule for all-stock deals, why it works, and what can override it.",
  "steps": [
   "Rule: if the buyer's P/E is higher than the P/E it pays for the target, the deal is accretive; if lower, dilutive.",
   "Why: the buyer issues shares priced at its own P/E and receives earnings priced at the purchase P/E.",
   "Use the purchase price, including the premium, for the target's P/E, not its pre-deal trading P/E.",
   "Example: buyer at 20x, target bought at 15x: accretive before other adjustments.",
   "Overrides: synergies, D&A from write-ups and transaction costs can change the result."
  ],
  "sample": [
   "In an all-stock deal, it comes down to comparing P/E multiples. If the buyer's P/E is higher than the P/E it is paying for the target, the deal is accretive. If the buyer's P/E is lower, it is dilutive.",
   "The intuition is that the buyer is using its stock as currency. A buyer trading at 20 times earnings effectively pays for each new dollar of earnings with shares valued at 20 times that buyer's earnings, an earnings yield of 5%. If it acquires the target at 15 times earnings, it receives earnings with a 6.7% yield. Buying 6.7% earnings with 5% currency raises EPS. Reverse the numbers, a buyer at 12 times acquiring a target at 18 times, and EPS falls.",
   "Two details matter. The target's P/E must be based on the offer price including the premium, not its undisturbed share price. And the rule ignores other adjustments: synergies can turn a dilutive deal accretive, while extra amortization from writing up intangible assets and transaction costs can do the opposite. So I use the P/E rule as a quick answer and confirm with a full pro forma calculation."
  ],
  "followups": [
   [
    "Does the size of the target change the answer?",
    "Not the direction under the simple rule, but it changes the magnitude of accretion or dilution."
   ]
  ],
  "mistakes": [
   "Using the target's pre-deal trading P/E instead of the purchase P/E.",
   "Reversing the rule.",
   "Ignoring synergies and amortization from write-ups.",
   "Applying the P/E rule to deals funded with cash or debt."
  ],
  "related": [
   "what-is-accretion-dilution",
   "cash-vs-stock-consideration",
   "walk-me-through-a-merger-model"
  ]
 },
 {
  "slug": "what-are-synergies",
  "q": "What are synergies in M&A?",
  "desc": "Synergies in M&A for IB interviews: cost vs revenue synergies, why cost synergies are more credible, integration costs, phasing and valuing them in a deal.",
  "level": "Easy",
  "src": [
   55,
   56
  ],
  "testing": "Whether you can distinguish synergy types, judge their credibility and explain how they enter deal valuation and negotiation.",
  "steps": [
   "Definition: the extra value from combining two companies beyond their standalone values.",
   "Cost synergies: overlapping headcount, facilities, systems and better purchasing terms.",
   "Revenue synergies: cross-selling, broader distribution, pricing power; less certain and slower.",
   "Model them realistically: phase in over several years and subtract one-time integration costs.",
   "Valuation: the present value of net synergies sets an upper bound on how much premium a buyer can rationally pay."
  ],
  "sample": [
   "Synergies are the additional value created when two companies combine, compared with operating separately. They are a major reason strategic buyers can pay more than financial buyers.",
   "There are two main kinds. Cost synergies come from eliminating overlap: combining head offices, closing duplicate facilities, merging IT systems and negotiating better terms with suppliers thanks to greater scale. Revenue synergies come from selling more: cross-selling each company's products to the other's customers, using a larger sales network or gaining pricing power. Cost synergies are considered more reliable because management controls them, while revenue synergies depend on customers and competitors and often take longer, so investors and buyers usually discount them heavily.",
   "In a model, I phase synergies in over two or three years rather than assuming they arrive on day one, and subtract the one-time integration costs needed to achieve them, such as severance and system migrations. The present value of net synergies tells the buyer the most extra premium it could pay before the deal destroys value. In practice the buyer wants to keep a good share of that value, so how much of the synergies get paid away is a central negotiating point."
  ],
  "followups": [
   [
    "What are dis-synergies?",
    "Value lost from combining, such as customer losses, employee departures or contracts terminated after a change of control."
   ]
  ],
  "mistakes": [
   "Treating revenue synergies as being as certain as cost synergies.",
   "Assuming synergies arrive immediately.",
   "Forgetting one-time integration costs.",
   "Paying away all expected synergies in the premium."
  ],
  "related": [
   "why-precedent-transactions-are-higher-than-comps",
   "what-is-accretion-dilution",
   "walk-me-through-a-merger-model"
  ]
 },
 {
  "slug": "cash-vs-stock-consideration",
  "q": "Cash vs stock consideration in M&A: what are the trade-offs?",
  "desc": "Cash vs stock consideration in M&A for IB interviews: certainty, risk sharing, tax treatment, cost of capital, dilution, signaling and execution trade-offs.",
  "level": "Medium",
  "src": [
   60
  ],
  "testing": "Whether you can weigh the consideration choice from both buyer and seller perspectives, including tax and signaling.",
  "steps": [
   "Cash: certain value for sellers; buyer keeps all upside and risk; funded with cash on hand or debt.",
   "Stock: sellers share future upside and risk; no new debt; dilutes buyer shareholders.",
   "Cost: cash or debt is usually cheaper than issuing stock when the buyer's after-tax cost of debt is below its earnings yield.",
   "Tax: cash is generally taxable to selling shareholders; stock in a qualifying reorganization can defer tax.",
   "Signals and execution: paying in stock may suggest the buyer thinks its shares are fully valued, and can require a shareholder vote or registration."
  ],
  "sample": [
   "From the seller's side, cash gives certainty: they know exactly what they are getting and can walk away. Stock means they become shareholders of the combined company, so they share in the upside if the deal works and the downside if it does not. Taxes matter too: cash is generally a taxable event for the selling shareholders, while stock received in a qualifying tax-free reorganization can let them defer the tax.",
   "From the buyer's side, cash keeps all the future upside for existing shareholders and avoids dilution, but it uses up cash or adds debt, which raises financial risk. It is usually cheaper than stock when the after-tax cost of debt is below the buyer's earnings yield, which is why cash and debt deals are more often accretive. Stock preserves the balance sheet and makes sense for very large deals or when the buyer's shares trade at a high multiple.",
   "There are softer factors. Paying with stock can signal that the buyer views its own shares as fully valued, and it ties the price to the buyer's share price between signing and closing, so the parties negotiate a fixed exchange ratio or a fixed value with collars. Many deals use a mix to balance these trade-offs."
  ],
  "followups": [
   [
    "What is the difference between a fixed exchange ratio and a fixed price in a stock deal?",
    "A fixed ratio fixes the number of shares, so value moves with the buyer's stock; a fixed price fixes value, so the number of shares moves."
   ]
  ],
  "mistakes": [
   "Ignoring the seller's tax position.",
   "Forgetting that stock shares risk with the seller.",
   "Saying stock is always cheaper because it needs no cash.",
   "Ignoring signaling and price movement between signing and closing."
  ],
  "related": [
   "all-stock-deal-accretive-or-dilutive",
   "what-is-accretion-dilution",
   "asset-deal-vs-stock-deal"
  ]
 },
 {
  "slug": "walk-me-through-a-sell-side-m-and-a-process",
  "q": "Walk me through a sell-side M&A process",
  "desc": "Sell-side M&A process for IB interviews: preparation, teaser and CIM, buyer outreach, IOIs, management meetings, data room, final bids, signing and closing.",
  "level": "Easy",
  "src": [
   66,
   64
  ],
  "testing": "Whether you understand how a sale is run in stages and what analysts produce at each stage.",
  "steps": [
   "Preparation: pitch and mandate, financial model, valuation, teaser, confidential information memorandum (CIM) and buyer list.",
   "Marketing: contact buyers with the teaser, sign NDAs, send the CIM.",
   "First round: non-binding indications of interest (IOIs) with a value range; select a shortlist.",
   "Second round: management presentations, data room diligence, draft purchase agreement, final binding bids.",
   "Negotiation, signing, regulatory and other approvals, then closing."
  ],
  "sample": [
   "It usually starts once the bank wins the mandate. In preparation, the team builds the financial model and valuation, works with management on the key selling points, drafts a short anonymous teaser and a detailed confidential information memorandum, and builds a list of strategic and financial buyers. As an analyst, much of my time would go into the model, the CIM and the buyer list.",
   "Then the bank goes to market. It sends the teaser to potential buyers, those interested sign a non-disclosure agreement and receive the CIM. After a few weeks, buyers submit non-binding indications of interest with a value range and key terms. The seller and bank use those to choose a shortlist for the second round.",
   "In the second round, shortlisted buyers meet management, do detailed diligence in a virtual data room and comment on a draft purchase agreement. They then submit final, binding bids with a marked-up agreement and financing details. The seller negotiates with one or two leading bidders, signs the purchase agreement and announces the deal, and closing follows after regulatory and shareholder approvals. A broad auction maximizes competition, while a targeted process with a few buyers protects confidentiality."
  ],
  "followups": [
   [
    "Why run a two-round auction?",
    "It creates competition while limiting the time management spends on detailed diligence to serious bidders."
   ]
  ],
  "mistakes": [
   "Skipping the preparation phase.",
   "Confusing non-binding IOIs with binding bids.",
   "Forgetting regulatory approvals between signing and closing.",
   "Not mentioning what an analyst actually does in the process."
  ],
  "related": [
   "why-precedent-transactions-are-higher-than-comps",
   "walk-me-through-a-merger-model",
   "asset-deal-vs-stock-deal"
  ]
 },
 {
  "slug": "asset-deal-vs-stock-deal",
  "q": "What is the difference between an asset deal and a stock deal?",
  "desc": "Asset deal vs stock deal for IB interviews: what the buyer acquires, liabilities, tax basis step-up, double taxation for C-corps, and the 338(h)(10) election.",
  "level": "Hard",
  "src": [
   67
  ],
  "testing": "Whether you understand the legal and tax differences between acquisition structures and why buyers and sellers prefer different ones.",
  "steps": [
   "Stock deal: the buyer acquires the target's shares and takes on all assets and liabilities, known and unknown.",
   "Asset deal: the buyer acquires selected assets and chooses which liabilities to assume.",
   "Tax: an asset deal steps up the tax basis of assets, giving tax-deductible depreciation and goodwill amortization (15 years in the US).",
   "Seller view: a C-corp selling assets can face double taxation, so sellers usually prefer stock deals.",
   "Middle ground: a Section 338(h)(10) election treats a stock purchase as an asset purchase for tax purposes in certain cases."
  ],
  "sample": [
   "In a stock deal, the buyer purchases the target company's shares, so it gets the whole legal entity: all assets, contracts and liabilities, including unknown ones such as future lawsuits. It is simpler to execute because contracts and licenses usually stay with the company. In an asset deal, the buyer purchases specific assets and assumes only the liabilities it agrees to, which limits risk but can require transferring contracts and permits one by one.",
   "The biggest difference is tax. In an asset deal, the buyer records the assets at the purchase price for tax purposes, a step-up in tax basis, so it gets higher tax-deductible depreciation, and in the US goodwill is amortized for tax over 15 years. That lowers future cash taxes. In a stock deal, the tax basis usually carries over; any book write-up creates a deferred tax liability instead.",
   "Sellers often prefer stock deals. If a C-corporation sells its assets, the company pays tax on the gain and shareholders pay tax again when proceeds are distributed. So buyers tend to prefer asset deals and sellers stock deals, and the price reflects that. A Section 338(h)(10) election, available in certain cases such as buying a subsidiary or an S-corp, can give the buyer the tax step-up while legally buying stock."
  ],
  "followups": [
   [
    "Why might a buyer pay more in an asset deal?",
    "The tax step-up creates future tax savings, whose value can be shared with the seller through a higher price."
   ]
  ],
  "mistakes": [
   "Saying the buyer takes on all liabilities in an asset deal.",
   "Forgetting the tax basis step-up.",
   "Ignoring double taxation for C-corp sellers.",
   "Confusing book write-ups in stock deals with tax step-ups."
  ],
  "related": [
   "how-to-calculate-goodwill-in-an-acquisition",
   "deferred-tax-asset-vs-deferred-tax-liability",
   "cash-vs-stock-consideration"
  ]
 },
 {
  "slug": "how-to-calculate-goodwill-in-an-acquisition",
  "q": "How do you calculate goodwill in an acquisition (purchase price allocation)?",
  "desc": "Goodwill calculation in a purchase price allocation: equity purchase price, book value, asset write-ups, new deferred tax liability, with a worked $1,000M example.",
  "level": "Hard",
  "src": [
   68,
   69
  ],
  "testing": "Whether you can run a purchase price allocation step by step, including write-ups, existing goodwill and the deferred tax liability.",
  "steps": [
   "Start with the equity purchase price paid for the target.",
   "Subtract the target's book value of equity, after removing any existing goodwill.",
   "Subtract write-ups of assets to fair value, including newly identified intangibles such as customer relationships.",
   "Add back the new deferred tax liability on those write-ups in a stock deal (write-up x tax rate).",
   "The remainder is new goodwill; it is tested for impairment, not amortized, for public companies under US GAAP."
  ],
  "sample": [
   "Purchase price allocation assigns the price paid to the target's assets and liabilities at fair value, and whatever is left over becomes goodwill. I start with the equity purchase price, then subtract the fair value of identifiable net assets.",
   "To get that fair value, I begin with the target's book equity and remove any goodwill already on its balance sheet, since that is replaced by the new calculation. Then I add write-ups: PP&E or inventory marked to fair value, and intangible assets that were not on the books, such as customer relationships, technology or brand names. In a stock deal those book write-ups do not change the tax basis, so they create a deferred tax liability equal to the write-up times the tax rate, which reduces net assets.",
   "For example, suppose the buyer pays $1,000M for a target with $600M of book equity and no existing goodwill. Asset write-ups total $200M, so at a 25% tax rate the new deferred tax liability is $50M. Identifiable net assets at fair value are $600M plus $200M minus $50M, or $750M, so goodwill is $1,000M minus $750M, or $250M. In an asset deal there would be no new deferred tax liability, because the tax basis steps up too."
  ],
  "followups": [
   [
    "Why do write-ups matter for the merger model?",
    "They create extra depreciation and amortization, which lowers pro forma earnings and affects accretion or dilution."
   ]
  ],
  "mistakes": [
   "Forgetting to remove the target's existing goodwill.",
   "Leaving out the deferred tax liability on write-ups in a stock deal.",
   "Using book value instead of fair value for net assets.",
   "Forgetting identified intangibles, which inflates goodwill."
  ],
  "related": [
   "what-is-goodwill",
   "asset-deal-vs-stock-deal",
   "deferred-tax-asset-vs-deferred-tax-liability"
  ]
 },
 {
  "slug": "what-makes-a-good-lbo-candidate",
  "q": "What makes a good LBO candidate?",
  "desc": "What makes a good LBO candidate for IB and PE interviews: stable cash flow, low capex, strong market position, improvement levers, reasonable price and a clear exit.",
  "level": "Easy",
  "src": [
   72
  ],
  "testing": "Whether you can link each characteristic to how an LBO generates returns, particularly the ability to carry and repay debt.",
  "steps": [
   "Stable, predictable cash flows to service and repay debt.",
   "Low capex and working capital needs, so more cash flow goes to debt paydown.",
   "Strong market position and defensible margins that hold up in a downturn.",
   "Operational upside: cost savings, pricing, growth or add-on acquisitions.",
   "Sensible entry price, limited existing debt, a capable management team and a credible exit route."
  ],
  "sample": [
   "In an LBO the buyer funds a large part of the price with debt, so the first thing I look for is cash flow that can support that debt: stable, recurring revenue and predictable margins. A business with long-term contracts or subscription revenue is better than one whose earnings swing with commodity prices.",
   "Second, the cash has to be available. Low capital expenditure and modest working capital needs mean more free cash flow goes to paying down debt, which builds equity value. A strong market position helps margins hold up in a recession, when the debt is most dangerous. Hard assets can also help, since lenders lend more against collateral.",
   "Third, there should be room to improve. Private equity returns come from growing EBITDA, so I want identifiable levers: cost savings, pricing, expansion or add-on acquisitions in a fragmented market. And the deal has to make sense financially: a reasonable entry multiple, a management team that can execute, and a believable exit, whether a sale to a strategic buyer, another sponsor or an IPO, after a typical holding period of several years."
  ],
  "followups": [
   [
    "Why is a high-growth tech company with heavy cash burn a poor LBO candidate?",
    "It cannot service debt from current cash flow, so leverage adds default risk without the paydown that drives returns."
   ]
  ],
  "mistakes": [
   "Listing only high growth, ignoring cash flow stability.",
   "Forgetting capex and working capital needs.",
   "Ignoring entry valuation and exit options.",
   "Not linking characteristics back to debt capacity."
  ],
  "related": [
   "walk-me-through-an-lbo-model",
   "three-ways-pe-firms-create-value",
   "how-do-you-do-a-paper-lbo"
  ]
 },
 {
  "slug": "three-ways-pe-firms-create-value",
  "q": "What are the three ways private equity firms create value?",
  "desc": "The three ways private equity creates value for IB and PE interviews: EBITDA growth, multiple expansion and debt paydown, with an example of each lever.",
  "level": "Medium",
  "src": [
   73
  ],
  "testing": "Whether you can decompose LBO returns into their drivers and judge which ones are most reliable.",
  "steps": [
   "EBITDA growth: revenue growth and margin improvement raise enterprise value at exit.",
   "Multiple expansion: selling at a higher EV/EBITDA multiple than the entry multiple.",
   "Debt paydown (deleveraging): free cash flow repays debt, so more of the enterprise value belongs to equity.",
   "Leverage itself amplifies these effects on equity returns.",
   "Reliability: EBITDA growth and paydown are more controllable; multiple expansion depends on markets."
  ],
  "sample": [
   "Returns in a leveraged buyout come from three levers. The first is EBITDA growth: increasing revenue through pricing, new products or add-on acquisitions, and improving margins through cost savings or better purchasing. If EBITDA grows from $100M to $130M and the exit multiple is unchanged, enterprise value grows by 30%.",
   "The second is multiple expansion: selling at a higher multiple than you paid. That can happen because the company becomes larger, faster-growing or less risky, or simply because market conditions improve. Private equity firms usually do not count on it when they underwrite a deal, because it depends heavily on the market at exit.",
   "The third is debt paydown. The company uses its free cash flow to repay the acquisition debt, so even if enterprise value stays flat, the equity's share of that value grows. Leverage amplifies all three, because equity is a small share of the capital: a modest increase in enterprise value becomes a larger percentage gain on equity. When I evaluate a deal, I want most of the projected return to come from EBITDA growth and paydown, which the firm can influence, rather than from multiple expansion."
  ],
  "followups": [
   [
    "Which lever is the most dependable?",
    "Debt paydown and cost-driven EBITDA improvement, since the firm controls them more than exit market multiples."
   ]
  ],
  "mistakes": [
   "Listing leverage as a lever without explaining how it amplifies the others.",
   "Relying on multiple expansion to justify a deal.",
   "Forgetting that paydown requires real free cash flow.",
   "Confusing revenue growth with EBITDA growth."
  ],
  "related": [
   "multiple-expansion-vs-leverage",
   "what-makes-a-good-lbo-candidate",
   "irr-vs-moic"
  ]
 },
 {
  "slug": "irr-vs-moic",
  "q": "What is the difference between IRR and MOIC?",
  "desc": "IRR vs MOIC for IB and PE interviews: definitions, why timing matters, converting 2.0x into IRR over three and five years, and how dividend recaps affect each.",
  "level": "Easy",
  "src": [
   75
  ],
  "testing": "Whether you understand both return metrics, can convert between them for a simple case, and know why investors look at both.",
  "steps": [
   "MOIC (multiple on invested capital): total value returned divided by equity invested; ignores time.",
   "IRR (internal rate of return): the annualized discount rate that makes the net present value of all cash flows zero; reflects timing.",
   "Single entry and exit shortcut: IRR = MOIC^(1 / years) - 1.",
   "Example: 2.0x over 3 years is about 26% IRR; over 5 years about 15%.",
   "Use both: IRR can be boosted by early cash returns, while MOIC shows how much money was actually made."
  ],
  "sample": [
   "MOIC tells you how many times your money you got back: if a fund invests $100M and receives $250M in total, MOIC is 2.5x. It says nothing about how long that took. IRR is the annualized return, the discount rate at which the present value of all cash outflows and inflows equals zero, so it captures timing.",
   "With one investment at the start and one exit at the end, the conversion is simple: IRR equals MOIC raised to the power of one over the number of years, minus one. Doubling your money over three years is about a 26% IRR, while doubling over five years is about 15%. Same multiple, very different annual return.",
   "Investors look at both because each can be flattering on its own. A quick flip can show a high IRR on a small multiple, which may not move the needle for a large fund. Returning cash early, for example through a dividend recap, raises IRR more than MOIC. A long hold can show a strong multiple with a mediocre IRR. Limited partners want a high IRR, but they also need real multiples of cash back, so funds report both."
  ],
  "followups": [
   [
    "Roughly what IRR is 3.0x over five years?",
    "About 25%, since 3 to the power of 0.2 is roughly 1.25."
   ]
  ],
  "mistakes": [
   "Saying MOIC accounts for time.",
   "Converting 2.0x over five years as 20% a year by simple division.",
   "Ignoring interim cash flows such as dividends in IRR.",
   "Judging a deal on IRR alone."
  ],
  "related": [
   "walk-me-through-an-lbo-model",
   "what-is-a-dividend-recapitalization",
   "how-do-you-do-a-paper-lbo"
  ]
 },
 {
  "slug": "multiple-expansion-vs-leverage",
  "q": "Which creates more value in an LBO: one turn of multiple expansion or one more turn of leverage?",
  "desc": "One turn of multiple expansion vs one more turn of leverage in an LBO: a worked $100M EBITDA example showing why expansion creates value and leverage only magnifies.",
  "level": "Hard",
  "src": [
   76
  ],
  "testing": "Whether you can reason with numbers about LBO returns and see that leverage amplifies outcomes without creating enterprise value.",
  "steps": [
   "Set up: $100M EBITDA, bought at 10x ($1,000M) with 5x debt ($500M) and $500M equity; assume flat EBITDA, no paydown, interest ignored.",
   "One turn of multiple expansion: exit at 11x = $1,100M; equity = $600M, so 1.2x.",
   "One more turn of leverage: 6x debt ($600M), equity $400M; exit at 10x = $1,000M; equity still $400M, so 1.0x.",
   "Conclusion: multiple expansion adds enterprise value; leverage only magnifies whatever change in value occurs.",
   "Nuance: with EBITDA growth, extra leverage raises returns more, at higher risk and interest cost."
  ],
  "sample": [
   "I would show it with a simple example. Say the company has $100M of EBITDA and is bought at 10 times, so $1,000M, funded with 5 times debt, $500M, and $500M of equity. To isolate the effect, assume EBITDA stays flat, no debt is repaid and interest is ignored.",
   "With one turn of multiple expansion, the company exits at 11 times, or $1,100M. After repaying the $500M of debt, equity is worth $600M, so the investor gets 1.2 times its money. With one more turn of leverage instead, debt is $600M and equity only $400M. If the exit is at the same 10 times, enterprise value is $1,000M, equity is still $400M, and the multiple is 1.0 times. Nothing was created, because leverage does not change the value of the business.",
   "So in this setup multiple expansion creates more value. Leverage magnifies whatever happens to enterprise value. If EBITDA grew to $120M and the exit was at 10 times, equity would be $700M on $500M invested with 5 times debt, 1.4 times, versus $600M on $400M with 6 times debt, 1.5 times. But in a downturn extra leverage hurts returns more and adds interest cost and default risk."
  ],
  "followups": [
   [
    "Why might a sponsor still add leverage?",
    "With expected EBITDA growth, more debt boosts equity returns and IRR, as long as cash flow can safely cover interest."
   ]
  ],
  "mistakes": [
   "Saying leverage creates enterprise value.",
   "Not stating simplifying assumptions such as flat EBITDA and no paydown.",
   "Forgetting that leverage magnifies losses too.",
   "Ignoring interest costs when discussing more debt."
  ],
  "related": [
   "three-ways-pe-firms-create-value",
   "irr-vs-moic",
   "walk-me-through-an-lbo-model"
  ]
 },
 {
  "slug": "what-is-a-dividend-recapitalization",
  "q": "What is a dividend recapitalization?",
  "desc": "Dividend recapitalization explained for IB and PE interviews: new debt paying a dividend to owners, effects on IRR and MOIC, the three statements and the risks.",
  "level": "Medium",
  "src": [
   77
  ],
  "testing": "Whether you understand why sponsors use dividend recaps, how they affect returns and the statements, and what risks they create.",
  "steps": [
   "Definition: the company raises new debt and uses the proceeds to pay a dividend to its owners, often a private equity sponsor.",
   "Returns: cash comes back early, which raises IRR; MOIC changes little and can even fall after interest costs.",
   "Statements: debt up and cash up, then cash down and equity down for the dividend; later, interest expense lowers net income.",
   "Conditions: works when the company has paid down debt or grown EBITDA and credit markets are open.",
   "Risks: higher leverage and default risk, less cash for investment, and scrutiny from lenders and other stakeholders."
  ],
  "sample": [
   "A dividend recap is when a company borrows new debt and pays it out as a dividend to its shareholders. It is common in private equity: a few years after the buyout, once the company has repaid some debt or grown its EBITDA, the sponsor relevers it and takes cash out without selling the business.",
   "The main motivation is returns. Getting cash back earlier raises IRR, because IRR is sensitive to timing. It does not create much value in itself, so MOIC barely changes, and the extra interest can lower the eventual multiple. It also lets the sponsor recover some of its investment, reducing its risk while keeping ownership.",
   "On the statements, issuing the debt raises cash and debt; paying the dividend lowers cash and shareholders' equity, so the net effect is more debt and lower equity, with both shown in financing cash flows. Going forward, interest expense reduces net income and cash. The risk is that the company now carries more debt with less cushion, so a downturn can lead to distress, and less cash is left for investment. Lenders will only agree when cash flow is stable and credit markets are receptive."
  ],
  "followups": [
   [
    "Does a dividend recap hit the income statement on the day it happens?",
    "No. The dividend is a distribution of equity, not an expense; only the later interest expense flows through net income."
   ]
  ],
  "mistakes": [
   "Recording the dividend as an expense on the income statement.",
   "Claiming it creates enterprise value.",
   "Saying it raises MOIC significantly.",
   "Ignoring the added default risk."
  ],
  "related": [
   "irr-vs-moic",
   "walk-me-through-an-lbo-model",
   "three-ways-pe-firms-create-value"
  ]
 },
 {
  "slug": "why-not-use-ev-ebitda-for-banks",
  "q": "Why can't you use EV/EBITDA to value a bank?",
  "desc": "Why EV/EBITDA does not work for banks in IB interviews: debt and interest are operating items, so use P/E, P/TBV, ROE and a dividend discount model instead.",
  "level": "Hard",
  "src": [
   86
  ],
  "testing": "Whether you understand how a bank's business model breaks the usual separation of operating and financing items, and know the right alternatives.",
  "steps": [
   "For banks, deposits and borrowings are raw material, not just financing.",
   "Interest income and interest expense are core operating items, so EBITDA is not meaningful.",
   "Enterprise value is hard to define because separating operating debt from financing debt is arbitrary.",
   "Use equity-based metrics: P/E, price to tangible book value (P/TBV), linked to return on equity.",
   "Intrinsic approach: a dividend discount model constrained by regulatory capital requirements."
  ],
  "sample": [
   "EV/EBITDA works for most companies because it separates operations from financing. Enterprise value captures the operating business for all capital providers, and EBITDA measures operating earnings before interest. For a bank, that separation breaks down.",
   "A bank's business is borrowing money, through deposits and wholesale funding, and lending it out at a higher rate. Debt is its raw material, and interest expense is its biggest operating cost, the equivalent of cost of goods sold for a manufacturer. Excluding interest to get EBITDA would remove the core of the business, and deciding which liabilities count as debt for enterprise value would be arbitrary.",
   "So banks are valued on an equity basis. The most common multiples are P/E and price to tangible book value, and P/TBV is usually interpreted alongside return on tangible equity: a bank earning a higher return on equity than its cost of equity should trade above book value. For intrinsic value, analysts use a dividend discount model rather than an unlevered DCF, projecting dividends the bank can pay while keeping regulatory capital ratios, such as CET1, above required levels."
  ],
  "followups": [
   [
    "Why does return on equity drive a bank's price to book multiple?",
    "A bank earning above its cost of equity creates value on each dollar of book equity, so the market pays a premium to book."
   ]
  ],
  "mistakes": [
   "Saying banks have no EBITDA without explaining why it is meaningless.",
   "Proposing an unlevered DCF for a bank.",
   "Ignoring regulatory capital constraints on dividends.",
   "Using P/B without linking it to return on equity."
  ],
  "related": [
   "enterprise-value-vs-equity-value",
   "how-to-build-a-comparable-companies-analysis",
   "how-do-you-calculate-cost-of-equity"
  ]
 },
 {
  "slug": "walk-me-through-your-resume",
  "q": "Walk me through your resume (investment banking interview)",
  "desc": "How to answer walk me through your resume in investment banking interviews: a two-minute story, key decisions, why banking, why now, and a sample structure.",
  "level": "Fit",
  "src": [],
  "testing": "Whether you can tell a concise, logical story of your background that explains how you arrived at banking, and whether you communicate like someone a client could hear from.",
  "steps": [
   "Keep it to about two minutes; it is a story, not a recital of every line.",
   "Start with a brief anchor: school, major or where your interest began.",
   "Pick two or three experiences and, for each, state the decision you made and what it taught you.",
   "Connect them to why you want banking, using a concrete moment.",
   "End with why you are interviewing now, then stop and let the interviewer ask questions."
  ],
  "sample": [
   "I am a senior studying economics, and I first got interested in finance in my sophomore year, when I joined the student investment club and pitched a mid-cap industrial company. Building that valuation was the first time I saw how accounting, strategy and markets connect, and I wanted to do more of that work.",
   "That led me to a summer internship at a corporate development team at a manufacturing company. I helped screen acquisition targets and built a simple comps analysis for one of them. The most valuable part was seeing how a deal moved from idea to board discussion, and also how much the advisers on the other side shaped that process. Last summer I interned in valuation advisory, where I worked on purchase price allocations and learned to be careful with models under deadline pressure.",
   "Those experiences pointed me toward investment banking: I want to be closer to transactions from start to finish, work on a wide range of companies and learn fast in a demanding team. That is why I am recruiting for analyst roles now, and why I am interested in this group in particular."
  ],
  "followups": [
   [
    "Why did you choose that internship over others?",
    "Give a specific reason tied to what you wanted to learn, and avoid sounding like it was the only offer."
   ]
  ],
  "mistakes": [
   "Reading the resume line by line.",
   "Talking for five minutes without a clear thread.",
   "Leaving out why banking and why now.",
   "Inventing a neat story that does not match your actual choices.",
   "Ending with a long list of skills instead of stopping."
  ],
  "related": [
   "why-investment-banking",
   "why-our-bank",
   "what-is-your-greatest-weakness"
  ]
 },
 {
  "slug": "why-our-bank",
  "q": "Why do you want to work at our bank?",
  "desc": "How to answer why our bank in IB interviews: specific deal and sector strengths, what you learned from people at the firm, team structure and fit with your goals.",
  "level": "Fit",
  "src": [],
  "testing": "Whether you have done real research on the firm and can give reasons that would not apply equally to every other bank.",
  "steps": [
   "Give two or three specific reasons, not generic praise.",
   "Point to concrete strengths: a sector group, recent deal types, product strength or client base.",
   "Use what you learned in conversations with people at the firm (without dropping names you cannot back up).",
   "Link the firm's structure, such as group size or generalist program, to how you want to learn.",
   "Close by connecting it to your goals and the role you are interviewing for."
  ],
  "sample": [
   "There are three reasons. First, the firm's position in industrials and business services fits my interest. In researching the group I read about several recent sell-side processes for mid-sized industrial companies, and that is exactly the kind of work I enjoyed when I built a comps analysis for a manufacturing target during my corporate development internship.",
   "Second, the people I spoke with described a lean deal team structure, where analysts are close to senior bankers and clients. One associate told me she drafted sections of a management presentation in her first year and joined the client meetings to hear how it landed. I learn best when I can see how my work gets used, so that matters to me.",
   "Third, the analyst program lets first-years work across products before specializing, which would let me build broad technical skills while staying in a sector I care about. Put together, it is the place where I think I would learn the most and contribute the fastest, and that is why I am excited about this role."
  ],
  "followups": [
   [
    "Which other banks are you interviewing with?",
    "Answer honestly and briefly, keep the focus on firms with similar strengths, and explain why this one is a strong fit."
   ]
  ],
  "mistakes": [
   "Praising the bank's reputation or culture in generic terms.",
   "Giving reasons that apply to every bulge bracket or boutique.",
   "Citing deals you cannot discuss in any detail.",
   "Mentioning compensation or prestige as the main reason."
  ],
  "related": [
   "why-investment-banking",
   "walk-me-through-your-resume",
   "walk-me-through-a-sell-side-m-and-a-process"
  ]
 },
 {
  "slug": "what-is-your-greatest-weakness",
  "q": "What is your greatest weakness? (investment banking interview)",
  "desc": "How to answer what is your greatest weakness in IB interviews: pick a real but manageable weakness, show the steps you took, give evidence and avoid clichés.",
  "level": "Fit",
  "src": [],
  "testing": "Whether you are self-aware, honest and coachable, and whether the weakness you pick would not make you unsafe in an analyst role.",
  "steps": [
   "Pick a real weakness that is not a core requirement of the job.",
   "Describe it briefly with a specific situation where it showed up.",
   "Explain the concrete steps you took to address it.",
   "Show evidence of improvement, ideally with a recent example.",
   "Keep it short; do not disguise a strength as a weakness."
  ],
  "sample": [
   "My weakness has been holding back in group settings when I am not yet sure of my view. In my first internship, I noticed an issue in how our team was treating a one-time charge in a comps set, but I waited until I had double-checked everything before raising it. By then the senior person had already reviewed the draft, and we had to redo part of it. Nothing went out wrong, but it cost the team time.",
   "Since then I have worked on raising issues earlier, even when they are not fully confirmed. I now flag things in the form of a question, such as asking whether we meant to include a restructuring charge, which lets me speak up without overstating my confidence. I also joined a case competition team where I had to present our recommendation, which forced me to get comfortable sharing views in front of others.",
   "In my most recent internship, I raised a data inconsistency on the first day I saw it, and it turned out to be a real error in the source file. I still prefer to prepare before speaking, but I no longer let that delay important questions."
  ],
  "followups": [
   [
    "How would that weakness affect you as an analyst?",
    "Acknowledge the risk, such as delaying a flag on a model error, and explain the habit you now use to prevent it."
   ]
  ],
  "mistakes": [
   "Using clichés such as being a perfectionist or working too hard.",
   "Choosing a weakness central to the role, such as poor attention to detail, without strong evidence of fixing it.",
   "Describing the weakness without any steps taken.",
   "Rambling or sounding defensive."
  ],
  "related": [
   "walk-me-through-your-resume",
   "why-investment-banking",
   "why-our-bank"
  ]
 }
]
