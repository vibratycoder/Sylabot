---
chapter: 1
title: Descriptive Statistics
subject: statistics
course: intro-statistics
prefix: STAT
code: "200"
keywords: [mean, median, mode, standard deviation, variance, range, percentile, quartile, histogram, frequency distribution, skewness, outlier, central tendency, dispersion]
prereqs: []
---

# Descriptive Statistics

## Overview
Descriptive statistics summarize and organize data to make it understandable. Measures of central tendency (mean, median, mode) describe the "center" of the data. Measures of dispersion (range, variance, standard deviation) describe how spread out the data is. Visualizations (histograms, box plots) reveal patterns, shapes, and outliers. These tools are the foundation of all statistical analysis.

## Key Terms
- **Mean (Average)**: Sum of all values divided by the number of values. Sensitive to outliers.
- **Median**: The middle value when data is sorted. Resistant to outliers. Better measure of center for skewed data.
- **Mode**: The most frequently occurring value. A distribution can be unimodal, bimodal, or multimodal.
- **Range**: Maximum - Minimum. Simple but sensitive to outliers.
- **Variance (s^2)**: Average of squared deviations from the mean. Measures spread. s^2 = sum of (xi - x-bar)^2 / (n-1).
- **Standard Deviation (s)**: Square root of variance. In the same units as the data. Most commonly used measure of spread.
- **Percentile**: The value below which a given percentage of data falls. The 90th percentile means 90% of values are below.
- **Quartiles**: Q1 (25th percentile), Q2 (median, 50th), Q3 (75th percentile).
- **Interquartile Range (IQR)**: Q3 - Q1. Measures spread of the middle 50%. Resistant to outliers.
- **Outlier**: A data point significantly different from others. Often defined as below Q1 - 1.5(IQR) or above Q3 + 1.5(IQR).
- **Skewness**: Asymmetry of the distribution. Right-skewed (tail to the right, mean > median), Left-skewed (tail to the left, mean < median), Symmetric (mean ≈ median).
- **Histogram**: Bar chart showing frequency distribution. Bars represent intervals of values.
- **Box Plot**: Visual showing Q1, median, Q3, whiskers, and outliers. Good for comparing distributions.
- **Normal Distribution**: Bell-shaped, symmetric. Mean = Median = Mode. 68-95-99.7 rule.

## Core Concepts

### Central Tendency
Mean is most common but affected by outliers. Median is robust to outliers (use for income data, home prices). Mode is useful for categorical data. For symmetric data: mean ≈ median ≈ mode. For skewed data: use median.

### The 68-95-99.7 Rule (Empirical Rule)
For approximately normal distributions: ~68% of data falls within 1 SD of the mean, ~95% within 2 SDs, ~99.7% within 3 SDs. Used for quick estimates of proportions and identifying unusual values.

### Choosing the Right Summary
Skewed data: report median and IQR. Symmetric data: report mean and SD. Always visualize with a histogram or box plot before computing statistics. The shape of the distribution determines which summary statistics are appropriate.

## Examples

### Income Data
US household incomes are right-skewed (a few very high earners pull the mean up). Mean income: ~$97,000. Median income: ~$75,000. The median better represents the "typical" household because the mean is inflated by outliers.

### Exam Scores
Class of 30 students. Scores: mean = 78, SD = 10, roughly normal. By the 68-95-99.7 rule: ~68% scored between 68-88, ~95% between 58-98, ~99.7% between 48-108. A score of 55 is unusual (below 2 SDs).

## Relationships
- Outliers -> Mean is pulled toward outliers; median is not
- Right-skewed -> Mean > Median
- Left-skewed -> Mean < Median
- Higher SD -> Data more spread out
- IQR -> Robust to outliers (use with median)

## Common Misconceptions
- **"Average always means mean"**: In statistics, specify which average (mean, median, mode). They can differ dramatically for skewed data.
- **"Standard deviation is the average distance from the mean"**: It's the square root of the average squared distance. Close conceptually but not mathematically identical.
- **"Outliers should always be removed"**: Outliers may represent real data (e.g., a billionaire in income data). Investigate before removing.

## Practice Angles
- Calculate: mean, median, mode, range, SD for a given dataset
- Interpret: a box plot and identify outliers, skewness
- Explain: when to use mean vs median (with examples of skewed data)
- Apply: the 68-95-99.7 rule to estimate percentages
- Analyze: how an outlier affects mean vs median
