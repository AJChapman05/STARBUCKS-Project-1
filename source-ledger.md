# Source Ledger — Starbucks Valuation

Use this ledger for every material input, adjustment, and output-defining convention. Do not
enter an input until its source and point-in-time availability have been checked. Prefer primary
sources: Starbucks Form 10-K and 10-Q filings, Starbucks investor-relations releases and earnings
materials, and authoritative market-data sources for market inputs. Record an as-of date for all
market data.

`[STUDENT ENTRY REQUIRED]` means the field must be completed from an actual reviewed source.

## Source-selection and point-in-time rules

- Financial statement and operating facts: use the relevant Starbucks Form 10-K or 10-Q first.
  Use an investor-relations release or earnings material only when it supplies an operating metric
  not available in the filing; cross-reference the filing when possible.
- Market data and WACC inputs: use an authoritative provider and record both the provider's
  observation date/time and the date accessed. Do not use data published after the declared source
  cutoff unless it is excluded or its treatment is explicitly disclosed.
- Define the observation exactly as reported before transforming it. Keep source values separate
  from normalized/model values.
- Include a risk for every item: definition mismatch, reporting-period mismatch, later
  restatement, segment reorganization, currency issue, stale market data, or another identified
  limitation.

## Master source register

Assign a source ID here, then cite that ID in each detailed table below.

| Source ID | Source URL | Source type / publisher | Filing or publication date | Reporting period / observation date | Available by valuation-date cutoff? | Page / table / section | Notes |
|---|---|---|---|---|---|---|---|
| S-001 | https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm | Form 10-K / Starbucks Corporation filed with SEC | 2025-11-14 | Fiscal year ended 2025-09-28 | Yes — filed before 2026-10-19 cutoff | Item 8: Statements of Earnings p. 43; Balance Sheets p. 45; Cash Flows pp. 46–47; Item 1 store summary pp. 6–8; notes in Item 8 | Primary audited annual source for FY2025, FY2024, and FY2023 statements; fiscal 2025 is 52 weeks. |
| S-002 | https://www.sec.gov/Archives/edgar/data/829224/000082922423000058/sbux-20231001.htm | Form 10-K / Starbucks Corporation filed with SEC | 2023-11-17 | Fiscal year ended 2023-10-01 | Yes — filed before 2026-10-19 cutoff | Item 8: Statements of Earnings p. 42; Balance Sheets p. 44; Cash Flows pp. 45–46; Note 15 EPS; Note 17 segments | Primary audited comparative source for FY2023/FY2022 and FY2021 income/cash-flow history; FY2021 has 53 weeks. |
| S-003 | https://www.sec.gov/Archives/edgar/data/829224/000082922426000080/sbux-20260329.htm | Form 10-Q / Starbucks Corporation filed with SEC | 2026-04-28 | Quarter and two quarters ended 2026-03-29 | [enter after valuation date and source cutoff are set] | Item 1 financial statements; Notes to Financial Statements; segment, PP&E, and China held-for-sale disclosures | Primary interim source. Use only if available by the project source cutoff; interim periods and classification changes may limit comparability. |
| S-004 | https://investor.starbucks.com/news/financial-releases/news-details/2025/Starbucks-Reports-Q4-and-Full-Fiscal-Year-2025-Results/default.aspx | FY2025 earnings release / Starbucks Investor Relations | 2025-10-29 | 13-week Q4 and 52-week fiscal year ended 2025-09-28 | [enter after valuation date and source cutoff are set] | FY2025 highlights; North America, International, China, and Channel Development tables; GAAP/non-GAAP reconciliations | Primary company earnings material for quarterly comparable-sales, transactions, average-ticket, and segment context. Reconcile to the 10-K before using in the model. |
| S-005 | https://investor.starbucks.com/financials/annual-reports/default.aspx | Annual Reports index / Starbucks Investor Relations | Live index; retrieve date required | FY2021–FY2025 annual-report archive | [enter after valuation date and source cutoff are set] | FY21–FY25 annual-report links | Primary company archive for cross-checking filing copies and annual-report pagination. |
| S-006 | https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve | Daily Treasury Par Yield Curve Rates / U.S. Department of the Treasury | Live series; observation date required | Selected valuation-date observation | [enter after valuation date and source cutoff are set] | Daily yield-curve table; selected tenor | Authoritative risk-free-rate source. Enter the chosen date, tenor, yield, units, and methodology only after the valuation date is approved. |
| S-007 | https://api.nasdaq.com/api/quote/SBUX/historical?assetclass=stocks | Historical SBUX quote endpoint / Nasdaq | Observation retrieval date required | Selected valuation-date closing-price observation | [enter after valuation date and source cutoff are set] | Historical-price response for selected date | Exchange-branded market-data endpoint for the equity-price observation. Preserve the retrieved response/date and confirm the field definition before use. |
| S-008 | https://www.sec.gov/Archives/edgar/data/829224/000082922424000057/sbux-20240929.htm | Form 10-K / Starbucks Corporation filed with SEC | 2024-11-20 | Fiscal year ended 2024-09-29 | Yes — filed before 2026-10-19 cutoff | Item 8, pp. 50–53 | Audited source for FY2024, FY2023 and FY2022 comparative statements; used here for FY2024 balance-sheet and cash-flow detail. |
| S-009 | https://www.sec.gov/Archives/edgar/data/829224/000082922422000058/sbux-20221002.htm | Form 10-K / Starbucks Corporation filed with SEC | 2022-11-18 | Fiscal year ended 2022-10-02 | Yes — filed before 2026-10-19 cutoff | Item 8, pp. 41–44 | Audited source for FY2022 and FY2021 historical statements and year-end balance sheets. |
| S-010 | https://www.sec.gov/Archives/edgar/data/829224/000082922426000130/sbux-20260628.htm | Form 10-Q / Starbucks Corporation filed with SEC | 2026-07-29 | Quarter and three quarters ended 2026-06-28; balance sheet as of 2026-06-28 | Yes — filed before 2026-10-19 cutoff | Cover p. 1; Statements of Earnings p. 3; Balance Sheets p. 5; Cash Flows p. 6; Equity p. 7 | Latest eligible Starbucks periodic filing identified before the source cutoff. Interim and unaudited. |
| S-011 | https://www.nasdaq.com/market-activity/stocks/sbux/historical | Nasdaq SBUX historical-data page | Retrieved 2026-10-19 | 2026-10-19 regular-session close requested | Page retrieved by cutoff; data response unavailable | Historical Data page / close field | Authoritative exchange-branded source selected by the decision contract. Preserve a response or download showing the close before using a market-price input. |
| S-012 | https://finance.yahoo.com/quote/SBUX/history/?p=SBUX | Yahoo Finance SBUX historical-data page | Retrieved 2026-10-19 | 2026-10-19 regular-session close | Retrieved daily row shows the regular session marked “At close: 4:00:00 PM EDT” | Historical Data daily table; `Close` and `Adj Close` fields | Reputable third-party market-data source used because the Nasdaq page did not yield a dated observation. The page defines `Close` as split-adjusted and `Adj Close` as adjusted for splits and distributions. |
| P-001 | https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm | McDonald’s Form 10-K / SEC | 2026-02-24 | Fiscal year ended 2025-12-31 | Yes — before cutoff | Consolidated statements, pp. 38–41; business, restaurant, and franchise disclosures | Audited annual source for MCD FY2025 results and business-model comparability. |
| P-002 | https://www.sec.gov/Archives/edgar/data/63908/000006390826000073/mcd-20260630.htm | McDonald’s Form 10-Q / SEC | 2026-08-07 | Quarter and six months ended 2026-06-30; balance sheet 2026-06-30 | Yes — before cutoff | Cover p. 1; statements pp. 3–7; MD&A pp. 19–30 | Latest reviewed MCD interim source; unaudited; used for point-in-time share, balance-sheet claims, and LTM roll-forward. |
| P-003 | https://stockanalysis.com/stocks/mcd/history/ | StockAnalysis historical MCD pricing (S&P Global Market Intelligence data as identified on provider page) | Retrieved 2026-10-19 | MCD regular close 2026-10-19, 4:00 PM EDT | Yes — observation by cutoff | Daily Historical Data row; `Close` and `Adj. Close` columns | Close $242.67; provider labels daily close and separately displays adjusted close. Third-party historical quote, not raw exchange tick data. |
| P-004 | https://chartexchange.com/symbol/nyse-mcd/historical/ | ChartExchange MCD historical prices | Retrieved 2026-10-19 | At close 2026-10-19 3:59:58 PM EDT | Yes — observation by cutoff | Historical Prices; close field | Displays $242.66, $0.01 below P-003. Conflict retained; P-003 selected for calculation. |
| P-005 | https://www.sec.gov/Archives/edgar/data/1041061/000104106126000084/yum-20251231.htm | Yum! Brands Form 10-K / SEC | 2026-02-20 | Fiscal year ended 2025-12-31 | Yes — before cutoff | Business overview and segment/franchise disclosures | Evidence for exclusion from quantitative peer sample: multi-brand (KFC, Taco Bell, Pizza Hut, Habit Burger & Grill), 63,000+ restaurants in 155 countries, primarily franchise/operate model. |
| P-006 | https://www.sec.gov/Archives/edgar/data/1041061/000104106126000160/yum-20260630.htm | Yum! Brands Form 10-Q / SEC | 2026-08-05 | Quarter and six months ended 2026-06-30 | Yes — before cutoff | Statements pp. 3–8 and segment disclosures | Current-period corroboration for excluded candidate; interim statements reviewed, not audited. |

## Completed historical-extraction ledger — FY2021–FY2025

This section supersedes the blank template rows below. All amounts are **USD millions** as
reported, except operating metrics explicitly labelled otherwise. `FY2021` ended October 3,
2021 and was a 53-week year; FY2022–FY2025 were 52-week years. A source-ID hyperlink is the
direct SEC or Starbucks link; the table citation identifies the exact reported table.

### Ledger IDs and source convention

`H-IS-*` identifies an income-statement series, `H-BS-*` a balance-sheet series, and `H-CF-*`
a cash-flow series. For FY2023–FY2025, source table locations are S-001: Statements of Earnings
p. 43, Balance Sheets p. 45, Cash Flows pp. 46–47. For FY2021–FY2022, S-009 locations are
Statements of Earnings p. 41, Balance Sheets p. 43, Cash Flows p. 44. FY2024 is cross-checked
against S-008, Statements of Earnings p. 50. A dash is not a zero unless the filing presents it
as such.

### Income statement: reported facts and model mapping

| Ledger ID | Required model input / reported definition | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Source ID and direct link; filing page/table | Model transformation | Risk / status |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| H-IS-REV | Revenue — **Total net revenues** | 29,060.6 | 32,250.3 | 35,975.6 | 36,176.2 | 37,184.4 | [S-009](https://www.sec.gov/Archives/edgar/data/829224/000082922422000058/sbux-20221002.htm), p. 41; [S-001](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm), p. 43 | Direct `income_statement.revenue`. | FY2021 53 weeks; otherwise ready. |
| H-IS-COS | Cost of sales — **Product and distribution costs** | 8,738.7 | 10,317.4 | 11,409.1 | 11,180.6 | 11,658.2 | S-009 p. 41; S-001 p. 43 | Direct `income_statement.cost_of_sales`. | Filing uses this label, not “cost of sales”; definition must remain unchanged. Ready. |
| H-IS-OPEX | Operating expenses — **Total operating expenses less product and distribution costs** (calculated from reported rows) | 15,835.1 | 17,549.2 | 19,085.4 | 19,888.0 | 22,837.4 | S-009 p. 41; S-001 p. 43 | Candidate `income_statement.operating_expenses` = reported total operating expenses − H-IS-COS. | **Not ready:** model identity also omits reported equity-investee income, gain on sale of assets, and FY2021 divestiture gain; using this value causes a reconciliation failure. |
| H-IS-INT | Interest expense | (469.8) | (482.9) | (550.1) | (562.0) | (542.6) | S-009 p. 41; S-001 p. 43 | Store absolute values 469.8/482.9/550.1/562.0/542.6; engine subtracts the positive expense. | Ready under approved sign convention. |
| H-IS-NONOP | Non-operating income/(expense) model bridge — income from equity investees + gain on sale of assets + divestiture gain + interest income and other, net | 1,339.9 | 331.1 | 470.9 | 424.0 | 361.1 | S-009 p. 41; S-001 p. 43 | Store as a positive income/gain in `income_statement.non_operating_income_expense`; it is added after subtracting positive interest expense. | **Model presentation differs from filing:** equity-investee income and asset-sale gain are included in reported operating income, but are isolated here to preserve core EBIT and reconcile net income. |
| H-IS-TAX | Income tax expense | 1,156.6 | 948.5 | 1,277.2 | 1,207.3 | 650.6 | S-009 p. 41; S-001 p. 43 | Direct tax-expense input, subject to model sign convention. | Tax expense is reported, not cash taxes; FY2025 effective rate affected by discrete items. Ready as a reported fact. |
| H-IS-NI | Net earnings including noncontrolling interests | 4,200.3 | 3,283.4 | 4,124.7 | 3,762.3 | 1,856.7 | S-009 p. 41; S-001 p. 43 | Direct `income_statement.net_income` and `cash_flow.net_income` under the approved consolidated basis. | The attributable-to-Starbucks line differs by 1.0, 1.8, 0.2, 1.4, and 0.3 respectively; retain that line as disclosure, not as the model basis. |

**Reported income-statement bridge constituents deliberately not folded into H-IS-OPEX:** income
from equity investees was 385.3, 234.1, 298.4, 301.2, and 247.8; gain from sale of assets was 0,
0, 91.3, 0, and 0; FY2021 had an 864.5 net gain from divestiture; and interest income and other,
net was 90.1, 97.0, 81.2, 122.8, and 113.3. These make H-IS-NONOP reconcile reported net income
under the model presentation without altering reported source values.

### Balance sheet: reported facts and transparent aggregation

| Ledger ID | Required model input / reported definition | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Source ID and direct link; filing page/table | Model transformation | Risk / status |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| H-BS-CASH | Cash and cash equivalents | 6,455.7 | 2,818.4 | 3,551.5 | 3,286.2 | 3,219.8 | S-009 p. 43; [S-002](https://www.sec.gov/Archives/edgar/data/829224/000082922423000058/sbux-20231001.htm) p. 44; S-001 p. 45 | Direct `balance_sheet.cash`. | Ready; excludes separately reported short-term investments. |
| H-BS-AR | Accounts receivable, net | 940.0 | 1,175.5 | 1,184.1 | 1,213.8 | 1,277.5 | S-009 p. 43; S-002 p. 44; S-001 p. 45 | Direct `accounts_receivable`. | Net presentation; ready. |
| H-BS-INV | Inventories | 1,603.9 | 2,176.6 | 1,806.4 | 1,777.3 | 2,185.6 | S-009 p. 43; S-002 p. 44; S-001 p. 45 | Direct `inventory`. | Ready. |
| H-BS-OCA | Prepaid expenses and other current assets | 594.6 | 483.7 | 359.9 | 313.1 | 452.2 | S-009 p. 43; S-002 p. 44; S-001 p. 45 | Direct `other_current_assets`; short-term investments are excluded and recorded separately. | Ready; not an operating-NWC conclusion by itself. |
| H-BS-STI | Short-term investments | 162.2 | 364.5 | 401.5 | 257.0 | 247.2 | S-009 p. 43; S-002 p. 44; S-001 p. 45 | Direct `short_term_investments`, outside operating NWC and separately visible in the valuation bridge. | Non-operating asset treatment is an approved model convention; do not include again in cash or other non-operating assets. |
| H-BS-PPE | Property, plant and equipment, net | 6,369.5 | 6,560.5 | 7,387.1 | 8,665.5 | 8,493.5 | S-009 p. 43; S-002 p. 44; S-001 p. 45 | Direct `net_ppe`. | Ready. |
| H-BS-ONCA | Other noncurrent assets — sum of separately reported long-term investments, equity investments, operating lease ROU asset, deferred taxes, other LT assets, intangibles, and goodwill | 15,266.7 | 14,399.2 | 14,755.0 | 15,826.4 | 16,143.9 | S-009 p. 43; S-002 p. 44; S-001 p. 45 | Explicit aggregation of named reported balance-sheet rows, needed because model has one bucket. | Includes lease ROU asset, deferred taxes, goodwill and intangibles; **requires student approval** as model bucket definition. |
| H-BS-AP | Accounts payable | 1,211.6 | 1,441.4 | 1,544.3 | 1,595.5 | 1,852.8 | S-009 p. 43; S-002 p. 44; S-001 p. 45 | Direct `accounts_payable`. | Ready. |
| H-BS-ACCR | Accrued liabilities | 2,321.2 | 2,137.1 | 2,145.1 | 2,194.7 | 2,359.7 | S-009 p. 43; S-002 p. 44; S-001 p. 45 | Direct `accrued_liabilities`. | Excludes separately reported accrued payroll and benefits. Ready as labelled. |
| H-BS-OL | Other liabilities — balancing aggregate of accrued payroll/benefits, current operating-lease liability, stored-value/deferred revenue, noncurrent operating-lease liability, deferred revenue and other LT liabilities | 18,558.5 | 18,054.7 | 18,344.2 | 19,422.3 | 19,821.6 | S-009 p. 43; S-002 p. 44; S-001 p. 45 | Total liabilities − AP − accrued liabilities − H-BS-DEBT. Components remain disclosed separately in the cited table. | **Requires student approval:** combines operating and financing-like lease obligations with deferred revenue and payroll to fit one model bucket. |
| H-BS-DEBT | Total debt — short-term debt/commercial paper plus current portion of long-term debt plus long-term debt | 14,615.8 | 15,043.9 | 15,399.7 | 15,568.4 | 16,074.8 | S-009 p. 43; S-002 p. 44; S-001 p. 45 | Sum of named debt rows; direct `total_debt` only after debt-definition approval. | Excludes lease liabilities; FY2021 has no separately reported short-term debt. |
| H-BS-EQ | Total deficit (shareholders’ deficit plus noncontrolling interests) | (5,314.5) | (8,698.7) | (7,987.8) | (7,441.6) | (8,089.2) | S-009 p. 43; S-002 p. 44; S-001 p. 45 | Candidate `equity`, selected to make the reported balance sheet total exactly. | It is a deficit; use of total deficit vs. shareholders’ deficit needs documented model convention. |

### Cash flow and financing: reported facts

| Ledger ID | Required model input / reported definition | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Source ID and direct link; filing page/table | Model transformation | Risk / status |
|---|---|---:|---:|---:|---:|---:|---|---|---|
| H-CF-DA | Depreciation and amortization (cash-flow add-back) | 1,524.1 | 1,529.4 | 1,450.3 | 1,592.4 | 1,771.5 | S-009 p. 44; S-002 p. 45; S-001 p. 46 | Historical D&A reference; do not substitute income-statement D&A expense without documenting the difference. | CFO add-back differs from the D&A expense line (e.g., FY2025 1,771.5 vs. 1,684.7). Ready as reported cash-flow value. |
| H-CF-CAPEX | Additions to property, plant and equipment | (1,470.0) | (1,841.3) | (2,333.6) | (2,777.5) | (2,305.5) | S-009 p. 44; S-002 p. 45; S-001 p. 46 | Store absolute outflow values 1,470.0/1,841.3/2,333.6/2,777.5/2,305.5; engine subtracts capex in CFI and FCFF. | Ready under approved sign convention. |
| H-CF-DIV | Cash dividends paid | (2,119.0) | (2,263.3) | (2,431.8) | (2,585.0) | (2,771.4) | S-009 p. 44; S-002 p. 45; S-001 p. 47 | Store absolute distribution values 2,119.0/2,263.3/2,431.8/2,585.0/2,771.4; engine subtracts dividends in financing cash flow and equity. | Ready under approved sign convention. |
| H-CF-DEBT | Debt issuance / repayment components | Short-term +215.1; short-term repayment (349.8); LT issue 0; LT repayment (1,250.0); commercial-paper repayment (296.5) | Short-term +36.6; repayment (36.6); LT issue +1,498.1; LT repayment (1,000.0); commercial-paper repayment +175.0 as displayed | Short-term +114.6; repayment (78.8); LT issue +1,497.8; LT repayment (1,000.0); commercial paper (175.0) | Short-term +123.8; repayment (157.5); LT issue +1,995.3; LT repayment (1,825.1) | Short-term +2.4; repayment (7.8); LT issue +1,748.5; LT repayment (1,250.0) | S-009 p. 44; S-002 p. 45; S-001 p. 47 | Preserve components; calculate `net_debt_issuance` only after the treatment and signs of commercial paper are reconciled. | **Not ready:** label/sign presentation for commercial-paper repayment needs review; leases excluded from debt. |
| H-CF-ENDCASH | Ending cash and cash equivalents | 6,455.7 | 2,818.4 | 3,551.5 | 3,286.2 | 3,219.8 | S-009 p. 44; S-002 p. 45; S-001 p. 47 | Direct `cash_flow.ending_cash`; ties H-BS-CASH. | Ready. |

### Valuation-date bridge evidence (separate from FY2025 historical base year)

All balance-sheet values below are the latest eligible filing facts available by the 2026-10-19
source cutoff. They are **not** valuation-date balance-sheet observations: the filing is interim,
unaudited, and dated 2026-06-28. Do not create bridge inputs until any classification judgment is
approved.

| Ledger ID | Bridge input / filing definition | Reported value | Units | Source and as-of date | Page / table | Approved treatment / timing limitation | Definition risk |
|---|---|---:|---|---|---|---|---|
| V-CASH-2026Q3 | Cash and cash equivalents | 3,449.8 | USD millions | [S-010](https://www.sec.gov/Archives/edgar/data/829224/000082922426000130/sbux-20260628.htm), balance sheet as of 2026-06-28; filed 2026-07-29 | p. 5, Consolidated Balance Sheets | Candidate `valuation.cash`; add once. Interim balance is 113 days before valuation date. | Does not include short-term investments. |
| V-STI-2026Q3 | Short-term investments | 160.5 | USD millions | S-010, as of 2026-06-28; filed 2026-07-29 | p. 5, Consolidated Balance Sheets | Candidate `valuation.short_term_investments`; add once, outside operating NWC. | Confirm liquidity/mark-to-market treatment; do not include in cash or other non-operating assets. |
| V-DEBT-2026Q3 | Interest-bearing debt: current portion of long-term debt plus long-term debt | 13,278.6 = 1,498.4 + 11,780.2 | USD millions | S-010, as of 2026-06-28; filed 2026-07-29 | p. 5, Consolidated Balance Sheets | Candidate `valuation.debt`; deduct once. Excludes operating leases. | The balance sheet does not present short-term debt separately at this date; confirm no omitted interest-bearing borrowing in the debt note before final bridge. |
| V-LEASE-2026Q3 | Operating lease liabilities: current portion plus noncurrent operating lease liability | 9,155.5 = 1,271.3 + 7,884.2 | USD millions | S-010, as of 2026-06-28; filed 2026-07-29 | p. 5, Consolidated Balance Sheets | Candidate `valuation.lease_obligations`; deduct once, separate from debt. | Only operating lease liabilities are presented in the cited balance sheet; confirm treatment of any finance leases or other lease-related claims in notes before final bridge. |
| V-NCI-2026Q3 | Noncontrolling interests | 7.2 | USD millions | S-010, as of 2026-06-28; filed 2026-07-29 | p. 5, Consolidated Balance Sheets | Candidate `valuation.noncontrolling_interest`; deduct once as a distinct material claim and exclude from `other_material_claims`. | Equity component is interim and not a 2026-10-19 observation. |
| V-OMC-2026Q3 | Other material claims, excluding debt, leases, and NCI | 0.0 — documented bridge-screening judgment, **not a reported line item** | USD millions | S-010, Note 14 p. 28, Note 15 p. 29, cover/balance sheet p. 1/5, and filing text search | Proposed `other_material_claims = 0.0`: no preferred shares outstanding; no convertible instrument or contingent-consideration disclosure found; company states it is not party to a legal proceeding expected to have a material adverse effect and views material contingent-loss risk as remote. | Absence of a pension/postretirement disclosure in an interim filing is not proof that no obligation exists. Reconfirm against the next 10-K and do not include debt, leases, or NCI again. |
| V-NOA-2026Q3 | Long-term investments — available-for-sale corporate debt, mortgage/asset-backed, and U.S. Treasury securities | 313.2 | USD millions | S-010, balance sheet p. 5; Note 4 pp. 17–18, as of 2026-06-28 | Proposed `other_non_operating_assets` inclusion: **313.2 only**, added once; these are separately reported financial investments, not operating NWC. | Bridge classification judgment, not a filing label. Securities may be retained for liquidity or corporate uses; cash and short-term investments remain separate. |
| V-EQINV-2026Q3 | Equity investments | 1,700.0 | USD millions | S-010, balance sheet p. 5; Note 2 p. 12, as of 2026-06-28 | **Exclude from bridge other-non-operating assets.** The filing identifies a retained ~40% China joint-venture interest of approximately 1.2bn, accounted for under the equity method, as part of the Company’s long-term China strategy; do not characterize the full balance as excess cash. | The filing does not allocate the full 1.7bn balance among investments. Revisit only with an investee-by-investee carrying-value and strategic-purpose schedule. |
| V-SHARES-2026Q3 | Basic common shares outstanding for per-share valuation | 1,140.0 | million shares | S-010 cover p. 1, as of 2026-07-23; Note 12 p. 28; Note 14 p. 28 | Use **basic common shares outstanding** as the approved per-share denominator. Do not add the 8.9m nonvested RSUs or derive a fully diluted count from the weighted-average diluted EPS figures. | This observation is 88 days before the valuation date. The filing lacks award-level information and post-2026-07-23 activity needed for a defensible fully diluted count as of 2026-10-19. The 4.2m Q3 / 4.0m YTD dilutive EPS effects and 1,143.8m / 1,143.0m weighted-average diluted shares are period averages, not valuation-date counts. |
| V-PRICE-2026-10-19 | SBUX regular-session closing price | 97.87 | USD per share | [S-012](https://finance.yahoo.com/quote/SBUX/history/?p=SBUX), daily historical row for 2026-10-19; retrieved 2026-10-19 | Historical Data daily table; marked “At close: 4:00:00 PM EDT” | Use Yahoo Finance’s `Close` field: **$97.87**. It is split-adjusted but not adjusted for dividends/distributions; `Adj Close` was also $97.87 for this date, so no dividend/distribution adjustment changes the observation. | Nasdaq’s historical page did not provide a valid dated observation. A [Financial Times historical-data page](https://markets.ft.markitdigital.com/data/equities/tearsheet/historical?s=SBUX%3ANSQ) retrieved for the same date displayed $98.26, creating an unresolved third-party-source conflict; retain retrieval evidence and recheck against a second regular-close source before treating the price as final. |

### Financing-policy evidence — latest eligible interim filing

| Ledger ID | Reported fact | Amount / terms | Source / page | Forecast-policy treatment | Risk |
|---|---|---|---|---|---|
| F-LIQ-CASH-2026Q3 | Cash and investments | 3.9bn as of 2026-06-28; approximately 1.1bn of cash and short-term investments held in foreign subsidiaries | S-010, Liquidity p. 51 | Supports the existence of material liquidity but **does not state a minimum cash policy**. The model’s $1.0bn floor is student judgment. | Interim point-in-time balance; foreign cash may not be freely deployable. |
| F-REVOLVER-2026Q3 | 2025 unsecured revolving credit facility | 3.0bn committed, including 150.0m available for letters of credit; matures 2030-06-13; no borrowings outstanding; available for working capital, capex, and general corporate purposes | S-010, Note 8 p. 22; Liquidity p. 51 | Model uses a maximum 3.0bn automatic draw capacity only. It excludes the uncommitted 1.0bn potential increase. | Term SOFR/Base Rate plus ratings-based margin; the filing does not provide a forecast all-in rate. Fixed-charge covenant must remain satisfied. |
| F-CP-2026Q3 | Commercial-paper program | Up to 3.0bn outstanding; individual maturities not over 397 days; backstopped by the 2025 credit facility; no borrowings outstanding | S-010, Note 8 p. 22; Liquidity p. 51 | Treated as the same 3.0bn committed backstop, not additive capacity. Company disclosures permit proceeds for working capital, capex, dividends, and repurchases. | Short-term refinancing and rate risk; do not add to revolver capacity. |
| F-DEBT-MAT-2026Q3 | Long-term debt maturities | FY2027 1,500.0; FY2028 1,076.5; FY2029 1,750.0; FY2030 928.2; thereafter 8,129.4 USD millions | S-010, Note 8 p. 24 | Existing maturity schedule is not modeled as a debt repayment forecast. The automatic-draw policy therefore is a liquidity floor only, not a maturity/refinancing plan. | Material maturity/refinancing omission remains. |
| F-DIV-2026Q3 | Cash dividend declarations | 0.62 per share for Q3; 1.86 per share for the three quarters ended 2026-06-28 | S-010, Statements of Equity p. 7 | Base model retains flat FY2025 cash dividends; no cut or increase is assumed to fund the cash floor. | Declared dividends are not a five-year policy commitment. |

### Operating, store, and geographic evidence

| Ledger ID | Reported fact | Period / reported value | Units / definition | Source ID and direct link; page/table | Model treatment and risk |
|---|---|---|---|---|---|
| O-STORE-25 | Company-operated stores | FY2025 end: North America 11,018; International 10,496; total **21,514** | Stores at 2025-09-28; 52% of 40,990 total stores. | [S-001](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm), Item 1 pp. 6–8, Company-operated and Licensed Store Summary | Direct evidence for company-operated footprint. Do not use as average stores or revenue without a stated transformation. |
| O-STORE-LIC-25 | Licensed stores | FY2025 end: North America 7,293; International 12,183; total **19,476** | Stores at 2025-09-28; remaining 48% of total stores. | [S-001](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm), Item 1 pp. 6–8, licensed-store table | Direct evidence for licensed footprint. Transfers/closures affect period comparability. |
| O-COMP-25 | Comparable-store sales, transactions, average ticket — global / North America / International / China | FY2025: global −1% / −2% / +1%; North America −2% / −4% / +2%; International 0% / +2% / −2%; China −1% / +4% / −5% | Percent changes. Comparable stores are company-operated stores open at least 13 months; FX excluded; temporary closures remain and permanent closures are removed the following month. | [S-004](https://investor.starbucks.com/news/financial-releases/news-details/2025/Starbucks-Reports-Q4-and-Full-Fiscal-Year-2025-Results/default.aspx), FY2025 highlights; S-001 Item 7 p. 27 definition | Preserve as separate causal indicators; do not add percentages mechanically. FY2025 restructuring closures and stated methodology limit cross-period comparability. |
| O-SEG-25 | Reportable-segment composition and revenue share | North America 74%; International 21%; Channel Development 5% of FY2025 net revenues | Starbucks reports North America (U.S./Canada), International (including China, Japan, APAC, EMEA, Latin America/Caribbean), and Channel Development; Corporate and Other is unallocated. | [S-001](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm), Item 1 p. 6 | Geography is not identical to the historical "Americas/China-Asia-Pacific" labels; map only with a documented reclassification policy. |
| O-SEG-Q4-25 | Q4 North America / International / China operating disclosure | North America revenue 6,901.5, operating income 308.5, margin 4.5%; International 2,070.9, 223.2, 10.8%; China revenue 831.6, comp +2%, transactions +9%, ticket −7%, stores 8,011 | USD millions except percentages and stores; Q4 ended 2025-09-28. | [S-004](https://investor.starbucks.com/news/financial-releases/news-details/2025/Starbucks-Reports-Q4-and-Full-Fiscal-Year-2025-Results/default.aspx), segment tables and China supplemental data | Quarter only; not a FY2025 segment annualization input. China is within International, not a current reportable segment. |

### Approved model-mapping policy (no forecast values approved)

**Sign convention.** Monetary expenses and cash outflows are stored as **positive** values in
historical inputs, forecast assumptions, and output statements. `interest_expense`, `capex`, and
`dividends` are therefore positive magnitudes. The engine subtracts them where applicable.
`non_operating_income_expense` is the sole signed exception: positive is income/gain and negative
is expense/loss; the engine adds it to pre-tax income. This policy applies to FCFF: `FCFF = EBIT −
cash taxes + D&A − capex − change in operating NWC`.

| Unresolved historical item | Approved accounting mapping | Source-ledger treatment / remaining risk |
|---|---|---|
| Equity-investee income, asset-sale gains, divestiture gains, and future analogous income/expense | New `income_statement.non_operating_income_expense`; historical value is the signed sum of those reported pre-tax items after any separately disclosed classification review. Forecast is the separately approved `non_operating_income_expense` series; no item is placed in operating expenses. | H-IS-OPEX remains operating expenses only. Each historical aggregation must preserve the constituent filing lines. A recurring forecast requires a separate student judgment. |
| Short-term investments | New `balance_sheet.short_term_investments` and forecast ending-balance series. It is outside operating NWC; `cash_from_investing = −capex − change_in_short_term_investments`. | Do not include it in H-BS-OCA. In the valuation bridge, it is added once as `short_term_investments`, separately from cash and other non-operating assets. |
| Interest-bearing debt | `total_debt` contains only commercial paper/short-term debt/current LT debt/long-term debt. | H-BS-DEBT; operating and finance lease liabilities are excluded. |
| Lease obligations | Lease liabilities remain visible in the H-BS-OL aggregation only to preserve historical total-liability articulation; they are separately supplied as `valuation.lease_obligations` and deducted once in the enterprise-to-equity bridge. | Risk of double counting if a valuation input includes a lease claim already embedded in another claims field; prohibit that duplicate entry. |
| Net income, equity, and NCI | Model basis is consolidated: `net_income` is **net earnings including noncontrolling interests** and `equity` is the filing’s **total deficit** (shareholders’ deficit plus NCI). NCI is also a distinct bridge material claim (`valuation.noncontrolling_interest`), sourced at the latest eligible balance-sheet date. | This exactly matches the historical cash-flow starting line and balance-sheet total. In the bridge, NCI is deducted once and is excluded from `other_material_claims`; interim timing remains a risk. |

### Reconciliation and readiness gate

The historical source extraction is complete as reported facts, but a `verified.json` file must
not be created until these source-to-model definition choices are approved:

1. **Historical non-operating aggregation:** transcribe and reconcile each annual signed sum into
   the new line; the policy is approved, but values must still be checked from each cited filing.
2. **Balance-sheet buckets:** the model's single `other_noncurrent_assets` and `other_liabilities`
   buckets require the transparent aggregations above; it separately has no fields for short-term
   investments, lease ROU assets/liabilities, deferred revenue, payroll accruals, goodwill, or
   deferred taxes.
3. **Leases and bridge:** the historical balance sheet may aggregate lease liabilities into other
   liabilities, but later valuation inputs must document an unduplicated lease-obligation figure.
4. **NCI forecast treatment:** the approved historical consolidated basis does not itself support
   a forecast assumption about NCI earnings or distributions.

## Source-to-input assignment (no model values entered)

The rows below identify the reported-fact source to extract. They do **not** constitute an
assumption, a normalization, or a model input until the specific value is transcribed, checked,
and linked to its source row.

| Input family | Primary source ID | Reporting periods available | Table / section | Units and definition | Transformation | Risk |
|---|---|---|---|---|---|---|
| Five-year income statement | S-001 + S-002 | FY2025–FY2021 | Consolidated Statements of Earnings | USD millions, except per-share data; consolidated annual statement | Combine overlapping annual statements only after matching fiscal year-end and week count | FY2021 is a 53-week year; classifications may change. |
| Five-year balance sheet | S-001 + S-002 | FY2025–FY2021 as annual snapshots, subject to available comparative balance sheets | Consolidated Balance Sheets | USD millions, except per-share data; point-in-time balances | Use year-end snapshots; preserve any unavailable prior snapshot as missing | Five-year balance-sheet series may require additional annual reports; do not estimate missing years. |
| Five-year cash-flow statement | S-001 + S-002 | FY2025–FY2021 | Consolidated Statements of Cash Flows | USD millions; annual cash-flow statement | Combine overlapping annual statements after fiscal-calendar review | FY2021 is a 53-week year; cash-flow classifications may differ. |
| Company-operated and licensed store count | S-001 | FY2025 and FY2024 opening/closing store tables; historical expansion requires earlier annual reports | Item 1, Company-operated and Licensed Store Summary and store-data tables | Store count at stated date; company-operated and licensed presented separately | Keep store type and geography separate | Store closures/transfers and fiscal-period ending dates affect comparability. |
| Comparable-store sales, transactions, average ticket | S-004 | Q4/FY2025; use corresponding official releases for prior quarters | FY2025 highlights and segment tables | Percentage changes under Starbucks’ reported comparable-store methodology | Do not combine component percentages into a new metric without disclosure | Quarterly versus annual period, geographic scope, and metric definition may change. |
| Americas/North America, International, China/Asia-Pacific information | S-001 + S-004 + S-003 | FY2025 and applicable quarterly periods | Item 1/Item 7 segment disclosures and earnings-release segment tables | Company-reported segment/geography labels and USD millions where disclosed | Preserve reported label; map only with a documented reason | Segment composition and China classification can change; S-003 flags a held-for-sale classification. |
| Operating margin, tax, stock compensation, D&A, capex, inventory, working capital | S-001 | FY2025–FY2023 | Statements of Earnings/Cash Flows/Balance Sheets and related notes | USD millions unless stated otherwise | Use reported value first; separately document any FCFF mapping | Cash-tax, working-capital, and D&A definitions may differ from valuation convention. |
| Cash, debt, lease obligations, diluted shares | S-001 | FY2025/FY2024 balance-sheet and annual diluted weighted-average shares | Balance Sheets p. 45; Statements of Earnings p. 43; debt, lease, and EPS notes | USD millions; shares in millions where presented | Keep cash, debt, lease liabilities, and weighted-average diluted shares distinct | End-period shares and weighted-average diluted shares are not interchangeable. |
| Restructuring, impairments, disposal items, accounting changes | S-001 + S-003 | FY2025 and applicable interim periods | Item 7; PP&E, restructuring, impairment, lease, tax, and accounting-policy notes | Reported amount and description in disclosed units | No normalization until recorded as a student judgment in the contamination catalog | Recurrence and cash/noncash treatment require evidence; interim classification changes may distort comparison. |
| Market price, risk-free rate, WACC inputs | S-006 + S-007; additional approved methodology source required for beta/ERP | Valuation-date observation only | Treasury daily yield table; Nasdaq historical-price response | Yield in percent; share price in USD, subject to provider field definition | Record date/time, tenor, adjustment convention, and methodology | No valuation date, source cutoff, beta methodology, or ERP source has been approved; leave these inputs blank. |

## Assumptions are not reported facts

Forecast growth, margins, reinvestment rates, WACC, terminal growth, peer selections, and any
normalization are **student assumptions/judgments**. Enter them in the approved-assumptions file
and `assumption-challenge-record.md`, with their source-evidence basis and risk. Do not place
them in this source ledger as reported Starbucks facts.

## Five-year financial statements

Enter one row per line item and fiscal year (or cite a source table that supports multiple rows).
Record values as reported first; document any reclassification, annualization, or normalization.

| Source ID | Statement | Fiscal year / period | Line item | Reported value | Units | Definition | Page / table | Transformation to model input | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [source ID] | Income statement | [FY] | [line item] | [value] | [units] | [reported definition] | [page/table] | [none or documented transformation] | [risk] |
| [source ID] | Balance sheet | [FY] | [line item] | [value] | [units] | [reported definition] | [page/table] | [none or documented transformation] | [risk] |
| [source ID] | Cash-flow statement | [FY] | [line item] | [value] | [units] | [reported definition] | [page/table] | [none or documented transformation] | [risk] |

## Store footprint and operating drivers

Use company-reported definitions. Separate company-operated and licensed stores, and do not
combine them without a documented reason.

| Source ID | Metric | Geography / segment | Fiscal year / quarter | Reported value | Units | Definition | Page / table | Transformation | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [source ID] | Company-operated store count | [geography/segment] | [period] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Licensed store count | [geography/segment] | [period] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Comparable-store sales | [geography/segment] | [period] | [value] | [%] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Transactions | [geography/segment] | [period] | [value] | [% or units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Average ticket | [geography/segment] | [period] | [value] | [% or currency] | [definition] | [page/table] | [transformation] | [risk] |

## Segment information

Use the segments and geographies reported in the applicable period. Record Americas,
International, and China/Asia-Pacific information when applicable; explain any change in naming,
composition, or disclosure.

| Source ID | Reported segment / geography | Fiscal year / quarter | Metric | Reported value | Units | Definition | Page / table | Transformation | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [source ID] | Americas | [period] | [metric] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | International | [period] | [metric] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | China/Asia-Pacific, if applicable | [period] | [metric] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |

## Profitability, capital structure, and tax inputs

Include reported values and any valuation-specific treatment. Do not treat lease, debt, or share
metrics as interchangeable without documenting definitions and timing.

| Source ID | Input | Fiscal year / quarter / as-of date | Reported value | Units | Definition | Page / table | Transformation | Risk |
|---|---|---|---|---|---|---|---|---|
| [source ID] | Operating margin | [period] | [value] | [%] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Operating lease liability / lease input | [period] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Debt | [period] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Cash and cash equivalents | [period] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Diluted shares | [period] | [value] | [shares] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Stock-based compensation | [period] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Income-tax expense / rate | [period] | [value] | [units or %] | [definition] | [page/table] | [transformation] | [risk] |

## Reinvestment and working-capital inputs

| Source ID | Input | Fiscal year / period | Reported value | Units | Definition | Page / table | Transformation | Risk |
|---|---|---|---|---|---|---|---|---|
| [source ID] | Capital expenditures | [period] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Depreciation and amortization | [period] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Inventory | [period] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Accounts receivable | [period] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Other operating current assets / liabilities | [period] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |
| [source ID] | Net working capital / change in NWC | [period] | [value] | [units] | [definition] | [page/table] | [transformation] | [risk] |

## One-time items and accounting changes

Capture the original report and the treatment decision. A nonrecurring label is an analytical
judgment, not a source fact; support it with evidence and disclose its risk.

| Source ID | Item | Fiscal year / period | Reported value | Units | Reported description | Page / table | Proposed treatment | Basis for treatment | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [source ID] | Restructuring | [period] | [value] | [units] | [description] | [page/table] | [treatment] | [evidence] | [risk] |
| [source ID] | Impairment | [period] | [value] | [units] | [description] | [page/table] | [treatment] | [evidence] | [risk] |
| [source ID] | One-time item | [period] | [value] | [units] | [description] | [page/table] | [treatment] | [evidence] | [risk] |
| [source ID] | Accounting change / restatement | [period] | [value] | [units] | [description] | [page/table] | [treatment] | [evidence] | [risk] |

## Peer, market, and WACC inputs

For every market observation, record its as-of date/time and provider. Record the calculation
method separately when the model derives a value from multiple inputs.

| Source ID | Input | Company / market | Observation date/time | Value | Units | Definition / methodology | Page / table or provider field | Transformation / calculation | Risk |
|---|---|---|---|---|---|---|---|---|---|
| [source ID] | Peer inclusion / exclusion evidence | [candidate] | [date] | [n/a] | [n/a] | [comparability definition] | [location] | [peer-policy reference] | [risk] |
| [source ID] | Share price / market capitalization input | [company] | [as-of date/time] | [value] | [currency or units] | [field definition] | [provider field] | [calculation] | [risk] |
| [source ID] | Equity beta or beta input | [company] | [as-of date/time] | [value] | [x] | [lookback/frequency definition] | [provider field] | [calculation] | [risk] |
| [source ID] | Risk-free rate | [market] | [as-of date/time] | [value] | [%] | [instrument and tenor] | [provider field] | [calculation] | [risk] |
| [source ID] | Equity risk premium input | [market] | [as-of date/time] | [value] | [%] | [methodology] | [provider field] | [calculation] | [risk] |
| [source ID] | Cost of debt / yield input | [company or market] | [as-of date/time] | [value] | [%] | [instrument or methodology] | [provider field] | [calculation] | [risk] |
| [source ID] | Tax rate for WACC | [company] | [period] | [value] | [%] | [definition] | [page/table] | [calculation] | [risk] |
| [source ID] | Capital structure weight | [company] | [as-of date/time] | [value] | [%] | [definition] | [provider field] | [calculation] | [risk] |

### Completed peer evidence for the 2026-10-19 comparison

Peer screening and calculations are in [peer-policy.md](peer-policy.md). The evidence set is
limited to one qualified quantitative reference (MCD); Yum! Brands was reviewed but excluded
from calculation, and Restaurant Brands International remains unassessed because a complete
cutoff-specific source package was not assembled. The one-peer result is not a statistical peer
range.

| Source ID | Input / calculation | Company / period | Value | Units | Definition / transformation | Risk |
|---|---|---|---:|---|---|---|
| P-001 | FY2025 operating income / D&A / net income | MCD FY ended 2025-12-31 | 12,393 / 2,199 / 8,563 | USD millions | Audited GAAP annual values; 10-K pp. 38 and 41. | Annual period ends three months later than Starbucks FY2025; reported, not normalized. |
| P-002 | LTM operating income / D&A / net income | MCD LTM to 2026-06-30 | 12,805 / 2,266 / 8,787 | USD millions | FY2025 plus six months to 2026-06-30 less six months to 2025-06-30; 10-Q pp. 4, 6. | Interim reports unaudited; no day-based calendarization. |
| P-002 | Basic common shares outstanding | MCD, as of 2026-06-30 | 707.641531 | million shares | Form 10-Q cover, p. 1. Used as point-in-time basic count; not weighted-average diluted shares. | Share count is 111 days earlier than valuation-date close. |
| P-002 | Debt / cash / operating lease liabilities | MCD, as of 2026-06-30 | 39,863 / 822 / 14,729 | USD millions | Balance sheet p. 3; debt excludes lease liabilities; lease liability = current 690 + long-term 14,039. EV multiple excludes leases consistently with EBITDA retaining rental/occupancy expense. | Current debt not separately presented; lease-excluded EV/EBITDA is not comparable with lease-capitalized EV definitions. |
| P-003 | Regular close | MCD, 2026-10-19 4:00 PM EDT | 242.67 | USD/share | StockAnalysis historical row, `Close`; not adjusted close. Market cap = 242.67 × 707.641531 = 171,723.37032777 USD millions. | Third-party historical provider; share count does not share the observation date. |
| P-004 | Close cross-check | MCD, 2026-10-19 3:59:58 PM EDT | 242.66 | USD/share | ChartExchange close. | $0.01 disagreement with P-003 retained, not reconciled. |
| P-001–P-004 | EV / LTM EBITDA | MCD, price 2026-10-19; LTM to 2026-06-30 | 13.9848× (14.0× rounded) | x | EV = basic market cap 171,723.3703 + debt 39,863 − cash 822 = 210,764.3703 USDm. EBITDA = LTM operating income 12,805 + LTM D&A 2,266 = 15,071 USDm. Lease obligations and preferred/NCI claims excluded; preferred reported none, no separate NCI presented. | Single qualified franchise-heavy peer. EBITDA is unadjusted; lease and revenue-mix differences are material. |
| P-001–P-003 | Market cap / LTM net income (P/E) | MCD, price 2026-10-19; LTM to 2026-06-30 | 19.5429× (19.5× rounded) | x | Basic market capitalization 171,723.3703 USDm / reported LTM net income 8,787 USDm. USD; no normalization. | Basic point-in-time shares are stale versus price; earnings include restructuring/other items; one-peer result only. |
| P-005–P-006 | Exclusion evidence | Yum! Brands; FY2025 and H1 2026 | Not calculated | n/a | SEC filings describe four-brand portfolio, 63,000+ restaurants, and a primarily franchise/operate business model. | Brand/category and franchising mix are materially different from Starbucks; no quantitative peer use. |

## Completeness check

- [ ] Every five-year financial-statement line used in the model has a source ID.
- [ ] Operating metrics and segment data use company-reported definitions and periods.
- [ ] Every market and WACC input has an authoritative source, as-of date/time, and definition.
- [ ] Every transformation is reproducible from reported values.
- [ ] Every material uncertainty, adjustment, and exclusion appears in the risk column and, when
  relevant, in `assumption-challenge-record.md` and `validation-and-ai-use.md`.
