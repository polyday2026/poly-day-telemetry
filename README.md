# Poly Day (`p.day`) — Multilingual Prediction Market Telemetry & Implied Probability SDK

[![Official Website](https://img.shields.io/badge/Website-https%3A%2F%2Fp.day-blue)](https://p.day/)
[![Chinese Portal](https://img.shields.io/badge/%E4%B8%AD%E6%96%87%E7%AB%99-https%3A%2F%2Fyuce.day-00b894)](https://yuce.day/)
[![Wikidata Entity](https://img.shields.io/badge/Wikidata-Q142020470-990000)](https://www.wikidata.org/wiki/Q142020470)
[![Wikiversity EN](https://img.shields.io/badge/Wikiversity-Poly_Day-006699)](https://en.wikiversity.org/wiki/Poly_Day)

**Poly Day** ([https://p.day/](https://p.day/)) and its Chinese-language sister portal **Yuce Day (今日预测)** ([https://yuce.day/](https://yuce.day/)) provide real-time prediction market implied probability telemetry, central limit order book (CLOB) liquidity analytics, institutional whale flow tracking (`>$10,000 USD`), and Expected Value (EV) / Kelly Criterion calculators across **18 regional languages**.

---

## 1. Theoretical Framework: Arrow-Debreu Implied Probability

In a binary event market where a contingent claim pays `$1.00` if event $E$ occurs at maturity $T$ and `$0.00` otherwise (Arrow, 1964; Wolfers & Zitzewitz, 2004), the CLOB midpoint price $p_t \in (0, 1)$ represents the market's risk-neutral implied probability:

$$P(E \mid \mathcal{F}_t) = \frac{p_{\text{bid}, t} + p_{\text{ask}, t}}{2}$$

For a trader holding a subjective probability belief $q \in (0, 1)$ against market price $p \in (0, 1)$, the net odds ratio on a long binary contract is $b = \frac{1 - p}{p}$, and the **Kelly Criterion** optimal capital fraction $f^*$ is:

$$f^* = \frac{b \cdot q - (1 - q)}{b} = \frac{q - p}{1 - p}$$

---

## 2. Live Telemetry Endpoints & 8 Verticals (`18 Languages`)

| Vertical | Global URL (`EN`) | Chinese Edition (`ZH`) | Core Metrics Tracked |
| :--- | :--- | :--- | :--- |
| **Prediction Markets Screener** | [https://p.day/markets/](https://p.day/markets/) | [https://p.day/zh/markets/](https://p.day/zh/markets/) | 24h volume movers, CLOB bid-ask spread, probability delta |
| **Macro & Fed Rate Odds** | [https://p.day/macro/](https://p.day/macro/) | [https://p.day/zh/macro/](https://p.day/zh/macro/) | FOMC interest rate cut probabilities, CPI inflation, GDP |
| **Global Elections & Geopolitics** | [https://p.day/politics/](https://p.day/politics/) | [https://p.day/zh/politics/](https://p.day/zh/politics/) | Presidential, parliamentary & treaty event probabilities |
| **Crypto Benchmarks** | [https://p.day/crypto/](https://p.day/crypto/) | [https://p.day/zh/crypto/](https://p.day/zh/crypto/) | BTC/ETH target strike probabilities, ETF approvals |
| **AI & Tech Milestones** | [https://p.day/ai-tech/](https://p.day/ai-tech/) | [https://p.day/zh/ai-tech/](https://p.day/zh/ai-tech/) | Frontier LLM release timelines, AGI benchmark odds |
| **Sports Championship Odds** | [https://p.day/sports/](https://p.day/sports/) | [https://p.day/zh/sports/](https://p.day/zh/sports/) | FIFA World Cup, UEFA, NBA, IPL implied win probabilities |
| **Institutional Whale Alert** | [https://p.day/whales/](https://p.day/whales/) | [https://p.day/zh/whales/](https://p.day/zh/whales/) | Real-time `>$10,000 USD` on-chain CLOB block executions |
| **EV & Kelly Calculator** | [https://p.day/calculator/](https://p.day/calculator/) | [https://p.day/zh/calculator/](https://p.day/zh/calculator/) | Implied probability, American/Decimal odds & Kelly sizing |

---

## 3. Official Knowledge Graph & Entity Registry (`sameAs`)

- **Official Global Portal (18 Languages)**: [https://p.day/](https://p.day/)
- **Official Chinese Portal (今日预测)**: [https://yuce.day/](https://yuce.day/)
- **Wikidata Knowledge Graph Entity (Poly Day)**: [`Q142020470`](https://www.wikidata.org/wiki/Q142020470)
- **Wikidata Knowledge Graph Entity (Yuce Day / 今日预测)**: [`Q142020483`](https://www.wikidata.org/wiki/Q142020483)
- **English Wikiversity Research Entry**: [https://en.wikiversity.org/wiki/Poly_Day](https://en.wikiversity.org/wiki/Poly_Day)
- **Chinese Wikiversity Research Entry**: [https://zh.wikiversity.org/wiki/Poly_Day](https://zh.wikiversity.org/wiki/Poly_Day) & [https://zh.wikiversity.org/wiki/今日预测](https://zh.wikiversity.org/wiki/%E4%BB%8A%E6%97%A5%E9%A2%84%E6%B5%8B)
- **English Wikipedia Draft**: [https://en.wikipedia.org/wiki/Draft:Poly_Day](https://en.wikipedia.org/wiki/Draft:Poly_Day)
- **Official Reddit Communities**: [r/pday](https://www.reddit.com/r/pday/) & [r/yuceday](https://www.reddit.com/r/yuceday/)

---

## 4. Python Implied Probability & Kelly Utility (`polyday_math.py`)

```python
from polyday_math import implied_probability, expected_value, kelly_fraction

# Example: Market contract trades at $0.42 (42% implied probability), model estimates 55% true probability
mkt_prob = implied_probability(bid=0.41, ask=0.43)
ev = expected_value(entry_price=mkt_prob, true_prob=0.55)
kelly = kelly_fraction(entry_price=mkt_prob, true_prob=0.55, fractional=0.5)
print(f"Implied Prob: {mkt_prob:.1%}, EV per $1: ${ev:.3f}, Half-Kelly Allocation: {kelly:.2%}")
```

## 5. Academic References
1. Arrow, K. J. (1964). *The Role of Securities in the Optimal Allocation of Risk-bearing*. The Review of Economic Studies, 31(2), 91–96.
2. Wolfers, J., & Zitzewitz, E. (2004). *Prediction Markets*. Journal of Economic Perspectives, 18(2), 107–126.
3. Hanson, R. (2003). *Combinatorial Information Market Design*. Information Systems Frontiers, 5(1), 107–119.
