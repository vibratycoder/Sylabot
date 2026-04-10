---
chapter: 5
title: Bond Valuation
subject: finance
course: financial-management
prefix: FIN
code: "201"
keywords: [bond, coupon, yield to maturity, par value, face value, premium bond, discount bond, current yield, interest rate risk, duration, credit risk, bond rating, zero-coupon bond, callable bond]
prereqs: [ch01, ch02]
---

# Bond Valuation

## Overview
A bond is a long-term debt instrument where the issuer (borrower) promises to pay periodic interest (coupons) and return the face value at maturity. Bond valuation applies time-value-of-money principles directly: the price of a bond equals the present value of all its future cash flows (coupons plus face value), discounted at the market's required rate of return (yield to maturity). Understanding bond valuation is essential for corporate finance (firms issue bonds to raise capital) and investments (bonds are a major asset class).

Bond prices move inversely with interest rates. When market rates rise, existing bond prices fall, and vice versa. This interest rate risk is the primary risk for investment-grade bonds.

## Key Terms
- **Bond**: A long-term debt security where the issuer promises to make periodic interest payments and repay the principal (face value) at maturity.
- **Coupon Rate**: The annual interest payment as a percentage of face value. A $1,000 bond with a 6% coupon pays $60/year.
- **Coupon Payment**: The dollar amount of interest paid each period. If semi-annual: Annual coupon / 2.
- **Face Value (Par Value)**: The amount the bond issuer repays at maturity, typically $1,000 for corporate bonds.
- **Maturity Date**: The date on which the bond's principal is repaid and the bond ceases to exist.
- **Yield to Maturity (YTM)**: The total annual return anticipated on a bond if held until maturity, accounting for coupon payments, face value, current price, and time to maturity. YTM is the discount rate that makes the PV of all future cash flows equal to the bond's current price.
- **Current Yield**: Annual coupon payment / Current bond price. A quick measure that ignores capital gains/losses.
- **Premium Bond**: A bond trading above par value (price > $1,000). Occurs when coupon rate > YTM.
- **Discount Bond**: A bond trading below par value (price < $1,000). Occurs when coupon rate < YTM.
- **Par Bond**: A bond trading at exactly face value. Occurs when coupon rate = YTM.
- **Zero-Coupon Bond**: A bond that makes no coupon payments. It is sold at a deep discount and matures at face value. Return comes entirely from price appreciation.
- **Interest Rate Risk**: The risk that bond prices will fall when market interest rates rise. Longer-maturity bonds have greater interest rate risk.
- **Reinvestment Risk**: The risk that coupon payments will be reinvested at a lower rate when interest rates fall.
- **Credit Risk (Default Risk)**: The risk that the issuer will fail to make promised payments. Measured by bond ratings (Moody's, S&P, Fitch).
- **Duration**: A measure of a bond's sensitivity to interest rate changes. Weighted average time to receive the bond's cash flows. Higher duration = more interest rate sensitivity.
- **Callable Bond**: A bond the issuer can redeem before maturity at a specified call price. Issuers call bonds when rates fall to refinance at lower rates.
- **Yield Curve**: A graph plotting YTM against maturity for bonds of similar credit quality. Normally upward-sloping (longer maturity = higher yield).
- **Indenture**: The legal contract between the bond issuer and bondholders specifying all terms.

## Core Concepts

### Bond Valuation Formula
The price of a bond equals the PV of its coupon annuity plus the PV of its face value:

**Bond Price = C x [(1 - (1+r)^(-n)) / r] + FV / (1+r)^n**

Where: C = periodic coupon payment, r = periodic yield (YTM / periods per year), n = total number of periods, FV = face value.

Example: $1,000 face value, 8% annual coupon, 10 years to maturity, YTM = 10%.
Price = $80 x [(1 - (1.10)^(-10)) / 0.10] + $1,000 / (1.10)^10
Price = $80 x 6.1446 + $1,000 x 0.3855
Price = $491.57 + $385.54 = $877.11 (discount bond, because coupon rate 8% < YTM 10%)

### Semi-Annual Bonds
Most bonds pay coupons semi-annually. Adjust:
- Divide annual coupon by 2
- Divide YTM by 2
- Multiply years to maturity by 2

Example: Same bond with semi-annual payments:
C = $40, r = 5%, n = 20
Price = $40 x [(1 - (1.05)^(-20)) / 0.05] + $1,000 / (1.05)^20
Price = $40 x 12.4622 + $1,000 x 0.3769 = $498.49 + $376.89 = $875.38

### Price-Yield Relationship
- Bond prices and yields move inversely: as YTM rises, bond price falls.
- The relationship is convex (curved), not linear. Price decreases less for a rate increase than it increases for an equal rate decrease.
- At maturity, all bonds converge to face value (assuming no default).

### Interest Rate Risk and Duration
- Longer maturity = greater interest rate sensitivity
- Lower coupon rate = greater interest rate sensitivity (more of the bond's value comes from the distant face value payment)
- Duration quantifies this: a bond with duration of 7 years will lose approximately 7% of its value for a 1% increase in rates.

### Zero-Coupon Bond Valuation
No coupons; price = PV of face value only:
**Price = FV / (1 + r)^n**

Example: 10-year zero-coupon, YTM = 8%:
Price = $1,000 / (1.08)^10 = $463.19
Return = $1,000 - $463.19 = $536.81 capital gain. No reinvestment risk because there are no coupons.

### Bond Ratings
- Investment grade: AAA, AA, A, BBB (S&P) / Aaa, Aa, A, Baa (Moody's)
- Speculative (junk): BB/Ba and below
- Higher rating = lower default risk = lower yield = higher price
- The yield spread between corporate bonds and Treasuries reflects credit risk.

## Examples

### Example 1: Premium vs. Discount
Bond A: 10% coupon, 5 years, YTM = 8%. Price = $100 x 3.9927 + $1,000 x 0.6806 = $399.27 + $680.58 = $1,079.85 (premium: coupon > YTM)
Bond B: 6% coupon, 5 years, YTM = 8%. Price = $60 x 3.9927 + $1,000 x 0.6806 = $239.56 + $680.58 = $920.15 (discount: coupon < YTM)

### Example 2: Finding YTM
A bond has a $1,000 face value, 7% coupon (annual), 10 years to maturity, current price $925. What is YTM?
$925 = $70 x [(1 - (1+r)^(-10)) / r] + $1,000 / (1+r)^10
Solve by trial-and-error or financial calculator: YTM is approximately 8.2%.
Since price < par, YTM > coupon rate (as expected for a discount bond).

### Example 3: Interest Rate Impact
A 30-year, 5% coupon bond at par ($1,000 when YTM = 5%).
If YTM rises to 6%: Price = $50 x 13.7648 + $1,000 x 0.1741 = $688.24 + $174.11 = $862.35
A 1% rate increase caused a 13.8% price decline -- illustrating why long-term bonds are risky when rates rise.

## Relationships
- Bond valuation is a direct application of TVM (Ch. 1) and annuities (Ch. 2)
- Bond yields connect to the risk-free rate in CAPM (Ch. 4)
- Corporate bond issuance is a financing decision related to capital structure (Ch. 9)
- Bond yields determine the cost of debt component in cost of capital (Ch. 8)
- Duration and convexity are expanded in FIN 458 (Debt Securities, Derivatives)
- Credit ratings connect to financial statement analysis (Ch. 3) -- stronger firms get higher ratings

## Common Misconceptions
- **Coupon rate and yield to maturity are the same**: They are only equal when the bond trades at par. Discount bonds have YTM > coupon rate; premium bonds have YTM < coupon rate.
- **Bond prices can't go above face value**: They absolutely can. When coupon rate > YTM, investors pay a premium because the bond's coupon payments exceed what the market requires.
- **Zero-coupon bonds have no risk**: They actually have the highest interest rate risk among bonds of the same maturity because their entire return comes from the distant face value payment.
- **YTM assumes you sell at maturity price**: YTM assumes you hold to maturity AND reinvest all coupons at the YTM rate. If reinvestment rates differ, actual return will differ from YTM.
- **Higher-rated bonds are always better investments**: Higher-rated bonds have lower yields. If you correctly identify bonds whose credit will improve, lower-rated bonds can outperform.

## Practice Angles
- Calculate bond prices for annual and semi-annual coupon bonds
- Determine whether a bond trades at premium, discount, or par
- Calculate current yield and compare to YTM
- Find YTM using trial-and-error given price, coupon, and maturity
- Calculate zero-coupon bond prices
- Explain how and why bond prices change when interest rates move
- Compare interest rate sensitivity of bonds with different maturities and coupon rates
