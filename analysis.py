"""Transparent five-year three-statement forecast engine for verified local inputs."""
from __future__ import annotations

import argparse
from copy import deepcopy
import json
from pathlib import Path
import subprocess
from typing import Any

FORECAST_YEARS = 5
TOLERANCE = 1e-6


class ModelValidationError(ValueError):
    """Raised when a verified input or a reconciliation is invalid."""


def _number(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ModelValidationError(f"{label} must be numeric; received {value!r}.")
    return float(value)


def _required(mapping: dict[str, Any], key: str, label: str) -> float:
    if key not in mapping:
        raise ModelValidationError(f"Missing required input: {label}.")
    return _number(mapping[key], label)


def _close(actual: float, expected: float, label: str) -> None:
    if abs(actual - expected) > TOLERANCE:
        raise ModelValidationError(f"Reconciliation failed: {label}. Expected {expected:.6f}; got {actual:.6f}.")


def _series(assumptions: dict[str, Any], key: str) -> list[float]:
    values = assumptions.get(key)
    if not isinstance(values, list) or len(values) != FORECAST_YEARS:
        raise ModelValidationError(f"Assumption '{key}' must contain exactly five values.")
    return [_number(value, f"assumptions.{key}[{i}]") for i, value in enumerate(values)]


def _nested_series(mapping: dict[str, Any], key: str, label: str) -> list[float]:
    values = mapping.get(key)
    if not isinstance(values, list) or len(values) != FORECAST_YEARS:
        raise ModelValidationError(f"{label}.{key} must contain exactly five values.")
    return [_number(value, f"{label}.{key}[{i}]") for i, value in enumerate(values)]


def _operating_driver_setup(historical: dict[str, Any], assumptions: dict[str, Any]) -> dict[str, Any] | None:
    """Validate optional causal revenue drivers without inferring missing operating data."""
    drivers = assumptions.get("operating_drivers")
    if drivers is None:
        return None
    if not isinstance(drivers, dict):
        raise ModelValidationError("operating_drivers must be an object when supplied.")
    if drivers.get("enabled") is False:
        return None
    components = historical.get("revenue_components")
    if not isinstance(components, dict):
        raise ModelValidationError("Operating-driver mode requires historical.revenue_components.")
    names = ("company_operated", "licensed", "other")
    values = {name: _required(components, name, f"historical.revenue_components.{name}") for name in names}
    _close(sum(values.values()), _required(historical["income_statement"], "revenue", "historical revenue"), "base-year revenue components = reported revenue")
    company = drivers.get("company_operated")
    if not isinstance(company, dict):
        raise ModelValidationError("operating_drivers.company_operated is required.")
    setup = {
        "company_operated": {key: _nested_series(company, key, "operating_drivers.company_operated") for key in ("transaction_growth", "average_ticket_growth", "net_store_growth")},
        "licensed_revenue_growth": _nested_series(drivers, "licensed_revenue_growth", "operating_drivers"),
        "other_revenue_growth": _nested_series(drivers, "other_revenue_growth", "operating_drivers"),
    }
    geographic_mix = drivers.get("geographic_mix")
    if geographic_mix is not None:
        if not isinstance(geographic_mix, dict) or not geographic_mix:
            raise ModelValidationError("operating_drivers.geographic_mix must be a non-empty object when supplied.")
        setup["geographic_mix"] = {name: _nested_series(geographic_mix, name, "operating_drivers.geographic_mix") for name in geographic_mix}
        for i in range(FORECAST_YEARS):
            _close(sum(weights[i] for weights in setup["geographic_mix"].values()), 1.0, f"geographic mix weights in forecast year {i + 1}")
    return setup


def _driver_revenue(prior_components: dict[str, float], setup: dict[str, Any], year: int) -> tuple[float, dict[str, Any]]:
    """Build revenue from transaction, ticket, store, and revenue-channel drivers."""
    company = setup["company_operated"]
    transaction_growth = company["transaction_growth"][year]
    ticket_growth = company["average_ticket_growth"][year]
    store_growth = company["net_store_growth"][year]
    comparable_sales_growth = (1 + transaction_growth) * (1 + ticket_growth) - 1
    components = {
        "company_operated": prior_components["company_operated"] * (1 + comparable_sales_growth) * (1 + store_growth),
        "licensed": prior_components["licensed"] * (1 + setup["licensed_revenue_growth"][year]),
        "other": prior_components["other"] * (1 + setup["other_revenue_growth"][year]),
    }
    return sum(components.values()), {
        "revenue_components": components,
        "comparable_transaction_growth": transaction_growth,
        "average_ticket_growth": ticket_growth,
        "comparable_sales_growth": comparable_sales_growth,
        "net_company_operated_store_growth": store_growth,
        "company_operated_revenue_mix": components["company_operated"] / sum(components.values()),
        "licensed_revenue_mix": components["licensed"] / sum(components.values()),
    }


def validate_base_year(historical: dict[str, Any]) -> None:
    """Check supplied base-year income statement, balance sheet, and cash-flow inputs."""
    income = historical.get("income_statement")
    balance = historical.get("balance_sheet")
    cash_flow = historical.get("cash_flow")
    if not all(isinstance(section, dict) for section in (income, balance, cash_flow)):
        raise ModelValidationError("Historical input requires income_statement, balance_sheet, and cash_flow objects.")
    revenue = _required(income, "revenue", "historical.income_statement.revenue")
    cogs = _required(income, "cost_of_sales", "historical.income_statement.cost_of_sales")
    opex = _required(income, "operating_expenses", "historical.income_statement.operating_expenses")
    interest = _required(income, "interest_expense", "historical.income_statement.interest_expense")
    taxes = _required(income, "income_tax_expense", "historical.income_statement.income_tax_expense")
    non_operating = _required(income, "non_operating_income_expense", "historical.income_statement.non_operating_income_expense")
    net_income = _required(income, "net_income", "historical.income_statement.net_income")
    _close(revenue - cogs - opex - interest + non_operating - taxes, net_income, "base-year income statement net income")
    assets = sum(_required(balance, key, f"historical.balance_sheet.{key}") for key in (
        "cash", "short_term_investments", "accounts_receivable", "inventory", "other_current_assets", "net_ppe", "other_noncurrent_assets"))
    liabilities = sum(_required(balance, key, f"historical.balance_sheet.{key}") for key in (
        "accounts_payable", "accrued_liabilities", "other_liabilities", "total_debt"))
    _close(assets, liabilities + _required(balance, "equity", "historical.balance_sheet.equity"), "base-year assets = liabilities + equity")
    _close(_required(cash_flow, "net_income", "historical.cash_flow.net_income"), net_income, "base-year cash-flow net income = income-statement net income")
    _close(_required(cash_flow, "ending_cash", "historical.cash_flow.ending_cash"), _required(balance, "cash", "historical.balance_sheet.cash"), "base-year ending cash = balance-sheet cash")


def _validate_forecast(year: dict[str, Any]) -> None:
    balance, cash_flow = year["balance_sheet"], year["cash_flow"]
    assets = sum(balance[key] for key in ("cash", "short_term_investments", "accounts_receivable", "inventory", "other_current_assets", "net_ppe", "other_noncurrent_assets"))
    liabilities = sum(balance[key] for key in ("accounts_payable", "accrued_liabilities", "other_liabilities", "total_debt"))
    _close(assets, liabilities + balance["equity"], f"{year['year']} assets = liabilities + equity")
    _close(cash_flow["ending_cash"], balance["cash"], f"{year['year']} ending cash = balance-sheet cash")


def _valuation_inputs(assumptions: dict[str, Any]) -> dict[str, float]:
    """Require explicit, traceable valuation inputs; no claims are inferred silently."""
    valuation = assumptions.get("valuation")
    if not isinstance(valuation, dict):
        raise ModelValidationError("Missing assumptions.valuation object.")
    required = (
        "wacc", "terminal_growth", "cash", "short_term_investments", "debt", "lease_obligations",
        "noncontrolling_interest", "other_material_claims", "other_non_operating_assets", "common_shares_outstanding",
    )
    values = {key: _required(valuation, key, f"assumptions.valuation.{key}") for key in required}
    if values["common_shares_outstanding"] <= 0:
        raise ModelValidationError("assumptions.valuation.common_shares_outstanding must be greater than zero.")
    if values["wacc"] <= values["terminal_growth"]:
        raise ModelValidationError("WACC must be greater than terminal growth for a stable-growth terminal value.")
    return values


def _financing_policy(assumptions: dict[str, Any]) -> dict[str, float] | None:
    """Validate an explicit liquidity backstop; never infer financing silently."""
    policy = assumptions.get("financing_policy")
    if policy is None:
        return None
    if not isinstance(policy, dict):
        raise ModelValidationError("financing_policy must be an object when supplied.")
    required = ("minimum_cash", "maximum_revolver_draw", "interest_rate")
    values = {key: _required(policy, key, f"financing_policy.{key}") for key in required}
    if values["minimum_cash"] < 0 or values["maximum_revolver_draw"] < 0 or values["interest_rate"] < 0:
        raise ModelValidationError("financing_policy values must be non-negative.")
    if policy.get("interest_starts_next_year") is not True:
        raise ModelValidationError("financing_policy.interest_starts_next_year must be true.")
    return values


def _dcf_from_forecast(forecast_years: list[dict[str, Any]], valuation: dict[str, float]) -> dict[str, Any]:
    """Calculate an FCFF DCF from the reconciled pro-forma, without changing its statements."""
    fcff_rows: list[dict[str, float]] = []
    present_value_fcff = 0.0
    for period, year in enumerate(forecast_years, start=1):
        income, cash_flow = year["income_statement"], year["cash_flow"]
        ebit = income["operating_income"]
        # Cash taxes are an explicit model convention: EBIT multiplied by the approved tax rate.
        cash_taxes = ebit * (income["income_tax_expense"] / income["pretax_income"]) if income["pretax_income"] else 0.0
        fcff = ebit - cash_taxes + cash_flow["depreciation"] - cash_flow["capex"] - cash_flow["change_in_nwc"]
        discount_factor = 1 / (1 + valuation["wacc"]) ** period
        pv_fcff = fcff * discount_factor
        present_value_fcff += pv_fcff
        fcff_rows.append({
            "year": year["year"], "ebit": ebit, "cash_taxes": cash_taxes,
            "depreciation": cash_flow["depreciation"], "capex": cash_flow["capex"],
            "change_in_nwc": cash_flow["change_in_nwc"], "fcff": fcff,
            "discount_factor": discount_factor, "present_value_fcff": pv_fcff,
        })
    terminal_fcff = fcff_rows[-1]["fcff"] * (1 + valuation["terminal_growth"])
    terminal_value = terminal_fcff / (valuation["wacc"] - valuation["terminal_growth"])
    present_value_terminal = terminal_value * fcff_rows[-1]["discount_factor"]
    enterprise_value = present_value_fcff + present_value_terminal
    if enterprise_value == 0:
        raise ModelValidationError("Enterprise value is zero; terminal-value share cannot be calculated.")
    equity_value = (
        enterprise_value + valuation["cash"] + valuation["short_term_investments"] + valuation["other_non_operating_assets"]
        - valuation["debt"] - valuation["lease_obligations"] - valuation["noncontrolling_interest"] - valuation["other_material_claims"]
    )
    return {
        "fcff_forecast": fcff_rows,
        "wacc": valuation["wacc"], "terminal_growth": valuation["terminal_growth"],
        "terminal_fcff": terminal_fcff, "terminal_value": terminal_value,
        "present_value_fcff": present_value_fcff, "present_value_terminal": present_value_terminal,
        "enterprise_value": enterprise_value,
        "terminal_value_share_of_enterprise_value": present_value_terminal / enterprise_value,
        "enterprise_to_equity_bridge": {
            "enterprise_value": enterprise_value, "cash": valuation["cash"],
            "short_term_investments": valuation["short_term_investments"],
            "other_non_operating_assets": valuation["other_non_operating_assets"],
            "debt": valuation["debt"], "lease_obligations": valuation["lease_obligations"], "noncontrolling_interest": valuation["noncontrolling_interest"],
            "other_material_claims": valuation["other_material_claims"], "equity_value": equity_value,
            "common_shares_outstanding": valuation["common_shares_outstanding"], "implied_value_per_common_share": equity_value / valuation["common_shares_outstanding"],
        },
        "material_inputs": {"valuation": valuation},
    }


def _validate_dcf_sensitivities(forecast_years: list[dict[str, Any]], valuation: dict[str, float], base_value: float) -> dict[str, bool]:
    """Fail if the standard DCF monotonicity relationships do not hold."""
    gap = valuation["wacc"] - valuation["terminal_growth"]
    bump = min(0.01, gap / 4)
    higher_wacc = dict(valuation, wacc=valuation["wacc"] + bump)
    higher_growth = dict(valuation, terminal_growth=valuation["terminal_growth"] + bump)
    if _dcf_from_forecast(forecast_years, higher_wacc)["enterprise_value"] >= base_value:
        raise ModelValidationError("DCF sensitivity failed: enterprise value must decline when WACC rises.")
    if _dcf_from_forecast(forecast_years, higher_growth)["enterprise_value"] <= base_value:
        raise ModelValidationError("DCF sensitivity failed: enterprise value must rise when terminal growth rises.")
    return {"higher_wacc_reduces_enterprise_value": True, "higher_terminal_growth_increases_enterprise_value": True}


CAUSAL_DRIVERS = {
    "revenue_growth", "gross_margin", "operating_expense_pct_revenue",
    "operating_drivers",
    "accounts_receivable_pct_revenue", "inventory_pct_cost_of_sales",
    "other_current_assets_pct_revenue", "accounts_payable_pct_cost_of_sales",
    "accrued_liabilities_pct_operating_expenses", "capex_pct_revenue",
    "depreciation_pct_beginning_net_ppe", "net_debt_issuance", "dividends",
}


def _apply_overrides(assumptions: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    """Copy only explicitly provided, approved scenario values into assumptions."""
    if not isinstance(overrides, dict):
        raise ModelValidationError("Scenario overrides must be an object.")
    result = deepcopy(assumptions)
    for key, value in overrides.items():
        if key == "valuation":
            if not isinstance(value, dict):
                raise ModelValidationError("Scenario valuation override must be an object.")
            result["valuation"] = dict(result.get("valuation", {}), **value)
        elif key in result:
            result[key] = value
        else:
            raise ModelValidationError(f"Scenario override is not an approved assumption: {key}.")
    return result


def _scenario_summary(result: dict[str, Any]) -> dict[str, float]:
    final = result["forecast_years"][-1]
    dcf = result["dcf"]
    return {
        "year_5_operating_income": final["income_statement"]["operating_income"],
        "year_5_fcff": dcf["fcff_forecast"][-1]["fcff"],
        "enterprise_value": dcf["enterprise_value"],
        "terminal_value_share": dcf["terminal_value_share_of_enterprise_value"],
        "implied_value_per_common_share": dcf["enterprise_to_equity_bridge"]["implied_value_per_common_share"],
        "minimum_cash_requirement_met": result["checks"]["minimum_cash_requirement_met"],
    }


def _market_implied_terminal_growth(dcf: dict[str, Any], market_ev: float) -> float:
    """Solve the constant terminal-growth rate implied by an explicit market EV input."""
    pv_terminal = market_ev - dcf["present_value_fcff"]
    discount_factor = dcf["fcff_forecast"][-1]["discount_factor"]
    terminal_value = pv_terminal / discount_factor
    terminal_fcff_base = dcf["fcff_forecast"][-1]["fcff"]
    denominator = terminal_value + terminal_fcff_base
    if terminal_value <= 0 or denominator == 0:
        raise ModelValidationError("Market-implied terminal growth cannot be solved from the supplied market enterprise value.")
    return (terminal_value * dcf["wacc"] - terminal_fcff_base) / denominator


def build_decision_analysis(historical: dict[str, Any], assumptions: dict[str, Any], base_result: dict[str, Any]) -> dict[str, Any]:
    """Build only user-specified low/base/high cases and one-at-a-time driver tests."""
    config = assumptions.get("decision_analysis")
    if not isinstance(config, dict):
        raise ModelValidationError("Missing assumptions.decision_analysis object for cases and sensitivities.")
    cases = config.get("cases")
    if not isinstance(cases, dict) or set(cases) != {"low", "base", "high"}:
        raise ModelValidationError("decision_analysis.cases must contain exactly low, base, and high.")
    case_results: dict[str, dict[str, float]] = {}
    for name, definition in cases.items():
        if not isinstance(definition, dict):
            raise ModelValidationError(f"Case '{name}' must be an object.")
        overrides = definition.get("overrides", {})
        if name in {"low", "high"} and not (set(overrides) & CAUSAL_DRIVERS):
            raise ModelValidationError(f"Case '{name}' must change at least one causal operating driver, not only valuation inputs.")
        scenario = _apply_overrides(assumptions, overrides)
        scenario.pop("decision_analysis", None)
        case_results[name] = _scenario_summary(run_analysis(historical, scenario, _include_decision_analysis=False))

    tests = config.get("one_at_a_time")
    if not isinstance(tests, list) or not tests:
        raise ModelValidationError("decision_analysis.one_at_a_time must contain approved driver tests.")
    sensitivity_rows = []
    for test in tests:
        if not isinstance(test, dict) or test.get("driver") not in CAUSAL_DRIVERS:
            raise ModelValidationError("Each one-at-a-time test must name a causal operating driver.")
        driver = test["driver"]
        if "low" not in test or "high" not in test:
            raise ModelValidationError(f"One-at-a-time test for {driver} requires low and high values.")
        low_assumptions = _apply_overrides(assumptions, {driver: test["low"]})
        high_assumptions = _apply_overrides(assumptions, {driver: test["high"]})
        low_assumptions.pop("decision_analysis", None)
        high_assumptions.pop("decision_analysis", None)
        low_result = _scenario_summary(run_analysis(historical, low_assumptions, _include_decision_analysis=False))
        high_result = _scenario_summary(run_analysis(historical, high_assumptions, _include_decision_analysis=False))
        sensitivity_rows.append({"driver": driver, "low": low_result, "high": high_result, "per_share_range": high_result["implied_value_per_common_share"] - low_result["implied_value_per_common_share"]})
    sensitivity_rows.sort(key=lambda row: abs(row["per_share_range"]), reverse=True)

    wacc_values = config.get("wacc_values")
    growth_values = config.get("terminal_growth_values")
    if not (isinstance(wacc_values, list) and isinstance(growth_values, list) and wacc_values and growth_values):
        raise ModelValidationError("Provide non-empty decision_analysis.wacc_values and terminal_growth_values.")
    matrix = []
    for wacc in wacc_values:
        for growth in growth_values:
            scenario = _apply_overrides(assumptions, {"valuation": {"wacc": wacc, "terminal_growth": growth}})
            scenario.pop("decision_analysis", None)
            result = run_analysis(historical, scenario, _include_decision_analysis=False)
            matrix.append({"wacc": wacc, "terminal_growth": growth, **_scenario_summary(result)})
    market_ev = _number(config.get("market_implied_enterprise_value"), "decision_analysis.market_implied_enterprise_value")
    return {
        "cases": case_results, "wacc_terminal_growth_sensitivity": matrix,
        "one_at_a_time_sensitivities": sensitivity_rows,
        "driver_ranking_qualification": "Ranking reflects only the approved tested ranges; it is not a probability ranking.",
        "market_implied_expectation": {"market_implied_enterprise_value": market_ev, "implied_terminal_growth": _market_implied_terminal_growth(base_result["dcf"], market_ev)},
        "multiples_vs_dcf_note": "DCF and multiples can disagree because they use different forecasts, discount rates, terminal assumptions, peer selection, capital-structure adjustments, timing conventions, and market pricing. Investigate the traceable inputs rather than force convergence.",
    }


def run_analysis(historical: dict[str, Any], assumptions: dict[str, Any], _include_decision_analysis: bool = True) -> dict[str, Any]:
    """Produce five reconciled forecasts; all inputs must be verified before this call."""
    validate_base_year(historical)
    if not isinstance(assumptions, dict):
        raise ModelValidationError("Assumptions must be an object.")
    driver_setup = _operating_driver_setup(historical, assumptions)
    financing_policy = _financing_policy(assumptions)
    required_series = (
        "gross_margin", "operating_expense_pct_revenue", "interest_expense", "non_operating_income_expense", "tax_rate",
        "accounts_receivable_pct_revenue", "inventory_pct_cost_of_sales", "other_current_assets_pct_revenue",
        "accounts_payable_pct_cost_of_sales", "accrued_liabilities_pct_operating_expenses", "capex_pct_revenue",
        "depreciation_pct_beginning_net_ppe", "short_term_investments", "other_noncurrent_assets", "other_liabilities", "net_debt_issuance", "dividends",
    )
    s = {key: _series(assumptions, key) for key in required_series}
    if driver_setup is None:
        s["revenue_growth"] = _series(assumptions, "revenue_growth")
    prior, forecasts = historical, []
    revolver_draw_balance = 0.0
    base_year = int(_required(historical, "year", "historical.year"))
    for i in range(FORECAST_YEARS):
        pi, pb = prior["income_statement"], prior["balance_sheet"]
        operating_detail: dict[str, Any] | None = None
        if driver_setup is None:
            revenue = _required(pi, "revenue", "prior revenue") * (1 + s["revenue_growth"][i])
        else:
            prior_components = historical["revenue_components"] if i == 0 else prior["operating_drivers"]["revenue_components"]
            revenue, operating_detail = _driver_revenue(prior_components, driver_setup, i)
            if "geographic_mix" in driver_setup:
                operating_detail["geographic_revenue"] = {name: revenue * weights[i] for name, weights in driver_setup["geographic_mix"].items()}
        cogs = revenue * (1 - s["gross_margin"][i])
        opex = revenue * s["operating_expense_pct_revenue"][i]
        operating_income = revenue - cogs - opex
        non_operating = s["non_operating_income_expense"][i]
        financing_interest = revolver_draw_balance * financing_policy["interest_rate"] if financing_policy else 0.0
        interest_expense = s["interest_expense"][i] + financing_interest
        pretax_income = operating_income - interest_expense + non_operating
        taxes = pretax_income * s["tax_rate"][i]
        net_income = pretax_income - taxes
        ar = revenue * s["accounts_receivable_pct_revenue"][i]
        inventory = cogs * s["inventory_pct_cost_of_sales"][i]
        oca = revenue * s["other_current_assets_pct_revenue"][i]
        ap = cogs * s["accounts_payable_pct_cost_of_sales"][i]
        accrued = opex * s["accrued_liabilities_pct_operating_expenses"][i]
        capex = revenue * s["capex_pct_revenue"][i]
        depreciation = _required(pb, "net_ppe", "prior net_ppe") * s["depreciation_pct_beginning_net_ppe"][i]
        net_ppe = _required(pb, "net_ppe", "prior net_ppe") + capex - depreciation
        prior_nwc = sum(_required(pb, key, f"prior {key}") for key in ("accounts_receivable", "inventory", "other_current_assets")) - sum(_required(pb, key, f"prior {key}") for key in ("accounts_payable", "accrued_liabilities"))
        current_nwc = ar + inventory + oca - ap - accrued
        change_nwc = current_nwc - prior_nwc
        cfo = net_income + depreciation - change_nwc
        short_term_investments = s["short_term_investments"][i]
        change_in_short_term_investments = short_term_investments - _required(pb, "short_term_investments", "prior short-term investments")
        cfi = -capex - change_in_short_term_investments
        base_net_debt_issuance = s["net_debt_issuance"][i]
        preliminary_cash = _required(pb, "cash", "prior cash") + cfo + cfi + base_net_debt_issuance - s["dividends"][i]
        financing_policy_draw = 0.0
        if financing_policy:
            needed_draw = max(0.0, financing_policy["minimum_cash"] - preliminary_cash)
            remaining_capacity = max(0.0, financing_policy["maximum_revolver_draw"] - revolver_draw_balance)
            financing_policy_draw = min(needed_draw, remaining_capacity)
        net_debt_issuance = base_net_debt_issuance + financing_policy_draw
        cff = net_debt_issuance - s["dividends"][i]
        ending_cash = preliminary_cash + financing_policy_draw
        year = {
            "year": base_year + i + 1,
            "income_statement": {"revenue": revenue, "cost_of_sales": cogs, "operating_expenses": opex, "operating_income": operating_income, "interest_expense": interest_expense, "base_interest_expense": s["interest_expense"][i], "financing_policy_interest": financing_interest, "non_operating_income_expense": non_operating, "pretax_income": pretax_income, "income_tax_expense": taxes, "net_income": net_income},
            "balance_sheet": {"cash": ending_cash, "short_term_investments": short_term_investments, "accounts_receivable": ar, "inventory": inventory, "other_current_assets": oca, "net_ppe": net_ppe, "other_noncurrent_assets": s["other_noncurrent_assets"][i], "accounts_payable": ap, "accrued_liabilities": accrued, "other_liabilities": s["other_liabilities"][i], "total_debt": _required(pb, "total_debt", "prior total_debt") + net_debt_issuance, "equity": _required(pb, "equity", "prior equity") + net_income - s["dividends"][i]},
            "cash_flow": {"net_income": net_income, "depreciation": depreciation, "change_in_nwc": change_nwc, "cash_from_operations": cfo, "capex": capex, "change_in_short_term_investments": change_in_short_term_investments, "cash_from_investing": cfi, "base_net_debt_issuance": base_net_debt_issuance, "financing_policy_draw": financing_policy_draw, "net_debt_issuance": net_debt_issuance, "dividends": s["dividends"][i], "cash_from_financing": cff, "ending_cash": ending_cash},
        }
        if financing_policy:
            revolver_draw_balance += financing_policy_draw
            year["financing_policy"] = {
                "minimum_cash": financing_policy["minimum_cash"],
                "pre_financing_cash": preliminary_cash,
                "revolver_draw": financing_policy_draw,
                "revolver_draw_balance": revolver_draw_balance,
                "remaining_capacity": financing_policy["maximum_revolver_draw"] - revolver_draw_balance,
                "minimum_cash_requirement_met": ending_cash >= financing_policy["minimum_cash"] - TOLERANCE,
            }
        if operating_detail is not None:
            year["operating_drivers"] = operating_detail
        _validate_forecast(year)
        forecasts.append(year)
        prior = year
    valuation = _valuation_inputs(assumptions)
    dcf = _dcf_from_forecast(forecasts, valuation)
    dcf["sensitivity_checks"] = _validate_dcf_sensitivities(forecasts, valuation, dcf["enterprise_value"])
    result = {"base_year": base_year, "forecast_years": forecasts, "dcf": dcf}
    if financing_policy:
        result["financing_policy"] = {
            **financing_policy,
            "minimum_cash_requirement_met": all(year["financing_policy"]["minimum_cash_requirement_met"] for year in forecasts),
            "warning": "Ending cash fell below the defined minimum; committed capacity was insufficient." if any(not year["financing_policy"]["minimum_cash_requirement_met"] for year in forecasts) else None,
        }
    else:
        result["financing_policy"] = {"minimum_cash_requirement_met": True, "warning": "No minimum-cash policy configured."}
    result["checks"] = {"minimum_cash_requirement_met": result["financing_policy"]["minimum_cash_requirement_met"]}
    if isinstance(assumptions.get("reporting"), dict):
        result["reporting"] = assumptions["reporting"]
    if _include_decision_analysis:
        result["decision_analysis"] = build_decision_analysis(historical, assumptions, result)
    return result


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ModelValidationError(f"Input file not found: {path}") from exc
    if not isinstance(value, dict):
        raise ModelValidationError(f"JSON root must be an object: {path}")
    return value


def build_visible_output(result: dict[str, Any]) -> dict[str, Any]:
    """Create the reviewable interface contract from computed analysis only."""
    reporting = result.get("reporting")
    if not isinstance(reporting, dict):
        raise ModelValidationError("Cannot freeze output without approved reporting metadata.")
    required = ("decision_user", "as_of_date", "source_cutoff", "action", "conditions", "reversal_trigger", "limitations", "material_inputs")
    missing = [key for key in required if key not in reporting]
    if missing:
        raise ModelValidationError(f"Cannot freeze output; reporting metadata is missing: {', '.join(missing)}.")
    dcf = result["dcf"]
    bridge = dcf["enterprise_to_equity_bridge"]
    cases = result.get("decision_analysis", {}).get("cases", {})
    if not all(name in cases for name in ("low", "base", "high")):
        raise ModelValidationError("Cannot freeze output without validated low/base/high cases.")
    try:
        version = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=Path(__file__).parent, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        version = "unavailable — record manually after resolving repository state"
    return {
        "decision_user": reporting["decision_user"], "as_of_date": reporting["as_of_date"],
        "source_cutoff": reporting["source_cutoff"], "action": reporting["action"],
        "conditions": reporting["conditions"], "reversal_trigger": reporting["reversal_trigger"],
        "limitations": reporting["limitations"], "material_inputs": reporting["material_inputs"],
        "valuation_range_per_common_share": {name: cases[name]["implied_value_per_common_share"] for name in ("low", "base", "high")},
        "base_case_valuation": {
            "enterprise_value": dcf["enterprise_value"],
            "equity_value": bridge["equity_value"],
            "implied_value_per_common_share": bridge["implied_value_per_common_share"],
            "terminal_value_share": dcf["terminal_value_share_of_enterprise_value"],
        },
        "checks": {"forecast_articulation": "passed — analysis.py completed without reconciliation errors", **result["checks"], **dcf["sensitivity_checks"]},
        "scenario_minimum_cash_checks": {name: cases[name]["minimum_cash_requirement_met"] for name in ("low", "base", "high")},
        "repository_version": version,
        "traceability": "Generated by analysis.py from approved local inputs; do not hand-edit material values.",
    }


def write_visible_output(result: dict[str, Any], path: Path) -> None:
    path.write_text(json.dumps(build_visible_output(result), indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the verified-input five-year forecast.")
    parser.add_argument("--historical", type=Path, required=True)
    parser.add_argument("--assumptions", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--visible-output", type=Path)
    args = parser.parse_args()
    result = run_analysis(_load_json(args.historical), _load_json(args.assumptions))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if args.visible_output:
        args.visible_output.parent.mkdir(parents=True, exist_ok=True)
        write_visible_output(result, args.visible_output)


if __name__ == "__main__":
    main()
