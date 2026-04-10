# MSBA 515: Preparing for MSBA and AI Success - Flashcard Reference Bank

---

## Statistics Review

### Key Terms & Definitions
- **Descriptive Statistics**: Procedures used to summarize, organize, and simplify data from a sample or population
- **Inferential Statistics**: Techniques that allow us to study samples and make generalizations about the populations from which they were selected
- **Parameter**: A numerical value that describes a characteristic of a population (e.g., population mean)
- **Statistic**: A numerical value that describes a characteristic of a sample (e.g., sample mean)
- **Standard Deviation**: A measure of how spread out data values are from the mean; the square root of variance
- **Confidence Interval**: A range of values, derived from sample data, that is likely to contain the true population parameter at a specified confidence level
- **P-value**: The probability of observing results as extreme as the sample results, assuming the null hypothesis is true
- **Type I Error**: Rejecting a true null hypothesis (false positive); probability equals the significance level (alpha)
- **Type II Error**: Failing to reject a false null hypothesis (false negative); probability is denoted as beta
- **R-squared**: The proportion of variance in the dependent variable explained by the independent variable(s) in a regression model
- **Bayes' Theorem**: A formula that updates the probability of a hypothesis given new evidence: P(A|B) = P(B|A) * P(A) / P(B)
- **Interquartile Range (IQR)**: The difference between the 75th percentile (Q3) and the 25th percentile (Q1), measuring the spread of the middle 50% of data

### Core Concepts (Q&A Format)
- Q: What is the difference between a parameter and a statistic?
- A: A parameter describes a population (fixed, usually unknown), while a statistic describes a sample (varies by sample, used to estimate the parameter).

- Q: When should you use the median instead of the mean as a measure of central tendency?
- A: When data is skewed or contains outliers, because the median is resistant to extreme values while the mean is pulled toward them.

- Q: What does a p-value of 0.03 mean in hypothesis testing?
- A: There is a 3% probability of observing results this extreme if the null hypothesis is true. At alpha = 0.05, you would reject the null hypothesis.

- Q: What is the relationship between confidence level and interval width?
- A: Higher confidence levels produce wider intervals. A 99% CI is wider than a 95% CI for the same data because greater certainty requires a larger range.

- Q: How do you interpret an R-squared value of 0.72?
- A: 72% of the variation in the dependent variable is explained by the independent variable(s) in the regression model.

- Q: What is the difference between correlation and causation?
- A: Correlation measures the strength and direction of a linear relationship between two variables; causation means one variable directly influences the other. Correlation does not imply causation.

- Q: What distinguishes the Pearson correlation from the Spearman correlation?
- A: Pearson measures linear relationships between continuous variables; Spearman measures monotonic relationships using rank-ordered data and is more robust to outliers.

- Q: What is the Central Limit Theorem?
- A: Regardless of the population distribution, the sampling distribution of the sample mean approaches a normal distribution as the sample size increases (typically n >= 30).

### Important Facts & Figures
- The empirical rule (68-95-99.7): In a normal distribution, approximately 68% of data falls within 1 SD, 95% within 2 SD, and 99.7% within 3 SD of the mean
- A t-test is used instead of a z-test when the population standard deviation is unknown and/or the sample size is small (n < 30)
- Chi-square tests assess relationships between categorical variables; they compare observed frequencies to expected frequencies
- The Pearson correlation coefficient (r) ranges from -1 to +1; values near 0 indicate no linear relationship
- In simple linear regression, the slope represents the expected change in Y for a one-unit change in X
- The significance level (alpha) is typically set at 0.05, meaning a 5% risk of Type I error
- The Poisson distribution models the number of events occurring in a fixed interval of time or space
- The binomial distribution models the number of successes in a fixed number of independent trials with constant probability

### Common Exam Questions
- Q: A researcher finds a correlation of r = -0.85 between study hours and error rate. Interpret this result.
- A: There is a strong negative linear relationship; as study hours increase, error rate tends to decrease. However, this does not prove causation.

- Q: What assumptions must be met for a simple linear regression to be valid?
- A: Linearity, independence of errors, homoscedasticity (constant variance of residuals), normality of residuals, and no significant outliers.

- Q: A 95% confidence interval for mean income is ($45,000, $55,000). What does this mean?
- A: We are 95% confident that the true population mean income falls between $45,000 and $55,000. If we repeated sampling many times, about 95% of such intervals would contain the true mean.

- Q: Explain when you would use a one-tailed vs. two-tailed hypothesis test.
- A: Use one-tailed when you have a directional hypothesis (e.g., mean > 50). Use two-tailed when testing for any difference (e.g., mean is not equal to 50). Two-tailed is more conservative.

- Q: What is the difference between standard deviation and standard error?
- A: Standard deviation measures variability within a single sample. Standard error measures the variability of the sample mean across multiple samples (SD / sqrt(n)).

---

## Programming Basics

### Key Terms & Definitions
- **Variable**: A named container that stores a value in memory; the value can change during program execution
- **Data Type**: A classification that specifies what kind of value a variable holds (e.g., integer, float, string, boolean)
- **Function**: A reusable block of code that performs a specific task, accepts parameters, and optionally returns a value
- **List**: An ordered, mutable collection in Python that can hold mixed data types; defined with square brackets []
- **Dictionary**: An unordered collection of key-value pairs in Python; defined with curly braces {}; keys must be unique
- **DataFrame**: A two-dimensional, labeled data structure in pandas; similar to a spreadsheet or SQL table with rows and columns
- **Loop**: A control structure that repeats a block of code; for loops iterate over sequences, while loops repeat until a condition is false
- **Boolean**: A data type with only two values: True or False; used in conditional logic and comparisons
- **Module/Library**: A file or collection of files containing reusable Python code; imported with the import statement (e.g., import pandas as pd)
- **Jupyter Notebook**: An interactive computing environment that lets you combine code execution, text, and visualizations in a single document

### Core Concepts (Q&A Format)
- Q: What is the difference between a list and a tuple in Python?
- A: Both are ordered sequences, but lists are mutable (can be changed after creation) while tuples are immutable (cannot be modified). Tuples use parentheses (), lists use brackets [].

- Q: When would you use a dictionary instead of a list?
- A: When you need to look up values by a meaningful key rather than a numeric index. Dictionaries provide O(1) lookup time and are ideal for mapping relationships (e.g., student_id to grade).

- Q: What is the difference between a for loop and a while loop?
- A: A for loop iterates over a known sequence (list, range, etc.) a fixed number of times. A while loop repeats as long as a condition is True and is used when the number of iterations is unknown.

- Q: How do you read a CSV file into a pandas DataFrame?
- A: Use pd.read_csv('filename.csv'). This creates a DataFrame object that you can filter, group, merge, and analyze.

- Q: What does the groupby() method do in pandas?
- A: It splits a DataFrame into groups based on column values, allowing you to apply aggregate functions (mean, sum, count) to each group independently.

- Q: Why are functions important in programming?
- A: Functions promote code reuse, reduce duplication, improve readability, and make code easier to test and debug by breaking complex logic into smaller, named units.

- Q: What is the difference between == and = in Python?
- A: A single = is the assignment operator (assigns a value to a variable). Double == is the comparison operator (checks if two values are equal, returns True/False).

### Important Facts & Figures
- Python uses zero-based indexing: the first element of a list is at index 0
- The pandas library is built on top of NumPy and provides DataFrame and Series as its primary data structures
- Common pandas operations: .head(), .describe(), .info(), .value_counts(), .groupby(), .merge(), .fillna(), .dropna()
- NumPy arrays are faster than Python lists for numerical computation because they use contiguous memory and vectorized operations
- Python is dynamically typed: you do not need to declare variable types explicitly
- The three main file formats for data work: CSV (comma-separated), JSON (key-value, nested), Excel (.xlsx)
- PEP 8 is the official Python style guide covering naming conventions, indentation (4 spaces), and line length (79 characters)
- .duplicated() identifies duplicate rows in a DataFrame; .drop_duplicates() removes them

### Common Exam Questions
- Q: Write a function that takes a list of numbers and returns the average.
- A: def average(nums): return sum(nums) / len(nums). This uses built-in sum() and len() functions for a concise solution.

- Q: What is the output of: [x**2 for x in range(5)]?
- A: [0, 1, 4, 9, 16]. This is a list comprehension that squares each number from 0 to 4.

- Q: How would you handle missing values in a pandas DataFrame?
- A: Use .isnull().sum() to identify missing values, then either .dropna() to remove rows/columns or .fillna(value) to replace with a specific value (mean, median, 0, etc.).

- Q: Explain the difference between .loc[] and .iloc[] in pandas.
- A: .loc[] selects data by label/name (e.g., df.loc[0, 'column_name']). .iloc[] selects data by integer position (e.g., df.iloc[0, 2]). Both can select rows and columns.

- Q: What happens if you try to access a key that does not exist in a dictionary?
- A: Python raises a KeyError. To avoid this, use .get(key, default) which returns the default value instead of raising an error.

---

## Visualization Basics

### Key Terms & Definitions
- **Data-Ink Ratio**: Concept from Edward Tufte; the proportion of ink in a chart devoted to displaying actual data versus non-data elements. Higher is better.
- **Chartjunk**: Unnecessary or distracting visual elements in a chart that do not contribute to understanding the data (coined by Tufte)
- **Bar Chart**: A chart using rectangular bars to compare values across categories; length of bars is proportional to values
- **Line Chart**: A chart connecting data points with lines to show trends over time; best for continuous temporal data
- **Scatter Plot**: A chart plotting individual data points on two axes to reveal relationships, correlations, or clusters between two numeric variables
- **Histogram**: A chart showing the distribution of a single numeric variable by grouping values into bins; similar to a bar chart but for continuous data
- **Box Plot**: A chart displaying the five-number summary (min, Q1, median, Q3, max) and outliers; ideal for comparing distributions across groups
- **Heatmap**: A matrix-style visualization using color intensity to represent values; useful for showing correlations or patterns in large datasets
- **Tableau**: A leading drag-and-drop business intelligence tool for creating interactive dashboards and visualizations
- **Matplotlib/Seaborn**: Python libraries for creating static, animated, and interactive visualizations programmatically

### Core Concepts (Q&A Format)
- Q: When should you use a bar chart vs. a line chart?
- A: Use a bar chart for comparing discrete categories (e.g., sales by region). Use a line chart for showing trends over continuous time periods (e.g., monthly revenue over two years).

- Q: Why are pie charts generally discouraged in data visualization?
- A: Humans are poor at comparing angles and areas. Bar charts convey the same part-to-whole information more accurately. Pie charts are only acceptable with very few categories (2-3).

- Q: What is wrong with truncating the y-axis on a bar chart?
- A: It exaggerates differences between values by making small changes appear large. Bar charts should start at zero to maintain proportional representation.

- Q: What are the two main purposes of data visualization?
- A: Exploration (discovering patterns, anomalies, and relationships in data for the analyst) and communication (presenting findings clearly to an audience for decision-making).

- Q: How should you choose colors for a visualization?
- A: Use sequential color scales for ordered data, diverging scales for data with a meaningful midpoint, and categorical palettes for distinct groups. Ensure colorblind accessibility.

- Q: What does Tufte mean by "maximize the data-ink ratio"?
- A: Remove all non-essential visual elements (gridlines, borders, backgrounds, decorations) so that the remaining ink communicates actual data. Every mark should convey information.

### Important Facts & Figures
- Edward Tufte's "The Visual Display of Quantitative Information" (1983) established foundational visualization principles
- The pre-attentive attributes that draw immediate visual attention: color, size, shape, position, orientation
- Dual y-axes can mislead viewers by implying a relationship between two variables that may not exist; avoid or use with caution
- 3D charts almost always distort data perception due to perspective effects and should be avoided for quantitative data
- Power BI (Microsoft) and Tableau (Salesforce) are the two dominant enterprise visualization/BI platforms
- Seaborn is built on top of Matplotlib and provides a higher-level interface with better default aesthetics
- Stephen Few identifies four key visual encodings for numeric values: position (bars), connection (lines), points, and boxes
- The "one message per chart" rule: each visualization should communicate a single clear takeaway

### Common Exam Questions
- Q: A colleague presents a 3D exploded pie chart with 8 slices. What improvements would you suggest?
- A: Replace with a horizontal bar chart sorted by value. Remove the 3D effect (distorts perception), reduce to essential categories, and add data labels for precision.

- Q: What chart type would you use to show the relationship between advertising spend and sales revenue?
- A: A scatter plot with advertising spend on the x-axis and sales revenue on the y-axis. Add a trend line to show the direction and strength of the relationship.

- Q: Name three common mistakes in data visualization and how to fix them.
- A: (1) Truncated y-axis -- start at zero for bar charts. (2) Too many colors -- limit to 5-7 distinct colors. (3) Missing labels/titles -- always include axis labels, units, and a descriptive title.

- Q: When would you use a heatmap instead of a bar chart?
- A: When visualizing a matrix of values (e.g., correlation matrix, time-by-category performance). Heatmaps excel at showing patterns across two dimensions simultaneously using color intensity.

---

## Communication Skills

### Key Terms & Definitions
- **Data Storytelling**: The practice of structuring analytical findings into a narrative with context, findings, and recommendations to drive action
- **Executive Summary**: A brief, high-level overview of key findings and recommendations placed at the beginning of a report for time-constrained decision-makers
- **Audience Awareness**: The practice of tailoring message complexity, vocabulary, and detail level based on who will receive the communication
- **The "So What?" Test**: Evaluating every finding by asking what actionable insight it provides to the audience; if you cannot answer, the finding may not be worth presenting
- **Active Listening**: Fully concentrating on, understanding, and responding to a speaker; critical for gathering accurate requirements from stakeholders
- **MECE Framework**: Mutually Exclusive, Collectively Exhaustive; a structuring principle ensuring categories do not overlap and cover all possibilities
- **Slide Design Principle**: One key message per slide with minimal text; visuals should support rather than replace the spoken narrative
- **Stakeholder Management**: The process of identifying, understanding, and effectively communicating with all parties who have an interest in or influence over a project
- **Technical Debt in Communication**: The cost of poorly documented methodology and assumptions, which creates confusion and rework downstream

### Core Concepts (Q&A Format)
- Q: How should you structure an analytics presentation for a mixed audience?
- A: Lead with business impact and recommendations (for executives), provide methodology summary in the middle (for managers), and include technical appendix (for analysts). Layer from simple to complex.

- Q: What is the difference between presenting to executives vs. technical teams?
- A: Executives want high-level impact: what happened, what it means, what to do next. Technical teams want methodology details: how the analysis was done, assumptions, limitations, and validation.

- Q: Why is the "so what?" test important for analytics communication?
- A: It ensures every finding is tied to a business implication or recommended action. Data without context or actionable interpretation is just noise to decision-makers.

- Q: What are the three components of effective data storytelling?
- A: Context (why the analysis matters), Findings (what the data shows), and Recommendations (what actions to take). This structure mirrors how business decisions are made.

- Q: How should you handle questions you cannot answer during a presentation?
- A: Acknowledge the question, note it for follow-up, and commit to a specific timeline for providing the answer. Never fabricate an answer.

- Q: Why do employers rank communication skills above technical skills for analytics hires?
- A: Because technical analysis only creates business value when findings are communicated clearly enough to influence decisions. The best analysis is worthless if stakeholders cannot understand or act on it.

### Important Facts & Figures
- Surveys consistently show communication is among the top competencies employers seek in analytics hires, often ranking above specific technical abilities
- The Pyramid Principle (Barbara Minto): Start with the answer/recommendation first, then provide supporting arguments, then data
- A well-structured report follows: Executive Summary, Introduction/Context, Methodology, Findings, Recommendations, Appendix
- The 10-20-30 rule (Guy Kawasaki): No more than 10 slides, 20 minutes, 30-point minimum font size for presentations
- Written communication should follow the inverted pyramid model: most important information first, details later
- Active listening involves paraphrasing, asking clarifying questions, and confirming understanding before responding
- Analytics professionals spend approximately 40-60% of their time communicating results rather than performing analysis

### Common Exam Questions
- Q: You found that customer churn increased 15% last quarter. How would you present this to the executive team?
- A: Frame with business impact first ("We risk losing $2M in annual revenue"), then show the trend and root causes, and close with specific retention strategies and expected ROI. Keep it to 3-5 slides.

- Q: What are common pitfalls in analytics presentations?
- A: (1) Leading with methodology instead of findings, (2) presenting all analyses instead of only relevant ones, (3) using jargon with non-technical audiences, (4) failing to tie findings to business actions.

- Q: How do you document an analytics project for reproducibility?
- A: Include data sources and versions, cleaning/transformation steps, assumptions made, methodology and parameters chosen, results with confidence measures, and limitations. Use version control for code.

- Q: Describe the difference between a report and a presentation in analytics communication.
- A: A report is a complete, standalone document with full methodology and detail for reference. A presentation is a visual aid for live delivery, focusing on key messages with minimal text, designed to support a spoken narrative.
