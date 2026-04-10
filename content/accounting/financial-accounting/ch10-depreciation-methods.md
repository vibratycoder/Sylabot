---
chapter: 10
title: Depreciation Methods
subject: accounting
course: financial-accounting
prefix: ACG
code: "203"
keywords: [depreciation, straight-line, declining balance, double declining balance, units of production, useful life, salvage value, residual value, accumulated depreciation, book value, asset disposal, impairment, amortization, depletion, MACRS]
prereqs: [ch04, ch06, ch07]
---

# Depreciation Methods

## Overview
Depreciation is the systematic allocation of the cost of a long-lived tangible asset (except land) over its useful life. It is NOT a valuation technique -- it does not measure the decline in market value. Rather, it applies the matching principle by spreading the cost of an asset over the periods that benefit from its use. The three primary methods are straight-line (equal expense each year), declining balance (accelerated -- more expense in early years), and units-of-production (based on actual usage).

The choice of depreciation method affects the pattern of expenses on the income statement, the book value of assets on the balance sheet, and the timing (but not the total amount) of tax deductions.

## Key Terms
- **Depreciation**: The systematic allocation of the cost of a tangible long-lived asset over its estimated useful life. Recognized as an expense each period.
- **Depreciable Base (Depreciable Cost)**: Cost - Salvage Value. The total amount to be depreciated over the asset's life.
- **Cost (Historical Cost)**: The purchase price plus all costs necessary to get the asset ready for use (shipping, installation, testing).
- **Salvage Value (Residual Value)**: The estimated amount the asset will be worth at the end of its useful life. May be zero.
- **Useful Life**: The estimated period over which the asset will provide economic benefits. Can be expressed in years or units of output.
- **Straight-Line Depreciation**: Allocates an equal amount of depreciation expense to each year of useful life. Most common method. Formula: (Cost - Salvage Value) / Useful Life.
- **Declining Balance Depreciation**: An accelerated method that applies a constant rate to the declining book value each year. Double-Declining Balance (DDB) uses twice the straight-line rate.
- **Double-Declining Balance (DDB)**: Rate = 2 / Useful Life. Annual depreciation = Rate x Beginning Book Value. Do not subtract salvage value in the calculation, but do not depreciate below salvage value.
- **Units-of-Production Depreciation**: Allocates cost based on actual usage or output. Depreciation per unit = (Cost - Salvage Value) / Total Estimated Units. Annual expense = Depreciation per unit x Actual units produced.
- **Accumulated Depreciation**: A contra-asset account that holds the total depreciation charged to date. Increases each period as depreciation expense is recorded.
- **Book Value (Net Book Value, Carrying Value)**: Cost - Accumulated Depreciation. The undepreciated portion of the asset's cost remaining on the balance sheet.
- **Impairment**: When an asset's book value exceeds its recoverable amount (fair value). The asset must be written down, and an impairment loss is recognized. Different from depreciation -- impairment is a one-time reduction.
- **Amortization**: The equivalent of depreciation for intangible assets (patents, copyrights). Usually straight-line over the useful or legal life.
- **Depletion**: The equivalent of depreciation for natural resources (oil, timber, minerals). Based on units extracted.
- **MACRS (Modified Accelerated Cost Recovery System)**: The depreciation system required for U.S. tax purposes. Uses prescribed recovery periods and accelerated rates. Not used for financial reporting (GAAP).
- **Half-Year Convention**: Under MACRS, assets are assumed to be placed in service at the midpoint of the year, so only half a year's depreciation is taken in the first and last years.

## Core Concepts

### Straight-Line Method
**Annual Depreciation = (Cost - Salvage Value) / Useful Life**

Example: Machine costs $50,000, salvage value $5,000, useful life 5 years.
Annual depreciation = ($50,000 - $5,000) / 5 = $9,000 per year

| Year | Depreciation | Accum. Depr. | Book Value |
|---|---|---|---|
| 0 | -- | -- | $50,000 |
| 1 | $9,000 | $9,000 | $41,000 |
| 2 | $9,000 | $18,000 | $32,000 |
| 3 | $9,000 | $27,000 | $23,000 |
| 4 | $9,000 | $36,000 | $14,000 |
| 5 | $9,000 | $45,000 | $5,000 |

Total depreciation = $45,000 = Depreciable base. Book value at end = Salvage value.

### Double-Declining Balance Method
**Rate = 2 / Useful Life**
**Annual Depreciation = Rate x Beginning Book Value**

Do NOT subtract salvage value in the rate calculation. But never depreciate below salvage value.

Example: Same machine ($50,000, $5,000 salvage, 5 years).
Rate = 2/5 = 40%

| Year | Beg. BV | Depr. (40%) | Accum. | End BV |
|---|---|---|---|---|
| 1 | $50,000 | $20,000 | $20,000 | $30,000 |
| 2 | $30,000 | $12,000 | $32,000 | $18,000 |
| 3 | $18,000 | $7,200 | $39,200 | $10,800 |
| 4 | $10,800 | $5,800* | $45,000 | $5,000 |
| 5 | $5,000 | $0 | $45,000 | $5,000 |

*Year 4: 40% x $10,800 = $4,320, but that would bring BV to $6,480. Instead, depreciate only $5,800 to reach salvage value of $5,000. Year 5: no more depreciation.

Note: DDB front-loads expense -- higher expense in early years, lower in later years.

### Units-of-Production Method
**Depreciation per Unit = (Cost - Salvage Value) / Total Estimated Units**
**Annual Depreciation = Depreciation per Unit x Actual Units**

Example: Machine produces an estimated 100,000 units over its life.
Rate = ($50,000 - $5,000) / 100,000 = $0.45 per unit
Year 1: 25,000 units produced. Depreciation = 25,000 x $0.45 = $11,250
Year 2: 30,000 units. Depreciation = 30,000 x $0.45 = $13,500

This method links expense directly to usage, which is appropriate for assets whose wear depends on output rather than time.

### Comparison of Methods
All three methods produce the same TOTAL depreciation ($45,000 in the example). They differ in TIMING:
- Straight-line: Equal each year. Best for assets used evenly over time.
- DDB: More early, less later. Best for assets that lose productivity quickly (technology, vehicles).
- Units-of-production: Varies with usage. Best for assets whose useful life depends on output (machinery, vehicles by miles).

### Disposal of Assets
When an asset is sold, scrapped, or discarded:
1. Record depreciation up to the disposal date
2. Remove the asset's cost and accumulated depreciation
3. Record any cash received
4. Recognize a gain or loss

Gain = Proceeds - Book Value (if positive)
Loss = Proceeds - Book Value (if negative)

Example: Machine (cost $50,000, accum. depr. $36,000, BV = $14,000) sold for $10,000.
Dr. Cash $10,000
Dr. Accumulated Depreciation $36,000
Dr. Loss on Disposal $4,000
  Cr. Equipment $50,000

### GAAP vs. Tax Depreciation
Companies maintain two sets of depreciation records:
- **GAAP (book)**: Systematic allocation matching the asset's useful life. Straight-line is most common.
- **Tax (MACRS)**: Required by the IRS. Uses shorter recovery periods and accelerated rates, resulting in larger deductions in early years (reducing taxable income sooner).

The difference creates a deferred tax liability on the balance sheet.

## Examples

### Example 1: Partial-Year Depreciation
Equipment purchased April 1 for $24,000, salvage $0, useful life 4 years, straight-line.
Annual rate = $24,000 / 4 = $6,000/year
Year 1 (Apr 1 - Dec 31 = 9 months): $6,000 x 9/12 = $4,500
Year 2: $6,000 (full year)

### Example 2: Changing Estimates
After 2 years, a machine (cost $100,000, salvage $10,000, original life 10 years) is now expected to last only 6 more years (8 total).
After 2 years: Accum. Depr. = 2 x ($90,000/10) = $18,000; BV = $82,000
Remaining depreciable base = $82,000 - $10,000 = $72,000
New annual depreciation = $72,000 / 6 = $12,000
Changes in estimates are applied prospectively (going forward), not retroactively.

## Relationships
- Depreciation is recorded through adjusting entries (Ch. 7)
- Accumulated depreciation is a contra-asset on the balance sheet (Ch. 4)
- Depreciation expense appears on the income statement (Ch. 3)
- Depreciation is added back in the cash flow statement under the indirect method (Ch. 5) -- it is a non-cash expense
- The depreciation tax shield affects capital budgeting (FIN 201 Ch. 7) and cost of capital
- Different methods for book vs. tax purposes create deferred taxes (ACG 301, 302)
- Cost allocation is expanded in cost accounting (ACG 204, 311)

## Common Misconceptions
- **Depreciation measures the decline in market value**: It does not. It is a cost allocation method. An asset's book value may be very different from its market value.
- **Land is depreciated**: Land is NOT depreciated because it has an unlimited useful life. Land improvements (parking lots, fences) ARE depreciated.
- **All companies use the same method**: Companies choose the method that best matches how the asset's benefits are consumed. Different methods can be used for different asset classes.
- **Accumulated depreciation is a cash reserve for replacing assets**: It is merely an accounting contra-asset. There is no corresponding pile of cash set aside.
- **Changing the depreciation estimate requires restating prior years**: Changes in estimates (useful life, salvage value) are applied prospectively. Prior financial statements are not changed.

## Practice Angles
- Calculate depreciation under straight-line, DDB, and units-of-production
- Build a complete depreciation schedule for an asset under each method
- Record the adjusting entry for depreciation
- Record the disposal of an asset with a gain or loss
- Handle partial-year depreciation
- Revise depreciation when estimates change
- Explain why GAAP and tax depreciation differ and the impact on deferred taxes
