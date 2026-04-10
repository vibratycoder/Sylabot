---
chapter: 2
title: Annuities and Complex Cash Flows
subject: finance
course: financial-management
prefix: FIN
code: "201"
keywords: [annuity, ordinary annuity, annuity due, perpetuity, present value of annuity, future value of annuity, amortization, uneven cash flows, growing annuity, growing perpetuity]
prereqs: [ch01]
---

# Annuities and Complex Cash Flows

## Overview
While Chapter 1 dealt with single lump-sum cash flows, most real financial situations involve multiple payments over time. An annuity is a series of equal payments made at regular intervals. Annuities appear everywhere in finance: mortgage payments, car loans, bond coupon payments, lease payments, retirement withdrawals, and insurance premiums. A perpetuity is an annuity that lasts forever. Understanding annuity formulas is essential for loan analysis, retirement planning, and valuation.

Beyond standard annuities, financial managers routinely encounter uneven (mixed) cash flows, growing annuities, and growing perpetuities. Each requires its own valuation approach, but all are built on the present value and future value principles from Chapter 1.

## Key Terms
- **Annuity**: A series of equal cash flows (payments or receipts) occurring at regular intervals for a specified number of periods.
- **Ordinary Annuity**: An annuity where payments occur at the end of each period. Most financial calculations assume ordinary annuities (e.g., bond coupons, most loan payments).
- **Annuity Due**: An annuity where payments occur at the beginning of each period. Examples include rent payments and insurance premiums. Each payment earns one extra period of interest compared to an ordinary annuity.
- **Perpetuity**: An annuity that continues forever. The present value of a perpetuity is simply PV = PMT / r.
- **Payment (PMT)**: The fixed amount paid or received each period in an annuity.
- **Present Value of an Annuity (PVA)**: The lump sum today that is equivalent to the entire stream of annuity payments, discounted at rate r.
- **Future Value of an Annuity (FVA)**: The total accumulated value of all annuity payments at a future date, with each payment compounded at rate r.
- **Amortization**: The process of paying off a debt with a series of equal periodic payments. Each payment covers interest on the remaining balance plus some principal repayment.
- **Amortization Schedule**: A table showing how each payment is split between interest and principal, and the remaining loan balance after each payment.
- **Growing Annuity**: An annuity whose payments grow at a constant rate g each period.
- **Growing Perpetuity**: A perpetuity whose payments grow at a constant rate g forever. PV = PMT / (r - g), valid only when r > g.
- **Uneven Cash Flows**: A series of cash flows that differ in amount from period to period. Must be valued individually and summed.

## Core Concepts

### Present Value of an Ordinary Annuity
**PVA = PMT x [(1 - (1 + r)^(-n)) / r]**

The bracketed term is the present value interest factor of an annuity (PVIFA).

Example: What is the PV of $1,000 received annually for 5 years at 10%?
PVA = $1,000 x [(1 - (1.10)^(-5)) / 0.10] = $1,000 x 3.7908 = $3,790.79

### Future Value of an Ordinary Annuity
**FVA = PMT x [((1 + r)^n - 1) / r]**

The bracketed term is the future value interest factor of an annuity (FVIFA).

Example: Save $1,000 per year for 5 years at 10%. What is the total?
FVA = $1,000 x [((1.10)^5 - 1) / 0.10] = $1,000 x 6.1051 = $6,105.10
Note: You deposited $5,000 total but have $6,105.10 -- the extra $1,105.10 is compounded interest.

### Annuity Due Adjustment
An annuity due has each payment one period earlier, so each is worth one extra period of compounding:

**PV of Annuity Due = PVA(ordinary) x (1 + r)**
**FV of Annuity Due = FVA(ordinary) x (1 + r)**

Example: If the $1,000/year annuity above were an annuity due:
PV = $3,790.79 x 1.10 = $4,169.87

### Perpetuity Valuation
A perpetuity pays PMT forever. Its present value:
**PV = PMT / r**

Example: An investment pays $100/year forever. At a 5% discount rate:
PV = $100 / 0.05 = $2,000

### Growing Perpetuity
If payments grow at rate g forever (and r > g):
**PV = PMT_1 / (r - g)**

Where PMT_1 is the first payment (received one period from now).

Example: A stock pays a $2 dividend next year, growing 3% annually. Required return is 10%.
PV = $2 / (0.10 - 0.03) = $2 / 0.07 = $28.57

### Growing Annuity
**PV = PMT_1 x [1 - ((1+g)/(1+r))^n] / (r - g)**

Example: You expect salary of $50,000 next year, growing 4%/year for 30 years. At 8%:
PV = $50,000 x [1 - ((1.04)/(1.08))^30] / (0.08 - 0.04) = approximately $680,000

### Loan Amortization
Given a loan of PV, rate r, and n periods, the periodic payment is:
**PMT = PV x [r / (1 - (1 + r)^(-n))]**

Each payment: Interest portion = remaining balance x r; Principal portion = PMT - interest; New balance = old balance - principal portion.

Example: $100,000 mortgage at 6% for 30 years (360 monthly payments):
Monthly rate = 0.06/12 = 0.005; n = 360
PMT = $100,000 x [0.005 / (1 - (1.005)^(-360))] = $599.55

In month 1: Interest = $100,000 x 0.005 = $500; Principal = $99.55; Balance = $99,900.45
Notice: early payments are almost entirely interest.

### Valuing Uneven Cash Flows
When cash flows differ each period, find the PV of each individual cash flow and sum them:
**PV = CF_1/(1+r)^1 + CF_2/(1+r)^2 + ... + CF_n/(1+r)^n**

Example: Year 1: $100, Year 2: $200, Year 3: $300 at 8%.
PV = 100/1.08 + 200/1.08^2 + 300/1.08^3 = 92.59 + 171.47 + 238.15 = $502.21

## Examples

### Example 1: Car Loan Payment
You borrow $25,000 for a car at 4.8% APR for 5 years (60 monthly payments).
Monthly rate = 0.048/12 = 0.004; n = 60
PMT = $25,000 x [0.004 / (1 - (1.004)^(-60))] = $469.72/month
Total paid = $469.72 x 60 = $28,183.20; Total interest = $3,183.20

### Example 2: Retirement Savings
You want $1,000,000 at age 65. You are 25 and will save annually at 9%.
FVA = PMT x [((1.09)^40 - 1) / 0.09] = $1,000,000
PMT = $1,000,000 / 337.882 = $2,959.67/year
Starting 10 years later (age 35, 30 years): PMT = $1,000,000 / 136.308 = $7,336.35/year
Waiting 10 years more than doubles the required annual savings.

### Example 3: Lottery Winnings
You win $1,000,000 paid as $50,000/year for 20 years. At a 7% discount rate:
PV = $50,000 x [(1 - (1.07)^(-20)) / 0.07] = $50,000 x 10.594 = $529,701
The "million dollar" prize is really worth about $530,000 in today's dollars.

## Relationships
- Ordinary Annuity vs Annuity Due: Annuity due = Ordinary annuity x (1 + r) for both PV and FV
- Perpetuity is a special case of annuity where n -> infinity
- Growing perpetuity -> Used in stock valuation (Gordon Growth Model)
- Amortization -> Applies annuity PV formula in reverse to find payments
- Uneven cash flows -> Foundation for NPV in capital budgeting (Ch. 7)
- Bond valuation = PV of coupon annuity + PV of face value lump sum (Ch. 5)

## Common Misconceptions
- **Confusing ordinary annuity and annuity due**: Always check whether payments happen at the end (ordinary) or beginning (annuity due) of each period. Most financial calculators and formulas default to ordinary annuity.
- **Forgetting to match payment frequency to rate and periods**: A monthly payment loan needs a monthly rate and number of months, not annual rate and years.
- **Thinking more payments always means more total cost**: More frequent payments on a loan can reduce total interest by paying down principal faster (e.g., biweekly mortgage payments).
- **Assuming perpetuity formula works when g >= r**: The growing perpetuity PV = C/(r-g) is only valid when r > g. If g >= r, the series diverges to infinity.
- **Misreading amortization schedules**: Early payments are mostly interest; later payments are mostly principal. People underestimate how little principal they pay in early years of a mortgage.

## Practice Angles
- Calculate PV and FV of ordinary annuities at various rates
- Convert between ordinary annuity and annuity due
- Build a loan amortization schedule for the first 5 payments
- Compare total interest paid on 15-year vs 30-year mortgages
- Value a perpetuity and a growing perpetuity
- Find the payment needed to reach a retirement savings goal
- Value a series of uneven cash flows
