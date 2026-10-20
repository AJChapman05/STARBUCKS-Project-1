# Research Evolution

## Edition A — preserved baseline

The student reports that Edition A and its Brightspace receipt are complete and saved outside
this repository. No Edition A document or receipt is included here, so the precise original thesis,
inputs, and language cannot be independently compared in this project copy. No Edition A material
was edited or reconstructed.

## Edition B — evidence-based update through 2026-10-19

**Decision user:** hypothetical buy-side long-only U.S. equity fund investment committee.  
**Decision horizon:** 12 months, quarterly monitoring.  
**Valuation date:** 2026-10-19.  
**Source cutoff:** public information available by 4:00 PM Eastern Time on 2026-10-19.

| Item | Edition A evidence available here | Edition B evidence/output | Reason for evolution | Status |
|---|---|---|---|---|
| Thesis / committee action | Edition A itself is not stored here; exact initial thesis unavailable for comparison. | Conditional **do not initiate** at approximately $98; computed base and high cases are $16.85 and $30.85 per basic share. The $9.91 low case is excluded from actionable comparison because it fails liquidity capacity. | The completed model shows substantial modeled value below the dated price in the base/high cases, while important market and valuation limitations remain. | Conditional, not final; see decision memo. |
| Historical evidence | No local Edition A input set available for comparison. | FY2021–FY2025 filings mapped in source ledger; FY2025 verified base year retained. | Builds an auditable historical base and keeps reported figures distinct from model transformations. | Historical reconciliation passes. |
| Assumption/model design | Not independently comparable to Edition A. | Student-judgment five-year statements, causal operating cases, FCFF DCF, WACC/growth grid, capex sensitivity, and committed-liquidity policy. | Makes assumptions, ranges, and financing treatment explicit and testable. | Proposal; review and source limitations remain. |
| Liquidity risk | Not independently comparable to Edition A. | Initial zero-financing run had negative cash in FY2028–FY2030. Updated base draws $2.75bn cumulative against $3.0bn committed capacity; low case and high-capex sensitivity fail the capacity check. | Filing evidence supports committed capacity, but not the $1.0bn cash floor or 5.0% interest-rate proxy. | Model warning remains material. |
| Market/valuation uncertainty | Not independently comparable to Edition A. | Yahoo Finance regular close $97.87 conflicts with Financial Times $98.26; WACC 9.0% and terminal growth 2.5% are provisional. | Dated close and discount-rate methodology are not fully reconciled. | Not resolved. |

## What changed and why

Edition B now has a cited FY2025 historical base, five-year model, explicit bridge, and validation
evidence. Forecast drivers, WACC, terminal growth, dividend treatment, and minimum-cash policy are
student judgments rather than sourced forecasts. The first forecast showed cash below zero under
flat dividends and no additional financing. The later policy draws only on the latest filing’s
$3.0bn committed revolver/CP backstop and preserves the prior negative-cash result in the validation
record. This improves the liquidity presentation but does not solve the low-case funding shortfall
or debt-refinancing plan.

## Evidence classification and AI-use disposition

| Type | Entry | Citation / path | Status |
|---|---|---|---|
| Sourced fact | FY2025 net revenues $37,184.4m; global comparable sales −1%; FY2026 Q3 filing reports $3.0bn committed revolving capacity. | `H-IS-REV`, `O-COMP-25`, `F-REVOLVER-2026Q3` in `docs/source-ledger.md` | Filing-derived; the facility was undrawn as of 2026-06-28. |
| Student assumption | $1.0bn cash floor, 5.0% borrowing proxy, $16.85 base and $30.85 high-case outputs dependent on approved judgment inputs. | `A-001`–`A-013`, `A-021`; `outputs/forecast-base.json` | Scenario/model inputs are not company guidance. |
| Model output | Five-year statements articulate; DCF value and scenario outputs are generated. | `outputs/forecast-base.json`, `visible_output.json` | Tests pass; low and high-capex cases fail minimum-liquidity check. |
| Risk / monitoring trigger | Two consecutive quarters at/above 0% or at/below −2% global comps; cash below $1.0bn; remaining committed capacity below $500m; base value changes at least 20% or reaches approximately $98. | `docs/decision-memo.md` | Student thresholds for review, not automatic action rules. |
| AI-use disposition | AI-assisted drafting and model implementation were used; generated assumptions were labeled as student judgments and checked by running the local engine and tests. | `docs/validation-and-ai-use.md` | Modify/qualify: outputs are reproducible from local inputs; evidence and unresolved limitations remain visible. |

## Remaining comparison limitation

Because Edition A is stored only by the student outside this project, this record cannot claim
which specific recommendation, assumption, or sentence changed from Edition A. Compare this table
with the preserved course submission before treating the A-to-B narrative as complete.
