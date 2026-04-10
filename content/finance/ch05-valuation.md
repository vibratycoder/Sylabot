---
chapter: 5
title: Bond and Stock Valuation
subject: finance
course: financial-management
prefix: FIN
code: "201"
keywords: [bond valuation, stock valuation, yield to maturity, coupon, par value, dividend discount model, P/E ratio, market capitalization, discount rate]
prereqs: [ch01, ch03]
---

# Bond and Stock Valuation

## Overview
Valuation is the process of determining what a financial asset is worth today. Bond value equals the present value of future coupon payments plus the present value of the par value at maturity. Stock value can be estimated using the dividend discount model (DDM), which discounts expected future dividends, or using multiples like the P/E ratio. Valuation connects TVM, risk-return theory, and real-world investing.

## Key Terms
- **Bond**: A debt instrument where the issuer promises to pay periodic interest (coupons) and return the principal (par value) at maturity.
- **Par Value (Face Value)**: The amount repaid at maturity, typically $1,000.
- **Coupon Rate**: The annual interest rate on the bond's par value. A 6% coupon on $1,000 par pays $60/year.
- **Yield to Maturity (YTM)**: The total return if the bond is held to maturity. The discount rate that equates the bond's price to the PV of its cash flows.
- **Premium Bond**: Sells above par (coupon rate > YTM). Investors pay extra for higher-than-market coupons.
- **Discount Bond**: Sells below par (coupon rate < YTM).
- **Stock (Equity)**: Ownership share in a company. Returns come from dividends and capital gains.
- **Dividend Discount Model (DDM)**: Stock price = PV of all future dividends. For constant growth: P = D1 / (r - g) (Gordon Growth Model).
- **Gordon Growth Model**: P = D1 / (r - g). Assumes dividends grow at a constant rate g forever. r = required return, D1 = next year's dividend.
- **Price-to-Earnings Ratio (P/E)**: Stock price / EPS. A relative valuation metric.
- **Market Capitalization**: Stock price x shares outstanding. Total market value of equity.
- **Dividend Yield**: Annual dividends per share / stock price.
- **Capital Gains Yield**: (P1 - P0) / P0. Price appreciation as a percentage.

## Core Concepts

### Bond Pricing
Bond price = PV of coupons (annuity) + PV of par value (lump sum). Price = C x [1-(1+r)^-n]/r + F/(1+r)^n. When market interest rates rise, bond prices fall (inverse relationship). Longer maturity = more price sensitivity to rate changes.

### Stock Pricing with DDM
If dividends grow at constant rate g: P0 = D1 / (r - g). Example: D1 = $2, r = 10%, g = 4%. P0 = $2 / (0.10 - 0.04) = $33.33. If actual price is $30, the stock is undervalued (buy). If $40, overvalued (sell).

### Interest Rate Risk
Bond prices move inversely to interest rates. A 1% rate increase reduces long-term bond prices much more than short-term bonds. This is duration risk -- longer duration = more sensitive.

## Examples

### Pricing a Corporate Bond
$1,000 par, 5% coupon (semiannual), 10 years to maturity, YTM = 6%. Semiannual coupon = $25, n = 20, r = 3%. Price = $25 x PVIFA(3%, 20) + $1,000 x PVIF(3%, 20) = $25(14.877) + $1,000(0.5537) = $371.93 + $553.68 = $925.61. Discount bond (coupon < YTM).

### Valuing a Stock
Apple pays a $0.96 dividend expected to grow 6%/year. Your required return is 9%. P = $0.96(1.06) / (0.09 - 0.06) = $1.018 / 0.03 = $33.92. (Simplified -- Apple's actual valuation involves more complex models.)

## Relationships
- Interest rates rise -> Bond prices fall
- Longer maturity -> Greater interest rate sensitivity
- Higher growth rate -> Higher stock price (DDM)
- Higher required return -> Lower stock price
- P/E ratio reflects market expectations of growth and risk

## Common Misconceptions
- **"Bonds are safe"**: Bonds have interest rate risk (price drops when rates rise), credit risk (default), and inflation risk. "Safe" is relative.
- **"A stock with no dividend is worthless"**: Growth stocks reinvest earnings. Value comes from expected future dividends or eventual liquidation. Price today reflects expected future payouts.
- **"Low P/E always means undervalued"**: Low P/E may reflect low growth expectations, high risk, or declining earnings. Context matters.

## Practice Angles
- Calculate: price of a bond given coupon rate, par value, maturity, and YTM
- Calculate: stock value using Gordon Growth Model
- Explain: the inverse relationship between interest rates and bond prices
- Compare: two stocks using P/E ratios -- which is more attractive?
- Analyze: what happens to a bond's price if the Fed raises interest rates by 1%?
