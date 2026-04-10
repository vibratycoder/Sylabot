# AA 630: Data Management for Analytics - Flashcard Reference Bank

---

## Data Acquisition

### Key Terms & Definitions
- **Data Acquisition**: The process of collecting and importing data from diverse sources, transforming real-world information into digital formats suitable for storage and analysis.
- **API (Application Programming Interface)**: A standardized programmatic interface (REST or GraphQL) that allows software systems to exchange data automatically.
- **Web Scraping**: Automated extraction of data from websites using tools like BeautifulSoup, Scrapy, or Selenium.
- **Primary Data**: Data collected firsthand by the researcher through experiments, surveys, sensors, or direct observation.
- **Secondary Data**: Pre-existing data collected by someone else, sourced from published datasets, government repositories, or commercial databases.
- **Data Provenance**: The documented history of data's origin, movement, and transformations, used to assess trustworthiness and lineage.
- **Batch Processing**: Periodic scheduled extraction of data at set intervals (hourly, daily, weekly).
- **Streaming/Real-Time Ingestion**: Continuous acquisition of data as events occur, enabling immediate processing and analysis.
- **Data Marketplace**: A commercial platform where organizations can buy, sell, or exchange datasets from third-party providers.
- **Schema**: The formal definition of a dataset's structure, including column names, data types, constraints, and relationships.

### Core Concepts (Q&A Format)
- Q: What are the four main strategies organizations use to acquire data?
- A: (1) Collecting new data directly, (2) converting/transforming legacy data, (3) sharing or exchanging data with partners, (4) purchasing data from commercial vendors.

- Q: What is the difference between primary and secondary data?
- A: Primary data is collected firsthand by the analyst (surveys, experiments, sensors); secondary data comes from pre-existing sources collected by others (government databases, published datasets).

- Q: Why is data provenance important in data acquisition?
- A: It establishes the origin, reliability, and chain of custody of data, allowing analysts to assess data quality and trustworthiness before using it in analysis.

- Q: What is the difference between batch and real-time data acquisition?
- A: Batch acquisition extracts data at scheduled intervals (e.g., nightly), while real-time acquisition continuously ingests data as events occur with minimal latency.

- Q: Name three key considerations when planning data acquisition.
- A: Data quality assessment, legal/ethical compliance (e.g., GDPR), and source reliability/cost evaluation.

- Q: What Python tools are commonly used for data acquisition?
- A: The `requests` library for API calls, `BeautifulSoup`/`Scrapy` for web scraping, `pandas.read_csv()` for file imports, and `SQLAlchemy` for database connections.

- Q: What is the difference between REST and GraphQL APIs?
- A: REST uses fixed endpoints returning predetermined data structures; GraphQL uses a single endpoint where clients specify exactly which data fields they need, reducing over-fetching.

### Important Facts & Figures
- Data acquisition is the first step in any analytics pipeline and directly determines the quality of downstream analysis.
- REST APIs are the most common method for programmatic data exchange between systems.
- GDPR (General Data Protection Regulation) governs data collection and privacy for EU citizens and applies to any organization handling their data.
- IoT (Internet of Things) sensors generate continuous streams of data requiring real-time ingestion architectures.
- JSON and CSV are the two most common file formats for data exchange; Parquet is preferred for large-scale columnar storage.
- Incremental extraction pulls only new or changed records, reducing load compared to full extraction.
- Data quality issues introduced at the acquisition stage propagate through the entire analytics pipeline ("garbage in, garbage out").

### Common Exam Questions
- Q: Compare and contrast two methods of data acquisition and explain when each is most appropriate.
- A: APIs provide structured, reliable, programmatic access ideal for recurring data pulls; web scraping extracts data from websites lacking APIs but requires more maintenance and raises legal considerations.

- Q: A company needs daily sales data from three different source systems. What acquisition approach would you recommend and why?
- A: A scheduled batch extraction process using API connections or database queries, feeding into a staging area where data from all three sources is validated and unified before loading into the analytics environment.

- Q: What legal and ethical considerations must be addressed during data acquisition?
- A: Privacy regulations (GDPR, CCPA), data licensing terms, consent requirements, intellectual property rights, and ensuring data is not obtained through deceptive or unauthorized means.

- Q: Explain the concept of data quality assessment during acquisition.
- A: Evaluating source reliability, checking for completeness and accuracy, validating data against expected schemas and formats, and establishing automated validation checks in the ingestion pipeline.

---

## Data Preparation

### Key Terms & Definitions
- **Data Preparation (Preprocessing)**: The process of cleaning, transforming, and organizing raw data into a format suitable for analysis and modeling.
- **Data Profiling**: Examining data structure, distributions, completeness, and relationships using summary statistics to identify quality issues before transformation.
- **Imputation**: Replacing missing values with estimated values such as mean, median, mode, or model-predicted values.
- **One-Hot Encoding**: Converting a categorical variable into multiple binary (0/1) columns, one per category.
- **Label Encoding**: Assigning a unique integer to each category in a categorical variable.
- **Normalization (Min-Max Scaling)**: Rescaling features to a fixed range, typically 0 to 1, using the formula: (x - min) / (max - min).
- **Standardization (Z-Score Scaling)**: Transforming features to have mean = 0 and standard deviation = 1, using the formula: (x - mean) / std.
- **Feature Engineering**: Creating new variables from existing data through aggregation, binning, polynomial features, or domain-specific transformations.
- **Data Splitting**: Dividing data into training, validation, and test sets to enable unbiased model evaluation.
- **K-Fold Cross-Validation**: A resampling method that splits data into k subsets, training on k-1 folds and testing on the remaining fold, rotating through all combinations.

### Core Concepts (Q&A Format)
- Q: Why is data preparation considered the most time-consuming phase of analytics?
- A: It typically consumes 60-80% of project effort because raw data contains missing values, inconsistencies, format mismatches, and structural problems that must be resolved before meaningful analysis.

- Q: When should you use normalization vs. standardization?
- A: Use min-max normalization when you need values in a bounded range (e.g., neural networks); use z-score standardization when the algorithm assumes normally distributed features or when outliers are present (standardization is less affected by outliers).

- Q: What is the difference between one-hot encoding and label encoding?
- A: One-hot encoding creates binary columns for each category (no ordinal assumption); label encoding assigns integers to categories (implies ordinal relationship, suitable only for ordinal variables).

- Q: Why is data splitting important before model building?
- A: It prevents overfitting by ensuring the model is evaluated on data it has never seen during training, providing an unbiased estimate of real-world performance.

- Q: What is the typical train/validation/test split ratio?
- A: Common ratios are 70/15/15 or 80/10/10; the training set builds the model, validation tunes hyperparameters, and the test set provides final performance evaluation.

- Q: What is the purpose of data profiling?
- A: To understand the data's structure, distributions, completeness, and quality issues before applying any transformations, guiding the preparation strategy.

- Q: What is feature engineering and why does it matter?
- A: Creating new predictive variables from existing data (e.g., extracting day-of-week from a date). It can dramatically improve model accuracy by providing the algorithm with more informative inputs.

### Important Facts & Figures
- Data preparation accounts for 60-80% of time in a typical analytics project.
- The four key preprocessing tasks are: cleaning, integration, transformation, and reduction.
- Listwise deletion removes entire rows with any missing value; pairwise deletion uses all available data for each calculation.
- Log transformation is commonly used to reduce right-skewed distributions.
- Scikit-learn's `Pipeline` object chains preprocessing steps to prevent data leakage and ensure reproducibility.
- Data leakage occurs when information from outside the training set influences model building, producing overly optimistic performance estimates.
- Decimal scaling normalizes by moving the decimal point based on the maximum absolute value in the feature.

### Common Exam Questions
- Q: A dataset has 15% missing values in a key numeric column. What imputation strategy would you recommend?
- A: For 15% missingness, simple deletion would lose too much data. Use median imputation if outliers are present (median is robust to outliers) or mean imputation for normally distributed data. For better accuracy, consider model-based imputation (e.g., KNN imputer or iterative imputer).

- Q: Explain why you should fit scalers on training data only and then transform both train and test sets.
- A: Fitting on the full dataset causes data leakage -- the scaler would incorporate information from the test set, leading to overly optimistic performance estimates that won't generalize to new data.

- Q: Describe three feature engineering techniques and when each is useful.
- A: (1) Binning continuous variables into categories (e.g., age groups) for interpretability; (2) Polynomial features to capture nonlinear relationships; (3) Interaction terms to model combined effects of two variables.

- Q: What is the difference between data reduction and data transformation?
- A: Data reduction decreases the volume of data (e.g., dimensionality reduction with PCA, sampling); data transformation changes the format or scale of data (e.g., normalization, encoding) without reducing its volume.

---

## Python for Analytics

### Key Terms & Definitions
- **pandas**: The primary Python library for data manipulation, providing DataFrame and Series structures for tabular data operations.
- **DataFrame**: A two-dimensional labeled data structure in pandas with columns of potentially different types (like a spreadsheet or SQL table).
- **Series**: A one-dimensional labeled array in pandas; each column of a DataFrame is a Series.
- **NumPy**: The foundational Python library for numerical computing, providing efficient n-dimensional array (ndarray) objects and mathematical operations.
- **ndarray**: NumPy's core data structure -- a homogeneous, fixed-size, multidimensional array that is faster and more memory-efficient than Python lists.
- **scikit-learn**: The standard Python library for machine learning, providing a unified API for classification, regression, clustering, and preprocessing.
- **Matplotlib**: A low-level Python plotting library for creating highly customizable static visualizations (line, bar, scatter, histogram).
- **Seaborn**: A statistical visualization library built on Matplotlib that provides high-level functions for attractive, informative plots with cleaner defaults.
- **Jupyter Notebook**: An interactive computing environment combining executable code, Markdown text, and visualizations in a single shareable document.
- **SQLAlchemy**: A Python SQL toolkit and ORM (Object-Relational Mapper) that enables database connectivity within Python workflows.

### Core Concepts (Q&A Format)
- Q: What is the difference between a pandas DataFrame and a NumPy array?
- A: A DataFrame supports heterogeneous data types across columns with labeled axes; a NumPy array requires homogeneous data types but offers faster numerical computation and lower memory usage.

- Q: What does `groupby()` do in pandas?
- A: It splits a DataFrame into groups based on one or more columns, applies an aggregate function (sum, mean, count, etc.) to each group, and combines the results -- analogous to SQL's GROUP BY.

- Q: How do you handle missing data in pandas?
- A: Use `isnull()` or `isna()` to detect missing values, `dropna()` to remove rows/columns with missing values, and `fillna()` to replace missing values with a specified value or method (forward-fill, backward-fill).

- Q: What is the difference between `merge()` and `concat()` in pandas?
- A: `merge()` joins DataFrames based on common columns (like SQL joins); `concat()` stacks DataFrames vertically (row-wise) or horizontally (column-wise) without matching on keys.

- Q: Why are NumPy arrays faster than Python lists for numerical operations?
- A: NumPy arrays store elements in contiguous memory with a fixed data type, enabling vectorized operations (SIMD), whereas Python lists store pointers to objects scattered in memory with type-checking overhead per element.

- Q: What is scikit-learn's fit/transform/predict pattern?
- A: `fit()` learns parameters from training data, `transform()` applies learned parameters to data (for preprocessing), and `predict()` generates outputs from a trained model. `fit_transform()` combines the first two steps.

- Q: What are the benefits of using Jupyter Notebooks for analytics?
- A: They combine code, documentation, and visualizations in one document; support iterative exploratory analysis; enable easy sharing of reproducible workflows; and allow inline visualization.

### Important Facts & Figures
- pandas is built on top of NumPy, so every DataFrame operation ultimately uses NumPy arrays under the hood.
- The `.describe()` method in pandas provides count, mean, std, min, 25%, 50%, 75%, and max for numerical columns -- a quick data profiling tool.
- Scikit-learn uses a consistent API: all estimators implement `fit()`, transformers implement `transform()`, and predictors implement `predict()`.
- `pivot_table()` in pandas creates spreadsheet-style pivot tables with aggregation, equivalent to Excel's PivotTable feature.
- Seaborn's `heatmap()` is commonly used to visualize correlation matrices.
- The `%matplotlib inline` magic command in Jupyter displays plots directly in the notebook.
- SciPy extends NumPy with optimization, integration, interpolation, and statistical functions.
- statsmodels provides detailed statistical model summaries including p-values and confidence intervals that scikit-learn does not.

### Common Exam Questions
- Q: Write pseudocode to load a CSV file, handle missing values, and calculate the mean of a column using pandas.
- A: `df = pd.read_csv('file.csv')` -> `df['col'].fillna(df['col'].median(), inplace=True)` -> `mean_val = df['col'].mean()`.

- Q: Explain the difference between Matplotlib and Seaborn and when you would use each.
- A: Matplotlib provides low-level control for custom visualizations; Seaborn provides high-level statistical plots (pair plots, heatmaps, distribution plots) with cleaner defaults. Use Matplotlib for custom/complex charts; use Seaborn for quick exploratory statistical visualizations.

- Q: How does scikit-learn's `train_test_split()` work and why is the `random_state` parameter important?
- A: It randomly divides a dataset into training and test subsets at a specified ratio. The `random_state` parameter seeds the random number generator so the split is reproducible across runs.

- Q: What is vectorization in NumPy and why is it important?
- A: Vectorization applies operations to entire arrays simultaneously instead of looping through elements, leveraging optimized C implementations. This makes NumPy operations 10-100x faster than equivalent Python loops.

---

## SQL

### Key Terms & Definitions
- **SQL (Structured Query Language)**: The standard language for managing and querying data in relational database management systems.
- **DDL (Data Definition Language)**: SQL commands that define database structure: CREATE, ALTER, DROP, TRUNCATE.
- **DML (Data Manipulation Language)**: SQL commands that modify data: INSERT, UPDATE, DELETE.
- **DQL (Data Query Language)**: SQL commands that retrieve data: SELECT.
- **DCL (Data Control Language)**: SQL commands that manage permissions: GRANT, REVOKE.
- **JOIN**: An operation that combines rows from two or more tables based on a related column. Types: INNER, LEFT, RIGHT, FULL OUTER, CROSS.
- **Aggregate Function**: A function that computes a single value from a set of rows: COUNT, SUM, AVG, MIN, MAX.
- **Window Function**: A function that performs calculations across a set of rows related to the current row without collapsing the result set (e.g., ROW_NUMBER, RANK, LAG, LEAD).
- **CTE (Common Table Expression)**: A temporary named result set defined with a WITH clause, used to simplify complex queries into readable modular components.
- **Subquery**: A SELECT statement nested inside another SQL statement, used for filtering, computing, or providing intermediate results.
- **Primary Key**: A column (or combination of columns) that uniquely identifies each row in a table.
- **Foreign Key**: A column that references the primary key of another table, establishing a relationship between the two tables.

### Core Concepts (Q&A Format)
- Q: What is the difference between INNER JOIN and LEFT JOIN?
- A: INNER JOIN returns only rows with matching values in both tables; LEFT JOIN returns all rows from the left table plus matching rows from the right table (NULLs where no match exists).

- Q: What is the difference between WHERE and HAVING?
- A: WHERE filters individual rows before grouping; HAVING filters groups after GROUP BY and works with aggregate functions.

- Q: What is the difference between RANK() and DENSE_RANK()?
- A: RANK() assigns the same rank to ties then skips subsequent numbers (1, 2, 2, 4); DENSE_RANK() assigns the same rank to ties with no gaps (1, 2, 2, 3).

- Q: When would you use a CTE instead of a subquery?
- A: CTEs improve readability for complex multi-step queries, can be referenced multiple times in the same query, and support recursive queries. Subqueries are simpler for one-time use.

- Q: What does GROUP BY do in SQL?
- A: It groups rows sharing the same values in specified columns into summary rows, enabling aggregate functions (SUM, COUNT, AVG) to be applied per group.

- Q: What is the difference between DELETE and TRUNCATE?
- A: DELETE removes specific rows (can use WHERE clause) and is logged per row; TRUNCATE removes all rows from a table, is faster, cannot be filtered, and resets auto-increment counters.

- Q: Explain what LAG() and LEAD() window functions do.
- A: LAG() accesses a value from a previous row in the result set; LEAD() accesses a value from a subsequent row. Both are useful for comparing consecutive records (e.g., month-over-month changes).

### Important Facts & Figures
- SQL was developed at IBM in the 1970s and standardized by ANSI in 1986.
- The logical order of SQL execution: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT.
- DISTINCT eliminates duplicate rows from query results.
- NULL represents the absence of a value; comparisons with NULL require IS NULL or IS NOT NULL (not = or !=).
- A CROSS JOIN produces the Cartesian product of two tables (every row combined with every other row).
- Indexes speed up data retrieval but slow down INSERT/UPDATE/DELETE operations due to index maintenance overhead.
- PARTITION BY in window functions divides the result set into partitions, similar to GROUP BY but without collapsing rows.
- Normalization (1NF, 2NF, 3NF) reduces data redundancy by organizing tables to minimize duplication.

### Common Exam Questions
- Q: Write a query to find the top 3 customers by total purchase amount.
- A: `SELECT customer_id, SUM(amount) AS total FROM orders GROUP BY customer_id ORDER BY total DESC LIMIT 3;`

- Q: Explain the difference between UNION and UNION ALL.
- A: UNION combines result sets from two queries and removes duplicates; UNION ALL combines them without removing duplicates (faster because no deduplication step).

- Q: Write a query using a window function to calculate a running total of sales by date.
- A: `SELECT date, amount, SUM(amount) OVER (ORDER BY date) AS running_total FROM sales;`

- Q: A query returns unexpected NULLs after a LEFT JOIN. What is the most likely cause?
- A: The right table has no matching rows for some left table records. LEFT JOIN preserves all left rows and fills right-side columns with NULL where no match exists. Check the join condition for correctness.

- Q: What is the difference between a correlated and non-correlated subquery?
- A: A non-correlated subquery runs independently and executes once; a correlated subquery references columns from the outer query and executes once per outer row, making it slower but more flexible.

---

## Data Cleaning

### Key Terms & Definitions
- **Data Cleaning (Data Cleansing/Scrubbing)**: The process of identifying and correcting errors, inconsistencies, and anomalies in datasets to improve data quality.
- **Missing Value**: An absent or null entry in a dataset caused by data entry errors, system failures, or non-response.
- **Imputation**: Filling in missing values using statistical methods (mean, median, mode) or predictive models.
- **Multiple Imputation**: Creating several plausible replacement datasets for missing values and pooling results for more robust inference.
- **Outlier**: A data point that significantly deviates from the overall pattern of the dataset.
- **IQR (Interquartile Range) Method**: Outlier detection method where values below Q1 - 1.5*IQR or above Q3 + 1.5*IQR are flagged as outliers.
- **Z-Score Method**: Outlier detection using standard deviations; values beyond 2-3 standard deviations from the mean are flagged.
- **Deduplication**: Identifying and removing duplicate records caused by data entry errors, system merges, or repeated imports.
- **Fuzzy Matching**: An approximate string matching technique used to identify near-duplicate records that differ slightly (e.g., "Jon Smith" vs. "John Smith").
- **Winsorizing**: Replacing extreme outlier values with the nearest non-outlier value (e.g., capping at the 5th and 95th percentiles) rather than removing them.
- **Validation Rules**: Domain-specific constraints applied to data (e.g., age must be positive, dates must be chronological) to flag invalid records.

### Core Concepts (Q&A Format)
- Q: What are the three main strategies for handling missing values?
- A: (1) Deletion -- removing incomplete records (listwise or pairwise); (2) Imputation -- replacing missing values with estimated values (mean, median, mode, model-predicted); (3) Flagging -- adding indicator variables to preserve missingness information.

- Q: When is mean imputation inappropriate?
- A: When data is skewed or contains outliers (the mean is distorted); when missingness is not random (biased estimates); and when the proportion of missing data is large (reduces variance artificially).

- Q: What is the difference between the IQR method and z-score method for outlier detection?
- A: IQR method uses quartiles (Q1, Q3) and is robust to non-normal distributions; z-score method assumes approximately normal distribution and flags values beyond 2-3 standard deviations.

- Q: Why should you document all data cleaning steps?
- A: For reproducibility, transparency, and audit trails -- allowing others to verify the cleaning process, understand what changes were made, and replicate the analysis.

- Q: What is the difference between exact matching and fuzzy matching for deduplication?
- A: Exact matching finds records with identical values; fuzzy matching uses string similarity algorithms (Levenshtein distance, Jaro-Winkler) to find near-duplicates with typos or formatting differences.

- Q: Should outlier detection happen before or after other preprocessing steps?
- A: Handle missing data and basic transformations first, then perform outlier detection, because missing values can affect the statistical measures (mean, IQR) used for outlier identification.

- Q: What is the difference between data cleaning and data preparation?
- A: Data cleaning is a subset of data preparation focused specifically on fixing errors and inconsistencies. Data preparation is broader, also including transformation, encoding, scaling, and feature engineering.

### Important Facts & Figures
- Poor data quality costs organizations an estimated $12.9 million annually (Gartner).
- The IQR method defines outliers as values below Q1 - 1.5*IQR or above Q3 + 1.5*IQR (where IQR = Q3 - Q1).
- Listwise deletion removes entire rows with any missing value; pairwise deletion uses all available data per analysis.
- MCAR (Missing Completely at Random), MAR (Missing at Random), and MNAR (Missing Not at Random) are the three patterns of missingness that determine which handling strategy is appropriate.
- Log transformation can normalize right-skewed distributions and reduce the impact of outliers.
- Python tools: `isnull()` detects missing values, `drop_duplicates()` removes duplicates, `replace()` standardizes inconsistent labels.
- DBSCAN (density-based clustering) can be used for outlier detection in multidimensional data.

### Common Exam Questions
- Q: A dataset has a column with values [10, 12, 11, 13, 95, 12, 11]. Identify the outlier and explain your method.
- A: Q1=11, Q3=13, IQR=2. Lower bound: 11-3=8, Upper bound: 13+3=16. The value 95 exceeds the upper bound and is an outlier. It should be investigated for data entry error, then removed, capped, or transformed.

- Q: Compare listwise deletion and mean imputation for a dataset with 5% missing values in one column.
- A: With only 5% missingness, listwise deletion is acceptable if data is MCAR (minimal information loss). Mean imputation preserves sample size but artificially reduces variance. For such a small proportion, either approach is reasonable.

- Q: Describe a complete data cleaning workflow for a new dataset.
- A: (1) Profile data with summary statistics and visualizations; (2) Handle missing values through deletion or imputation; (3) Detect and treat outliers; (4) Remove duplicates; (5) Standardize formats and fix inconsistencies; (6) Apply validation rules; (7) Document all steps.

- Q: What are the risks of removing all outliers from a dataset?
- A: Legitimate extreme values may represent important phenomena (e.g., fraud, rare events). Removing them can bias results, reduce variance, and eliminate valuable information. Always investigate outliers before removing them.

---

## ETL

### Key Terms & Definitions
- **ETL (Extract, Transform, Load)**: A three-phase data integration process that extracts data from sources, transforms it to fit target requirements, and loads it into a destination system.
- **ELT (Extract, Load, Transform)**: A variant where raw data is loaded into the target system first, then transformed in-place using the target's processing power.
- **Extract**: The phase where data is read from heterogeneous source systems (databases, files, APIs) into a staging area.
- **Transform**: The phase where data is cleansed, validated, deduplicated, reformatted, and restructured to conform to the target schema.
- **Load**: The phase where transformed data is written to the target system (data warehouse, data lake, data mart).
- **Staging Area**: A temporary storage location where extracted data is held during the transformation phase before loading.
- **Data Warehouse**: A centralized repository of integrated data from multiple sources, optimized for analytical queries and reporting.
- **Data Lake**: A storage repository that holds raw data in its native format until needed for analysis, supporting both structured and unstructured data.
- **Incremental Loading**: Loading only new or changed records since the last extraction, identified via timestamps or Change Data Capture (CDC).
- **Full Refresh**: Replacing all data in the target with a complete new extraction, simpler but more resource-intensive.
- **Change Data Capture (CDC)**: A technique that identifies and captures only the data that has changed since the last extraction.
- **Data Pipeline**: The end-to-end flow of data from source to destination, encompassing extraction, transformation, loading, and orchestration.

### Core Concepts (Q&A Format)
- Q: What is the key difference between ETL and ELT?
- A: ETL transforms data before loading into the target; ELT loads raw data first and transforms in-place using the target system's compute power. ELT is preferred for modern cloud warehouses (Snowflake, BigQuery, Redshift) that have powerful processing engines.

- Q: When would you choose incremental loading over full refresh?
- A: For large datasets where full refresh is too slow or resource-intensive, when only a small percentage of records change between loads, and when near-real-time data availability is needed.

- Q: What is the purpose of a staging area in ETL?
- A: It provides a temporary workspace to hold extracted data during transformation, isolating source systems from target systems and allowing quality checks before loading.

- Q: What is the difference between a data warehouse and a data lake?
- A: A data warehouse stores structured, transformed, schema-on-write data optimized for analytics; a data lake stores raw data in native format (structured and unstructured) with schema-on-read, offering more flexibility but requiring more processing at query time.

- Q: What is batch ETL vs. streaming ETL?
- A: Batch ETL runs on scheduled intervals (hourly, daily) and processes accumulated data in bulk. Streaming ETL processes data continuously in near-real-time using tools like Apache Kafka or Spark Streaming.

- Q: What role does orchestration play in ETL?
- A: Orchestration tools (e.g., Apache Airflow) manage the scheduling, dependencies, monitoring, and error handling of ETL pipeline tasks, ensuring they execute in the correct order and recover from failures.

- Q: What is a data mart and how does it differ from a data warehouse?
- A: A data mart is a subset of a data warehouse focused on a specific business area (e.g., sales, marketing). It contains pre-aggregated data for faster query performance for a particular department.

### Important Facts & Figures
- ETL has been used since the 1970s and remains the backbone of enterprise data integration.
- Modern cloud data warehouses (Snowflake, BigQuery, Redshift) have shifted the industry toward ELT due to their massive in-platform compute capabilities.
- Apache Airflow is the most popular open-source workflow orchestration tool for ETL pipelines.
- dbt (data build tool) is the leading transformation tool in ELT architectures, enabling SQL-based transformations with version control and testing.
- Common ETL tools: Informatica, Talend, AWS Glue, Azure Data Factory, Apache NiFi, and custom Python scripts using pandas/SQLAlchemy.
- CDC methods include log-based (reading database transaction logs), trigger-based (database triggers on changes), and timestamp-based (comparing last-modified dates).
- ETL failure modes include schema drift (source schema changes break the pipeline), data quality issues, and timeout/resource constraints.
- The "T" in ETL typically includes: data type conversion, deduplication, null handling, business rule application, aggregation, and key generation.

### Common Exam Questions
- Q: Design a basic ETL pipeline for loading daily sales data into a data warehouse.
- A: Extract: Connect to the transactional database and pull records where transaction_date = yesterday. Transform: Join with product and customer dimension tables, validate data types, handle nulls, calculate derived metrics (revenue = quantity x price). Load: Insert transformed records into the fact_sales table in the warehouse using incremental append.

- Q: What are the advantages and disadvantages of ELT compared to traditional ETL?
- A: Advantages: faster loading (no pre-processing delay), leverages cloud compute power, preserves raw data for flexible transformations. Disadvantages: requires powerful target system, raw data in target may pose security/governance concerns, transformation logic is target-system dependent.

- Q: Explain Change Data Capture and its importance in ETL.
- A: CDC identifies only the records that have changed (inserted, updated, deleted) since the last extraction. It dramatically reduces data volume transferred and processing time, enabling more frequent and efficient incremental loads.

- Q: What happens when an ETL pipeline fails mid-process? How should it be handled?
- A: Implement idempotent operations (re-runnable without side effects), use staging tables with transaction control, log all steps for debugging, set up alerting/monitoring, and design retry mechanisms. Failed loads should be rollback-safe to prevent partial data in the target.

---
