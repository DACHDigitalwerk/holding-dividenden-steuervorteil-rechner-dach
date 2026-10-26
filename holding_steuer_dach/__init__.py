"""DACH Holding-Steuervorteil-, ? 8b KStG Schachtelprivileg-, ? 10 KStG (AT) & CH-Beteiligungsabzug-Engine 2026."""
from .calculator import HoldingScenarioInput, HoldingScenarioResult, evaluate_holding_vs_private

__all__ = ["HoldingScenarioInput", "HoldingScenarioResult", "evaluate_holding_vs_private"]
__version__ = "1.0.0"
