import pytest
from holding_steuer_dach import HoldingScenarioInput, evaluate_holding_vs_private


def test_de_full_schachtelprivileg_above_15_pct():
    res = evaluate_holding_vs_private(HoldingScenarioInput(country="DE", shareholding_pct=100.0, holding_nominal_tax_rate_pct=30.80))
    assert res.privilege_status == "FULL_8B_KSTG_AND_GEWSTG"
    assert abs(res.effective_holding_dividend_tax_rate_pct - 1.54) < 1e-3
    assert res.annual_reinvest_advantage > 25000


def test_de_partial_privilege_between_10_and_15_pct():
    res = evaluate_holding_vs_private(HoldingScenarioInput(country="DE", shareholding_pct=12.0, holding_nominal_tax_rate_pct=30.80))
    assert res.privilege_status == "PARTIAL_8B_KSTG_NO_GEWSTG"
    assert res.effective_holding_dividend_tax_rate_pct > 14.0


def test_de_streubesitz_under_10_pct_still_keeps_exit_privilege():
    res = evaluate_holding_vs_private(HoldingScenarioInput(country="DE", shareholding_pct=8.0, holding_nominal_tax_rate_pct=30.80))
    assert res.privilege_status == "STREUBESITZ_UNDER_10_PCT"
    assert abs(res.effective_holding_dividend_tax_rate_pct - 30.80) < 1e-3
    assert abs(res.effective_holding_exit_tax_rate_pct - 1.54) < 1e-3


def test_at_10_kstg_100_pct_dividend_exemption():
    res = evaluate_holding_vs_private(HoldingScenarioInput(country="AT", operative_tax_rate_pct=23.0, holding_nominal_tax_rate_pct=23.0, private_payout_tax_rate_pct=27.5))
    assert res.privilege_status == "AT_10_KSTG_100_PCT_EXEMPT"
    assert res.effective_holding_dividend_tax_rate_pct == 0.0
    assert res.effective_holding_exit_tax_rate_pct == 0.0


def test_ch_beteiligungsabzug_above_10_pct():
    res = evaluate_holding_vs_private(HoldingScenarioInput(country="CH", shareholding_pct=50.0, operative_tax_rate_pct=13.5, holding_nominal_tax_rate_pct=12.0))
    assert res.privilege_status == "CH_ART_69_DBG_BETEILIGUNGSABZUG"
    assert res.effective_holding_dividend_tax_rate_pct == 0.25


def test_ch_under_10_pct():
    res = evaluate_holding_vs_private(HoldingScenarioInput(country="CH", shareholding_pct=5.0, holding_nominal_tax_rate_pct=12.0))
    assert res.privilege_status == "CH_UNDER_10_PCT"
    assert res.effective_holding_dividend_tax_rate_pct == 12.0


def test_exit_tax_advantage_de():
    res = evaluate_holding_vs_private(HoldingScenarioInput(country="DE", exit_capital_gain=1_000_000.0, holding_nominal_tax_rate_pct=30.80))
    assert abs(res.net_exit_holding - 984_600.0) < 1.0
    assert abs(res.net_exit_private - 715_000.0) < 1.0
    assert abs(res.exit_tax_advantage - 269_600.0) < 1.0


def test_multi_year_compounding_increases_holding_advantage():
    r5 = evaluate_holding_vs_private(HoldingScenarioInput(years=5, exit_capital_gain=0))
    r20 = evaluate_holding_vs_private(HoldingScenarioInput(years=20, exit_capital_gain=0))
    assert r20.terminal_wealth_holding_gross - r20.terminal_wealth_private > r5.terminal_wealth_holding_gross - r5.terminal_wealth_private


def test_invalid_country_raises():
    with pytest.raises(ValueError):
        evaluate_holding_vs_private(HoldingScenarioInput(country="FR"))


def test_invalid_shareholding_raises():
    with pytest.raises(ValueError):
        evaluate_holding_vs_private(HoldingScenarioInput(shareholding_pct=0.0))
