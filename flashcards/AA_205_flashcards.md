# AA 205: Introduction to Applied Analytics - Flashcard Reference Bank

---

## Applied Analytics

### Key Terms & Definitions
- **Applied Analytics**: The strategic use of data, statistical methods, and computational techniques to transform raw information into actionable business insights
- **Descriptive Analytics**: Analytics that answers "What happened?" by summarizing historical data through dashboards and reports
- **Diagnostic Analytics**: Analytics that answers "Why did it happen?" using drill-down analysis, correlation, and segmentation to identify root causes
- **Predictive Analytics**: Analytics that answers "What will happen?" by applying regression, forecasting, and machine learning to project future outcomes
- **Prescriptive Analytics**: Analytics that answers "What should we do?" by combining predictive models with optimization techniques and simulations to recommend optimal actions
- **Business Intelligence (BI)**: The technologies, practices, and strategies used to collect, integrate, analyze, and present business data to support decision-making
- **A/B Testing**: A controlled experiment comparing two versions (A and B) of a variable to determine which performs better on a defined metric
- **Hypothesis Testing**: A statistical method used to decide whether there is enough evidence to reject a null hypothesis about a population parameter
- **Analytics Pipeline**: The end-to-end workflow of data collection, cleaning, exploratory analysis, modeling, validation, deployment, and monitoring
- **Data-Driven Decision Making**: The practice of basing organizational decisions on verified, analyzed data rather than intuition or observation alone

### Core Concepts (Q&A Format)
- Q: What is the analytics maturity spectrum and what order do the four types follow?
- A: The spectrum progresses from Descriptive (what happened) to Diagnostic (why it happened) to Predictive (what will happen) to Prescriptive (what should we do). Each level builds on the previous and adds more value.

- Q: How does predictive analytics differ from prescriptive analytics?
- A: Predictive analytics forecasts what is likely to happen using statistical models and machine learning. Prescriptive analytics goes further by recommending specific actions to optimize outcomes based on those predictions.

- Q: What are the stages of the analytics pipeline?
- A: Data collection, data cleaning, exploratory analysis, modeling, validation, deployment, and monitoring -- forming a continuous improvement cycle.

- Q: Why is domain expertise important in applied analytics?
- A: Domain expertise provides context for interpreting analytical results, helps frame the right questions, ensures models are meaningful in real-world settings, and enables effective communication of findings to stakeholders.

- Q: What is the difference between structured and unstructured data in analytics?
- A: Structured data is organized in predefined formats (databases, spreadsheets) and is easily searchable. Unstructured data (emails, social media, images) lacks predefined format and requires specialized techniques like NLP to analyze.

- Q: Give a real-world example of each analytics type.
- A: Descriptive: monthly sales dashboard. Diagnostic: analyzing why Q3 revenue dropped (found pricing change was the cause). Predictive: forecasting next quarter's customer churn rate. Prescriptive: recommending optimal delivery routes based on traffic and weather data.

- Q: What common tools are used in applied analytics?
- A: Python (pandas, scikit-learn), R, Tableau, Power BI, SQL, TensorFlow, Excel, and SAS.

### Important Facts & Figures
- Approximately 80% of business data exists in unstructured form (text, images, video)
- The four analytics types form a maturity model: organizations typically start with descriptive and progress toward prescriptive
- A/B testing is considered the gold standard for establishing causal relationships in business experiments
- The analytics pipeline is iterative, not linear -- monitoring results feeds back into data collection
- Prescriptive analytics provides the highest business value but requires the most sophisticated techniques
- Python and R are the two most widely used programming languages for applied analytics
- Statistical literacy, critical thinking, and data communication are considered core non-technical skills for analysts

### Common Exam Questions
- Q: List and define the four types of analytics in order of increasing complexity. For each, provide the key question it answers and one example.
- A: (1) Descriptive -- "What happened?" -- e.g., sales report. (2) Diagnostic -- "Why did it happen?" -- e.g., root cause analysis. (3) Predictive -- "What will happen?" -- e.g., demand forecasting. (4) Prescriptive -- "What should we do?" -- e.g., route optimization.

- Q: Describe the analytics pipeline and explain why it is considered a cycle rather than a linear process.
- A: The pipeline includes collection, cleaning, exploration, modeling, validation, deployment, and monitoring. It is a cycle because monitoring results reveal new questions and data quality issues that feed back into earlier stages.

- Q: What is the role of A/B testing in applied analytics, and how does it relate to hypothesis testing?
- A: A/B testing is a practical application of hypothesis testing where two versions of a variable are compared. A null hypothesis (no difference) is tested statistically, and results determine which version performs better.

- Q: Compare and contrast business intelligence (BI) and applied analytics.
- A: BI focuses on descriptive reporting -- dashboards, KPIs, and historical summaries. Applied analytics extends beyond BI into diagnostic, predictive, and prescriptive methods to generate forward-looking, actionable insights.

---

## Data Visualization

### Key Terms & Definitions
- **Data Visualization**: The graphical representation of data using visual elements like charts, graphs, and maps to make complex data accessible and actionable
- **Lie Factor**: The ratio of the size of effect shown in a graphic to the size of effect in the data; ideally between 0.95 and 1.05
- **Data-Ink Ratio**: The proportion of a graphic's ink devoted to the non-redundant display of data-information; should be maximized
- **Chart Junk**: Decorative, non-informational elements in a visualization that clutter the display and reduce the data-ink ratio
- **Small Multiples**: A series of similar graphs or charts using the same scale and axes, allowing comparisons across different categories or time periods
- **Graphical Integrity**: Tufte's principle that visual representations must accurately and truthfully represent the underlying data
- **Data Density**: The amount of data displayed per unit area of a graphic; higher density is generally preferred
- **Edward Tufte**: Yale professor widely regarded as the leading authority on data visualization design and graphical integrity
- **Data Encoding**: The method by which data values are mapped to visual properties such as position, length, angle, area, color, or shape
- **Sparkline**: A small, word-sized graphic embedded in text or a table, coined by Tufte, showing data trends without axes or labels

### Core Concepts (Q&A Format)
- Q: What is the Lie Factor and how do you calculate it?
- A: Lie Factor = (size of effect shown in graphic) / (size of effect in data). A value of 1.0 means perfect accuracy. Values between 0.95 and 1.05 are acceptable. Values far from 1 indicate the graphic distorts the truth.

- Q: What are Tufte's five principles related to data-ink?
- A: (1) Above all else, show the data. (2) Maximize the data-ink ratio. (3) Erase non-data-ink. (4) Erase redundant data-ink. (5) Revise and edit.

- Q: Rank the data encoding methods from most to least perceptually accurate.
- A: Position (most accurate) > Aligned lengths > Angles > Area > Brightness > Color hue > Shape (least accurate). Position-based encodings (like bar charts and scatter plots) are the most precisely interpreted.

- Q: When should you use a bar chart vs. a line chart vs. a scatter plot?
- A: Bar charts compare categories. Line charts show trends over time. Scatter plots reveal relationships between two continuous variables.

- Q: What are the most common data visualization pitfalls?
- A: Truncated axes that exaggerate differences, 3D effects that distort proportions, dual-axis charts that imply false correlations, and excessive color palettes that obscure rather than clarify.

- Q: Why does Tufte advocate for small multiples?
- A: Small multiples allow the viewer to compare patterns across many dimensions simultaneously using a consistent scale, making differences and trends easier to spot than in a single complex chart.

- Q: What is the difference between data variation and design variation?
- A: Data variation reflects actual differences in the data (desirable). Design variation reflects changes in graphic appearance unrelated to data (undesirable and misleading).

### Important Facts & Figures
- Tufte's Lie Factor should stay between 0.95 and 1.05 for graphical integrity
- Position is the most perceptually accurate data encoding method; shape is the least
- Tufte published "The Visual Display of Quantitative Information" in 1983, considered a foundational text
- The data-ink ratio = (data-ink) / (total ink used in the graphic)
- Tufte identified six principles of graphical integrity, including proportional representation and showing data in context
- Pie charts are generally discouraged because they rely on angle encoding, which humans perceive poorly
- Heat maps are effective for displaying density patterns across two dimensions
- Labels and annotations placed directly on the graphic are preferred over external legends

### Common Exam Questions
- Q: Define the Lie Factor. A visualization shows a 50% increase in data but the graphic element appears 150% larger. What is the Lie Factor, and does it violate graphical integrity?
- A: Lie Factor = 150/50 = 3.0. This significantly exceeds the acceptable range of 0.95-1.05, so yes, it violates graphical integrity.

- Q: What is the data-ink ratio and why does Tufte argue it should be maximized?
- A: The data-ink ratio is the proportion of ink in a graphic devoted to displaying actual data. Maximizing it removes chart junk and redundancy, focusing the viewer's attention on the data itself.

- Q: Identify three common visualization pitfalls and explain how each distorts the viewer's understanding.
- A: (1) Truncated axes exaggerate small differences by removing context. (2) 3D effects distort proportions through perspective. (3) Dual-axis charts can imply false correlations between unrelated variables by manipulating scales.

- Q: Match the chart type to its best use case: bar chart, line chart, scatter plot, histogram, heat map.
- A: Bar chart = comparing categories. Line chart = trends over time. Scatter plot = relationships between variables. Histogram = distribution of a single variable. Heat map = density patterns across two dimensions.

---

## Text Mining

### Key Terms & Definitions
- **Text Mining**: The process of extracting meaningful information from unstructured text data using NLP, machine learning, and statistical techniques
- **Sentiment Analysis**: A technique that determines the emotional tone of text (positive, negative, neutral) from documents, reviews, or social media
- **Topic Modeling**: An unsupervised method that discovers abstract themes or topics across a collection of documents; LDA is the most common algorithm
- **Tokenization**: The process of splitting text into individual words, phrases, or meaningful units (tokens) as a preprocessing step
- **Stemming**: Reducing words to their root form by removing suffixes (e.g., "running" becomes "run"); crude but fast
- **Lemmatization**: Reducing words to their dictionary base form using vocabulary and morphological analysis (e.g., "better" becomes "good"); more accurate than stemming
- **Stop Words**: Common words (the, is, and, a) that are typically removed during preprocessing because they carry little analytical value
- **Named Entity Recognition (NER)**: The task of identifying and classifying named entities (people, organizations, locations, dates) in text
- **Latent Dirichlet Allocation (LDA)**: A generative probabilistic model used for topic modeling that assumes documents are mixtures of topics
- **TF-IDF (in text mining context)**: Term Frequency-Inverse Document Frequency; a statistical measure that evaluates how important a word is to a document relative to an entire corpus
- **F1-Score**: The harmonic mean of precision and recall, providing a single metric that balances both; used to evaluate text classification models

### Core Concepts (Q&A Format)
- Q: What is the text mining preprocessing pipeline and why is each step important?
- A: Language identification, tokenization, stemming/lemmatization, stop word removal, part-of-speech tagging, and syntax parsing. Each step reduces noise and normalizes text so algorithms can extract meaningful patterns.

- Q: What is the difference between stemming and lemmatization?
- A: Stemming chops off word endings using rules (fast but imprecise -- "studies" becomes "studi"). Lemmatization uses a dictionary to find the true root form ("studies" becomes "study"). Lemmatization is more accurate but slower.

- Q: How does sentiment analysis work and what are its main approaches?
- A: Sentiment analysis classifies text as positive, negative, or neutral. Approaches include lexicon-based (using dictionaries of sentiment words), machine learning-based (trained classifiers), and deep learning-based (neural networks like transformers).

- Q: What is topic modeling and how does LDA work?
- A: Topic modeling discovers hidden themes in document collections. LDA assumes each document is a mixture of topics, and each topic is a distribution over words. It uses probabilistic inference to assign words to topics.

- Q: How does text mining differ from NLP?
- A: NLP is the broader field of enabling computers to understand and generate human language. Text mining specifically focuses on extracting patterns and actionable knowledge from text corpora. Text mining uses NLP techniques as tools.

- Q: What evaluation metrics are used for text classification tasks?
- A: Precision (of predicted positives, how many are correct), recall (of actual positives, how many were found), F1-score (harmonic mean of precision and recall), and accuracy (overall correct predictions).

- Q: Why is text mining important for business?
- A: An estimated 80% of business data is unstructured text. Text mining unlocks insights from customer reviews, emails, social media, and documents that would be impossible to analyze manually at scale.

### Important Facts & Figures
- Approximately 80% of business data exists in unstructured text form
- LDA (Latent Dirichlet Allocation) is the most widely used topic modeling algorithm
- NMF (Non-negative Matrix Factorization) is an alternative to LDA for topic modeling
- Precision = True Positives / (True Positives + False Positives)
- Recall = True Positives / (True Positives + False Negatives)
- F1-Score = 2 x (Precision x Recall) / (Precision + Recall)
- Common data sources for text mining: customer reviews, social media, news articles, emails, support tickets, legal documents
- Tokenization is always the first step after language identification in the preprocessing pipeline

### Common Exam Questions
- Q: List and describe the five core text mining techniques.
- A: (1) Sentiment analysis -- determines emotional tone. (2) Topic modeling -- discovers themes across documents. (3) Text classification -- assigns predefined categories. (4) Named entity recognition -- identifies people, places, organizations. (5) Document clustering -- groups similar texts without predefined labels.

- Q: Describe the text preprocessing pipeline in order, and explain the purpose of each step.
- A: (1) Language identification -- determines the language. (2) Tokenization -- splits text into words. (3) Stop word removal -- filters common words. (4) Stemming/lemmatization -- reduces words to roots. (5) POS tagging -- labels grammatical roles. (6) Syntax parsing -- analyzes sentence structure. Purpose: prepare clean, normalized text for analysis.

- Q: Compare precision and recall. In what scenario would you prioritize recall over precision?
- A: Precision measures accuracy of positive predictions; recall measures completeness. Prioritize recall when missing a positive case is costly (e.g., detecting disease, fraud detection) even if it means more false positives.

- Q: Explain the difference between text classification and document clustering.
- A: Text classification is supervised -- it assigns documents to predefined categories using labeled training data. Document clustering is unsupervised -- it groups documents by similarity without predefined labels, discovering natural groupings.

---

## Data Mining

### Key Terms & Definitions
- **Data Mining**: The process of discovering patterns, correlations, and anomalies in large datasets using machine learning, statistics, and database methods
- **KDD (Knowledge Discovery in Databases)**: The broader process of extracting high-level knowledge from raw data, of which data mining is the core analysis step
- **CRISP-DM**: Cross-Industry Standard Process for Data Mining; the most widely used data mining methodology (~43% adoption), consisting of six iterative phases
- **SEMMA**: SAS Institute's data mining methodology: Sample, Explore, Modify, Model, Assess
- **Association Rule Mining**: Discovering relationships between variables in datasets (e.g., market basket analysis: customers who buy bread often buy butter)
- **Classification**: Assigning data points to predefined categories using algorithms like decision trees, naive Bayes, and SVMs
- **Clustering**: Grouping similar data points without predefined labels using methods like k-means and hierarchical clustering
- **Anomaly Detection**: Identifying unusual observations that deviate significantly from expected patterns in a dataset
- **Decision Tree**: A classification algorithm that splits data into branches based on feature values, creating a tree-like model of decisions
- **K-Means Clustering**: An algorithm that partitions data into k clusters by minimizing the distance between points and their assigned cluster center (centroid)
- **Support Vector Machine (SVM)**: A classification algorithm that finds the optimal hyperplane separating different classes with maximum margin
- **Cross-Validation**: A model evaluation technique that partitions data into subsets, training on some and testing on others, to assess generalizability

### Core Concepts (Q&A Format)
- Q: What are the five stages of the KDD process?
- A: (1) Selection -- choosing relevant data. (2) Preprocessing -- cleaning and handling missing values. (3) Transformation -- normalizing and reducing dimensionality. (4) Data Mining -- applying algorithms. (5) Interpretation/Evaluation -- validating and presenting results.

- Q: What are the six phases of CRISP-DM and what makes it different from KDD?
- A: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment. Unlike KDD's sequential approach, CRISP-DM is iterative -- outcomes from any phase can loop back to earlier stages.

- Q: Compare classification and clustering.
- A: Classification is supervised (uses labeled training data to assign predefined categories). Clustering is unsupervised (groups data by similarity without predefined labels). Classification predicts known categories; clustering discovers unknown groupings.

- Q: What is association rule mining and what is market basket analysis?
- A: Association rule mining finds relationships between variables. Market basket analysis is its most famous application -- discovering which products are frequently purchased together (e.g., bread and butter) to inform store layout and promotions.

- Q: How do you evaluate a data mining model?
- A: Using metrics like accuracy, precision, recall, F1-score, and ROC curves. Cross-validation tests the model on unseen data to assess generalizability and guard against overfitting.

- Q: What is the difference between CRISP-DM and SEMMA?
- A: CRISP-DM is a comprehensive project methodology covering business understanding through deployment (6 phases, 24 tasks). SEMMA is a narrower technical workflow focused on the modeling process itself (Sample, Explore, Modify, Model, Assess). CRISP-DM includes business context; SEMMA focuses on statistical rigor.

- Q: What is anomaly detection and where is it applied?
- A: Anomaly detection identifies data points that deviate significantly from expected patterns. Applications include fraud detection in financial transactions, network intrusion detection, manufacturing defect identification, and medical diagnosis.

### Important Facts & Figures
- CRISP-DM has approximately 43% adoption as the most widely used data mining methodology
- CRISP-DM was published in 1999/2000 and consists of 6 phases and 24 tasks
- KDD assumes sequential execution; CRISP-DM emphasizes iterative execution
- SEMMA was developed by SAS Institute
- Common classification algorithms: decision trees, naive Bayes, SVM, random forests, neural networks
- Common clustering algorithms: k-means, hierarchical clustering, DBSCAN
- ROC curve plots true positive rate vs. false positive rate; AUC (area under curve) near 1.0 indicates a good classifier
- Data mining is the core step within the broader KDD process

### Common Exam Questions
- Q: Compare and contrast the KDD, CRISP-DM, and SEMMA methodologies. Include phases and key differences.
- A: KDD: 5 sequential stages (Selection, Preprocessing, Transformation, Mining, Interpretation). CRISP-DM: 6 iterative phases (Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment). SEMMA: 5 technical phases (Sample, Explore, Modify, Model, Assess). Key difference: KDD is sequential, CRISP-DM is iterative with business focus, SEMMA is technically focused.

- Q: Explain the five core data mining methods with examples.
- A: (1) Association rules -- market basket analysis. (2) Classification -- spam email detection. (3) Clustering -- customer segmentation. (4) Regression -- predicting house prices. (5) Anomaly detection -- credit card fraud detection.

- Q: A retail company wants to discover which products are frequently bought together. Which data mining method should they use, and why?
- A: Association rule mining (market basket analysis). It discovers co-occurrence patterns in transactional data, revealing item pairs/groups frequently purchased together. This informs product placement, cross-selling, and bundle promotions.

- Q: Define overfitting and explain how cross-validation helps prevent it.
- A: Overfitting occurs when a model learns noise in training data and performs poorly on new data. Cross-validation partitions data into training and test sets across multiple folds, ensuring the model is evaluated on unseen data and generalizes well.

---

## Cross-Disciplinary Analytics

### Key Terms & Definitions
- **Cross-Disciplinary Analytics**: The application of data science methods across multiple fields, integrating knowledge from computer science, statistics, and specific application domains
- **Data Science**: An interdisciplinary field synthesizing statistics, informatics, computing, communication, management, and sociology to study data and its environments
- **Three Pillars of Data Science**: (1) Computer science and technology, (2) Mathematics and statistics, (3) Domain expertise
- **Domain Expertise**: Subject-matter knowledge in a specific field that gives context and meaning to analytical results
- **Precision Medicine**: Using data analytics to develop personalized treatment plans based on a patient's genetic makeup and health history
- **Algorithmic Trading**: Using data-driven models and automated systems to execute trades in financial markets based on analytical signals
- **Data Storytelling**: The practice of communicating data insights through narrative, context, and visualization to drive understanding and action
- **Interdisciplinary Team**: A group of professionals from different fields (e.g., statisticians, domain experts, engineers) collaborating on data problems
- **Heterogeneous Data**: Data from multiple sources with varying formats, scales, quality standards, and structures that must be integrated for analysis

### Core Concepts (Q&A Format)
- Q: What are the three pillars of data science and why are all three necessary?
- A: (1) Computer science/technology (data engineering, programming). (2) Mathematics/statistics (modeling, inference). (3) Domain expertise (subject-matter knowledge). All three are needed because technical skills without domain knowledge produce meaningless results, and domain knowledge without technical skills cannot leverage data at scale.

- Q: How is cross-disciplinary analytics applied in healthcare?
- A: Healthcare combines medical expertise with machine learning for personalized treatment plans, drug discovery, clinical decision support, disease prediction, and analyzing genomic data alongside clinical records for precision medicine.

- Q: What are the main challenges of cross-disciplinary analytics?
- A: (1) Communication barriers -- different disciplines use different jargon and methodologies. (2) Data integration -- heterogeneous sources with varying formats and quality. (3) Building shared mental models across team members with different training backgrounds.

- Q: How does cross-disciplinary analytics apply in public policy?
- A: Analytics is used for crime pattern identification, traffic optimization, transit planning, fair housing analysis, education financing, and evidence-based policy design by combining social science with statistical methods.

- Q: What distinguishes cross-disciplinary analytics from traditional analytics?
- A: Traditional analytics typically operates within a single domain. Cross-disciplinary analytics deliberately integrates methods and knowledge across fields, generating insights that no single discipline could produce alone.

- Q: Why is data communication and storytelling a core skill in cross-disciplinary work?
- A: Because team members and stakeholders come from different backgrounds, analysts must translate complex findings into accessible narratives. Without effective communication, even the best analytical insights will fail to drive decisions.

### Important Facts & Figures
- Data science is formally defined as an interdisciplinary field combining statistics, informatics, computing, communication, management, and sociology
- Precision medicine combines genomic data with clinical records to personalize treatments
- Climate modeling, pollution tracking, and biodiversity monitoring are key environmental analytics applications
- Algorithmic trading and risk modeling are primary cross-disciplinary finance applications
- Communication barriers are consistently cited as the top challenge in cross-disciplinary analytics teams
- The three pillars model (CS + Math/Stats + Domain) is the dominant framework for understanding data science competencies
- Cross-disciplinary analytics drives innovation by connecting analytical methods with real-world domain problems
- Customer journey optimization integrates behavioral psychology with predictive analytics

### Common Exam Questions
- Q: Name and describe the three pillars of data science. Explain why a professional lacking one pillar would be limited.
- A: (1) Computer Science -- programming, data engineering. (2) Math/Statistics -- modeling, inference, probability. (3) Domain Expertise -- subject-matter context. A professional lacking domain expertise might build technically sound models that are meaningless in practice. One lacking statistics might misinterpret results. One lacking CS cannot implement solutions at scale.

- Q: Give three examples of cross-disciplinary analytics applications across different industries.
- A: (1) Healthcare -- precision medicine using genomic + clinical data. (2) Environmental science -- climate modeling combining satellite imagery with socioeconomic data. (3) Finance -- fraud detection combining network analysis with behavioral patterns.

- Q: What are the key challenges of working in cross-disciplinary analytics teams, and how can they be addressed?
- A: Challenges: communication barriers (different jargon), data integration (heterogeneous formats), and building shared mental models. Solutions: establish common vocabulary, use standardized data formats, conduct regular cross-training sessions, and employ data storytelling to bridge understanding gaps.

- Q: Explain how cross-disciplinary analytics could be applied to improve disaster relief planning.
- A: By integrating satellite imagery (remote sensing), socioeconomic data (demographics, infrastructure), weather models (meteorology), and historical disaster records (emergency management), teams can predict vulnerable areas, optimize resource allocation, and improve response time.

---
