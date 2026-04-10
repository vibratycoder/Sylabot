---
chapter: 4
title: Risk and Return
subject: finance
course: financial-management
prefix: FIN
code: "201"
keywords: [risk, return, expected return, standard deviation, variance, diversification, systematic risk, unsystematic risk, beta, CAPM, capital asset pricing model, security market line, risk premium, portfolio theory, correlation]
prereqs: [ch01, ch02, ch03]
---

# Risk and Return

## Overview
The tradeoff between risk and return is the central theme of finance. Investors demand higher expected returns for bearing higher risk. Risk in finance is measured by the variability (uncertainty) of returns, typically quantified by standard deviation or variance. Modern portfolio theory shows that diversification -- holding a mix of assets -- can reduce risk without proportionally reducing return, because individual asset risks partly cancel each other out.

The Capital Asset Pricing Model (CAPM) formalizes the relationship between systematic risk (measured by beta) and expected return. It implies that only systematic (market) risk is rewarded with higher expected returns, because unsystematic (firm-specific) risk can be diversified away.

## Key Terms
- **Return**: The gain or loss on an investment over a period, expressed as a percentage. Total return = (ending price - beginning price + income) / beginning price.
- **Expected Return E(R)**: The probability-weighted average of all possible returns. E(R) = sum of [probability_i x return_i].
- **Risk**: The uncertainty surrounding future returns. In finance, risk is typically measured by the dispersion (variability) of possible returns.
- **Standard Deviation (sigma)**: The square root of variance. Measures total risk -- how spread out returns are around the expected value. Higher sigma = more risk.
- **Variance (sigma-squared)**: The probability-weighted average of squared deviations from the expected return.
- **Risk Premium**: The additional return above the risk-free rate that investors require for bearing risk. Risk premium = E(R) - R_f.
- **Risk-Free Rate (R_f)**: The return on an investment with zero risk, typically proxied by U.S. Treasury bill yields.
- **Diversification**: Combining assets in a portfolio to reduce overall risk. Works because asset returns are imperfectly correlated.
- **Systematic Risk (Market Risk)**: Risk that affects the entire market and cannot be diversified away. Examples: interest rate changes, recessions, inflation. Measured by beta.
- **Unsystematic Risk (Firm-Specific Risk)**: Risk unique to a particular company or industry that can be eliminated through diversification. Examples: a product recall, a CEO departure.
- **Beta (B)**: A measure of an asset's sensitivity to market movements. Beta = Cov(R_asset, R_market) / Var(R_market). Market beta = 1.0. Beta > 1 = more volatile than market; Beta < 1 = less volatile.
- **Capital Asset Pricing Model (CAPM)**: E(R_i) = R_f + B_i x [E(R_m) - R_f]. States that expected return is a linear function of systematic risk (beta).
- **Security Market Line (SML)**: The graphical representation of CAPM. Plots expected return (y-axis) vs beta (x-axis). All correctly priced assets plot on the SML.
- **Market Risk Premium**: E(R_m) - R_f. The extra return the overall market provides above the risk-free rate. Historically about 5-7% for U.S. stocks.
- **Correlation Coefficient (rho)**: Measures the degree to which two assets move together. Ranges from -1 (perfect negative) to +1 (perfect positive). Lower correlation = greater diversification benefit.
- **Covariance**: Measures how two assets' returns move together. Cov(A,B) = rho_AB x sigma_A x sigma_B.
- **Portfolio Expected Return**: E(R_p) = w_A x E(R_A) + w_B x E(R_B), where w = portfolio weight.
- **Portfolio Standard Deviation** (two-asset): sigma_p = sqrt[w_A^2 x sigma_A^2 + w_B^2 x sigma_B^2 + 2 x w_A x w_B x Cov(A,B)]
- **Efficient Frontier**: The set of portfolios offering the highest expected return for each level of risk. Rational investors choose portfolios on the efficient frontier.
- **Sharpe Ratio**: (E(R_p) - R_f) / sigma_p. Measures excess return per unit of total risk. Higher = better risk-adjusted performance.
- **Treynor Ratio**: (E(R_p) - R_f) / Beta_p. Measures excess return per unit of systematic risk.

## Core Concepts

### Calculating Expected Return and Standard Deviation
Given n scenarios with probabilities p_i and returns R_i:

E(R) = sum of p_i x R_i

Variance = sum of p_i x [R_i - E(R)]^2

Standard Deviation = sqrt(Variance)

Example: Three scenarios -- Boom (30% probability, 25% return), Normal (50%, 12%), Recession (20%, -8%).
E(R) = 0.30(25%) + 0.50(12%) + 0.20(-8%) = 7.5% + 6.0% - 1.6% = 11.9%
Variance = 0.30(25-11.9)^2 + 0.50(12-11.9)^2 + 0.20(-8-11.9)^2 = 51.44 + 0.005 + 79.202 = 130.65
Std Dev = sqrt(130.65) = 11.43%

### Portfolio Diversification
When combining two assets A and B with weights w_A and w_B:
- Portfolio return = w_A x E(R_A) + w_B x E(R_B)
- Portfolio risk depends on individual risks AND correlation between the assets

If rho = +1: No diversification benefit. Portfolio risk = weighted average of individual risks.
If rho < +1: Diversification benefit exists. Portfolio risk < weighted average of individual risks.
If rho = -1: Perfect hedging possible. A specific combination can eliminate all risk.

### CAPM
**E(R_i) = R_f + B_i x [E(R_m) - R_f]**

Example: Risk-free rate = 3%, Market return = 10%, Stock beta = 1.5.
E(R_stock) = 3% + 1.5 x (10% - 3%) = 3% + 10.5% = 13.5%

Interpretation: Because this stock is 50% more volatile than the market (beta = 1.5), investors demand 10.5% above the risk-free rate, versus only 7% for the market as a whole.

### Alpha
If actual return > CAPM predicted return, the asset has positive alpha (it outperformed on a risk-adjusted basis).
Alpha = Actual return - CAPM expected return.
Positive alpha = undervalued; Negative alpha = overvalued.

### Beta Estimation
Beta is estimated by regressing the asset's historical returns against market returns. The slope of the regression line is beta. Beta of the overall market = 1.0. Beta of a risk-free asset = 0.

Portfolio beta = weighted average of individual betas:
B_p = w_1 x B_1 + w_2 x B_2 + ... + w_n x B_n

## Examples

### Example 1: Portfolio of Two Stocks
Stock A: E(R) = 14%, sigma = 20%, weight = 60%
Stock B: E(R) = 8%, sigma = 12%, weight = 40%
Correlation = 0.3

E(R_p) = 0.60(14%) + 0.40(8%) = 8.4% + 3.2% = 11.6%

sigma_p = sqrt[(0.6)^2(0.20)^2 + (0.4)^2(0.12)^2 + 2(0.6)(0.4)(0.3)(0.20)(0.12)]
= sqrt[0.0144 + 0.002304 + 0.003456] = sqrt[0.02016] = 14.2%

Weighted average of individual std devs = 0.6(20%) + 0.4(12%) = 16.8%
Diversification reduced portfolio risk from 16.8% to 14.2%.

### Example 2: CAPM Application
Treasury bill rate = 4%. S&P 500 expected return = 11%. A stock's beta = 0.8.
CAPM E(R) = 4% + 0.8(11% - 4%) = 4% + 5.6% = 9.6%
If you expect the stock to actually return 12%, alpha = 12% - 9.6% = +2.4% (the stock appears undervalued).

### Example 3: Risk Decomposition
A stock has total risk (standard deviation) of 30%. Its beta is 1.2 and the market std dev is 15%.
Systematic risk (std dev) = Beta x Market std dev = 1.2 x 15% = 18%
Unsystematic risk can be approximated using: Total^2 = Systematic^2 + Unsystematic^2
Unsystematic risk = sqrt(30%^2 - 18%^2) = sqrt(9% - 3.24%) = sqrt(5.76%) = 24%
Most of this stock's risk is unsystematic and can be diversified away.

## Relationships
- Risk-return tradeoff is the foundation for all asset pricing
- Beta connects to cost of equity in cost of capital calculations (Ch. 8)
- CAPM expected return is the required return used to discount stock cash flows (Ch. 6)
- Diversification principle underlies portfolio management (FIN 312, FIN 454)
- Risk-free rate connects to bond valuation (Ch. 5)
- Market risk premium connects to equity valuation and capital budgeting hurdle rates (Ch. 7)

## Common Misconceptions
- **Risk and return are always proportional**: Only systematic risk is rewarded. A firm-specific gamble (like buying a single stock) can be very risky but earn no extra expected return because that risk is diversifiable.
- **Beta measures total risk**: Beta only measures systematic risk. Two stocks can have the same beta but very different total risk (standard deviation).
- **Diversification eliminates all risk**: Diversification eliminates unsystematic risk but cannot remove systematic (market) risk. Even a perfectly diversified portfolio still moves with the market.
- **CAPM is perfectly accurate**: CAPM is a simplified model. Real-world returns are influenced by factors beyond beta (size, value, momentum). But CAPM remains the most widely taught baseline model.
- **Negative beta means the asset is risk-free**: Negative beta means the asset moves opposite to the market. It still has risk; it just provides a hedging benefit. CAPM says its expected return should be below the risk-free rate.
- **Standard deviation of past returns perfectly predicts future risk**: Historical volatility is a guide but not a guarantee. Risk regimes can change.

## Practice Angles
- Calculate expected return and standard deviation from probability distributions
- Compute portfolio expected return and standard deviation for a two-asset portfolio
- Use CAPM to find required return given beta, risk-free rate, and market return
- Determine whether a stock is overvalued or undervalued using CAPM and expected return
- Calculate portfolio beta from individual stock betas and weights
- Compare Sharpe ratios of two portfolios to determine which has better risk-adjusted performance
- Explain why adding a low-correlation asset to a portfolio reduces risk
