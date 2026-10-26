"""CLI entry point for dach-holding."""
import argparse
import json
from dataclasses import asdict
from .calculator import HoldingScenarioInput, evaluate_holding_vs_private


def main() -> None:
    parser = argparse.ArgumentParser(description="DACH Holding Tax & Dividend Advantage Calculator 2026")
    parser.add_argument("--country", default="DE", choices=["DE", "AT", "CH"])
    parser.add_argument("--ebt", type=float, default=180000.0)
    parser.add_argument("--share", type=float, default=100.0)
    parser.add_argument("--years", type=int, default=15)
    parser.add_argument("--exit-gain", type=float, default=500000.0)
    args = parser.parse_args()

    res = evaluate_holding_vs_private(
        HoldingScenarioInput(
            country=args.country,
            ebt_operative=args.ebt,
            shareholding_pct=args.share,
            years=args.years,
            exit_capital_gain=args.exit_gain,
        )
    )
    print(json.dumps(asdict(res), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
