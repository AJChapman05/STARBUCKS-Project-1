"""Known-answer and loud-failure tests using synthetic, non-Starbucks fixtures only."""
import json
from copy import deepcopy
from pathlib import Path
import unittest

from analysis import ModelValidationError, run_analysis


FIXTURES = Path(__file__).with_name("fixtures")


def fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class ThreeStatementModelTests(unittest.TestCase):
    def test_synthetic_known_answer_first_forecast_year(self) -> None:
        result = run_analysis(fixture("synthetic_historical.json"), fixture("synthetic_assumptions.json"))
        self.assertEqual(len(result["forecast_years"]), 5)
        year_one = result["forecast_years"][0]
        self.assertEqual(year_one["year"], 2025)
        self.assertAlmostEqual(year_one["income_statement"]["revenue"], 110.0)
        self.assertAlmostEqual(year_one["income_statement"]["net_income"], 15.0)
        self.assertAlmostEqual(year_one["balance_sheet"]["cash"], 14.1)
        self.assertAlmostEqual(year_one["cash_flow"]["ending_cash"], 14.1)

    def test_every_synthetic_forecast_year_reconciles(self) -> None:
        result = run_analysis(fixture("synthetic_historical.json"), fixture("synthetic_assumptions.json"))
        for year in result["forecast_years"]:
            balance = year["balance_sheet"]
            assets = sum(balance[key] for key in ("cash", "short_term_investments", "accounts_receivable", "inventory", "other_current_assets", "net_ppe", "other_noncurrent_assets"))
            liabilities = sum(balance[key] for key in ("accounts_payable", "accrued_liabilities", "other_liabilities", "total_debt"))
            self.assertAlmostEqual(assets, liabilities + balance["equity"])
            self.assertAlmostEqual(year["cash_flow"]["ending_cash"], balance["cash"])

    def test_synthetic_dcf_exposes_bridge_and_monotonicity_checks(self) -> None:
        result = run_analysis(fixture("synthetic_historical.json"), fixture("synthetic_assumptions.json"))
        dcf = result["dcf"]
        self.assertEqual(len(dcf["fcff_forecast"]), 5)
        self.assertIn("enterprise_value", dcf)
        self.assertIn("implied_value_per_common_share", dcf["enterprise_to_equity_bridge"])
        self.assertTrue(dcf["sensitivity_checks"]["higher_wacc_reduces_enterprise_value"])
        self.assertTrue(dcf["sensitivity_checks"]["higher_terminal_growth_increases_enterprise_value"])

    def test_cases_sensitivities_and_market_implied_output_are_visible(self) -> None:
        result = run_analysis(fixture("synthetic_historical.json"), fixture("synthetic_assumptions.json"))
        analysis = result["decision_analysis"]
        self.assertEqual(set(analysis["cases"]), {"low", "base", "high"})
        self.assertEqual(len(analysis["wacc_terminal_growth_sensitivity"]), 4)
        self.assertEqual(analysis["one_at_a_time_sensitivities"][0]["driver"], "revenue_growth")
        self.assertIn("implied_terminal_growth", analysis["market_implied_expectation"])

    def test_operating_drivers_build_revenue_and_preserve_articulation(self) -> None:
        historical = fixture("synthetic_historical.json")
        historical["revenue_components"] = {"company_operated": 70.0, "licensed": 20.0, "other": 10.0}
        assumptions = fixture("synthetic_assumptions.json")
        assumptions["operating_drivers"] = {
            "company_operated": {"transaction_growth": [0.1] * 5, "average_ticket_growth": [0.0] * 5, "net_store_growth": [0.0] * 5},
            "licensed_revenue_growth": [0.0] * 5, "other_revenue_growth": [0.0] * 5,
            "geographic_mix": {"Americas": [0.6] * 5, "International": [0.3] * 5, "China_Asia_Pacific": [0.1] * 5},
        }
        result = run_analysis(historical, assumptions, _include_decision_analysis=False)
        year_one = result["forecast_years"][0]
        drivers = year_one["operating_drivers"]
        self.assertAlmostEqual(year_one["income_statement"]["revenue"], 107.0)
        self.assertAlmostEqual(drivers["comparable_sales_growth"], 0.1)
        self.assertAlmostEqual(drivers["revenue_components"]["company_operated"], 77.0)
        self.assertAlmostEqual(sum(drivers["geographic_revenue"].values()), 107.0)
        balance = year_one["balance_sheet"]
        self.assertAlmostEqual(sum(balance[key] for key in ("cash", "short_term_investments", "accounts_receivable", "inventory", "other_current_assets", "net_ppe", "other_noncurrent_assets")), sum(balance[key] for key in ("accounts_payable", "accrued_liabilities", "other_liabilities", "total_debt")) + balance["equity"])

    def test_non_operating_income_reconciles_without_affecting_operating_income(self) -> None:
        historical = fixture("synthetic_historical.json")
        historical["income_statement"]["non_operating_income_expense"] = 4.0
        historical["income_statement"]["income_tax_expense"] = 4.0
        historical["income_statement"]["net_income"] = 18.0
        historical["cash_flow"]["net_income"] = 18.0
        assumptions = fixture("synthetic_assumptions.json")
        assumptions["non_operating_income_expense"] = [4.0] * 5
        result = run_analysis(historical, assumptions, _include_decision_analysis=False)
        year_one = result["forecast_years"][0]
        self.assertAlmostEqual(year_one["income_statement"]["operating_income"], 22.0)
        self.assertAlmostEqual(year_one["income_statement"]["non_operating_income_expense"], 4.0)
        self.assertAlmostEqual(year_one["income_statement"]["pretax_income"], 24.0)

    def test_short_term_investments_are_separate_from_nwc_and_bridge(self) -> None:
        historical = fixture("synthetic_historical.json")
        historical["balance_sheet"]["cash"] = 5.0
        historical["balance_sheet"]["short_term_investments"] = 5.0
        historical["cash_flow"]["ending_cash"] = 5.0
        assumptions = fixture("synthetic_assumptions.json")
        assumptions["short_term_investments"] = [5.0] * 5
        assumptions["valuation"]["cash"] = 5.0
        assumptions["valuation"]["short_term_investments"] = 5.0
        assumptions["valuation"]["noncontrolling_interest"] = 2.0
        result = run_analysis(historical, assumptions, _include_decision_analysis=False)
        year_one = result["forecast_years"][0]
        self.assertAlmostEqual(year_one["cash_flow"]["change_in_short_term_investments"], 0.0)
        self.assertAlmostEqual(year_one["cash_flow"]["change_in_nwc"], 4.9)
        bridge = result["dcf"]["enterprise_to_equity_bridge"]
        self.assertEqual(bridge["short_term_investments"], 5.0)
        self.assertAlmostEqual(bridge["equity_value"], bridge["enterprise_value"] + 5.0 + 5.0 - 45.0 - 2.0)

    def test_financing_policy_restores_minimum_cash_and_adds_next_year_interest(self) -> None:
        assumptions = fixture("synthetic_assumptions.json")
        assumptions["dividends"] = [100.0] * 5
        assumptions["financing_policy"] = {
            "minimum_cash": 10.0,
            "maximum_revolver_draw": 100.0,
            "interest_rate": 0.10,
            "interest_starts_next_year": True,
        }
        result = run_analysis(fixture("synthetic_historical.json"), assumptions, _include_decision_analysis=False)
        first, second = result["forecast_years"][:2]
        self.assertAlmostEqual(first["balance_sheet"]["cash"], 10.0)
        self.assertAlmostEqual(first["cash_flow"]["financing_policy_draw"], 95.9)
        self.assertAlmostEqual(second["income_statement"]["financing_policy_interest"], 9.59)
        self.assertTrue(first["financing_policy"]["minimum_cash_requirement_met"])

    def test_operating_driver_geographic_mix_must_sum_to_one(self) -> None:
        historical = fixture("synthetic_historical.json")
        historical["revenue_components"] = {"company_operated": 70.0, "licensed": 20.0, "other": 10.0}
        assumptions = fixture("synthetic_assumptions.json")
        assumptions["operating_drivers"] = {
            "company_operated": {"transaction_growth": [0.0] * 5, "average_ticket_growth": [0.0] * 5, "net_store_growth": [0.0] * 5},
            "licensed_revenue_growth": [0.0] * 5, "other_revenue_growth": [0.0] * 5,
            "geographic_mix": {"Americas": [0.7] * 5, "International": [0.3] * 5, "China_Asia_Pacific": [0.1] * 5},
        }
        with self.assertRaisesRegex(ModelValidationError, "geographic mix"):
            run_analysis(historical, assumptions, _include_decision_analysis=False)

    def test_unreconciled_base_year_fails_loudly(self) -> None:
        historical = deepcopy(fixture("synthetic_historical.json"))
        historical["cash_flow"]["ending_cash"] = 999.0
        with self.assertRaisesRegex(ModelValidationError, "base-year ending cash"):
            run_analysis(historical, fixture("synthetic_assumptions.json"))


if __name__ == "__main__":
    unittest.main()
