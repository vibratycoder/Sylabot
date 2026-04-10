---
chapter: 10
title: Working Capital Management
subject: finance
course: financial-management
prefix: FIN
code: "201"
keywords: [working capital, net working capital, cash conversion cycle, operating cycle, inventory management, accounts receivable, accounts payable, cash management, short-term financing, line of credit, commercial paper, trade credit, EOQ]
prereqs: [ch03, ch07]
---

# Working Capital Management

## Overview
Working capital management deals with the day-to-day financial operations of a firm: managing cash, inventory, accounts receivable, and accounts payable. While capital budgeting focuses on long-term investments, working capital management ensures the firm has enough liquidity to meet its short-term obligations while minimizing the cost of maintaining those liquid assets.

The cash conversion cycle measures how long it takes from paying for raw materials to collecting cash from customers. Shorter cycles free up cash; longer cycles tie up capital. Effective working capital management balances the tradeoff between liquidity (having enough cash on hand) and profitability (investing idle cash for returns).

## Key Terms
- **Working Capital**: Current assets -- the total investment in short-term assets (cash, receivables, inventory, prepaid expenses).
- **Net Working Capital (NWC)**: Current Assets - Current Liabilities. Measures the cushion of liquid assets above short-term obligations.
- **Cash Conversion Cycle (CCC)**: The time (in days) between paying for inventory and collecting cash from sales. CCC = Days Inventory Outstanding + Days Sales Outstanding - Days Payable Outstanding.
- **Operating Cycle**: The time from purchasing inventory to collecting cash from sales. Operating Cycle = DIO + DSO.
- **Days Inventory Outstanding (DIO)**: 365 / Inventory Turnover. Average days to sell inventory.
- **Days Sales Outstanding (DSO)**: 365 / Accounts Receivable Turnover. Average days to collect payment from customers.
- **Days Payable Outstanding (DPO)**: 365 / Accounts Payable Turnover. Average days to pay suppliers.
- **Trade Credit**: Short-term financing from suppliers (buying now, paying later). Terms like "2/10, net 30" mean a 2% discount if paid within 10 days, otherwise full payment due in 30 days.
- **Credit Terms**: The conditions under which a firm extends credit to customers, including the discount percentage, discount period, and net period.
- **Economic Order Quantity (EOQ)**: The optimal order size that minimizes total inventory costs (ordering + holding). EOQ = sqrt(2 x S x O / C), where S = annual demand, O = ordering cost per order, C = carrying cost per unit per year.
- **Safety Stock**: Extra inventory held to protect against stockouts due to demand variability or supply delays.
- **Line of Credit**: A pre-arranged borrowing limit with a bank that a firm can draw upon as needed for short-term financing.
- **Commercial Paper**: Short-term unsecured promissory notes issued by large, creditworthy firms to raise short-term funds, usually at rates below bank lending rates.
- **Factoring**: Selling accounts receivable to a third party (factor) at a discount for immediate cash.
- **Lockbox System**: A payment collection method where customers send payments to a P.O. box managed by a bank, reducing float and speeding cash collection.
- **Float**: The time between when a payment is initiated and when funds are available. Includes mail float, processing float, and clearing float.

## Core Concepts

### Cash Conversion Cycle
**CCC = DIO + DSO - DPO**

Example: DIO = 45 days, DSO = 30 days, DPO = 35 days.
CCC = 45 + 30 - 35 = 40 days
The firm must finance 40 days of operations from the time it pays suppliers to when it collects from customers.

Strategies to reduce CCC:
- Reduce DIO: faster inventory turnover (just-in-time, better demand forecasting)
- Reduce DSO: tighter credit policies, faster collection
- Increase DPO: negotiate longer payment terms (but maintain supplier relationships)

### Trade Credit Cost
If terms are "2/10, net 30" and you forgo the discount:
**Annualized cost = [Discount / (1 - Discount)] x [365 / (Net period - Discount period)]**
= [0.02 / 0.98] x [365 / 20] = 0.0204 x 18.25 = 37.2%

Forgoing a 2% discount to keep money 20 extra days costs 37.2% annually -- extremely expensive. Almost always cheaper to borrow from a bank and take the discount.

### Inventory Management
Total inventory cost = Ordering cost + Carrying cost
= (S/Q) x O + (Q/2) x C

Where Q = order quantity. EOQ minimizes total cost:
**EOQ = sqrt(2SO / C)**

Example: Annual demand S = 10,000 units, Ordering cost O = $50/order, Carrying cost C = $2/unit/year.
EOQ = sqrt(2 x 10,000 x 50 / 2) = sqrt(500,000) = 707 units
Number of orders per year = 10,000 / 707 = 14.1 orders

### Aggressive vs. Conservative Working Capital Policies
**Aggressive**: Minimize current assets, use more short-term (cheaper) financing. Higher profitability but higher risk of liquidity crisis.
**Conservative**: Maintain higher current assets, use more long-term financing. Lower profitability but greater liquidity safety.
**Moderate**: Balance between the two.

## Examples

### Example 1: CCC Impact
Company A: DIO=30, DSO=25, DPO=40. CCC = 15 days (very efficient).
Company B: DIO=60, DSO=45, DPO=30. CCC = 75 days (lots of cash tied up).
If Company B has $1M daily operating costs, it needs $75M in working capital financing vs. $15M for Company A.

### Example 2: EOQ Decision
A retailer sells 5,000 widgets/year. Ordering cost = $25/order. Holding cost = $4/widget/year.
EOQ = sqrt(2 x 5,000 x 25 / 4) = sqrt(62,500) = 250 widgets per order
Orders per year = 5,000 / 250 = 20 orders
Total cost = 20 x $25 + (250/2) x $4 = $500 + $500 = $1,000

## Relationships
- Working capital changes affect project cash flows in capital budgeting (Ch. 7)
- Liquidity ratios from financial analysis (Ch. 3) measure working capital adequacy
- Short-term financing connects to capital structure decisions (Ch. 9)
- Cash management relates to risk management and opportunity cost concepts
- Trade credit is the most common form of short-term financing

## Common Misconceptions
- **More working capital is always better**: Excess working capital means idle cash and bloated inventory, which reduce profitability. The goal is the right amount -- enough for operations but not wasteful.
- **The cash conversion cycle can't be negative**: It can. Companies like Amazon and Dell collect from customers before paying suppliers, creating a negative CCC -- effectively being financed by their suppliers.
- **Trade credit is free**: Only if you take the discount. Forgoing trade discounts is one of the most expensive forms of financing.
- **Working capital management is less important than capital budgeting**: Poor working capital management has caused many profitable firms to go bankrupt from cash flow shortfalls.

## Practice Angles
- Calculate the cash conversion cycle from financial statement data
- Determine the annualized cost of forgoing a trade discount
- Calculate EOQ and total inventory costs
- Compare aggressive vs. conservative working capital strategies
- Analyze how changes in DIO, DSO, or DPO affect the CCC and cash needs
- Evaluate short-term financing options (bank loan vs. commercial paper vs. trade credit)
