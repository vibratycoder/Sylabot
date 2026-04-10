---
chapter: 11
title: Derivatives and Options Basics
subject: finance
course: financial-management
prefix: FIN
code: "201"
keywords: [derivative, option, call option, put option, strike price, exercise price, premium, expiration, futures, forward, hedge, speculation, intrinsic value, time value, payoff diagram, Black-Scholes, option pricing]
prereqs: [ch04, ch05]
---

# Derivatives and Options Basics

## Overview
A derivative is a financial instrument whose value depends on (is "derived from") the value of an underlying asset such as a stock, bond, commodity, or interest rate. The most common derivatives are options, futures, and forwards. Derivatives serve two primary purposes: hedging (reducing risk) and speculation (betting on price movements).

Options give the holder the right, but not the obligation, to buy or sell an asset at a predetermined price by a certain date. This asymmetric payoff structure makes options uniquely powerful tools for managing risk and creating investment strategies. FIN 201 introduces the basics; advanced treatment is covered in FIN 458.

## Key Terms
- **Derivative**: A financial contract whose value depends on the price of an underlying asset. Major types: options, futures, forwards, swaps.
- **Call Option**: Gives the holder the right (not obligation) to BUY an asset at the strike price before or on the expiration date. You buy a call when you think the price will rise.
- **Put Option**: Gives the holder the right (not obligation) to SELL an asset at the strike price before or on the expiration date. You buy a put when you think the price will fall.
- **Strike Price (Exercise Price)**: The predetermined price at which the option holder can buy (call) or sell (put) the underlying asset.
- **Premium**: The price paid by the option buyer to the option seller (writer) for the option contract. This is the maximum the buyer can lose.
- **Expiration Date**: The last date the option can be exercised. After this date, the option is worthless.
- **American Option**: Can be exercised at any time up to and including the expiration date. Most stock options in the U.S. are American.
- **European Option**: Can only be exercised on the expiration date. Easier to value theoretically.
- **In-the-Money (ITM)**: A call is ITM when stock price > strike price. A put is ITM when stock price < strike price. The option has positive intrinsic value.
- **Out-of-the-Money (OTM)**: A call is OTM when stock price < strike. A put is OTM when stock price > strike. No intrinsic value.
- **At-the-Money (ATM)**: Stock price equals the strike price.
- **Intrinsic Value**: The value if exercised immediately. Call: max(0, S - X). Put: max(0, X - S). Where S = stock price, X = strike price.
- **Time Value**: Option premium - intrinsic value. Reflects the probability that the option will become more valuable before expiration. Time value declines as expiration approaches (time decay).
- **Option Writer (Seller)**: The party who sells the option and receives the premium. Has an obligation (not a right) to fulfill the contract if exercised.
- **Futures Contract**: A standardized agreement to buy or sell an asset at a set price on a specific future date. Both buyer and seller are obligated. Traded on exchanges.
- **Forward Contract**: Similar to futures but customized and traded over-the-counter (OTC). No daily settlement.
- **Hedging**: Using derivatives to reduce or eliminate risk from adverse price movements. Example: a farmer uses futures to lock in a crop price.
- **Speculation**: Using derivatives to profit from expected price movements. Higher risk/reward than hedging.
- **Swap**: An agreement to exchange cash flows between two parties. Most common: interest rate swaps (fixed for floating).

## Core Concepts

### Call Option Payoff
**Payoff at expiration (to buyer) = max(0, S_T - X) - Premium**

If S_T > X: exercise the option, profit = S_T - X - Premium
If S_T <= X: option expires worthless, loss = Premium

Maximum loss = Premium paid (limited)
Maximum gain = Unlimited (stock can rise without limit)

Example: Buy a call on stock XYZ. Strike = $50, Premium = $3, Stock at expiration = $60.
Payoff = max(0, 60-50) - 3 = $10 - $3 = $7 profit per share.
If stock = $45: Payoff = max(0, 45-50) - 3 = 0 - $3 = -$3 loss (the premium).

### Put Option Payoff
**Payoff at expiration (to buyer) = max(0, X - S_T) - Premium**

If S_T < X: exercise the option, profit = X - S_T - Premium
If S_T >= X: option expires worthless, loss = Premium

Maximum loss = Premium paid (limited)
Maximum gain = X - Premium (stock can fall to zero)

Example: Buy a put on stock XYZ. Strike = $50, Premium = $4, Stock at expiration = $40.
Payoff = max(0, 50-40) - 4 = $10 - $4 = $6 profit per share.

### Factors Affecting Option Value
Five key factors (Black-Scholes inputs):
1. **Stock price (S)**: Higher S -> higher call value, lower put value
2. **Strike price (X)**: Higher X -> lower call value, higher put value
3. **Time to expiration (T)**: More time -> higher value for both calls and puts
4. **Volatility (sigma)**: Higher volatility -> higher value for both (more chance of large moves)
5. **Risk-free rate (r)**: Higher rate -> slightly higher call value, slightly lower put value

### Put-Call Parity
For European options on non-dividend-paying stocks:
**C + PV(X) = P + S**

Where C = call premium, P = put premium, PV(X) = present value of strike price, S = current stock price.

This relationship must hold; otherwise, arbitrage opportunities exist.

### Hedging with Options
**Protective Put**: Buy stock + buy put. Limits downside loss while preserving upside. The put acts as insurance.
Cost = stock price + put premium. Max loss = stock price - strike + put premium.

**Covered Call**: Own stock + sell call. Generates income (premium) but caps upside.
Useful when you expect the stock to stay flat or rise slightly.

### Futures and Forwards
- **Long position**: Agrees to BUY at the futures price. Profits when price rises.
- **Short position**: Agrees to SELL at the futures price. Profits when price falls.
- **Marking to market**: Futures positions are settled daily. Gains/losses are credited/debited each day.

Example hedge: A wheat farmer expects to harvest 10,000 bushels in 3 months. Current futures price = $5/bushel. By selling futures, the farmer locks in $50,000 revenue regardless of price movements.

## Examples

### Example 1: Speculating with Calls
You believe Company ABC (currently $45) will rise. You buy a call with strike $50 for $2.
If ABC rises to $58: Profit = (58-50) - 2 = $6/share = 300% return on $2 investment.
If ABC stays at $45: Loss = $2/share = 100% of investment.
Leverage: A 29% stock move produced a 300% option return (or a 100% loss).

### Example 2: Protective Put
You own 100 shares of XYZ at $80. You buy a put with strike $75 for $3.
If stock falls to $60: Exercise put, sell at $75. Loss = (80-75) + 3 = $8/share instead of $20.
If stock rises to $100: Let put expire. Gain = (100-80) - 3 = $17/share.
The put limits your maximum loss to $8/share regardless of how far the stock falls.

### Example 3: Option Value Components
Stock = $52, Call strike = $50, Call premium = $5.
Intrinsic value = max(0, 52-50) = $2
Time value = $5 - $2 = $3
The $3 reflects the probability of further favorable movement before expiration.

## Relationships
- Options pricing connects to stock valuation (Ch. 6) and risk concepts (Ch. 4)
- Put-call parity is an application of the no-arbitrage principle
- Hedging with derivatives connects to risk management (FIN 381)
- Real options in capital budgeting use option pricing concepts (FIN 460)
- Detailed derivatives coverage in FIN 458 (Debt Securities, Derivatives)
- Financial modeling of options in FIN 380

## Common Misconceptions
- **Options are always risky**: Options can reduce risk (hedging) or increase risk (speculation). It depends on how they are used. A protective put reduces portfolio risk.
- **You must exercise an option to profit**: You can sell the option in the market before expiration. Most options are traded rather than exercised.
- **Selling (writing) options is like buying options**: Sellers have opposite payoffs. A call writer has unlimited loss potential; a call buyer has limited loss. The risk profiles are fundamentally different.
- **Options are a zero-sum game only between buyer and seller**: While the option contract itself is zero-sum, hedging can create value by allowing firms to take on more profitable projects with reduced risk.
- **Higher stock price always means higher option value**: True for calls but false for puts. A higher stock price increases call value but decreases put value.

## Practice Angles
- Calculate call and put payoffs at expiration for various stock prices
- Draw payoff diagrams for long call, long put, short call, short put
- Determine if an option is ITM, ATM, or OTM
- Decompose an option premium into intrinsic value and time value
- Apply put-call parity to find a missing option price
- Describe how a protective put or covered call works
- Explain the effect of each factor (S, X, T, sigma, r) on option value
