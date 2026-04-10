# AA 306: Data Mining for Effective Decision Making - Flashcard Reference Bank

---

## Data Mining

### Key Terms & Definitions
- **Data Mining**: The computational process of discovering patterns, correlations, and anomalies within large datasets to predict outcomes and generate actionable knowledge
- **KDD (Knowledge Discovery in Databases)**: The overall process of converting raw data into useful information; data mining is one step within KDD
- **CRISP-DM**: Cross-Industry Standard Process for Data Mining; the leading six-phase methodology for data mining projects
- **Classification**: A supervised learning technique that assigns data instances to predefined categorical labels based on learned patterns
- **Clustering**: An unsupervised learning technique that groups similar data instances together without predefined labels
- **Association Rule Mining**: A method for discovering interesting relationships and co-occurrence patterns between variables in large datasets
- **Anomaly Detection**: The identification of data points that deviate significantly from expected behavior or patterns
- **Regression Analysis**: A supervised technique that predicts continuous numerical outcomes based on input variables
- **Supervised Learning**: Machine learning where the algorithm is trained on labeled data (known outcomes)
- **Unsupervised Learning**: Machine learning where the algorithm discovers hidden patterns in data without labeled outcomes
- **Overfitting**: When a model learns noise in training data rather than the underlying pattern, performing poorly on new data

### Core Concepts (Q&A Format)
- Q: What are the five stages of the KDD pipeline?
- A: Data selection, preprocessing, transformation, data mining, interpretation/evaluation

- Q: What are the six phases of CRISP-DM?
- A: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment

- Q: What is the difference between classification and clustering?
- A: Classification is supervised (uses labeled data to predict categories); clustering is unsupervised (groups similar data without predefined labels)

- Q: Why is CRISP-DM considered iterative rather than linear?
- A: The sequence of phases is not strict; moving back and forth between phases is always required as new insights emerge

- Q: What is the most time-consuming phase of CRISP-DM?
- A: Data Preparation, which involves cleaning, transforming, and formatting raw data for modeling

- Q: What distinguishes data mining from traditional statistical analysis?
- A: Data mining is designed to handle large-scale datasets, discover previously unknown patterns, and uses computational/algorithmic approaches rather than hypothesis-driven testing alone

- Q: Name three industries where data mining is commonly applied.
- A: Healthcare (patient risk prediction), finance (fraud detection), and retail (market basket analysis)

### Important Facts & Figures
- CRISP-DM was published in 1999 and remains the most widely used data mining methodology
- The KDD process was formalized by Fayyad, Piatetsky-Shapiro, and Smyth in 1996
- Data Preparation typically consumes 60-80% of a data mining project's time
- The Apriori algorithm (1994, Agrawal & Srikant) is the foundational algorithm for association rule mining
- Classification, clustering, and association rules are the three primary data mining task categories
- Data mining sits at the intersection of machine learning, statistics, and database systems
- The outer circle in the CRISP-DM diagram symbolizes the cyclic nature of data mining -- it does not end once a solution is deployed

### Common Exam Questions
- Q: Explain the KDD process and where data mining fits within it.
- A: KDD is the full process of turning raw data into knowledge: selection, preprocessing, transformation, data mining, and interpretation. Data mining is the core analytical step where algorithms discover patterns in prepared data.

- Q: Compare and contrast supervised and unsupervised learning with examples of each.
- A: Supervised learning uses labeled data to train models (e.g., classification with decision trees, regression). Unsupervised learning finds hidden structure in unlabeled data (e.g., clustering with K-means, association rules with Apriori).

- Q: Why is business understanding the first phase of CRISP-DM?
- A: Without understanding the business problem, objectives, and constraints, the entire project risks solving the wrong problem. Business understanding translates organizational needs into data mining goals.

- Q: What happens during the Evaluation phase of CRISP-DM?
- A: The model is assessed against business objectives using metrics like accuracy and error rates to determine if it meets the project's goals before deployment.

---

## Pattern Discovery

### Key Terms & Definitions
- **Pattern Discovery**: The process of detecting regularities, structures, and meaningful relationships within data
- **Frequent Itemset**: A set of items that appears together in a dataset at least a minimum number of times (minimum support threshold)
- **Support**: The proportion of transactions in a dataset that contain a particular itemset; measures how frequently items appear together
- **Confidence**: The probability that item B is purchased given that item A was purchased; measures the strength of an association rule
- **Lift**: The ratio of observed support to expected support if items were independent; lift > 1 indicates a positive association, lift < 1 indicates negative association
- **Apriori Algorithm**: An iterative, level-wise search algorithm that finds frequent itemsets by using k-itemsets to discover (k+1)-itemsets
- **Sequential Pattern**: An ordered pattern in data where one event follows another over time (e.g., buying a car, then insurance within a week)
- **Trend Analysis**: Identifying directional changes in data over time
- **Anomaly/Outlier**: A data point that deviates significantly from the expected pattern
- **Bayesian Classification**: A probabilistic classification technique based on Bayes' Theorem, assuming feature independence

### Core Concepts (Q&A Format)
- Q: What are the five main types of patterns discovered in data?
- A: Clusters (natural groupings), associations (co-occurrence), sequences (ordered patterns), trends (directional changes over time), and anomalies (deviations)

- Q: How does the Apriori algorithm work?
- A: It uses a level-wise iterative approach: first finds all frequent 1-itemsets, then uses those to generate candidate 2-itemsets, prunes infrequent ones, and repeats until no more frequent itemsets can be found

- Q: What do the three association rule metrics (support, confidence, lift) each measure?
- A: Support measures frequency of occurrence; confidence measures the conditional probability of the consequent given the antecedent; lift measures whether the association is stronger than random chance

- Q: What does a lift value of exactly 1.0 indicate?
- A: The items are statistically independent -- there is no real association between them; their co-occurrence is purely by chance

- Q: How does sequential pattern mining differ from association rule mining?
- A: Sequential pattern mining considers the order and timing of events (e.g., purchase sequences), while association rule mining only considers co-occurrence without regard to order

- Q: What is the Apriori property (downward closure)?
- A: If an itemset is infrequent, then all its supersets must also be infrequent. This allows pruning of the search space.

- Q: Name two real-world applications of pattern discovery.
- A: Market basket analysis (retail), fraud detection (finance), customer behavior analysis (marketing), gene sequence analysis (bioinformatics)

### Important Facts & Figures
- The Apriori algorithm was introduced by Agrawal and Srikant in 1994
- Market basket analysis is the classic application of association rule mining
- Support, confidence, and lift are the three fundamental metrics for evaluating association rules
- A lift value greater than 1 indicates a positive association; less than 1 indicates a negative association; equal to 1 indicates independence
- Clustering, association mining, and sequential mining are all categorized as descriptive mining techniques
- Neural networks and genetic algorithms are also used for advanced pattern discovery
- The "Apriori property" (anti-monotonicity) states: all subsets of a frequent itemset must also be frequent

### Common Exam Questions
- Q: A grocery store finds that {bread, butter} has support = 0.05, confidence = 0.60, and lift = 1.5. Interpret these values.
- A: 5% of all transactions contain both bread and butter. When bread is purchased, butter is also purchased 60% of the time. The lift of 1.5 means customers are 1.5 times more likely to buy butter when they buy bread than if the two were independent.

- Q: Explain the Apriori property and why it is important for efficiency.
- A: The Apriori property states that if an itemset is infrequent, all its supersets are also infrequent. This allows the algorithm to prune large portions of the search space, dramatically reducing computation.

- Q: Distinguish between descriptive and predictive pattern discovery techniques.
- A: Descriptive techniques (clustering, association rules) summarize and find structure in existing data. Predictive techniques (classification, regression) use discovered patterns to forecast future outcomes.

- Q: What is the difference between a cluster and a classification group?
- A: Clusters are discovered organically by the algorithm based on similarity (unsupervised), while classification groups are predefined categories that the algorithm learns to assign data to (supervised).

---

## Decision Making

### Key Terms & Definitions
- **DDDM (Data-Driven Decision Making)**: The practice of using facts, metrics, and data rather than intuition to guide strategic business decisions
- **Descriptive Analytics**: Answers "What happened?" by summarizing historical data (e.g., monthly sales reports, dashboards)
- **Diagnostic Analytics**: Answers "Why did it happen?" by identifying root causes through data discovery, mining, and correlation analysis
- **Predictive Analytics**: Answers "What will happen?" by forecasting future outcomes using statistical models and machine learning
- **Prescriptive Analytics**: Answers "What should we do?" by recommending specific actions to optimize results
- **Analytics Pyramid**: The progression from descriptive to diagnostic to predictive to prescriptive analytics, representing a path from hindsight to foresight
- **KPI (Key Performance Indicator)**: A measurable value that demonstrates how effectively an organization is achieving key business objectives
- **Dashboard**: A visual display of the most important information needed to achieve objectives, consolidated on a single screen
- **Data Governance**: Policies and procedures ensuring data quality, security, accessibility, and proper usage across an organization
- **A/B Testing**: A controlled experiment comparing two versions to determine which performs better for a given metric

### Core Concepts (Q&A Format)
- Q: What are the four types of analytics in order of increasing complexity?
- A: Descriptive (what happened), Diagnostic (why it happened), Predictive (what will happen), Prescriptive (what to do about it)

- Q: Why do most organizations struggle with becoming data-driven?
- A: Only 32.4% of organizations report success in becoming data-driven despite 98.6% aspiring to it, primarily due to cultural challenges and technology-first approaches without cultural support

- Q: What is the difference between predictive and prescriptive analytics?
- A: Predictive analytics forecasts what will likely happen; prescriptive analytics goes further by recommending specific actions to take based on those predictions

- Q: Give an example of each type of analytics in a retail context.
- A: Descriptive: last month's sales report. Diagnostic: why sales dropped in Q3. Predictive: forecasting holiday demand. Prescriptive: recommending optimal inventory levels and pricing strategies.

- Q: What role do dashboards play in data-driven decision making?
- A: Dashboards consolidate key metrics and visualizations into a single view, enabling decision-makers to quickly monitor performance, identify trends, and act on insights

- Q: Why is data governance critical for DDDM?
- A: Without data governance, poor data quality, inconsistent definitions, and security issues undermine trust in analytics, leading to flawed decisions

- Q: What is the Analytics Pyramid?
- A: A framework showing the progression from basic descriptive analytics to advanced prescriptive analytics, where each level builds on the one below and adds increasing value and complexity

### Important Facts & Figures
- Only 32.4% of organizations report success in becoming data-driven (despite 98.6% aspiring to it)
- The four analytics types form a pyramid: descriptive (base/most common) to prescriptive (top/most advanced)
- Descriptive analytics is the most widely used form and serves as the foundation for all other analytics
- Prescriptive analytics is the most complex and least adopted type
- Data-driven organizations consistently outperform their peers in financial performance
- Common DDDM applications: healthcare (patient risk), finance (portfolio optimization), marketing (campaign targeting), operations (resource allocation)
- A data-driven culture requires both technology investment AND organizational change management

### Common Exam Questions
- Q: A company has data showing declining customer retention. Walk through how each analytics type would be applied.
- A: Descriptive: Report showing retention rates over time. Diagnostic: Analyze why customers leave (survey data, usage patterns). Predictive: Model which current customers are likely to churn. Prescriptive: Recommend targeted interventions for at-risk customers.

- Q: Explain why an organization might fail at DDDM despite investing heavily in analytics technology.
- A: Technology alone is insufficient. Success requires a data-driven culture, leadership buy-in, data literacy among employees, proper data governance, and organizational processes that incorporate data into decision workflows.

- Q: What distinguishes diagnostic analytics from descriptive analytics?
- A: Descriptive analytics summarizes what happened (e.g., sales dropped 10%). Diagnostic analytics investigates why it happened by drilling into data, finding correlations, and identifying root causes (e.g., a competitor launched a promotion).

- Q: Why is prescriptive analytics considered the most valuable yet least adopted?
- A: It provides direct action recommendations, but it requires the most sophisticated models, highest data quality, domain expertise, and integration with decision-making systems.

---

## Problem Solving

### Key Terms & Definitions
- **Analytical Problem Solving**: A structured approach using data and logical reasoning to decompose complex challenges, analyze root causes, and develop evidence-based solutions
- **CRISP-DM**: Cross-Industry Standard Process for Data Mining; a six-phase iterative methodology for structuring data mining projects
- **DMAIC**: Define, Measure, Analyze, Improve, Control; a data-driven improvement cycle from Lean Six Sigma for optimizing business processes
- **MECE Principle**: Mutually Exclusive, Collectively Exhaustive; a McKinsey-popularized framework ensuring categories do not overlap and nothing is left out
- **Five Whys**: A root cause analysis technique where you ask "Why?" repeatedly (typically five times) to drill down to the fundamental cause of a problem
- **Hypothesis Tree**: A structured breakdown of possible explanations for a problem, organized hierarchically for systematic testing
- **Issue Tree**: A visual framework that breaks a complex problem into smaller, manageable sub-problems in a MECE structure
- **Pareto Analysis (80/20 Rule)**: The principle that roughly 80% of effects come from 20% of causes; used to prioritize the most impactful factors
- **Root Cause Analysis**: A systematic process for identifying the fundamental reasons why a problem occurs, rather than treating symptoms
- **Hypothesis-Driven Approach**: McKinsey method of forming an initial hypothesis about the answer, then systematically testing it with data

### Core Concepts (Q&A Format)
- Q: What are the five steps of structured analytical problem solving?
- A: Define the problem, analyze root causes, generate possible solutions, evaluate and select the best option, implement with follow-up learning

- Q: What does MECE stand for and why is it important?
- A: Mutually Exclusive (no overlaps) and Collectively Exhaustive (no gaps). It ensures complete coverage of a problem without double-counting, making analysis and communication precise.

- Q: What are the five phases of DMAIC?
- A: Define (state the problem and goals), Measure (collect baseline data), Analyze (identify root causes), Improve (implement solutions), Control (sustain the improvements)

- Q: How does DMAIC differ from CRISP-DM?
- A: DMAIC is focused on improving existing business processes (Lean Six Sigma context). CRISP-DM is specifically designed for data mining projects. DMAIC emphasizes process control; CRISP-DM emphasizes data modeling.

- Q: What is the Five Whys technique and when would you use it?
- A: A technique where you ask "Why?" repeatedly to drill past symptoms to root causes. Example: "Why did the server crash?" leads through successive answers to discover the root cause was inadequate capacity planning.

- Q: How does Pareto Analysis help prioritize problems?
- A: It identifies the vital few causes (roughly 20%) that produce the majority of effects (roughly 80%), allowing analysts to focus effort where it will have the greatest impact.

- Q: What is the difference between an issue tree and a hypothesis tree?
- A: An issue tree breaks a problem into sub-issues without assumptions. A hypothesis tree starts with a proposed answer and breaks it into components that must be true for the hypothesis to hold.

### Important Facts & Figures
- The MECE principle was popularized by McKinsey & Company and is a cornerstone of consulting problem-solving
- The Pareto Principle (80/20 rule) was named after economist Vilfredo Pareto
- DMAIC originated from Lean Six Sigma quality improvement methodology
- The Five Whys technique was originally developed by Sakichi Toyoda and used within the Toyota Production System
- CRISP-DM's iterative nature means projects frequently cycle back to earlier phases
- Hypothesis-driven problem solving (McKinsey approach) begins with a potential answer, then tests it -- opposite of purely exploratory analysis
- Structured problem solving is essential for translating business questions into analytical approaches

### Common Exam Questions
- Q: You are tasked with improving customer satisfaction scores. Apply the DMAIC framework to this problem.
- A: Define: Customer satisfaction has dropped 15%, goal is to restore it within 6 months. Measure: Collect current CSAT scores, survey data, complaint logs. Analyze: Identify root causes (e.g., slow response times, product quality). Improve: Implement fixes such as staff training, process changes. Control: Monitor CSAT scores monthly, establish alert thresholds.

- Q: Break down "Why is our company losing market share?" using the MECE principle.
- A: MECE breakdown: (1) Product issues (quality, features, pricing), (2) Competition (new entrants, competitor improvements), (3) Customer changes (shifting preferences, demographics), (4) Distribution/access (availability, channels), (5) Brand/marketing (awareness, perception). Each category is distinct and together they cover all possibilities.

- Q: Compare the Five Whys and Pareto Analysis as root cause tools. When would you use each?
- A: Five Whys is best for drilling into a single problem to find its root cause through iterative questioning. Pareto Analysis is best when multiple problems exist and you need to prioritize which ones to solve first based on impact.

- Q: Why is structured problem solving preferred over ad hoc approaches in analytics?
- A: Structured approaches are systematic, repeatable, and evidence-based. They ensure nothing is overlooked, reduce cognitive bias, enable clear communication with stakeholders, and produce more reliable outcomes.

---

## Analytical Methods

### Key Terms & Definitions
- **Descriptive Statistics**: Methods that summarize and describe characteristics of a dataset (mean, median, mode, standard deviation)
- **Inferential Statistics**: Methods that draw conclusions about a population based on a sample of data
- **Mean**: The arithmetic average of a dataset; sensitive to outliers
- **Median**: The middle value when data is ordered; resistant to outliers
- **Mode**: The most frequently occurring value in a dataset
- **Standard Deviation**: A measure of the spread of data around the mean; higher values indicate greater dispersion
- **Variance**: The average of squared deviations from the mean (standard deviation squared)
- **Hypothesis Testing**: A statistical method for making decisions about a population parameter based on sample data by testing a null hypothesis against an alternative
- **Null Hypothesis (H0)**: The default assumption of no effect, no difference, or no relationship
- **Alternative Hypothesis (H1/Ha)**: The hypothesis that there is an effect, difference, or relationship
- **P-value**: The probability of observing results as extreme as the sample data, assuming the null hypothesis is true
- **Confidence Interval**: A range of values within which the true population parameter is expected to fall with a specified probability (e.g., 95%)

### Core Concepts (Q&A Format)
- Q: When do you use a t-test vs. ANOVA vs. chi-square test?
- A: T-test: comparing means of exactly two groups. ANOVA: comparing means of three or more groups. Chi-square: testing relationships between categorical variables.

- Q: What does a p-value of 0.03 mean when alpha is 0.05?
- A: Since p (0.03) < alpha (0.05), we reject the null hypothesis. There is statistically significant evidence of a difference or relationship. There is only a 3% probability of observing such extreme results if the null hypothesis were true.

- Q: What is the difference between Type I and Type II errors?
- A: Type I error (false positive): Rejecting a true null hypothesis. Type II error (false negative): Failing to reject a false null hypothesis.

- Q: When would you use regression analysis?
- A: When you want to model the relationship between a dependent variable and one or more independent variables, especially to predict outcomes or estimate the effect of changes in predictors.

- Q: What is PCA and when is it used?
- A: Principal Component Analysis reduces the number of variables in a dataset while retaining most of the variance. Used when datasets have many correlated features and dimensionality reduction is needed.

- Q: Why is the median sometimes preferred over the mean?
- A: The median is resistant to outliers and skewed distributions. For example, median household income better represents "typical" income than mean income, which is pulled up by extremely high earners.

- Q: What does ANOVA stand for and what does it test?
- A: Analysis of Variance. It tests whether there are statistically significant differences between the means of three or more independent groups.

- Q: What assumptions must be met for a t-test?
- A: Data should be approximately normally distributed, observations should be independent, and for the two-sample t-test, variances should be approximately equal (or use Welch's t-test).

### Important Facts & Figures
- Alpha level of 0.05 (5% significance) is the most common threshold in hypothesis testing
- If p-value <= alpha, reject the null hypothesis; the result is statistically significant
- T-tests compare exactly 2 groups; ANOVA compares 3 or more groups
- Chi-square tests are used exclusively for categorical (nominal/ordinal) data
- R-squared in regression indicates the proportion of variance in the dependent variable explained by the independent variables (0 to 1)
- Correlation does not imply causation -- a fundamental principle of statistical analysis
- Parametric tests (t-test, ANOVA) assume normal distribution; non-parametric alternatives exist for non-normal data (e.g., Mann-Whitney U, Kruskal-Wallis)
- A 95% confidence interval means: if we repeated the sampling 100 times, approximately 95 intervals would contain the true population parameter

### Common Exam Questions
- Q: A researcher wants to test whether three different teaching methods produce different exam scores. Which test should be used and why?
- A: One-way ANOVA, because we are comparing means across three groups (more than two) with a continuous dependent variable (exam scores).

- Q: Explain the relationship between confidence level, sample size, and confidence interval width.
- A: Higher confidence level = wider interval. Larger sample size = narrower interval. There is a trade-off between precision (narrow interval) and confidence (high probability of capturing the true value).

- Q: A study finds a correlation of r = 0.85 between ice cream sales and drowning incidents. Can we conclude ice cream causes drowning? Explain.
- A: No. Correlation does not imply causation. Both variables are likely driven by a confounding variable (temperature/summer season). This illustrates spurious correlation.

- Q: When would you choose a non-parametric test over a parametric one?
- A: When data violates parametric assumptions: non-normal distribution, ordinal data, small sample sizes, or presence of significant outliers. Examples include Mann-Whitney U (instead of t-test) and Kruskal-Wallis (instead of ANOVA).

- Q: What is the difference between simple and multiple regression?
- A: Simple regression uses one independent variable to predict the dependent variable. Multiple regression uses two or more independent variables. Multiple regression can reveal which predictors have the strongest effect while controlling for others.

---
