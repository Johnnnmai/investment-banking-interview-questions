# 100 Investment Banking Interview Questions and Answers (2026)

_Last updated: November 1, 2026_ · Every question answered · Tagged by topic and difficulty · Free, no sign-up

100 technical IB interview questions with concise model answers — accounting, valuation, M&A, LBO, and current events, organized the way a superday is.

### Quick start

🆓 **Top 30 questions** — [Free 13-page guide with model answers](https://sirjohnnymai.gumroad.com/l/ib-top-30-questions?utm_source=github&utm_medium=readme&utm_campaign=line26_20261101&utm_content=investment-banking-interview-questions)

🆓 **Self-check** — [Paste your answer and get a score in 30 seconds](https://johnnnmai.github.io/ai-engineer-interview-questions/answer-check/?track=ib&utm_source=github&utm_medium=readme&utm_campaign=line26_20261101&utm_content=investment-banking-interview-questions)

🆓 **Question deep dives** — [Answer frameworks, sample answers and common mistakes for 50 of the most-asked questions](questions/)

---

**How to drill:** answer out loud first, then read the answer. Score yourself 1 to 5: 1 = can't start; 3 = right answer but shaky on the why; 5 = clean answer that handles the follow-up. Re-drill anything under 4. Numbers use a 25% tax rate unless stated.

## Contents

1. [Accounting (1-25)](#accounting-1-25)
2. [Valuation (26-50)](#valuation-26-50)
3. [M&A (51-70)](#ma-51-70)
4. [LBO (71-85)](#lbo-71-85)
5. [Industry, Restructuring and Current Events (86-100)](#industry-restructuring-and-current-events-86-100)
6. [Fit questions (bonus)](#fit-questions-bonus)
7. [How to prepare in two weeks](#how-to-prepare-in-two-weeks)

## Must-know before any superday

| Topic | Questions |
|---|---|
| Three statements and how they link | 1, 2 |
| $10 depreciation walk-through | 3 |
| Enterprise value vs equity value and the bridge | 8-10 |
| Walk me through a DCF, WACC, terminal value | 26-31 |
| Comps and precedents | 33-38 |
| Merger model and accretion/dilution | 51-53 |
| LBO and a paper LBO | 71-75 |

## Accounting (1-25)

### 1. Walk me through the three financial statements.

*Fundamentals · Easy*

The income statement shows revenue, expenses and net income over a period. The balance sheet shows assets, liabilities and shareholders' equity at a point in time, and assets must equal liabilities plus equity. The cash flow statement starts with net income, adjusts for non-cash items and changes in working capital (cash flow from operations), then adds cash flow from investing and from financing, giving the net change in cash.

> Follow-up: Which statement would you pick if you could only have one? A common answer is the cash flow statement, because it shows real cash generation, and you can roughly rebuild the rest with a beginning balance sheet.

### 2. How do the three statements link together?

*Linkages · Easy*

Net income from the income statement is the first line of the cash flow statement. Non-cash charges (such as depreciation) and changes in balance sheet working capital items adjust it to cash from operations; capital expenditures, debt and equity flows appear in investing and financing. The net change in cash updates cash on the balance sheet, and net income (less dividends) flows into retained earnings, which keeps the balance sheet balanced.

### 3. If depreciation goes up by $10, walk me through the impact on all three statements.

*Linkages · Medium*

Assume a 25% tax rate. Income statement: operating income and pre-tax income fall by $10; net income falls by $7.50. Cash flow statement: net income is down $7.50, but depreciation is a non-cash expense, so you add back $10; cash is up $2.50 (the tax saving). Balance sheet: cash +$2.50, net PP&E -$10, so total assets are down $7.50; retained earnings fall by $7.50, so liabilities plus equity are also down $7.50. It balances.

> Common mistake: saying cash goes down. Depreciation does not use cash; the only cash effect is lower taxes.

### 4. What is the difference between cash-based and accrual-based accounting?

*Fundamentals · Easy*

Accrual accounting records revenue when earned and expenses when incurred, regardless of when cash moves; it is required under US GAAP for most public companies. Cash accounting records transactions only when cash is received or paid. That gap is why the cash flow statement exists: it reconciles accrual-based net income back to cash.

### 5. A company prepays $12M in rent for the year. Walk me through the impact.

*Accruals · Medium*

At payment (25% tax rate): no income statement effect yet. Cash falls by $12M and a prepaid expense asset rises by $12M; on the cash flow statement the increase in prepaid expenses is a $12M use of cash in operating activities. As each month passes, $1M of rent expense is recognized and the prepaid balance falls by $1M. Over the full year: pre-tax income -$12M, net income -$9M; on the cash flow statement the $12M decline in prepaid expenses is added back, so that period's operating cash flow is +$3M (the tax saving). Across both steps, cash is down $9M, prepaid is back to zero and retained earnings are down $9M.

### 6. What is goodwill? How is it created?

*Acquisitions · Easy*

Goodwill is the amount by which the purchase price of an acquired company exceeds the fair value of its identifiable net assets (after writing up assets and recognizing intangibles such as customer relationships and technology). It represents things like brand value, assembled workforce and expected synergies that cannot be separately identified. Under US GAAP it is not amortized for public companies; it is tested for impairment at least annually.

### 7. How does a goodwill impairment affect the three statements?

*Acquisitions · Medium*

Say a $100 impairment that is not tax-deductible (the usual case for goodwill from a stock deal). Income statement: a $100 impairment charge reduces pre-tax and net income by $100. Cash flow statement: net income -$100, add back the $100 non-cash charge, so cash is unchanged. Balance sheet: goodwill -$100 and retained earnings -$100. If the impairment were tax-deductible at 25%, net income would fall $75 and cash would rise $25.

> Follow-up: Why is it not usually deductible? Goodwill from a stock purchase has no tax basis, unlike goodwill from an asset deal, which is amortized for US tax over 15 years.

### 8. What is the difference between enterprise value and equity value?

*Valuation · Easy*

Equity value is the value of the company's shares to common shareholders: diluted shares outstanding times the share price. Enterprise value is the value of the core operating business to all capital providers (debt, preferred, noncontrolling interests and equity), excluding non-operating assets such as excess cash. Use EV with metrics available to all capital providers (revenue, EBITDA, EBIT, unlevered FCF) and equity value with metrics after interest (net income, EPS, levered FCF).

### 9. Walk me through the enterprise value bridge.

*Valuation · Medium*

Start with equity value (diluted shares times share price). Add debt, preferred stock and noncontrolling interests, plus other debt-like items if relevant (for example unfunded pension obligations, and lease liabilities when the metric excludes lease expense). Subtract cash and cash equivalents and non-operating assets such as equity-method investments. The result is enterprise value.

### 10. Why do we add back minority interest in the EV bridge?

*Valuation · Hard*

When a parent owns more than 50% of a subsidiary, it consolidates 100% of that subsidiary's revenue and EBITDA even though it owns less than all of it. Adding the noncontrolling interest makes the numerator (EV) consistent with a denominator (EBITDA) that includes the whole subsidiary. Equity-method investments (under 50%) are subtracted for the opposite reason: their EBITDA is not consolidated.

### 11. What is deferred revenue? Give an example.

*Accruals · Easy*

Deferred revenue is cash received for goods or services not yet delivered; it is a liability until earned. Example: a customer pays $1,200 upfront for a 12-month software subscription. The company records $1,200 of deferred revenue and recognizes $100 of revenue each month as it delivers the service.

### 12. Is deferred revenue a source or use of cash?

*Cash flow · Medium*

An increase in deferred revenue is a source of cash: the company has collected cash before recognizing revenue, so it appears as a positive working capital adjustment in cash flow from operations. A decrease is a use of cash.

### 13. What is the difference between LIFO and FIFO? How does each affect the financial statements in an inflationary environment?

*Inventory · Medium*

FIFO expenses the oldest inventory costs first; LIFO expenses the newest. With rising prices, LIFO gives higher cost of goods sold, lower net income and lower taxes (so higher cash flow) and a lower ending inventory balance; FIFO gives lower COGS, higher net income, higher taxes and an inventory balance closer to current cost. LIFO is allowed under US GAAP but not IFRS.

### 14. How do you calculate free cash flow to firm (FCFF)?

*Cash flow · Easy*

FCFF (unlevered free cash flow) = EBIT x (1 - tax rate) + depreciation and amortization - capital expenditures - increase in net working capital. Equivalently, cash flow from operations + after-tax interest expense - capital expenditures. It is the cash available to all capital providers, before debt payments.

### 15. How do you calculate free cash flow to equity (FCFE)?

*Cash flow · Medium*

FCFE (levered free cash flow) = net income + D&A - capital expenditures - increase in net working capital + net borrowing (new debt minus repayments). Equivalently, FCFF - interest x (1 - tax rate) + net borrowing. It is the cash available to equity holders and is discounted at the cost of equity.

### 16. What is stock-based compensation? Why do some people add it back in FCFF?

*SBC · Hard*

Stock-based compensation pays employees in shares or options instead of cash. It is a non-cash expense, so it is added back on the cash flow statement. It is still a real cost to shareholders because it dilutes them. If you add SBC back to free cash flow, you must reflect the future dilution in the share count; the more conservative approach is to treat it as a cash-like expense and not add it back.

> Common mistake: adding SBC back and ignoring future dilution, which overstates value per share.

### 17. A company issues $100M in debt to buy back stock. Walk me through the impact on all three statements.

*Capital structure · Hard*

At the transaction: debt +$100M and shareholders' equity -$100M (treasury stock), so the balance sheet still balances; on the cash flow statement, financing shows +$100M from debt and -$100M for the buyback, so cash is unchanged; no income statement effect. Going forward: interest expense rises (at 6%, $6M pre-tax, $4.5M after tax at 25%), net income falls, but share count falls too, so EPS can rise if the after-tax cost of debt is below the earnings yield on the repurchased shares.

### 18. What is a deferred tax asset? A deferred tax liability? Give examples of each.

*Taxes · Hard*

A deferred tax liability arises when pre-tax income on the financial statements is higher than taxable income because of a timing difference, so more tax will be paid later. Example: accelerated depreciation for tax and straight-line for the books, or asset write-ups in a stock acquisition that are not deductible for tax. A deferred tax asset is the reverse: taxable income is higher now, or a future tax deduction exists. Examples: net operating loss carryforwards, and warranty or bad-debt reserves expensed in the books before they are tax-deductible.

### 19. Why would two companies with identical pre-tax income have different tax rates?

*Taxes · Medium*

Different geographic mix (tax rates differ by country and state), tax credits such as R&D credits, use of net operating losses, permanent differences (non-deductible expenses, tax-exempt income), changes in valuation allowances, and one-time items such as settlements with tax authorities.

### 20. What is working capital? How does an increase in working capital affect cash flow?

*Working capital · Easy*

Working capital is current assets minus current liabilities. For valuation, bankers usually use operating working capital, which excludes cash and debt (accounts receivable + inventory + prepaid expenses - accounts payable - accrued expenses - deferred revenue). An increase in operating working capital means more cash is tied up in the business, so it reduces cash flow; a decrease releases cash.

### 21. What is the difference between capitalizing and expensing?

*Fundamentals · Easy*

Capitalizing records a cost as an asset on the balance sheet and expenses it over time through depreciation or amortization; it is used when the item provides benefit over more than one year (e.g. equipment). Expensing records it immediately on the income statement (e.g. salaries, rent). Capitalizing makes current-period income higher and puts the cash outflow in investing rather than operating activities.

### 22. A company changes from straight-line to accelerated depreciation. Impact?

*Depreciation · Medium*

Accelerated depreciation means more expense in early years and less later; total depreciation over the asset's life is the same. Early years: higher depreciation, lower pre-tax and net income; assuming the method applies for tax purposes, taxes fall, so cash flow rises (by depreciation change times the tax rate), PP&E falls faster and retained earnings fall. Later years reverse. If only the book method changes and tax depreciation does not, cash taxes are unchanged and a deferred tax effect appears instead.

### 23. How do operating leases appear on the financial statements under ASC 842?

*Leases · Hard*

Under ASC 842, an operating lease puts a right-of-use asset and a lease liability on the balance sheet. On the income statement, there is a single straight-line lease cost within operating expenses (unlike a finance lease, which shows amortization and interest separately). Payments are in cash flow from operations. Because lease cost stays inside US GAAP EBITDA, bankers usually do not add operating lease liabilities to enterprise value; under IFRS 16, where lease cost sits in depreciation and interest, lease liabilities are usually added.

> Rule: be consistent. If the metric excludes lease expense, count leases as debt in EV; if it includes it, do not.

### 24. A company sells an asset for more than book value. Walk me through the impact.

*Asset sales · Medium*

Say an asset with a $80 book value sells for $100 and the tax rate is 25%. Income statement: $20 gain, net income +$15. Cash flow statement: net income +$15, subtract the $20 gain in operating activities (it is non-operating), and record $100 of proceeds in investing activities: cash +$95. Balance sheet: cash +$95, PP&E -$80, total assets +$15; retained earnings +$15. It balances.

### 25. What is diluted shares outstanding and how do you calculate it using the treasury stock method?

*Share count · Medium*

Diluted shares include the effect of options, warrants, RSUs and convertibles. Under the treasury stock method, assume in-the-money options are exercised and the company uses the exercise proceeds to buy back shares at the current price. Example: 100M basic shares, 10M options with a $10 strike, share price $20. Proceeds are $100M, which buys back 5M shares, so net new shares are 5M and diluted shares are 105M. Out-of-the-money options are excluded.

## Valuation (26-50)

### 26. Walk me through a DCF.

*DCF · Easy*

Project the company's unlevered free cash flows, usually for 5 to 10 years, from revenue, margins, taxes, capex and working capital. Calculate a terminal value at the end of the projection period with the Gordon Growth method or an exit multiple. Discount the cash flows and the terminal value to today at the weighted average cost of capital. The sum is enterprise value; subtract net debt and other claims to get equity value, and divide by diluted shares to get value per share.

> Follow-up: why use unlevered free cash flow? Because the discount rate (WACC) reflects all capital providers, so the cash flow must be before debt payments too.

### 27. What is WACC and how do you calculate it?

*DCF · Medium*

WACC is the blended required return of all capital providers: WACC = E/(D+E) x cost of equity + D/(D+E) x cost of debt x (1 - tax rate), plus a preferred-stock term if relevant. Use market values or a target capital structure for the weights. Cost of debt is the current yield or borrowing rate, after tax because interest is tax-deductible.

### 28. How do you calculate cost of equity?

*DCF · Medium*

With the Capital Asset Pricing Model: cost of equity = risk-free rate + levered beta x equity risk premium. Some practitioners add a size or company-specific premium. The risk-free rate is usually a long-term government bond yield matching the currency of the cash flows.

### 29. What beta would you use for a private company?

*DCF · Hard*

A private company has no trading history, so use comparable public companies. Take each peer's levered beta, unlever it to remove its capital structure (unlevered beta = levered beta / (1 + (1 - tax rate) x debt/equity)), take the median, then relever it at the private company's target capital structure.

### 30. What is the terminal value and how do you calculate it?

*DCF · Medium*

Terminal value captures the value of cash flows beyond the projection period. Gordon Growth: final-year free cash flow x (1 + long-term growth rate) / (discount rate - growth rate). Exit multiple: final-year EBITDA (or another metric) x an exit multiple from comparable companies. Discount it back to today from the end of the projection period. It is often the majority of a DCF's value, so sensitivity tables on its inputs matter.

### 31. Gordon Growth vs. Exit Multiple for terminal value: when do you use each?

*DCF · Medium*

Exit multiple is common in banking because it ties to market valuations and to how buyers think about exits. Gordon Growth suits mature, stable businesses and is preferred when there are few good comparables or when market multiples are distorted. Best practice is to cross-check: compute the growth rate implied by your exit multiple and the multiple implied by your growth rate. The long-term growth rate should not exceed long-run nominal GDP growth.

### 32. A company has negative free cash flow for the next 5 years. Can you still do a DCF?

*DCF · Hard*

Yes. Extend the projection period until cash flows turn positive and reach a steady state, then calculate terminal value. The result will be heavily dependent on terminal value and assumptions, so use a higher discount rate if risk is higher, run scenarios, and cross-check with comparable companies and transactions.

### 33. Walk me through how you would build a comparable companies analysis.

*Comps · Easy*

Select a peer set of similar companies, gather their financials (historical LTM and projected NTM or forward-year figures) and share data, calculate equity value and enterprise value for each, compute multiples such as EV/Revenue, EV/EBITDA and P/E, then look at the median and the 25th to 75th percentile range. Apply that range to the target's corresponding metrics to get an implied valuation range.

### 34. How do you select comparable companies?

*Comps · Medium*

Start with industry and business model, then filter by size (revenue or market cap), growth, margins, geography and end markets. You want companies investors would see as substitutes. Usually 5 to 15 peers, adjusted when the closest names have unusual circumstances (pending acquisition, distress).

### 35. Why do we use NTM multiples vs. LTM multiples?

*Comps · Medium*

Valuation is forward-looking: the market prices expected earnings, so NTM multiples reflect consensus expectations and smooth one-time items in historical results. They matter most for fast-growing or changing companies. LTM multiples use actual reported results and are more objective when forecasts are unreliable or unavailable.

### 36. Why do precedent transactions typically give higher valuations than comparable companies?

*Precedents · Easy*

Because acquirers pay a control premium over the market price to gain control of the target, and they often pay part of the expected synergies. Precedent multiples also reflect market conditions at the time of each deal, which may differ from today.

### 37. If you could only use one valuation methodology, which would you choose?

*General · Hard*

There is no single right answer; the interviewer wants your reasoning. A common answer is a DCF, because it values the company's own cash flows and does not depend on whether the market is mispricing peers, as long as cash flows are reasonably predictable. Another defensible answer is trading comparables, because they reflect what investors pay today and rely on fewer assumptions. Pick one and give the trade-off.

### 38. Which gives the highest valuation: DCF, comps, or precedent transactions?

*General · Medium*

There is no fixed rule. Precedent transactions often come out highest because they include control premiums. A DCF has the widest range because it is very sensitive to assumptions. Trading comparables often come out lower than precedents. The answer depends on the market environment and the assumptions.

### 39. When would you not use a DCF?

*DCF · Medium*

When cash flows are unpredictable or there is no reasonable way to project them, such as an early-stage startup. For banks and insurers, a standard unlevered DCF does not work because debt and interest are part of operations, so use a dividend discount model or residual income model instead. In distressed situations, liquidation or recovery analysis may be more relevant.

### 40. A company's DCF gives $50/share but it trades at $30. What could explain this?

*DCF · Hard*

The market may see risks your model does not, your projections may be too optimistic, your discount rate may be too low, or your terminal assumptions too aggressive. Or the market may be mispricing the stock temporarily, for example because of short-term sentiment or limited information. Sense-check your assumptions against consensus estimates and comparable multiples before concluding the stock is undervalued.

### 41. How does a decrease in WACC affect the DCF output?

*DCF · Easy*

A lower WACC increases the present value of future cash flows and the terminal value, so enterprise value goes up. With the Gordon Growth method the effect is magnified because value depends on the spread between the discount rate and the growth rate.

### 42. What is the equity risk premium and what value do you use?

*DCF · Medium*

The equity risk premium is the extra return investors expect from equities over the risk-free rate. There is no single correct number; US practitioners commonly use a figure in roughly the 4% to 6% range, sourced from a house view, historical averages, or implied-premium estimates such as those published by Aswath Damodaran or advisory firms. Say what source you use and why.

### 43. How do you value a company with no revenue?

*Special situations · Hard*

Use methods that do not rely on current profits: a DCF with a long projection period and scenario or probability weighting, comparable companies on forward revenue or operating metrics (users, subscribers), recent private funding rounds or precedent transactions, and for drug developers a risk-adjusted NPV based on clinical success probabilities. Asset or liquidation value can set a floor.

### 44. What is a sum-of-the-parts valuation?

*General · Medium*

A sum-of-the-parts values each business segment separately with the method and multiples appropriate to it, then adds them, subtracts unallocated corporate costs (capitalized) and net debt, and sometimes applies a conglomerate discount. It is used for diversified companies whose segments have very different growth, margins or peer groups, and to test break-up or spin-off value.

### 45. How do you value a cyclical company?

*Special situations · Hard*

Avoid valuing a cyclical company on peak or trough earnings. Normalize: use mid-cycle or average EBITDA and margins across a full cycle, apply multiples to normalized figures, and in a DCF project a full cycle so the terminal year is not at a peak. Cross-check with multiples of peers at a similar point in the cycle.

### 46. What are calendarized financials and why do they matter for comps?

*Comps · Medium*

Calendarization adjusts financial results of companies with different fiscal year-ends to the same calendar period so multiples are comparable. Example: for a company with a June fiscal year-end, calendar year 2026 = 6/12 of fiscal year ending June 2026 + 6/12 of fiscal year ending June 2027.

### 47. How do convertible bonds affect the EV calculation?

*EV bridge · Hard*

Check whether the convertible is in the money (share price above the conversion price). If it is, treat it as equity: add the shares it converts into to the diluted share count (if-converted method) and do not count it as debt. If it is out of the money, treat it as debt in the EV bridge. Do not count it in both places.

### 48. A company has $500M in cash. Does all of it get subtracted in the EV bridge?

*EV bridge · Hard*

Not necessarily. You subtract cash that is not needed to run the business. Some analysts keep a minimum operating cash balance in the business, and restricted or trapped cash, or cash held abroad that would be taxed on repatriation, may be adjusted. Whatever you choose, stay consistent across the target and its comparables.

### 49. What is unlevered free cash flow and how does it differ from levered FCF?

*DCF · Medium*

Unlevered free cash flow is cash flow before interest and debt payments, available to all capital providers; discount it at WACC to get enterprise value. Levered free cash flow is after interest and mandatory debt repayments, available only to equity holders; discount it at the cost of equity to get equity value.

### 50. If you raise the discount rate in a DCF by 1%, does the value go up or down? By approximately how much?

*DCF sensitivity · Medium*

Value goes down. The size depends on the inputs, especially the gap between the discount rate and the terminal growth rate. Example with Gordon Growth only: at a 10% discount rate and 2% growth, terminal value is proportional to 1/0.08; at 11% it is 1/0.09, about 11% lower. A one-point change commonly moves DCF value by roughly 10% to 15%, which is why bankers show sensitivity tables.

> Want model answers to the 30 most-asked IB questions? Get the free [IB Top 30 guide](https://sirjohnnymai.gumroad.com/l/ib-top-30-questions?utm_source=github&utm_medium=qbank&utm_campaign=ib_qbank_20261101&utm_content=readme_mid).

## M&A (51-70)

### 51. Walk me through a merger model.

*M&A mechanics · Easy*

Set the purchase price and form of consideration (cash, stock, debt). Project both companies' income statements. Combine them and adjust for foregone interest on cash used, interest on new debt, new shares issued, amortization of new intangibles, and synergies. Compute pro forma EPS and compare it with the buyer's standalone EPS to see accretion or dilution. A fuller model also builds the pro forma balance sheet with purchase price allocation and goodwill.

### 52. What is accretion/dilution?

*M&A mechanics · Easy*

A deal is accretive if the combined company's pro forma EPS is higher than the buyer's standalone EPS, and dilutive if it is lower. It is a shorthand that markets watch, but it is not the same as value creation; a dilutive deal can still create value and vice versa.

### 53. In an all-stock deal, what determines if it is accretive or dilutive?

*Accretion/dilution · Medium*

Compare the buyer's P/E with the P/E it pays for the seller. If the buyer's P/E is higher than the purchase P/E for the target, the deal is accretive, ignoring synergies and other adjustments. Put differently, the cost of stock (the buyer's earnings yield, 1/P/E) is lower than the yield of the earnings acquired.

> Follow-up: for a mixed deal, compare the weighted cost of acquisition (after-tax cost of debt, foregone interest on cash, buyer's earnings yield for stock) with the seller's earnings yield at the purchase price.

### 54. Why might a company do a dilutive acquisition?

*M&A strategy · Medium*

Because accretion/dilution is a short-term EPS measure. The buyer may expect synergies that ramp up later, the target may grow faster than the buyer, it may add strategic capabilities, markets or technology, or it may be defensive against a competitor. Dilution in year one can turn into accretion in later years.

### 55. What are synergies? Types and typical ranges?

*Synergies · Easy*

Synergies are the extra value from combining two companies. Cost synergies come from eliminating overlapping costs: headcount, facilities, procurement and systems. Revenue synergies come from cross-selling, pricing and access to new channels or markets. There are also financial synergies such as tax benefits or cheaper financing. Cost synergies are more predictable, so investors and bankers usually discount revenue synergies more heavily. Sanity-check estimates as a percentage of the target's cost base and against precedent deals.

### 56. Why do most acquisitions fail to deliver expected synergies?

*M&A strategy · Hard*

Integration is harder than planned (systems, culture, key people leaving), revenue synergies assume customer behavior that does not happen, customers and employees leave during uncertainty, one-time integration costs are underestimated, and the buyer overpays, so even achieved synergies do not cover the premium.

### 57. What is a fairness opinion?

*M&A process · Medium*

A fairness opinion is a letter from a financial advisor to a company's board stating that the consideration in a transaction is fair, from a financial point of view, to the company's shareholders. It is supported by valuation analyses (DCF, comps, precedents) and helps the board show it made an informed decision. It is not a statement that the price is the best obtainable.

### 58. What is a go-shop provision?

*M&A process · Medium*

A go-shop clause lets the target actively solicit competing offers for a set period after signing a merger agreement, often around 30 to 60 days, usually with a lower break-up fee for a deal signed during that window. It is common when the target negotiated with one buyer without a broad auction, and it helps the board satisfy its duty to seek the best value.

### 59. What is a MAC clause?

*M&A process · Hard*

A material adverse change (or material adverse effect) clause lets a buyer walk away if something seriously harms the target between signing and closing. It is heavily negotiated, with carve-outs for general economic, market or industry conditions. Delaware courts set a high bar; Akorn v. Fresenius (2018) was the first time the Delaware Court of Chancery found an MAE allowing a buyer to terminate.

### 60. Cash vs. stock vs. mixed consideration: trade-offs?

*Deal structure · Medium*

Cash gives the seller certainty and full exit, is usually taxable to the seller, and requires the buyer to have cash or raise debt. Stock shares risk and upside with the seller, can be tax-deferred, avoids new debt, but dilutes the buyer's shareholders and the value fluctuates until closing. Buyers tend to use stock when they think their shares are richly valued; mixed consideration balances these trade-offs.

### 61. What is a reverse merger?

*M&A types · Medium*

A reverse merger is when a private company merges with an existing public company (often a shell with little operations) so the private company's owners take control and the company becomes public without a traditional IPO. It is faster and cheaper than an IPO but usually raises less capital and can carry diligence and reputational risk.

### 62. What is an earnout and when is it used?

*Deal structure · Medium*

An earnout is part of the purchase price paid later only if the target hits agreed milestones, such as revenue, EBITDA or regulatory approval. It bridges a valuation gap between buyer and seller, especially for high-growth or uncertain businesses (for example biotech or early-stage tech). Downsides: disputes over measurement and less buyer freedom to integrate.

### 63. Name three anti-takeover defenses.

*Hostile M&A · Medium*

A poison pill (shareholder rights plan) lets existing holders buy shares at a discount if an acquirer crosses an ownership threshold, diluting the acquirer. A staggered board means only part of the board is elected each year, slowing a takeover. Other defenses: a white knight (friendly alternative buyer), dual-class shares, and golden parachutes.

### 64. What is the role of the sell-side advisor vs. the buy-side advisor?

*M&A process · Easy*

The sell-side advisor represents the company or owner being sold: prepares the materials, identifies and contacts buyers, runs the auction and negotiates to maximize value and certainty. The buy-side advisor represents the acquirer: identifies targets, values them, advises on bid strategy, structure and financing, and helps negotiate. Both typically help with fairness opinions or financing as needed.

### 65. What factors influence the premium paid in an acquisition?

*Deal economics · Medium*

Synergies the buyer expects, competition among bidders, the target's growth and strategic value, the buyer's ability to pay and financing conditions, the target's recent share price and how much speculation is already in it, market conditions, and governance factors such as shareholder support or defenses.

### 66. Walk me through a sell-side M&A process.

*M&A process · Medium*

Preparation: valuation, buyer list, teaser and confidential information memorandum (CIM), data room. First round: buyers sign NDAs, receive the CIM and submit non-binding indications of interest. Second round: selected buyers get management presentations and data room access and submit final bids with a markup of the purchase agreement. Then negotiation, signing, regulatory approvals and closing. A full process commonly takes several months.

### 67. What is the difference between an asset deal and a stock deal?

*Deal structure · Hard*

In an asset deal the buyer purchases specific assets and assumes only chosen liabilities; it gets a step-up in tax basis, so it can depreciate and amortize the asset write-ups (including goodwill, amortized over 15 years for US tax). A C-corporation seller may face double taxation. In a stock deal the buyer acquires the shares and all liabilities; there is generally no tax step-up. Buyers usually prefer asset deals and sellers stock deals. A Section 338(h)(10) or 336(e) election can treat a stock deal as an asset deal for tax purposes in certain situations.

### 68. How do you calculate goodwill in an acquisition?

*Accounting · Medium*

Goodwill = purchase price for the equity - fair value of the target's identifiable net assets. In practice: purchase equity value - target's book value of equity (excluding existing goodwill) - write-ups of assets including new identifiable intangibles + any deferred tax liability created by the write-ups.

### 69. What is purchase price allocation?

*Accounting · Hard*

Purchase price allocation assigns the purchase price to the fair values of the target's acquired assets and assumed liabilities, including identifiable intangibles (customer relationships, technology, trade names). Any excess is goodwill. It determines future depreciation and amortization, which affects the pro forma income statement.

### 70. A company wants to acquire a target but cannot afford to pay cash. What options does it have?

*Deal structure · Medium*

Pay in stock, raise debt (bank loans or bonds), issue new equity or a hybrid such as convertibles, use seller financing (a seller note) or an earnout to defer part of the price, partner with a private equity firm or co-investor, sell non-core assets first, or buy a partial stake or form a joint venture.

## LBO (71-85)

### 71. Walk me through an LBO model.

*LBO mechanics · Easy*

A private equity firm buys a company using a large amount of debt and some equity. Steps: set the purchase price and sources and uses (debt and sponsor equity versus purchase price and fees); project the company's cash flows; use free cash flow to pay interest and repay debt; assume an exit after about 3 to 7 years at an exit multiple; subtract remaining net debt to get exit equity value; calculate IRR and MOIC on the sponsor's equity.

### 72. What makes a good LBO candidate?

*LBO strategy · Easy*

Stable, predictable cash flows to service debt; limited capital expenditure needs; a strong market position; room to improve operations or grow; a reasonable purchase price; assets that support borrowing; a capable management team; and a clear path to exit through a sale or IPO.

### 73. What are the three ways PE firms create value?

*Value creation · Easy*

EBITDA growth (revenue growth and margin improvement), multiple expansion (selling at a higher multiple than the purchase multiple) and debt paydown (deleveraging, which increases the equity's share of enterprise value). Leverage itself magnifies returns on all three.

### 74. Do a paper LBO: 10x entry, $200M EBITDA, 6x debt, 5% growth, exit 10x in 5 years.

*Paper LBO · Medium*

Entry: 10x x $200M = $2,000M enterprise value; debt 6x = $1,200M; equity $800M (ignore fees). EBITDA in year 5 = $200M x 1.05^5, about $255M. Exit at 10x = about $2,553M. If no debt is repaid, exit equity = $2,553M - $1,200M = $1,353M, MOIC about 1.7x, IRR about 11%. If, say, $300M of debt is repaid from free cash flow, exit equity is about $1,653M, MOIC about 2.1x, IRR about 15 to 16%.

> Rules of thumb: 2x in 5 years is about 15% IRR; 2x in 3 years is about 26%; 3x in 5 years is about 25%.

### 75. What is IRR? What is MOIC? How do they relate?

*Returns · Easy*

IRR is the discount rate that makes the net present value of the equity cash flows zero, so it accounts for timing. MOIC (multiple on invested capital) is total value returned divided by equity invested, with no time element. For a single entry and exit, IRR = MOIC^(1/years) - 1, so the same MOIC over a shorter hold means a higher IRR.

### 76. Which creates more value: 1 turn of multiple expansion or 1 turn of additional leverage?

*Sensitivity · Hard*

It depends on the numbers, so show it. One turn of exit multiple adds one turn times exit EBITDA of value directly to equity. One more turn of leverage reduces the equity check; it raises returns only if the business earns more than the after-tax cost of the extra debt and can service it, and it raises risk. Example: $100M EBITDA, 10x entry and exit, 5x debt, no growth or paydown: equity in $500M, out $500M. Exit at 11x: out $600M, +20%. Use 6x debt instead: equity in $400M, out $400M, still 1.0x, because nothing grew. In a no-growth case, multiple expansion helps more.

### 77. What is a dividend recapitalization?

*PE strategy · Medium*

A dividend recapitalization is when a portfolio company raises new debt and uses it to pay a dividend to its private equity owners. It returns capital early and raises IRR without selling the company, but increases leverage and default risk.

### 78. Why can PE firms pay higher multiples than strategic buyers in some situations?

*PE vs. strategic · Hard*

Normally strategic buyers can pay more because of synergies. A sponsor can pay more when debt is cheap and plentiful, when it sees operational improvements the market undervalues, when it has a platform that creates add-on synergies, or when a strategic buyer is constrained by its own share price, balance sheet, antitrust concerns or EPS dilution.

### 79. What is PIK (payment in kind) interest?

*Debt structure · Medium*

Payment-in-kind interest is not paid in cash; it is added to the principal, so the debt balance grows. It preserves cash for the borrower but carries a higher rate and compounds. In the model, PIK interest reduces net income but is added back on the cash flow statement as a non-cash expense.

### 80. What debt covenants are common in LBOs?

*Debt structure · Medium*

Maintenance covenants require ongoing tests, such as a maximum total leverage ratio (debt/EBITDA) or minimum interest or fixed-charge coverage. Incurrence covenants restrict actions such as taking on more debt, paying dividends, making acquisitions or selling assets unless a test is met. Many institutional term loans today are covenant-lite, meaning they have no maintenance covenants.

### 81. How do interest rates affect LBO returns?

*Macro impact · Medium*

Higher rates raise interest costs, lower the amount of debt a company can support, reduce free cash flow for debt paydown, and can pressure exit multiples, all of which reduce returns; sponsors respond by using more equity, paying lower prices or holding longer. Lower rates do the opposite.

### 82. What is a club deal in PE?

*PE strategy · Easy*

A club deal is when two or more private equity firms jointly acquire a company. It lets them do larger deals, share risk and combine expertise, but governance and exit decisions are more complex.

### 83. How does add-on acquisition strategy work in PE?

*Buy and build · Medium*

A buy-and-build strategy acquires a platform company, then adds smaller bolt-on companies, often at lower multiples. Value comes from combined synergies, scale, professionalized management and multiple arbitrage: the combined company may exit at the platform's higher multiple. Risks include integration difficulty and overpaying for add-ons.

### 84. A PE firm buys a company at 8x EBITDA with $100M EBITDA. It does 3 bolt-on acquisitions at 5x EBITDA adding $50M total EBITDA. If it exits at 8x on combined EBITDA, what is the value creation from multiple arbitrage?

*Buy and build math · Hard*

Platform: 8x x $100M = $800M. Bolt-ons: 5x x $50M = $250M. Total cost $1,050M for $150M of EBITDA. Exit at 8x x $150M = $1,200M. Value created from multiple arbitrage is (8x - 5x) x $50M = $150M, before any EBITDA growth or synergies.

### 85. What is a continuation fund?

*PE strategy · Hard*

A continuation fund (continuation vehicle) is a GP-led secondary transaction: the private equity firm moves one or more assets from an older fund into a new vehicle that it also manages. Existing investors can sell their stake for cash or roll into the new vehicle, and secondary buyers provide new capital. It lets the firm keep strong assets longer. Because the firm is on both sides, it typically uses an independent valuation or fairness opinion and LP advisory committee review.

## Industry, Restructuring and Current Events (86-100)

### 86. Why cannot you use EV/EBITDA for a bank?

*FIG · Easy*

For a bank, debt and interest are operating items: deposits and borrowing are its raw material, and interest expense is like cost of goods sold. So separating operating and financing activities does not make sense, and EBITDA and enterprise value are not meaningful. Use equity-based measures: P/E, price to tangible book value (often compared with return on tangible equity), and dividend discount or residual income models.

### 87. What is the Rule of 40 in SaaS?

*TMT · Easy*

For a software company, revenue growth rate plus profit margin (commonly free cash flow or EBITDA margin) should be at least 40%. It balances growth against profitability; a company growing 30% with a 10% margin meets it, as does one growing 10% with a 30% margin.

### 88. What is rNPV and when would you use it?

*Healthcare · Hard*

Risk-adjusted net present value: project the cash flows of a drug or pipeline asset, multiply each period's cash flows by the cumulative probability that the drug reaches that stage (clinical phases, approval), and discount them. It is used for biotech and pharmaceutical assets whose outcomes are binary and stage-dependent.

### 89. What is NAV in the context of energy valuation?

*Energy · Medium*

For oil and gas producers and miners, net asset value is the present value of cash flows from producing the company's reserves over their life, minus net debt and other liabilities. There is usually no terminal value because reserves deplete. Inputs include reserves, production profiles, commodity price decks, costs and discount rates.

### 90. What is FFO and why is it used instead of net income for REITs?

*Real estate · Medium*

Funds from operations, as defined by Nareit: net income + real estate depreciation and amortization - gains on sales of depreciable property, + impairments of depreciable real estate, with adjustments for joint ventures. REITs use it because real estate depreciation is a large non-cash charge and properties often hold value. AFFO further subtracts recurring capital expenditures and adjusts for straight-line rent.

### 91. What is happening in the M&A market right now?

*Current events · Medium*

Do not memorize numbers from an old article. Prepare a short answer from sources dated within a week or two of your interview: (1) overall direction of deal volume and count versus last year, (2) what drives it (financing costs, equity markets, regulation, sponsor dry powder), (3) one or two notable recent deals, ideally in the group you are interviewing with, and (4) your view on the next six months. Sources: financial press and league-table reports from data providers.

### 92. Where is the 10-year Treasury? What does this mean for deal activity?

*Current events · Medium*

Check the level the morning of the interview (e.g. Treasury yield data or a financial news site) and know the direction over recent months. Then explain the link: higher long-term yields raise discount rates and borrowing costs, which lowers valuations and LBO debt capacity and can slow deal activity; falling yields support valuations and financing. Mention any second-order effects you have read about, such as refinancing needs.

### 93. Tell me about a deal you find interesting.

*Deal discussion · Medium*

Pick a deal from the last 6 to 12 months you can discuss deeply, ideally in the group you are interviewing with. Structure: the parties and what they do; size, consideration and valuation multiple compared with peers or precedents; strategic rationale and synergies; financing; risks such as regulatory review or integration; and your view on whether it makes sense. Expect follow-ups on the numbers.

### 94. Walk me through the IPO process.

*ECM · Medium*

Select underwriters, conduct due diligence, and draft the registration statement (Form S-1 in the US), which the SEC reviews and comments on. Companies can submit drafts confidentially, but must file publicly at least 15 days before the roadshow. Then the roadshow and book-building, pricing and allocation the night before trading, and the first day of trading. Underwriters usually have an over-allotment (greenshoe) option of up to 15% of the shares, and insiders are typically subject to a lock-up, often 180 days.

### 95. What is a SPAC and why did the market cool on them?

*ECM · Medium*

A special purpose acquisition company is a shell that raises money in an IPO, holds it in trust, and has a limited time (often 18 to 24 months) to merge with a private company, which then becomes public. The market cooled after the 2020 to 2021 boom because many de-SPAC companies traded poorly, redemption rates were high, sponsor promote and warrants diluted shareholders, rising rates made trust yields compete, and the SEC adopted rules in January 2024 expanding disclosure and liability around SPAC projections.

### 96. What is the fulcrum security?

*Restructuring · Hard*

In a restructuring, the fulcrum security is the most senior class of claims that will not be paid in full given the company's enterprise value. It is usually expected to receive most of the reorganized company's equity, so its holders have the most influence over the plan.

### 97. What is Chapter 11 bankruptcy?

*Restructuring · Medium*

Chapter 11 of the US Bankruptcy Code lets a company reorganize while continuing to operate, usually as a debtor in possession. An automatic stay halts most creditor collection, the company can obtain debtor-in-possession financing, and it proposes a plan of reorganization that creditor classes vote on and the court confirms, generally following the absolute priority rule. Chapter 7, by contrast, is liquidation.

### 98. If you were a CEO of a company with $2B in excess cash, would you do a buyback, a dividend, or an acquisition?

*Capital allocation · Hard*

There is no single right answer; show a framework. Acquisition if there is a target with a return above the cost of capital and clear strategic fit. Buyback if the shares are undervalued and the company wants flexibility; it raises EPS and can be stopped at any time. Dividend if cash generation is stable and shareholders value income; dividends are sticky, so a special dividend suits one-time excess cash. Also consider leverage targets, taxes, signaling, and keeping a cushion for downturns, then pick one and defend it.

### 99. A company issues convertible notes instead of straight debt. Why?

*Capital structure · Medium*

Convertibles carry a lower coupon than straight debt because investors get an option to convert into shares, and conversion happens at a premium to today's price, so dilution is deferred and smaller than issuing stock now. They suit companies with high growth or volatile shares and limited access to cheap straight debt. Trade-offs: possible dilution, hedge-fund hedging activity around issuance, and refinancing risk if the stock does not rise.

### 100. Pitch me a stock.

*Investment thesis · Hard*

Keep it to about two minutes: (1) what the company does and how it makes money; (2) your thesis in two or three points on why the market is mispricing it; (3) valuation versus peers and history with an implied target price or upside; (4) catalysts that could close the gap; (5) key risks and what would make you wrong. Choose a company you follow and can defend under questioning.

## Fit questions (bonus)

Fit decides as many superdays as technicals. Prepare these six:

**Walk me through your resume.** About 90 seconds, chronological and story-shaped: where you started, two or three choices that led you toward finance, what you learned in each, and why this role is the logical next step. End on why you are here today.

**Why investment banking?** Give two or three specific reasons tied to your experience: the type of work (transactions, analysis, client exposure), the learning curve, and what you want to do later. Show you understand the hours and workload. Avoid generic answers about money or prestige.

**Why our bank (or group)?** Name concrete things: recent deals the group advised on, its focus areas, people you spoke to and what you learned from them, and how its deal mix fits your interests.

**Tell me about a time you worked in a team under pressure.** Use a brief STAR structure (situation, task, action, result). Focus on what you did, quantify the result, and say what you would do differently.

**What is your greatest weakness?** A real but manageable weakness, a concrete example, and what you are doing about it. Avoid disguised strengths.

**What questions do you have for us?** Ask about the interviewer's experience, a recent deal, how analysts are staffed and reviewed, or what separates top performers. Do not ask anything the website answers.

## How to prepare in two weeks

| Days | Focus |
|---|---|
| 1-3 | Accounting 1-25 out loud; redo 3, 5, 17 and 24 on paper until the balance sheet balances every time |
| 4-6 | Valuation 26-50; build one simple DCF and one comps table in Excel |
| 7-8 | M&A 51-70; do two accretion/dilution examples by hand |
| 9-10 | LBO 71-85; do the paper LBO in 74 in under 5 minutes without a calculator |
| 11-12 | Industry 86-100 for your target group; prepare one deal and one stock pitch |
| 13-14 | Fit stories plus a timed mock: 10 random questions, 1 minute each |

## Next step
[**IB Interview: Top 30 Questions**: model answers to the 30 most-asked questions, free](https://sirjohnnymai.gumroad.com/l/ib-top-30-questions?utm_source=github&utm_medium=qbank&utm_campaign=ib_qbank_20261101&utm_content=readme_bottom)

---
Published by Valenx Press, from *The 0 to 1 Interview Playbook* series. Last updated November 1, 2026. Questions reflect common public interview patterns; no bank affiliation. Answers are for interview preparation, not investment advice. Spotted an error or want to add a question you were asked? Open an issue or PR.
