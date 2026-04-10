---
chapter: 8
title: Cost of Capital
subject: finance
course: financial-management
prefix: FIN
code: "201"
keywords: [cost of capital, WACC, weighted average cost of capital, cost of equity, cost of debt, cost of preferred stock, after-tax cost of debt, capital structure weights, flotation costs, CAPM, dividend growth model, marginal cost of capital]
prereqs: [ch04, ch05, ch06, ch07]
---

# Cost of Capital

## Overview
The cost of capital is the minimum rate of return a firm must earn on its investments to satisfy all of its investors (debt holders, preferred stockholders, and common stockholders). It serves as the hurdle rate for capital budgeting decisions: projects earning above the cost of capital create value; those earning below it destroy value.

The Weighted Average Cost of Capital (WACC) blends the costs of all funding sources according to their proportions in the firm's target capital structure. Estimating WACC requires calculating the cost of each component: debt, preferred equity, and common equity.

## Key Terms
- **Cost of Capital**: The required rate of return that makes an investment worthwhile. It is the opportunity cost of using funds for a specific project rather than investing in the financial market at the same risk level.
- **Weighted Average Cost of Capital (WACC)**: The blended cost of all sources of capital, weighted by their target proportions. WACC = w_d x r_d x (1-T) + w_p x r_p + w_e x r_e.
- **Cost of Debt (r_d)**: The yield to maturity on the firm's outstanding debt. Represents the return debt holders require.
- **After-Tax Cost of Debt**: r_d x (1 - T), where T is the corporate tax rate. Interest is tax-deductible, so the true cost of debt is reduced by the tax shield.
- **Cost of Preferred Stock (r_p)**: r_p = D_p / P_p. The preferred dividend divided by the current preferred stock price.
- **Cost of Common Equity (r_e)**: The return common shareholders require. Estimated using CAPM, the Dividend Growth Model, or the Bond Yield Plus Risk Premium approach.
- **CAPM Approach to Cost of Equity**: r_e = R_f + Beta x (R_m - R_f). Uses market risk data.
- **Dividend Growth Model Approach**: r_e = (D_1 / P_0) + g. Uses current dividend yield plus expected growth rate.
- **Bond Yield Plus Risk Premium**: r_e = r_d + equity risk premium (typically 3-5%). A rough approximation.
- **Target Capital Structure**: The ideal mix of debt, preferred stock, and equity the firm aims to maintain over time.
- **Market Value Weights**: Using current market values (not book values) of debt and equity to calculate WACC. Market values are preferred because they reflect current economic conditions.
- **Flotation Costs**: Fees paid to investment banks when issuing new securities. Increase the effective cost of capital.
- **Marginal Cost of Capital (MCC)**: The cost of raising one additional dollar of capital. May increase as the firm raises more capital.
- **Tax Shield**: The reduction in taxes from deducting interest payments. Tax shield = Interest x Tax Rate.

## Core Concepts

### WACC Formula
**WACC = w_d x r_d x (1 - T) + w_p x r_p + w_e x r_e**

Where:
- w_d, w_p, w_e = weight (proportion) of debt, preferred stock, and equity
- r_d = cost of debt (pre-tax)
- T = corporate tax rate
- r_p = cost of preferred stock
- r_e = cost of common equity
- All weights should sum to 1.0

Example: Target structure: 40% debt, 10% preferred, 50% equity.
r_d = 7%, T = 30%, r_p = 9%, r_e = 14%
WACC = 0.40 x 7% x (1-0.30) + 0.10 x 9% + 0.50 x 14%
WACC = 0.40 x 4.9% + 0.90% + 7.0% = 1.96% + 0.90% + 7.0% = 9.86%

### Estimating Cost of Equity
Three methods:

**Method 1: CAPM**
r_e = R_f + Beta x (R_m - R_f)
Example: R_f = 3%, Beta = 1.2, Market premium = 7%
r_e = 3% + 1.2 x 7% = 11.4%

**Method 2: Dividend Growth Model (DCF)**
r_e = (D_1 / P_0) + g
Example: D_1 = $2, P_0 = $40, g = 6%
r_e = ($2 / $40) + 6% = 5% + 6% = 11%

**Method 3: Bond Yield + Risk Premium**
r_e = r_d + equity risk premium
Example: r_d = 7%, premium = 4%
r_e = 7% + 4% = 11%

Best practice: Use multiple methods and average/judgment-weight the results.

### Why Debt is Cheaper than Equity
1. **Tax deductibility**: Interest payments reduce taxable income, creating a tax shield.
2. **Priority in bankruptcy**: Debt holders are paid before equity holders, so debt is less risky to investors.
3. **Contractual obligation**: Debt payments are fixed and certain, unlike uncertain dividends.

But more debt increases financial risk, which increases both the cost of equity (shareholders demand more) and eventually the cost of debt (higher default risk).

### Project-Specific WACC
The firm-wide WACC is only appropriate for projects with similar risk to the firm's existing operations. For projects with different risk levels:
- Higher-risk projects should use a higher discount rate
- Lower-risk projects should use a lower discount rate

Using a single WACC for all projects leads to accepting too many risky projects and rejecting good low-risk projects.

## Examples

### Example 1: Full WACC Calculation
Firm data: Market value of debt = $4M, preferred = $1M, equity = $5M. Total = $10M.
Weights: w_d = 0.40, w_p = 0.10, w_e = 0.50
YTM on bonds = 6%, Preferred dividend yield = 8%, CAPM cost of equity = 13%, Tax rate = 25%.
WACC = 0.40 x 6% x (1-0.25) + 0.10 x 8% + 0.50 x 13% = 1.80% + 0.80% + 6.50% = 9.10%

### Example 2: Impact of Capital Structure on WACC
All-equity firm: WACC = r_e = 14%
After adding 30% debt at 7% (tax rate 30%):
WACC = 0.30 x 7% x 0.70 + 0.70 x 14% = 1.47% + 9.80% = 11.27%
Debt reduced WACC from 14% to 11.27% because of the tax shield. But too much debt will increase both r_d and r_e.

## Relationships
- WACC is the discount rate used in NPV calculations (Ch. 7)
- Cost of equity comes from CAPM (Ch. 4) or DDM (Ch. 6)
- Cost of debt comes from bond valuation (Ch. 5)
- WACC depends on capital structure decisions (Ch. 9)
- Tax shield benefits connect to financial statements (Ch. 3)
- Market value weights require understanding of stock and bond valuation

## Common Misconceptions
- **Book value weights are just as good as market value weights**: Market values reflect the current required returns of investors. Book values are historical and may bear little relation to current costs.
- **Cost of debt is the coupon rate**: It is the yield to maturity, not the coupon rate. YTM reflects the current market-required return.
- **Retained earnings are free**: Shareholders could invest those funds elsewhere. The cost of retained earnings equals the cost of equity -- it is the opportunity cost to shareholders.
- **WACC is fixed**: WACC changes when market conditions change (interest rates, stock price, risk perception) or when the firm changes its capital structure.
- **Lower WACC always means more value**: A lower WACC is only better if achieved without excessive risk. Overloading debt initially lowers WACC but eventually increases both debt and equity costs.

## Practice Angles
- Calculate WACC given component costs and weights
- Estimate cost of equity using CAPM and the Dividend Growth Model, then compare results
- Calculate after-tax cost of debt
- Determine the impact of changing capital structure on WACC
- Explain why a firm should not use its overall WACC for projects of different risk
- Calculate the flotation-cost-adjusted cost of new equity
