---
chapter: 1
title: Time Value of Money
subject: finance
course: financial-management
prefix: FIN
code: "201"
keywords: [time value of money, present value, future value, discount rate, compounding, discounting, interest rate, lump sum]
prereqs: []
---

# Time Value of Money

## Overview
The time value of money (TVM) is the most fundamental concept in finance. A dollar today is worth more than a dollar in the future because today's dollar can be invested to earn interest. This principle underlies virtually every financial decision: valuing bonds and stocks, evaluating capital projects, structuring loan payments, and planning for retirement. TVM allows us to compare cash flows occurring at different points in time by converting them to a common time period.

There are two directions of TVM calculation: compounding (moving a present amount forward to find its future value) and discounting (moving a future amount backward to find its present value). The interest rate used in discounting is called the discount rate, required rate of return, or opportunity cost of capital.

## Key Terms
- **Time Value of Money (TVM)**: The principle that money available now is worth more than the same amount in the future due to its earning capacity. This is the foundation of all valuation in finance.
- **Present Value (PV)**: The current worth of a future sum of money or stream of cash flows, given a specified rate of return. PV answers: "What is a future payment worth today?"
- **Future Value (FV)**: The value of a current asset at a specified date in the future, assuming a certain rate of growth. FV answers: "What will today's money be worth later?"
- **Discount Rate (r)**: The interest rate used to calculate the present value of future cash flows. It reflects the opportunity cost of capital -- the return you could earn on an alternative investment of similar risk.
- **Compounding**: The process of earning interest on both the original principal and on previously earned interest. Compounding grows money exponentially over time.
- **Discounting**: The reverse of compounding. The process of determining the present value of a future cash flow by removing the effects of time and the discount rate.
- **Compound Interest**: Interest calculated on the initial principal and also on the accumulated interest from previous periods. Contrast with simple interest.
- **Simple Interest**: Interest calculated only on the original principal amount. Formula: Interest = Principal x Rate x Time.
- **Number of Periods (n)**: The total number of compounding or discounting periods. Can be years, months, quarters, etc.
- **Opportunity Cost**: The return foregone by choosing one investment over the next-best alternative. This concept motivates the entire TVM framework.

## Core Concepts

### Future Value of a Lump Sum
If you invest PV dollars today at interest rate r per period for n periods, the future value is:

**FV = PV x (1 + r)^n**

The term (1 + r)^n is the future value interest factor (FVIF). It tells you how much $1 today will grow to after n periods at rate r.

Example: Invest $1,000 at 8% for 3 years.
FV = $1,000 x (1.08)^3 = $1,000 x 1.2597 = $1,259.71

The $259.71 earned is more than 3 x $80 = $240 (simple interest) because of compounding -- you earn interest on interest.

### Present Value of a Lump Sum
To find what a future amount is worth today, rearrange the FV formula:

**PV = FV / (1 + r)^n**

Or equivalently: PV = FV x [1 / (1 + r)^n]

The term 1/(1 + r)^n is the present value interest factor (PVIF) or discount factor.

Example: What is $1,259.71 received in 3 years worth today at 8%?
PV = $1,259.71 / (1.08)^3 = $1,259.71 / 1.2597 = $1,000.00

### Compounding Frequency
Interest can compound annually, semi-annually, quarterly, monthly, or even continuously.

For m compounding periods per year:
**FV = PV x (1 + r/m)^(n x m)**

The effective annual rate (EAR) converts any compounding frequency to an equivalent annual rate:
**EAR = (1 + r/m)^m - 1**

Example: 12% nominal rate compounded monthly:
EAR = (1 + 0.12/12)^12 - 1 = (1.01)^12 - 1 = 12.68%

For continuous compounding: FV = PV x e^(r x n), where e = 2.71828...

### Solving for Unknown Variables
The TVM equation FV = PV x (1 + r)^n has four variables. Given any three, you can solve for the fourth:

- **Solve for r**: r = (FV/PV)^(1/n) - 1
- **Solve for n**: n = ln(FV/PV) / ln(1 + r)

Example (solving for r): You invest $500 and receive $750 after 5 years. What annual rate did you earn?
r = (750/500)^(1/5) - 1 = (1.5)^0.2 - 1 = 8.45%

### The Rule of 72
A quick approximation: the number of years to double your money equals 72 / interest rate.
At 8%, money doubles in approximately 72/8 = 9 years.
At 12%, money doubles in approximately 72/12 = 6 years.

## Examples

### Example 1: College Savings
A parent invests $10,000 when a child is born. If the account earns 7% annually, what will it be worth when the child turns 18?
FV = $10,000 x (1.07)^18 = $10,000 x 3.3799 = $33,799.32
The investment more than triples due to compounding over 18 years.

### Example 2: Retirement Goal
You want $1,000,000 at retirement in 30 years. If you can earn 10% annually, how much must you invest today as a lump sum?
PV = $1,000,000 / (1.10)^30 = $1,000,000 / 17.4494 = $57,308.55
You need to invest only about $57,000 today because compounding does the heavy lifting.

### Example 3: Comparing Compounding Frequencies
Bank A offers 6% compounded annually. Bank B offers 5.9% compounded daily. Which is better?
Bank A EAR = 6.00%
Bank B EAR = (1 + 0.059/365)^365 - 1 = 6.08%
Bank B is actually better despite the lower stated rate, because daily compounding boosts the effective rate.

## Relationships
- Present Value and Future Value are inverse operations: PV = FV / (1+r)^n and FV = PV x (1+r)^n
- Higher discount rate -> Lower present value (money in the future is worth less when opportunity cost is higher)
- More compounding periods -> Higher effective rate -> Higher future value
- Longer time horizon -> Greater impact of compounding (exponential growth)
- TVM -> Bond Valuation: Bond price = PV of all coupon payments + PV of face value
- TVM -> Stock Valuation: Stock price = PV of all expected future dividends
- TVM -> Capital Budgeting: NPV = PV of future cash inflows - initial investment

## Common Misconceptions
- **Confusing simple and compound interest**: Simple interest grows linearly; compound interest grows exponentially. Most financial calculations assume compound interest.
- **Using the wrong compounding frequency**: A 12% annual rate compounded monthly is NOT the same as 12% compounded annually. Always check whether a rate is nominal (stated) or effective.
- **Forgetting that n and r must match**: If compounding is monthly, r must be the monthly rate and n must be the number of months. Mixing annual rates with monthly periods produces wrong answers.
- **Assuming TVM doesn't matter for short periods**: Even over a few months, TVM matters for large sums. A $10 million investment at 5% earns about $41,667 per month.
- **Ignoring inflation**: The real return (adjusted for inflation) is what actually increases purchasing power. Real rate is approximately: nominal rate - inflation rate.

## Practice Angles
- Calculate FV and PV for different rates and time periods
- Compare compounding frequencies (annual vs. semi-annual vs. monthly)
- Solve for the unknown interest rate given PV, FV, and n
- Solve for the number of periods given PV, FV, and r
- Apply the Rule of 72 to quick-estimate doubling time
- Convert between nominal and effective annual rates
