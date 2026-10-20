# Base-Year Contamination Catalog — Starbucks Valuation

## Status

The source ledger now identifies official SEC/Starbucks sources, but the project has not selected
a valuation date or base year. The disclosed items below are a research catalog, **not** a decision
to adjust any base-year figure. Apply an item only if it falls inside the approved base period and
its definition, units, and model mapping are verified.

An item appearing in this catalog is a review category, not evidence that it occurred. A
normalization is an analytical choice, not a reported fact: every proposed normalization below is
explicitly **MY JUDGMENT** and requires your decision, rationale, and uncertainty assessment.

## Review protocol

1. Record the reported fact exactly as disclosed, including its fiscal period, amount, units, and
   definition.
2. Link the fact to its source-ledger ID and provide the direct filing/release citation.
3. State a proposed base-year treatment only after distinguishing a reported disclosure from your
   analytical judgment.
4. Quantify the effect only from a verified figure. If the effect cannot be computed, write
   `not quantified — source or definition missing`; do not estimate it.
5. Keep the item unadjusted when the evidence does not support a normalization.

## Disclosed items requiring base-year review

| Item | Reported fact — sourced disclosure | Source citation | Proposed normalization — **MY JUDGMENT** | Rationale — **MY JUDGMENT** | Quantified effect on base year | Uncertainty / limit |
|---|---|---|---|---|---|---|
| FY2025 restructuring and impairment | Starbucks reported $892 million of restructuring and impairments in FY2025. The disclosure identifies $352.8 million related to impairment and disposition of company-operated-store assets and $239.3 million primarily related to accelerated amortization of ROU lease assets and other lease-exit costs from store closures. | [S-001 FY2025 Form 10-K, Item 7/Restructuring discussion](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm); source-ledger S-001. | **MY JUDGMENT: no normalization selected.** | **MY JUDGMENT:** Assess recurrence, cash effect, tax treatment, and overlap with PP&E/lease lines before any adjustment. | Reported FY2025 amount: $892.0 million. No model adjustment quantified. | The disclosed total has components with potentially different cash, lease, and recurring-cost implications; avoid double counting against individual impairment/disposition or lease-exit rows. |
| FY2025 disposal/impairment charges | Starbucks disclosed net disposition and impairment charges of $595.3 million in FY2025, including $102.2 million of impairment losses in store operating expenses; it also states that $352.8 million of total impairment/disposition charges was restructuring-related. | [S-001 FY2025 Form 10-K, Note 6 / PP&E discussion, p. 52](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm); source-ledger S-001. | **MY JUDGMENT: no separate normalization selected.** | **MY JUDGMENT:** Treat only as an analytical cross-check against the restructuring row unless a non-overlapping component can be identified. | Reported FY2025 net disposition and impairment charge: $595.3 million. No separate adjustment quantified. | This row overlaps the FY2025 restructuring/impairment disclosure; summing the two would overstate an adjustment. |
| FY2025 discrete tax items | Starbucks reported a 25.9% FY2025 effective tax rate versus 24.3% in FY2024. It attributed approximately +290 basis points to changed indefinite-reinvestment assertions for certain foreign entities and approximately −120 basis points to a tax-status change for a certain foreign entity. | [S-001 FY2025 Form 10-K, MD&A tax-rate discussion, p. 31 and Note 14](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm); source-ledger S-001. | **MY JUDGMENT: no tax-rate normalization selected.** | **MY JUDGMENT:** Determine whether the FCFF tax convention uses reported cash taxes, a normalized operating tax rate, or another disclosed method before adjusting. | Reported directional effects: +290 bps and −120 bps; no dollar adjustment or normalized tax rate calculated. | The filing identifies discrete rate effects but not a valuation-model tax policy; a rate adjustment could be inappropriate or duplicate other tax assumptions. |
| FY2025 segment-disclosure accounting adoption | Starbucks adopted enhanced segment-disclosure guidance in Q4 FY2025. The filing states that the amendments did not change segment determination, aggregation, or reportable-segment thresholds. | [S-001 FY2025 Form 10-K, Recent Accounting Pronouncements](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm); source-ledger S-001. | **MY JUDGMENT: no normalization selected.** | **MY JUDGMENT:** Treat as disclosure-only unless source review finds a measurement or presentation change affecting the chosen input. | No reported income-statement, cash-flow, or valuation effect identified in the cited disclosure. | Confirm that later segment tables remain comparable before using them in a trend analysis. |
| FY2026 China retail operations held for sale / basis change | In FY2026, Starbucks classified its China retail disposal group as held for sale, ceased related PP&E depreciation and operating-lease ROU amortization, and changed indefinite-reinvestment assertions. The filing says no impairment was recorded on classification; it also describes later deconsolidation and a shift to equity-method income/product-sales/royalty revenue. | [S-003 FY2026 Form 10-Q, Assets Held for Sale and related notes, pp. 10–11](https://www.sec.gov/Archives/edgar/data/829224/000082922426000080/sbux-20260329.htm); source-ledger S-003. | **MY JUDGMENT: no normalization selected.** | **MY JUDGMENT:** Do not blend pre- and post-transaction operating metrics unless the approved valuation date/base period requires it and a documented recast/mapping is available. | Reported at 2026-03-29: assets held for sale $5,043.4 million; liabilities held for sale $1,685.6 million. No base-year adjustment made. | This is post-FY2025 and may be outside the source cutoff. It changes comparability of depreciation, lease amortization, tax expense, segment composition, and revenue recognition. |
| FY2026 China-related discrete tax effect | The FY2026 interim filing attributes a $273 million discrete income-tax expense effect (approximately 1,830 bps) to changed indefinite-reinvestment assertions upon China held-for-sale classification. | [S-003 FY2026 Form 10-Q, Income Taxes discussion](https://www.sec.gov/Archives/edgar/data/829224/000082922426000080/sbux-20260329.htm); source-ledger S-003. | **MY JUDGMENT: no normalization selected.** | **MY JUDGMENT:** Consider only if the selected base period includes this interim period and the approved tax convention supports separate treatment. | Reported interim discrete tax effect: $273 million; no model adjustment made. | Post-FY2025 timing and transaction-specific nature may make it ineligible for the selected valuation period. |

## Exclusions from this catalog

No separate litigation, regulatory-settlement, or disposal-gain item is cataloged because the
reviewed source excerpts did not provide a specific, model-relevant disclosure that could be
recorded without inference. Add an item only after citing a verified filing or earnings-material
disclosure in the source ledger.

## Decision checklist for each populated item

- [ ] Reported fact matches the cited source’s definition, period, units, and sign.
- [ ] The fact is present in `source-ledger.md` with a complete citation.
- [ ] **MY JUDGMENT:** I have decided whether to retain, normalize, separately model, or exclude
  the item and have not represented that choice as a company-reported fact.
- [ ] **MY JUDGMENT:** I have explained whether the item is likely recurring, its expected timing,
  and why the proposed treatment is appropriate.
- [ ] Any base-year, tax, cash-flow, margin, or valuation effect is calculated from verified inputs
  and is linked to a reproducible file or test.
- [ ] Remaining uncertainty is disclosed in `validation-and-ai-use.md` and, where material, in the
  decision memo.
