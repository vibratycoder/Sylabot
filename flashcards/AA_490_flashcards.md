# AA 490: Applied Analytics Capstone - Flashcard Reference Bank

---

## Capstone Project

### Key Terms & Definitions
- **Capstone Project**: A culminating academic experience where students integrate skills from prior coursework to solve a real-world data problem end-to-end
- **High-Impact Practice (HIP)**: An educational approach recognized for significantly increasing student engagement and learning; capstones are a recognized HIP
- **Data Science Methodology**: A step-by-step iterative framework (developed by John Rollins) ensuring analytics projects are structured, repeatable, and goal-oriented
- **Project Charter**: A document that defines the business objectives, scope, timeline, resources, constraints, and deliverables of a project
- **Exploratory Data Analysis (EDA)**: Initial investigation of data using summary statistics and visualizations to discover patterns, spot anomalies, and check assumptions
- **Model Evaluation**: The process of assessing model performance using metrics such as accuracy, precision, recall, F1-score, and RMSE
- **Scope Creep**: The uncontrolled expansion of a project's requirements beyond the original objectives; a common risk in capstone projects
- **Deliverables**: The tangible outputs of a project, typically including technical reports, final project reports, code repositories, and formal presentations
- **5W1H Method**: A systematic questioning technique (Who, What, Where, When, Why, How) used to thoroughly understand a business problem
- **Analytic Approach**: The phase where the problem is framed in machine learning or statistical terms and appropriate techniques are selected

### Core Concepts (Q&A Format)
- Q: What are the main phases of a capstone analytics project workflow?
- A: Problem definition, data collection, exploratory analysis, preprocessing, model building, evaluation, and results communication

- Q: Why are capstone projects considered a High-Impact Practice?
- A: They bridge theory and practice by requiring students to independently scope real problems, select methods, handle messy real-world data, and communicate findings -- developing both technical and soft skills simultaneously

- Q: What is the role of the project charter in a capstone?
- A: It formally defines the business problem, objectives, scope, timeline, resources, and deliverables, ensuring alignment between the project goals and stakeholder expectations before work begins

- Q: What four types of analytics must be considered when defining the analytic approach?
- A: Descriptive (what happened), Diagnostic (why), Predictive (what will happen), Prescriptive (what to do)

- Q: How does the 5W1H method contribute to business understanding?
- A: It ensures comprehensive problem exploration by asking: Who is involved, What is the problem, Where does it occur, When does it happen, Why is it important, and How will it be addressed

- Q: What makes a capstone project different from a regular class assignment?
- A: Capstones require end-to-end execution with real-world data, independent decision-making on methodology, handling ambiguity, and communicating results to diverse audiences -- mirroring professional analytics work

- Q: What are common evaluation metrics used in capstone projects?
- A: Accuracy, Precision, Recall, F1-Score (for classification); RMSE, MAE, R-squared (for regression); Silhouette Score (for clustering)

- Q: What is the most common reason capstone projects fail or underdeliver?
- A: Poor problem definition and scope creep. Without a clearly defined, feasible question and bounded scope, projects drift and produce unfocused results.

### Important Facts & Figures
- Data Science Methodology follows an iterative process -- earlier phases are revisited as new insights emerge
- Data preparation typically consumes 60-80% of total project time, even in capstone settings
- Capstone projects require three types of deliverables: technical reports, final project reports (including challenges faced), and formal presentations
- The analytic approach phase determines whether the project uses classification, regression, clustering, or another technique
- Real-world datasets are messy: missing values, inconsistencies, and formatting issues are expected challenges
- Capstone projects develop both hard skills (coding, modeling, statistics) and soft skills (communication, project management, critical thinking)
- Proper documentation of all analytical steps is required for reproducibility and academic rigor

### Common Exam Questions
- Q: Describe the end-to-end workflow for an analytics capstone project.
- A: Begin with business understanding and problem definition using 5W1H. Determine the analytic approach. Collect and understand data through EDA. Prepare data (clean, transform, handle missing values). Build and train models. Evaluate model performance against business objectives. Communicate findings through reports and presentations. Document all steps for reproducibility.

- Q: You are starting a capstone project on predicting customer churn. What would your project charter include?
- A: Business objective (reduce churn by X%), problem statement (identify at-risk customers), scope (which customer segments, time period), data sources (CRM data, transaction logs, support tickets), analytic approach (classification -- predictive analytics), success criteria (model accuracy targets), timeline and milestones, deliverables (model, report, presentation).

- Q: Why is iterating back to earlier phases common in data science methodology?
- A: New discoveries during data understanding or modeling often reveal issues with problem framing, data quality, or approach selection. For example, EDA may reveal insufficient data for the original question, requiring scope revision.

- Q: Compare how a capstone project differs from the academic exercises completed in prerequisite courses like AA 306.
- A: Prerequisite courses teach individual techniques in isolation with clean datasets. Capstones require selecting and combining multiple techniques, working with real messy data, managing an entire project lifecycle, and making independent analytical decisions.

---

## Integrated Analytics

### Key Terms & Definitions
- **Integrated Analytics**: The end-to-end process of combining data acquisition, preparation, analysis, modeling, and communication into a cohesive analytical workflow
- **Data Pipeline**: An automated sequence of processes that moves data from source systems through transformation stages to a destination for analysis
- **ETL (Extract, Transform, Load)**: A three-phase data integration process: extract data from sources, transform it into a usable format, and load it into a target system
- **ELT (Extract, Load, Transform)**: A modern alternative where raw data is loaded first into cloud storage, then transformed in-place using the destination's compute resources
- **Data Warehouse**: A centralized repository that stores structured, processed data optimized for analytical querying and reporting
- **Data Lake**: A storage repository that holds vast amounts of raw data in its native format until needed for analysis
- **Data Ingestion**: The process of collecting and importing data from various sources into a storage system for processing
- **Data Wrangling/Munging**: The process of cleaning, restructuring, and enriching raw data into a usable format for analysis
- **API (Application Programming Interface)**: A set of protocols allowing different software applications to communicate and share data
- **Feature Engineering**: The process of creating new variables from raw data to improve model performance
- **Data Validation**: The process of checking data against rules and constraints to ensure accuracy, completeness, and consistency

### Core Concepts (Q&A Format)
- Q: What are the five stages of an integrated analytics pipeline?
- A: Data ingestion (gathering from sources), processing (cleaning, transformation, validation, merging), storage (warehouses or data lakes), analysis and modeling, visualization and reporting

- Q: What is the difference between ETL and ELT?
- A: ETL transforms data before loading it into the destination (traditional approach). ELT loads raw data first, then transforms it in the destination using its compute power (modern cloud approach). ELT is faster for large datasets and more flexible.

- Q: What is the difference between a data warehouse and a data lake?
- A: A data warehouse stores structured, processed data optimized for queries (schema-on-write). A data lake stores raw data in any format until needed (schema-on-read). Warehouses are for reporting; lakes are for exploration and advanced analytics.

- Q: Why is data validation important in an integrated pipeline?
- A: Without validation, errors propagate downstream -- a concept called "garbage in, garbage out." Validation catches missing values, format inconsistencies, duplicates, and out-of-range values before they corrupt analysis.

- Q: What skills are needed to build integrated analytics workflows?
- A: Connecting diverse data sources, data cleaning and transformation, selecting appropriate analytical methods, combining statistics/ML/visualization, programming (Python/R/SQL), and understanding business context

- Q: Why do real-world problems require integrated analytics rather than a single technique?
- A: Real problems involve multiple data sources, require various analytical techniques (statistics, ML, visualization), and demand end-to-end pipelines from raw data to actionable insights. No single technique covers the full workflow.

- Q: What role does feature engineering play in integrated analytics?
- A: Feature engineering creates meaningful input variables from raw data (e.g., calculating customer lifetime value from transaction records), directly impacting model accuracy and interpretability.

### Important Facts & Figures
- ETL is the traditional approach; ELT is the modern cloud-native approach gaining dominance
- Data pipelines automate the flow of data, reducing manual effort and human error
- Common pipeline orchestration tools include Apache Airflow, dbt, and cloud-native services
- Data integration typically involves combining data from 3-10+ different source systems in enterprise settings
- Data quality issues cost organizations an estimated 15-25% of revenue according to industry research
- The "garbage in, garbage out" principle is foundational: poor input data guarantees poor analytical outputs
- Real-time analytics pipelines process data within seconds to minutes; batch pipelines process on scheduled intervals (hourly, daily)
- SQL remains the most essential language for data pipeline work and integrated analytics

### Common Exam Questions
- Q: Design a high-level integrated analytics pipeline for a retail company wanting to analyze customer purchasing behavior.
- A: Ingestion: Pull data from POS systems, e-commerce platform, CRM, and loyalty program via APIs and database connections. Processing: Clean records (handle missing values, remove duplicates), merge customer IDs across sources, validate data consistency. Storage: Load into a data warehouse with fact and dimension tables. Analysis: Apply RFM segmentation, market basket analysis, and churn prediction models. Visualization: Create dashboards showing customer segments, purchasing trends, and recommendations.

- Q: Explain why data preparation is the most time-consuming step in integrated analytics.
- A: Real-world data is messy: multiple formats, missing values, inconsistent naming conventions, duplicates, and schema changes across sources. Merging datasets requires resolving key mismatches and ensuring consistency. This step consumes 60-80% of project time.

- Q: Compare batch processing and real-time processing in data pipelines.
- A: Batch processing handles data in scheduled chunks (e.g., nightly updates) -- suitable for reports and historical analysis. Real-time processing handles data as it arrives (streaming) -- suitable for fraud detection, live dashboards, and time-sensitive decisions. Batch is simpler; real-time requires more infrastructure.

- Q: What is the "garbage in, garbage out" principle and how does it apply to integrated analytics?
- A: If the data entering a pipeline is inaccurate, incomplete, or poorly formatted, the resulting analysis and models will be unreliable regardless of how sophisticated the methods are. This is why data validation and cleaning are critical pipeline stages.

---

## Project Presentation

### Key Terms & Definitions
- **Data Storytelling**: The practice of combining data, narrative, and visuals to communicate analytical findings in a compelling, actionable way
- **Narrative Arc**: The structured flow of a presentation: setup (introduce the problem), conflict (reveal the data/challenge), resolution (present insights and recommendations)
- **Audience Awareness**: Understanding the expertise level, interests, and decision-making needs of stakeholders to tailor the presentation accordingly
- **Call to Action**: The specific recommendations or next steps presented to the audience based on analytical findings
- **Annotation**: Labels, callouts, or notes added directly to visualizations to guide the audience's attention to key findings
- **Executive Summary**: A brief overview at the beginning of a report or presentation that highlights key findings, conclusions, and recommendations for time-pressed stakeholders
- **Data Visualization**: The graphical representation of data using charts, graphs, maps, and diagrams to communicate patterns and insights
- **Dashboard**: An interactive visual display consolidating key metrics and visualizations for ongoing monitoring and decision support
- **Actionable Insight**: A finding from data analysis that directly suggests a specific course of action with measurable expected outcomes
- **Technical Debt (in presentations)**: Overloading a presentation with methodology details that obscure the key findings and recommendations

### Core Concepts (Q&A Format)
- Q: What are the three essential components of data storytelling?
- A: Data (clean, accurate, thoroughly analyzed), narrative (a story communicating insights), and visuals (charts, graphs, and diagrams supporting the story)

- Q: What is the recommended storytelling structure for analytics presentations?
- A: Hook (introduce the problem to grab attention), Context (background and data overview), Insights (key findings from analysis), Call to Action (specific recommendations)

- Q: Why should you lead with insights rather than methodology?
- A: Stakeholders care about what was found and what to do, not how you did it. Leading with methodology loses audience attention and buries the actionable takeaways. Methodology can be included in an appendix.

- Q: How do you tailor a presentation for a non-technical executive audience?
- A: Use plain language (no jargon), lead with business impact and recommendations, use simple visualizations, focus on the "so what?" rather than the "how," and keep it concise with an executive summary upfront

- Q: When should you use a line chart vs. a bar chart vs. a pie chart?
- A: Line chart: trends over time. Bar chart: comparing categories or discrete values. Pie chart: showing parts of a whole (use sparingly and only with few categories).

- Q: What makes a visualization effective vs. misleading?
- A: Effective: clear labels, appropriate scale, honest axes starting at zero (for bar charts), minimal clutter, annotations highlighting key points. Misleading: truncated axes, cherry-picked data, overcrowded visuals, misleading color scales.

- Q: Why is the call to action the most important part of an analytics presentation?
- A: Analysis without action is wasted effort. The call to action translates findings into specific, implementable recommendations that drive organizational decisions and demonstrate the value of the analytical work.

### Important Facts & Figures
- 71% of executives prioritize data storytelling skills for reporting to key stakeholders
- The three pillars of data storytelling are: data, narrative, and visuals
- Presentations should follow the "inverted pyramid" approach: most important findings first, details later
- Best practice: no more than one key message per slide
- Annotated visuals increase audience comprehension by guiding attention to the most important data points
- The ultimate metric for successful data storytelling is when the audience is moved to act on the findings
- Color should be used purposefully: highlight key data, not decorate
- Analysts should rehearse presentations and anticipate stakeholder questions about assumptions, limitations, and alternative interpretations
- Edward Tufte's principle: maximize the "data-ink ratio" -- every element on a visualization should serve a purpose

### Common Exam Questions
- Q: You have completed an analysis showing that a company should shift marketing budget from Channel A to Channel B. How would you structure your presentation to the CMO?
- A: Executive Summary: Recommend shifting X% of budget from Channel A to B for projected Y% ROI increase. Hook: Current marketing spend is underperforming benchmarks. Context: Analysis of 12 months of campaign data across channels. Insights: Channel B delivers 3x higher conversion at 40% lower cost per acquisition (show comparative bar chart). Call to Action: Shift 30% of Channel A budget to Channel B in Q3, with specific dollar amounts and expected outcomes. Appendix: methodology details and data sources.

- Q: What are common mistakes in analytics presentations?
- A: Leading with methodology instead of insights, using overly technical jargon for non-technical audiences, overcrowding slides with too many visuals, failing to include a clear call to action, not tailoring content to audience level, presenting raw data without interpretation, and using misleading visualizations.

- Q: Why is audience awareness the first consideration in preparing an analytics presentation?
- A: The same findings need different framing for different audiences. Executives want business impact and recommendations. Technical peers want methodology and validation. Frontline managers want operational implications. Without audience awareness, the presentation fails to resonate or drive action.

- Q: Explain the difference between presenting data and telling a story with data.
- A: Presenting data shows charts and statistics. Telling a story with data weaves those elements into a narrative with context, meaning, and direction. A story explains why the data matters, what it means for the audience, and what should be done about it. Stories are memorable and persuasive; raw data is not.

- Q: How should an analyst handle questions about limitations or weaknesses in their analysis during a presentation?
- A: Be transparent and prepared. Acknowledge limitations proactively (e.g., data gaps, assumptions made, model limitations). Explain how limitations were mitigated and how they affect confidence in the conclusions. This builds credibility rather than undermining it.

---
