---
chapter: 3
title: Risk and Return
subject: finance
course: financial-management
prefix: FIN
code: "201"
keywords: [risk, return, standard deviation, beta, CAPM, diversification, systematic risk, unsystematic risk, portfolio, risk premium, expected return, efficient frontier]
prereqs: [ch01]
---

# Risk and Return

## Overview
The fundamental tradeoff in finance: higher expected returns require taking on more risk. Risk is measured by the variability (standard deviation) of returns. Diversification reduces firm-specific (unsystematic) risk but cannot eliminate market (systematic) risk. The Capital Asset Pricing Model (CAPM) quantifies the relationship between systematic risk (beta) and expected return, providing a framework for pricing risky assets.

## Key Terms
- **Risk**: The uncertainty of future returns. Measured by standard deviation or variance.
- **Return**: The percentage gain or loss on an investment. Total return = (ending price - beginning price + dividends) / beginning price.
- **Expected Return**: The probability-weighted average of possible returns.
- **Standard Deviation**: A measure of volatility -- how much returns deviate from the mean. Higher SD = more risk.
- **Diversification**: Holding multiple assets to reduce risk. "Don't put all your eggs in one basket."
- **Systematic Risk (Market Risk)**: Risk affecting the entire market (recessions, interest rate changes, inflation). Cannot be diversified away.
- **Unsystematic Risk (Firm-Specific Risk)**: Risk unique to a company or industry (management changes, lawsuits, product failures). Can be diversified away.
- **Beta (B)**: A measure of systematic risk. B = 1 means same risk as the market. B > 1 = more volatile. B < 1 = less volatile.
- **Capital Asset Pricing Model (CAPM)**: Expected return = Risk-free rate + Beta x (Market return - Risk-free rate). E(r) = rf + B(rm - rf).
- **Risk Premium**: The extra return investors demand for bearing risk. Equity risk premium = market return - risk-free rate.
- **Risk-Free Rate**: Return on a riskless investment (typically US Treasury bills).
- **Efficient Frontier**: The set of portfolios offering the highest return for each level of risk. Rational investors choose portfolios on the efficient frontier.
- **Correlation**: How two assets' returns move together. Low/negative correlation = better diversification benefit.

## Core Concepts

### Diversification Reduces Risk
A portfolio of 20-30 stocks from different industries eliminates most unsystematic risk. Adding more stocks provides diminishing benefit. Only systematic risk remains and determines the portfolio's expected return. This is why beta (not total risk) matters for pricing.

### CAPM
E(r) = rf + B(rm - rf). If rf = 3%, rm = 10%, and a stock's beta = 1.5: E(r) = 3% + 1.5(10% - 3%) = 13.5%. Higher beta stocks require higher expected returns to compensate for higher systematic risk. CAPM provides the "required return" used as the discount rate in valuation.

### Risk-Return Tradeoff
Stocks have higher average returns than bonds, which have higher returns than Treasury bills -- because stocks are riskier. Investors are risk-averse: they require a premium to accept risk. The equity risk premium has historically been ~5-7% per year.

## Examples

### Portfolio Diversification
Holding only airline stocks is risky (industry-specific shocks). Adding tech, healthcare, and consumer staples reduces portfolio volatility because these industries don't move in perfect sync. An index fund holding 500 stocks has very low unsystematic risk.

### Beta in Practice
Tesla's beta is ~2.0 (twice as volatile as the market). Coca-Cola's beta is ~0.6 (less volatile). In a bull market, Tesla outperforms; in a bear market, Tesla falls harder. Investors in Tesla demand higher expected returns to compensate.

## Relationships
- Higher risk (SD) -> Higher expected return required
- Diversification -> Eliminates unsystematic risk
- Higher beta -> Higher expected return (CAPM)
- Negative correlation between assets -> Better diversification
- Only systematic risk is priced (compensated with higher returns)

## Common Misconceptions
- **"Risk and return are always correlated"**: For well-diversified portfolios, yes. For individual stocks, high risk doesn't guarantee high return -- a risky stock can lose everything.
- **"Diversification eliminates all risk"**: Only unsystematic risk. Systematic risk (market crashes) affects all stocks.
- **"Beta is fixed"**: Beta changes over time as a company's business and leverage change.
- **"CAPM perfectly predicts returns"**: CAPM is a simplified model. Real returns depend on many factors CAPM doesn't capture (size, value, momentum).

## Practice Angles
- Calculate: expected return using CAPM given rf, rm, and beta
- Calculate: portfolio expected return and standard deviation with two assets
- Explain: why diversification reduces risk but can't eliminate it entirely
- Compare: high-beta vs low-beta stocks in bull and bear markets
- Analyze: is a stock overpriced or underpriced using CAPM? (compare actual return to required return)
