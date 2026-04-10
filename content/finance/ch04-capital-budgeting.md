---
chapter: 4
title: Capital Budgeting
subject: finance
course: financial-management
prefix: FIN
code: "201"
keywords: [capital budgeting, NPV, IRR, payback period, profitability index, cash flow, WACC, project evaluation, investment decision]
prereqs: [ch01, ch03]
---

# Capital Budgeting

## Overview
Capital budgeting is the process of evaluating long-term investment projects. Should a firm build a new factory, launch a product, or acquire a competitor? The gold-standard tool is Net Present Value (NPV), which discounts all project cash flows at the firm's cost of capital. Other methods include IRR, payback period, and profitability index. Good capital budgeting creates shareholder value; bad decisions destroy it.

## Key Terms
- **Capital Budgeting**: The process of analyzing and selecting long-term investments.
- **Net Present Value (NPV)**: Sum of present values of all cash flows (initial investment + future inflows). NPV = sum of [CF_t / (1+r)^t]. Accept if NPV > 0.
- **Internal Rate of Return (IRR)**: The discount rate that makes NPV = 0. Accept if IRR > required return (WACC).
- **Payback Period**: Time required to recover the initial investment. Simple but ignores TVM and cash flows after payback.
- **Discounted Payback Period**: Like payback but uses discounted cash flows. Better than simple payback but still ignores post-payback flows.
- **Profitability Index (PI)**: PV of future cash flows / Initial investment. Accept if PI > 1. Useful for capital rationing.
- **Incremental Cash Flows**: Only cash flows that change as a result of the project. Ignore sunk costs; include opportunity costs.
- **Sunk Cost**: A cost already incurred that cannot be recovered. Should NOT affect the investment decision.
- **Opportunity Cost**: The value of the best alternative use of a resource. SHOULD be included in analysis.
- **Weighted Average Cost of Capital (WACC)**: The firm's blended cost of debt and equity. Used as the discount rate for NPV. WACC = (E/V)re + (D/V)rd(1-T).

## Core Concepts

### NPV Decision Rule
NPV is the single best method because it: considers all cash flows, accounts for TVM, uses the correct risk-adjusted discount rate, and directly measures value creation. NPV > 0 means the project earns more than the cost of capital.

### Cash Flow Estimation
Operating cash flow = EBIT(1-T) + Depreciation. Include: initial investment, working capital changes, salvage value. Exclude: sunk costs, financing costs (captured in WACC). Consider: cannibalization (new product stealing sales from existing products), erosion, and side effects.

### NPV vs IRR Conflicts
For independent projects, NPV and IRR agree. For mutually exclusive projects, they can conflict (different scales, timing). Always choose NPV when they disagree. IRR can also have multiple solutions for non-conventional cash flows.

## Examples

### New Product Launch
Cost: $500K. Expected cash flows: $150K/year for 5 years. WACC: 10%. NPV = -$500K + $150K(PVIFA 10%, 5) = -$500K + $568,618 = $68,618. NPV > 0, so launch the product.

### Mutually Exclusive Projects
Project A: costs $100K, NPV = $40K. Project B: costs $200K, NPV = $50K. Choose B (higher NPV). IRR might favor A (higher percentage return) but NPV is what maximizes shareholder value.

## Relationships
- NPV > 0 -> Project creates value -> Accept
- IRR > WACC -> Project acceptable (for independent, conventional projects)
- Higher WACC -> Lower NPV (harder to create value)
- Sunk costs are irrelevant to capital budgeting decisions
- Opportunity costs must be included

## Common Misconceptions
- **"Higher IRR means better project"**: Not for mutually exclusive projects. A small project with 50% IRR may create less value than a large project with 20% IRR.
- **"Payback period is good enough"**: Payback ignores TVM and post-payback cash flows. A project with a long payback but huge later cash flows could be rejected by mistake.
- **"Sunk costs should be recouped"**: Never. Money already spent is gone regardless of the decision. Only future cash flows matter.

## Practice Angles
- Calculate: NPV and IRR for a project given cash flows and discount rate
- Compare: two mutually exclusive projects using NPV, IRR, and payback
- Identify: sunk costs vs opportunity costs in a case scenario
- Explain: why NPV is preferred over IRR for mutually exclusive projects
- Calculate: WACC given debt/equity mix, cost of equity, cost of debt, and tax rate
