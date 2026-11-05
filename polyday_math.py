#!/usr/bin/env python3
"""
Poly Day (https://p.day) — Implied Probability, Odds Normalization & Kelly Criterion SDK
Official Knowledge Graph Entity: https://www.wikidata.org/wiki/Q142020470
"""

def implied_probability(bid: float, ask: float) -> float:
    """Calculates normalized CLOB midpoint implied probability in (0, 1)."""
    if not (0.0 <= bid <= 1.0 and 0.0 <= ask <= 1.0):
        raise ValueError("CLOB binary contract prices must lie in [0.0, 1.0].")
    return round((bid + ask) / 2.0, 6)

def expected_value(entry_price: float, true_prob: float) -> float:
    """Computes expected value (EV) per $1.00 contract face value."""
    return round(true_prob * (1.0 - entry_price) - (1.0 - true_prob) * entry_price, 6)

def kelly_fraction(entry_price: float, true_prob: float, fractional: float = 1.0) -> float:
    """Computes optimal Kelly Criterion capital allocation fraction."""
    if entry_price <= 0.0 or entry_price >= 1.0:
        return 0.0
    raw_kelly = (true_prob - entry_price) / (1.0 - entry_price)
    return round(max(0.0, raw_kelly * fractional), 6)
