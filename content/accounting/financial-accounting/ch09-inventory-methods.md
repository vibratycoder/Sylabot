---
chapter: 9
title: Inventory Methods
subject: accounting
course: financial-accounting
prefix: ACG
code: "203"
keywords: [inventory, FIFO, LIFO, weighted average, specific identification, periodic system, perpetual system, cost of goods sold, lower of cost or market, inventory turnover, gross profit method, retail method]
prereqs: [ch03, ch04, ch06]
---

# Inventory Methods

## Overview
Inventory is one of the most significant assets for merchandising and manufacturing companies. When identical items are purchased at different costs throughout the period, the company must choose a cost flow assumption to determine which costs go to Cost of Goods Sold (expense) and which remain in Ending Inventory (asset). The three main methods -- FIFO, LIFO, and Weighted Average -- produce different COGS and inventory values, affecting both the income statement and balance sheet.

The choice of inventory method is important because it directly impacts reported net income, taxable income, and the value of inventory on the balance sheet. Under the lower of cost or market (LCM) rule, inventory must be written down if its market value falls below its cost, reflecting the conservatism principle.

## Key Terms
- **Inventory**: Goods held for sale in the ordinary course of business. For merchandisers, this is finished goods. For manufacturers: raw materials, work-in-process, and finished goods.
- **Cost of Goods Sold (COGS)**: The cost of inventory that was sold during the period. COGS = Beginning Inventory + Purchases - Ending Inventory.
- **Cost of Goods Available for Sale**: Beginning Inventory + Purchases (or + Cost of Goods Manufactured). This total is split between COGS and Ending Inventory.
- **FIFO (First-In, First-Out)**: Assumes the oldest inventory items are sold first. Ending inventory reflects the most recent purchase costs. During rising prices, FIFO gives the lowest COGS, highest net income, and highest ending inventory.
- **LIFO (Last-In, First-Out)**: Assumes the newest inventory items are sold first. Ending inventory reflects the oldest purchase costs. During rising prices, LIFO gives the highest COGS, lowest net income (and thus lowest taxes), and lowest ending inventory. Allowed under GAAP but NOT under IFRS.
- **Weighted Average Cost**: Each unit is assigned the average cost of all units available for sale. Weighted Average Cost per Unit = Cost of Goods Available for Sale / Units Available for Sale.
- **Specific Identification**: Each item is individually tracked and its actual cost is assigned to COGS when sold. Used for unique, high-value items (cars, jewelry, art).
- **Periodic Inventory System**: Inventory and COGS are calculated at the end of the period using a physical count. Purchases are recorded in a Purchases account, not directly in Inventory.
- **Perpetual Inventory System**: Inventory records are updated continuously with each purchase and sale. Provides a running balance of inventory on hand.
- **Lower of Cost or Market (LCM)**: Inventory is reported at the lower of its original cost or current market (replacement) value. If market < cost, inventory is written down and a loss is recognized. Reflects conservatism.
- **Lower of Cost or Net Realizable Value (LCNRV)**: Under current GAAP (ASC 330) for non-LIFO methods, inventory is reported at the lower of cost or net realizable value (estimated selling price minus costs to complete and sell).
- **LIFO Reserve**: The difference between inventory valued at FIFO and LIFO. Companies using LIFO must disclose the LIFO reserve so users can compare.
- **LIFO Liquidation**: When a company sells more units than it buys, dipping into old, low-cost LIFO layers. This inflates profits artificially because very old (low) costs are matched against current revenues.
- **Inventory Turnover**: COGS / Average Inventory. Measures how quickly inventory is sold. Higher turnover generally indicates better management.
- **Days in Inventory**: 365 / Inventory Turnover. Average number of days to sell inventory.

## Core Concepts

### COGS Formula
**COGS = Beginning Inventory + Net Purchases - Ending Inventory**

Equivalently: Beginning Inventory + Net Purchases = Cost of Goods Available for Sale
COGAS = COGS + Ending Inventory (these two always sum to the same total)

### Comparison Under Rising Prices
Given the same transactions, different methods produce different results:

| Method | COGS | Net Income | Ending Inventory | Taxes |
|---|---|---|---|---|
| FIFO | Lowest | Highest | Highest | Highest |
| LIFO | Highest | Lowest | Lowest | Lowest |
| Weighted Avg | Middle | Middle | Middle | Middle |

Under falling prices, the effects reverse.

### Detailed Example
Beginning Inventory: 100 units @ $10 = $1,000
Purchase 1: 150 units @ $12 = $1,800
Purchase 2: 200 units @ $14 = $2,800
Total: 450 units, COGAS = $5,600
Units sold: 300; Units remaining: 150

**FIFO** (first purchased are first sold):
COGS = (100 x $10) + (150 x $12) + (50 x $14) = $1,000 + $1,800 + $700 = $3,500
Ending Inventory = 150 x $14 = $2,100

**LIFO** (last purchased are first sold):
COGS = (200 x $14) + (100 x $12) = $2,800 + $1,200 = $4,000
Ending Inventory = (100 x $10) + (50 x $12) = $1,000 + $600 = $1,600

**Weighted Average**:
Average cost = $5,600 / 450 = $12.44 per unit
COGS = 300 x $12.44 = $3,733
Ending Inventory = 150 x $12.44 = $1,867

Check: COGS + Ending Inventory = COGAS ($5,600) for all methods.

### Lower of Cost or Market
If replacement cost of inventory drops below original cost, write it down:
Example: Inventory cost $2,100 (FIFO). Market value drops to $1,800.
Journal entry: Dr. Loss on Inventory Write-Down $300 / Cr. Inventory $300
Report inventory at $1,800 on the balance sheet. The $300 loss appears on the income statement.

### Tax Implications of LIFO
LIFO produces lower taxable income in periods of rising prices, resulting in real tax savings. The IRS LIFO conformity rule requires that companies using LIFO for tax purposes must also use it for financial reporting.

## Examples

### Example 1: Impact on Financial Ratios
Using the example above (rising prices):
FIFO: Gross profit = Revenue - $3,500; Current ratio higher (larger inventory asset)
LIFO: Gross profit = Revenue - $4,000; Current ratio lower (smaller inventory asset)
Analysts must adjust when comparing firms using different inventory methods.

### Example 2: LIFO Liquidation
A company using LIFO has old layers at $5/unit. Current cost is $15/unit. If the company sells from old layers:
COGS per unit = $5 (old cost) instead of $15 (current cost)
This makes profits look artificially high. Analysts watch for LIFO liquidations.

## Relationships
- Inventory method affects COGS on the income statement (Ch. 3) and inventory on the balance sheet (Ch. 4)
- The choice of method is governed by GAAP principles (Ch. 6), especially consistency and conservatism
- LCM rule enforces conservatism
- Inventory turnover is a key efficiency ratio in financial analysis (FIN 201 Ch. 3)
- LIFO vs. FIFO affects cash flow through tax savings (Ch. 5)
- Inventory connects to cost accounting in managerial accounting (ACG 204, ACG 311)

## Common Misconceptions
- **FIFO, LIFO, and weighted average track physical movement of goods**: These are COST FLOW assumptions, not physical flow. A company can use LIFO accounting even if it physically ships the oldest goods first.
- **LIFO always produces lower net income**: Only when prices are rising. If prices are falling, LIFO produces higher net income than FIFO.
- **Companies can switch methods freely**: GAAP requires consistency. Changing methods requires justification and disclosure, and the cumulative effect must be reported.
- **Weighted average gives the same result as the midpoint of FIFO and LIFO**: Not necessarily. The weighted average depends on the specific quantities and costs at each purchase.
- **LIFO is allowed everywhere**: LIFO is permitted under U.S. GAAP but prohibited under IFRS. International companies cannot use LIFO.

## Practice Angles
- Calculate COGS and ending inventory under FIFO, LIFO, and weighted average
- Determine which method produces the highest/lowest net income given price trends
- Apply the lower of cost or market rule
- Analyze the impact of inventory method choice on financial statements and ratios
- Calculate inventory turnover and days in inventory
- Explain the tax advantages of LIFO in an inflationary environment
- Convert between LIFO and FIFO using the LIFO reserve
