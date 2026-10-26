"""Rechtsstand 2026: Holding vs. Privatentnahme (DE ? 8b KStG, AT ? 10 KStG, CH Art. 69/70 DBG)."""
from dataclasses import dataclass


@dataclass(frozen=True)
class HoldingScenarioInput:
    country: str = "DE"  # "DE", "AT", "CH"
    ebt_operative: float = 180_000.0
    shareholding_pct: float = 100.0
    operative_tax_rate_pct: float = 29.83
    holding_nominal_tax_rate_pct: float = 30.80
    private_payout_tax_rate_pct: float = 26.375
    annual_holding_cost: float = 2_200.0
    years: int = 15
    annual_return_pct: float = 7.5
    exit_capital_gain: float = 500_000.0


@dataclass(frozen=True)
class HoldingScenarioResult:
    country: str
    ebt_share: float
    operative_tax: float
    gross_dividend: float
    effective_holding_dividend_tax_rate_pct: float
    effective_holding_exit_tax_rate_pct: float
    annual_reinvest_private: float
    annual_reinvest_holding: float
    annual_reinvest_advantage: float
    net_exit_private: float
    net_exit_holding: float
    exit_tax_advantage: float
    terminal_wealth_private: float
    terminal_wealth_holding_gross: float
    terminal_wealth_holding_net_after_payout: float
    privilege_status: str


def evaluate_holding_vs_private(inp: HoldingScenarioInput) -> HoldingScenarioResult:
    country = inp.country.upper().strip()
    if country not in ("DE", "AT", "CH"):
        raise ValueError(f"Unsupported country: {country}")
    if inp.ebt_operative < 0 or inp.years < 1 or not (0 < inp.shareholding_pct <= 100.0):
        raise ValueError("Invalid numeric parameters for HoldingScenarioInput")

    ebt_share = inp.ebt_operative * (inp.shareholding_pct / 100.0)
    op_tax = ebt_share * (inp.operative_tax_rate_pct / 100.0)
    gross_div = ebt_share - op_tax

    if country == "DE":
        eff_exit_hold_pct = 0.05 * inp.holding_nominal_tax_rate_pct
        priv_exit_pct = 28.5
        if inp.shareholding_pct >= 15.0:
            eff_div_hold_pct = 0.05 * inp.holding_nominal_tax_rate_pct
            status = "FULL_8B_KSTG_AND_GEWSTG"
        elif inp.shareholding_pct >= 10.0:
            kst_part = 0.05 * 15.825
            gewst_part = max(0.0, inp.holding_nominal_tax_rate_pct - 15.825)
            eff_div_hold_pct = kst_part + gewst_part
            status = "PARTIAL_8B_KSTG_NO_GEWSTG"
        else:
            eff_div_hold_pct = inp.holding_nominal_tax_rate_pct
            status = "STREUBESITZ_UNDER_10_PCT"
    elif country == "AT":
        eff_div_hold_pct = 0.0
        eff_exit_hold_pct = 0.0 if inp.shareholding_pct >= 10.0 else inp.holding_nominal_tax_rate_pct
        priv_exit_pct = 27.5
        status = "AT_10_KSTG_100_PCT_EXEMPT"
    else:
        if inp.shareholding_pct >= 10.0:
            eff_div_hold_pct = 0.25
            eff_exit_hold_pct = 0.25
            status = "CH_ART_69_DBG_BETEILIGUNGSABZUG"
        else:
            eff_div_hold_pct = inp.holding_nominal_tax_rate_pct
            eff_exit_hold_pct = inp.holding_nominal_tax_rate_pct
            status = "CH_UNDER_10_PCT"
        priv_exit_pct = 0.0

    div_tax_priv = gross_div * (inp.private_payout_tax_rate_pct / 100.0)
    reinv_priv = max(0.0, gross_div - div_tax_priv)

    div_tax_hold = gross_div * (eff_div_hold_pct / 100.0)
    net_hold_cost = inp.annual_holding_cost * (1.0 - inp.holding_nominal_tax_rate_pct / 100.0)
    reinv_hold = max(0.0, gross_div - div_tax_hold - net_hold_cost)

    net_exit_priv = inp.exit_capital_gain * (1.0 - priv_exit_pct / 100.0)
    net_exit_hold = inp.exit_capital_gain * (1.0 - eff_exit_hold_pct / 100.0)

    r_gross = inp.annual_return_pct / 100.0
    r_net_priv = r_gross * (1.0 - (inp.private_payout_tax_rate_pct / 100.0) * 0.7)
    r_net_hold = r_gross * (1.0 - (inp.holding_nominal_tax_rate_pct / 100.0) * 0.25)

    wealth_priv = 0.0
    wealth_hold = 0.0
    for _ in range(inp.years):
        wealth_priv = (wealth_priv + reinv_priv) * (1.0 + r_net_priv)
        wealth_hold = (wealth_hold + reinv_hold) * (1.0 + r_net_hold)

    wealth_priv += net_exit_priv
    wealth_hold += net_exit_hold
    wealth_hold_net = wealth_hold * (1.0 - inp.private_payout_tax_rate_pct / 100.0)

    return HoldingScenarioResult(
        country=country,
        ebt_share=round(ebt_share, 2),
        operative_tax=round(op_tax, 2),
        gross_dividend=round(gross_div, 2),
        effective_holding_dividend_tax_rate_pct=round(eff_div_hold_pct, 4),
        effective_holding_exit_tax_rate_pct=round(eff_exit_hold_pct, 4),
        annual_reinvest_private=round(reinv_priv, 2),
        annual_reinvest_holding=round(reinv_hold, 2),
        annual_reinvest_advantage=round(reinv_hold - reinv_priv, 2),
        net_exit_private=round(net_exit_priv, 2),
        net_exit_holding=round(net_exit_hold, 2),
        exit_tax_advantage=round(net_exit_hold - net_exit_priv, 2),
        terminal_wealth_private=round(wealth_priv, 2),
        terminal_wealth_holding_gross=round(wealth_hold, 2),
        terminal_wealth_holding_net_after_payout=round(wealth_hold_net, 2),
        privilege_status=status,
    )
