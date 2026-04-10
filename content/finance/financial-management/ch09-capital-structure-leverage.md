---
chapter: 9
title: Capital Structure and Leverage
subject: finance
course: financial-management
prefix: FIN
code: "201"
keywords: [capital structure, leverage, financial leverage, operating leverage, Modigliani-Miller, MM, trade-off theory, pecking order theory, debt capacity, optimal capital structure, degree of financial leverage, degree of operating leverage, EPS, EBIT, interest tax shield, bankruptcy costs]
prereqs: [ch07, ch08]
---

# Capital Structure and Leverage

## Overview
Capital structure is the mix of debt and equity a firm uses to finance its operations. The fundamental question is: does the choice of financing affect firm value? Modigliani and Miller (1958) showed that under perfect market conditions, capital structure is irrelevant. But in the real world, taxes, bankruptcy costs, and information asymmetries make capital structure matter significantly.

The tax deductibility of interest creates an incentive to use debt (the tax shield), but excessive debt raises the probability of financial distress and bankruptcy. The optimal capital structure balances these forces to minimize the weighted average cost of capital and maximize firm value.

## Key Terms
- **Capital Structure**: The proportion of debt and equity used to finance a firm's assets. Also called the firm's financial structure or leverage.
- **Financial Leverage**: The use of debt in a firm's capital structure. Amplifies both gains and losses to equity holders.
- **Operating Leverage**: The extent to which a firm uses fixed costs in its operations. High operating leverage means a small change in sales produces a large change in EBIT.
- **Degree of Financial Leverage (DFL)**: DFL = EBIT / (EBIT - Interest). Measures the sensitivity of EPS to changes in EBIT.
- **Degree of Operating Leverage (DOL)**: DOL = (Revenue - Variable Costs) / EBIT = Contribution Margin / EBIT. Measures sensitivity of EBIT to changes in revenue.
- **Degree of Total Leverage (DTL)**: DTL = DOL x DFL. Measures sensitivity of EPS to changes in revenue.
- **Modigliani-Miller (MM) Proposition I (no taxes)**: In a perfect market, the total value of a firm is unaffected by its capital structure. V_levered = V_unlevered.
- **MM Proposition I (with taxes)**: The value of a levered firm equals the value of an unlevered firm plus the tax shield. V_L = V_U + T x D.
- **MM Proposition II**: The cost of equity increases linearly with the debt-to-equity ratio. r_e = r_0 + (r_0 - r_d) x (D/E) x (1-T), where r_0 = cost of capital for an unlevered firm.
- **Trade-Off Theory**: Firms choose a target capital structure by balancing the tax benefits of debt against the costs of financial distress. The optimal structure is where the marginal tax shield equals the marginal distress cost.
- **Pecking Order Theory**: Firms prefer internal financing first, then debt, then equity as a last resort. This hierarchy arises from information asymmetry -- issuing equity signals that management thinks the stock is overvalued.
- **Financial Distress**: A situation where a firm has difficulty meeting its debt obligations. Costs include legal fees, lost customers, loss of key employees, and forced asset sales.
- **Bankruptcy Costs**: Direct costs (legal and administrative fees) and indirect costs (lost business, management distraction, supplier reluctance) of financial distress.
- **Interest Tax Shield**: The tax savings from deducting interest payments. Annual tax shield = Interest x Tax Rate.
- **EBIT-EPS Analysis**: A method comparing EPS under different financing alternatives (debt vs. equity) at various EBIT levels to find the breakeven EBIT.
- **Optimal Capital Structure**: The debt-equity mix that minimizes WACC and maximizes firm value.
- **Debt Capacity**: The maximum amount of debt a firm can reasonably support given its cash flows, assets, and industry norms.

## Core Concepts

### Financial Leverage Effect
Financial leverage amplifies returns to equity holders:
- When ROA > cost of debt: leverage increases ROE
- When ROA < cost of debt: leverage decreases ROE
- When ROA = cost of debt: leverage has no effect on ROE

ROE = ROA + (ROA - r_d) x (D/E) x (1 - T)

### EBIT-EPS Analysis
Compare two financing options (e.g., all equity vs. partial debt) at different EBIT levels.

Breakeven EBIT: the level of operating income where EPS is the same under both plans.

Example:
Plan A: 100% equity, 100,000 shares
Plan B: 50% debt at 8% ($500,000 debt), 50,000 shares

At EBIT = $100,000, T = 30%:
Plan A: EPS = ($100,000)(1-0.30) / 100,000 = $0.70
Plan B: EPS = ($100,000 - $40,000)(1-0.30) / 50,000 = $0.84

Debt plan gives higher EPS because EBIT is high enough to cover interest and leave more per share.

### Trade-Off Theory in Practice
Value of levered firm = Value if all-equity + PV(tax shields) - PV(financial distress costs)

At low debt levels: tax benefits dominate; firm value increases.
At high debt levels: distress costs dominate; firm value decreases.
Optimal: where marginal tax benefit = marginal distress cost.

### Industry Patterns
Capital structure varies by industry:
- Utilities: high debt (stable cash flows, large tangible assets)
- Technology: low debt (volatile cash flows, intangible assets)
- Real estate: high debt (tangible collateral)
- Pharma/biotech: low debt (uncertain R&D outcomes)

## Examples

### Example 1: MM with Taxes
An unlevered firm is worth $5M with cost of capital 12%. It borrows $2M at 8%. Tax rate = 35%.
Tax shield = T x D = 0.35 x $2M = $700,000
V_L = $5M + $700,000 = $5.7M

### Example 2: Leverage and ROE
Firm A (no debt): Assets $10M, Equity $10M, EBIT $1.5M, Tax 30%.
ROA = $1.5M(1-0.30)/$10M = 10.5%. ROE = 10.5%.

Firm B (50% debt at 7%): Assets $10M, Debt $5M, Equity $5M, EBIT $1.5M, Tax 30%.
Net Income = ($1.5M - $350K)(1-0.30) = $805K. ROE = $805K / $5M = 16.1%.
Leverage boosted ROE from 10.5% to 16.1% because ROA > cost of debt.

## Relationships
- Capital structure directly affects WACC (Ch. 8)
- Operating leverage connects to cost structure analysis (Ch. 3)
- Tax shield benefits require understanding of tax accounting
- Financial distress connects to credit analysis (FIN 384) and bond ratings (Ch. 5)
- MM propositions provide the theoretical framework for cost of capital
- EBIT-EPS analysis applies financial statement skills (Ch. 3)

## Common Misconceptions
- **More debt always lowers WACC**: Only true up to a point. Beyond the optimal level, the increase in both cost of equity and cost of debt overwhelms the tax benefit.
- **MM irrelevance means capital structure doesn't matter**: MM irrelevance holds only under perfect market assumptions. In reality, taxes and bankruptcy costs make structure very relevant.
- **Financial leverage only has upside**: Leverage is a double-edged sword. It amplifies gains when times are good AND amplifies losses when times are bad.
- **Operating leverage and financial leverage are the same**: Operating leverage comes from the cost structure (fixed vs variable costs). Financial leverage comes from the financing structure (debt vs equity). Both amplify risk but from different sources.
- **Firms should always match the industry average**: While industry norms are a useful guide, the optimal capital structure depends on the specific firm's cash flow stability, tax situation, growth opportunities, and asset tangibility.

## Practice Angles
- Perform EBIT-EPS analysis comparing debt and equity financing
- Calculate the effect of leverage on ROE at different EBIT levels
- Apply MM Propositions with and without taxes
- Calculate the value of the tax shield
- Explain the trade-off theory graphically
- Determine optimal capital structure using WACC minimization
- Calculate DOL, DFL, and DTL
