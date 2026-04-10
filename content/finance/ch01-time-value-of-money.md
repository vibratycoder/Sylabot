---
chapter: 1
title: Time Value of Money
subject: finance
course: financial-management
prefix: FIN
code: "201"
keywords: [time value of money, present value, future value, discount rate, compounding, annuity, perpetuity, NPV, interest rate]
prereqs: []
---

# Time Value of Money

## Overview
The time value of money (TVM) is the foundational concept in finance: a dollar today is worth more than a dollar tomorrow because today's dollar can be invested to earn interest. TVM underlies all financial decisions -- loans, investments, retirement planning, business valuation. Present value (PV) converts future cash flows to today's value; future value (FV) projects today's money forward. Mastering TVM formulas is essential for every finance course.

## Key Terms
- **Time Value of Money (TVM)**: The principle that money available now is worth more than the same amount in the future due to its earning potential.
- **Future Value (FV)**: The value of a current sum at a future date. FV = PV x (1 + r)^n.
- **Present Value (PV)**: The current value of a future sum. PV = FV / (1 + r)^n.
- **Discount Rate (r)**: The interest rate used to calculate present value. Reflects the opportunity cost of capital, risk, and inflation.
- **Compounding**: Earning interest on interest. More frequent compounding -> higher effective return.
- **Compound Interest**: Interest calculated on both the initial principal and accumulated interest. Contrast with simple interest (on principal only).
- **Annuity**: A series of equal payments at regular intervals. Ordinary annuity: payments at end of period. Annuity due: payments at beginning.
- **Perpetuity**: An annuity that continues forever. PV = Payment / r.
- **Net Present Value (NPV)**: The sum of present values of all cash flows (including initial investment). NPV > 0 means the investment creates value.
- **Internal Rate of Return (IRR)**: The discount rate that makes NPV = 0. The investment's implied return.
- **Rule of 72**: Approximate doubling time = 72 / interest rate (%).
- **Effective Annual Rate (EAR)**: The actual annual rate after accounting for compounding frequency. EAR = (1 + r/n)^n - 1.

## Core Concepts

### Future Value and Compounding
FV = PV x (1 + r)^n. $1,000 at 8% for 10 years: FV = $1,000 x (1.08)^10 = $2,159. The power of compounding: after 30 years, it becomes $10,063. Einstein allegedly called compound interest the "eighth wonder of the world."

### Present Value and Discounting
PV = FV / (1 + r)^n. If you'll receive $10,000 in 5 years and the discount rate is 6%: PV = $10,000 / (1.06)^5 = $7,473. This means $7,473 today is equivalent to $10,000 in 5 years at 6%.

### Annuity Formulas
PV of annuity = PMT x [(1 - (1+r)^-n) / r]. FV of annuity = PMT x [((1+r)^n - 1) / r]. These are used for loan payments, retirement savings, and bond valuation.

### NPV Decision Rule
Calculate NPV of all cash flows. If NPV > 0, accept the investment (it creates value). If NPV < 0, reject. If NPV = 0, indifferent. NPV is the gold standard for investment decisions because it accounts for the time value of money, risk, and all cash flows.

## Examples

### Student Loans
You borrow $40,000 at 5% for 10 years. Monthly payment = $40,000 x [0.004167 / (1 - 1.004167^-120)] = $424.26/month. Total paid: $50,911. Interest paid: $10,911.

### Retirement Planning
Save $500/month for 40 years at 7% annual return. FV of annuity = $500 x [((1.005833)^480 - 1) / 0.005833] = ~$1,197,811. Starting 10 years later (30 years): only ~$566,765. The 10-year delay costs over $600,000 due to compounding.

### Investment Decision
A project costs $100,000 and generates $30,000/year for 5 years. At 10% discount rate: NPV = -$100,000 + $30,000/1.1 + $30,000/1.21 + $30,000/1.331 + $30,000/1.4641 + $30,000/1.6105 = $13,724. NPV > 0, so accept.

## Relationships
- Higher discount rate -> Lower present value
- More compounding periods -> Higher effective rate
- Longer time horizon -> More powerful compounding effect
- NPV > 0 -> Investment creates value -> Accept
- IRR > required return -> Accept (equivalent to NPV > 0 for conventional cash flows)

## Common Misconceptions
- **"A high interest rate is always bad"**: High rates are bad for borrowers but good for savers/investors. Context matters.
- **"Simple interest and compound interest are similar"**: Over long periods, compound interest generates dramatically more. $1,000 at 10% simple for 30 years = $4,000. Compound = $17,449.
- **"NPV and IRR always agree"**: For mutually exclusive projects or non-conventional cash flows, NPV and IRR can give conflicting rankings. Always defer to NPV.
- **"You can add cash flows from different time periods"**: Never. Cash flows must be converted to the same point in time (usually present value) before comparing or summing.

## Practice Angles
- Calculate: future value of a lump sum with annual and monthly compounding
- Calculate: present value of an annuity (e.g., loan payment calculation)
- Compare: two investments using NPV at different discount rates
- Explain with example: why starting retirement savings early matters (compounding)
- Apply: use the perpetuity formula to value a stock with constant dividends
