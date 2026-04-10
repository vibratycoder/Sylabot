---
chapter: 3
title: Cost Accounting Fundamentals
subject: accounting
course: managerial-accounting
prefix: ACG
code: "204"
keywords: [job-order costing, process costing, direct materials, direct labor, manufacturing overhead, cost object, cost driver, predetermined overhead rate, applied overhead, over-applied, under-applied, product costs, period costs, prime costs, conversion costs, cost of goods manufactured]
prereqs: [ch01]
---

# Cost Accounting Fundamentals

## Overview
Cost accounting determines the cost of producing a product or providing a service. This information is used for pricing, profitability analysis, inventory valuation, and decision-making. Costs are classified as product costs (inventoriable) or period costs (expensed immediately). Product costs include direct materials, direct labor, and manufacturing overhead.

The two primary costing systems are job-order costing (for custom or distinct products/services) and process costing (for mass-produced identical products). Both systems accumulate costs and assign them to cost objects, but they differ in how costs are tracked and averaged.

## Key Terms
- **Cost Object**: Anything for which a separate measurement of cost is desired -- a product, service, department, project, or customer.
- **Direct Materials**: Raw materials that become an integral part of the finished product and can be physically and conveniently traced to it. Example: lumber in a table, steel in a car.
- **Direct Labor**: Labor costs of workers who directly work on converting materials into finished products. Can be physically traced to specific products.
- **Manufacturing Overhead (MOH)**: All manufacturing costs that are NOT direct materials or direct labor. Includes indirect materials, indirect labor, factory rent, utilities, depreciation on factory equipment, and factory insurance. Also called factory overhead or burden.
- **Product Costs (Inventoriable Costs)**: Costs that attach to units of product: DM + DL + MOH. They are assets (inventory) until the product is sold, then they become COGS.
- **Period Costs**: Costs that are expensed in the period incurred, not attached to products. Include selling expenses and administrative expenses.
- **Prime Costs**: Direct Materials + Direct Labor. The costs directly traceable to the product.
- **Conversion Costs**: Direct Labor + Manufacturing Overhead. The costs of converting raw materials into finished products.
- **Predetermined Overhead Rate (POHR)**: Estimated MOH / Estimated Activity Base (e.g., direct labor hours, machine hours). Used to apply overhead to products throughout the year.
- **Applied Overhead**: The overhead assigned to products using the POHR. Applied MOH = POHR x Actual Activity.
- **Over-Applied Overhead**: When applied overhead > actual overhead. The company applied too much to products.
- **Under-Applied Overhead**: When applied overhead < actual overhead. Products were under-costed.
- **Cost of Goods Manufactured (COGM)**: The total cost of goods completed during the period. COGM = DM Used + DL + MOH Applied + Beginning WIP - Ending WIP.
- **Work-in-Process (WIP)**: Partially completed products still on the factory floor.
- **Finished Goods**: Completed products waiting to be sold.
- **Job-Order Costing**: A system that assigns costs to specific jobs, batches, or orders. Used when products are distinct/customized (construction, consulting, custom manufacturing). Costs accumulate on a job cost sheet.
- **Process Costing**: A system that assigns costs to departments/processes and averages them over all identical units produced. Used for homogeneous mass production (chemicals, food, cement). Uses equivalent units to handle partially completed products.
- **Equivalent Units**: A measure of productive output that converts partially completed units into the equivalent number of fully completed units. Example: 1,000 units that are 60% complete = 600 equivalent units.
- **Job Cost Sheet**: A document that records all costs (DM, DL, MOH) assigned to a specific job.

## Core Concepts

### Product Cost Flow
```
Raw Materials Inventory -> Work-in-Process Inventory -> Finished Goods Inventory -> COGS
(DM used)                   (+DL, +MOH applied)         (when sold)
```

### Predetermined Overhead Rate
Because actual overhead is only known at year-end, companies estimate overhead at the beginning:
**POHR = Estimated Total MOH / Estimated Total Activity Base**

Example: Estimated MOH = $300,000. Estimated direct labor hours = 20,000.
POHR = $300,000 / 20,000 = $15 per DL hour.

If Job #101 uses 50 DL hours: Applied MOH = 50 x $15 = $750.

### Over/Under-Applied Overhead
At year-end, compare applied to actual:
- If Applied $310,000 > Actual $300,000: $10,000 over-applied (credit to COGS to reduce it)
- If Applied $290,000 < Actual $300,000: $10,000 under-applied (debit to COGS to increase it)

### Job-Order Costing Example
Job #205: Custom furniture order
- Direct materials requisitioned: $4,000
- Direct labor: 80 hours at $25/hour = $2,000
- MOH applied: 80 hours x $15/hour POHR = $1,200
- Total job cost: $4,000 + $2,000 + $1,200 = $7,200
- If 10 units: cost per unit = $720

### Process Costing: Equivalent Units
Department produced 8,000 completed units and has 2,000 units in ending WIP (40% complete for conversion).
Equivalent units for conversion = 8,000 + (2,000 x 0.40) = 8,800 equivalent units
If total conversion costs = $176,000:
Cost per equivalent unit = $176,000 / 8,800 = $20

### Cost of Goods Manufactured Schedule
```
Direct Materials Used
  Beginning Raw Materials         $10,000
  + Purchases                      50,000
  - Ending Raw Materials           (8,000)
  = DM Used                                   $52,000
Direct Labor                                   80,000
Manufacturing Overhead Applied                 60,000
Total Manufacturing Costs                     $192,000
+ Beginning WIP                                15,000
- Ending WIP                                  (12,000)
= Cost of Goods Manufactured                 $195,000
```

## Examples

### Example 1: Product vs Period Costs
Factory supervisor salary: Product cost (manufacturing overhead -- indirect labor)
Sales manager salary: Period cost (selling expense)
Glue used in production: Product cost (indirect material -- overhead, unless traceable)
Advertising: Period cost (selling expense)
Factory building depreciation: Product cost (manufacturing overhead)
Office building depreciation: Period cost (administrative expense)

### Example 2: Complete Job Cost
A printing company receives an order for 500 brochures.
DM: Paper $200, Ink $100 = $300
DL: 4 hours at $22/hour = $88
MOH: 4 hours x $18 POHR = $72
Total: $460. Per brochure: $0.92. Mark up 40%: sell for $1.29 each ($644 total).

## Relationships
- Product costs flow through inventory accounts on the balance sheet and to COGS on the income statement
- Cost classifications underpin CVP analysis (Ch. 1) and budgeting (Ch. 2)
- Manufacturing overhead application connects to variance analysis (Ch. 2)
- Job-order and process costing are extended in ACG 311 (Cost Management) and ACG 471
- COGS calculation directly affects the income statement and inventory valuation
- POHR uses estimated figures -- differences resolved at year-end through overhead variances

## Common Misconceptions
- **All factory costs are direct costs**: Only DM and DL are direct. Manufacturing overhead includes many indirect costs (factory rent, utilities, supervisor salaries) that cannot be traced to specific units.
- **Product costs are expenses**: Product costs are ASSETS (inventory) until the product is sold. Only then do they become expenses (COGS). This is a critical distinction.
- **POHR gives exact overhead per product**: It is an estimate. Over- or under-applied overhead results from the difference between estimated and actual overhead and activity.
- **Job-order and process costing give different total costs**: Both systems aim to compute the same total cost of production. They differ in HOW costs are accumulated (by job vs. by department) and averaged.
- **Equivalent units apply to direct materials the same way as conversion**: Direct materials are often added at the beginning of a process (100% complete), while conversion happens gradually. Equivalent units may differ for DM and conversion.

## Practice Angles
- Classify costs as direct materials, direct labor, MOH, or period costs
- Calculate the predetermined overhead rate
- Apply overhead to a job and calculate total job cost
- Calculate over-applied or under-applied overhead at year-end
- Prepare a cost of goods manufactured schedule
- Calculate equivalent units and cost per equivalent unit in process costing
- Distinguish product costs from period costs with examples
