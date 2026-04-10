# MSDS 640: Data Science and AI Capstone

**Credits:** 3  
**Level:** graduate  
**Prerequisites:** None

## Course Description
Capstone experience applying data science and AI skills to real-world problems.

## Key Topics
- Capstone project
- End-to-end data science
- AI application

---

## Information Bank
*Research and supplementary materials for each key topic below.*

### Capstone project

A data science capstone project is a culminating academic experience that requires students to apply the full range of skills acquired throughout their graduate program to solve a real-world problem. Capstone projects bridge the gap between theory and practice, typically involving collaboration with industry sponsors who propose authentic business challenges. Students work in teams — reflecting professional data science environments — and deliver a complete solution encompassing problem framing, data acquisition, modeling, evaluation, and presentation of actionable insights.

- **Problem Scoping and Planning:** A critical early step is defining a question of sufficient depth while ensuring data availability. Best practices include engaging with faculty advisors one to two months before the project begins to refine scope and identify potential data access or legal issues.
- **Team-Based Collaboration:** Capstone projects emphasize collaborative teamwork with defined roles, project management timelines, and shared accountability — mirroring how data science operates in industry.
- **End-to-End Execution:** Students are responsible for the entire pipeline: data collection, cleaning, exploratory analysis, feature engineering, model building, validation, and deployment or prototyping.
- **Stakeholder Communication:** Projects culminate in formal presentations and written reports that convey the project's significance, methodology, results, and proposed products to both technical and non-technical audiences.
- **Portfolio Development:** The capstone serves as a flagship portfolio piece, demonstrating to employers the student's ability to manage ambiguity, work with real data, and deliver business value.

**Practical Applications:** Capstone projects have produced solutions ranging from predictive maintenance systems for manufacturing firms to customer churn models for subscription services and NLP-powered document classification tools for legal firms.

---

### End-to-end data science

End-to-end data science encompasses the complete lifecycle of a data science project, from initial business understanding through deployment and monitoring. The most widely adopted framework is CRISP-DM (Cross-Industry Standard Process for Data Mining), a cyclical six-phase methodology developed in the 1990s that remains the industry standard. The process is inherently iterative — teams frequently revisit earlier phases as new insights emerge, and a common rule of thumb is that 50-80% of project effort is spent in the data preparation phase alone.

- **Business Understanding:** Define the project objectives, success criteria, and key questions from the stakeholder's perspective. This phase ensures that technical work is aligned with actual business needs.
- **Data Understanding:** Explore available data sources, assess data quality, and perform initial exploratory data analysis (EDA) to identify patterns, anomalies, and potential features.
- **Data Preparation:** Clean, transform, integrate, and engineer features from raw data. This is typically the most time-intensive phase, involving handling missing values, encoding categorical variables, scaling, and creating derived features.
- **Modeling:** Select and train appropriate algorithms (regression, classification, clustering, deep learning), tune hyperparameters, and validate models using cross-validation and holdout sets.
- **Evaluation:** Assess model performance against business success criteria — not just statistical metrics — and determine whether the model is ready for deployment or requires further iteration.
- **Deployment and Monitoring:** Move validated models into production environments, integrate with business systems, and establish monitoring for performance decay, data drift, and bias.

**Practical Applications:** The CRISP-DM lifecycle is used across industries — from banks building credit scoring models to hospitals developing patient readmission predictors — providing a repeatable, structured approach that reduces project failure rates and improves stakeholder alignment.

---

### AI application

AI application development refers to the process of building, deploying, and maintaining machine learning and AI systems that solve real-world problems in production environments. While frameworks like PyTorch and TensorFlow have made model training accessible, deploying models reliably at scale remains a significant challenge — estimates suggest that up to 90% of ML models never make it into production. Successful AI applications require not only strong modeling but also robust engineering for real-time data handling, system integration, security, and continuous monitoring.

- **MLOps Lifecycle:** MLOps (Machine Learning Operations) streamlines the entire ML lifecycle — from data preparation and model training to deployment and monitoring — using CI/CD pipelines, version control for data and models, and automated testing.
- **Deployment Strategies:** Production deployments use patterns such as blue-green deployment (running old and new versions simultaneously), shadow deployment (processing live traffic silently with a new model for offline comparison), and canary releases (gradually routing traffic to the new model).
- **Production Requirements:** Real-world AI systems must meet sub-second response times, support horizontal scalability for traffic variations, implement fault tolerance, validate incoming data, and provide comprehensive observability through logging and metrics.
- **Model Monitoring:** Continuous monitoring detects performance decay, data drift, bias creep, and training-serving skew, ensuring issues are identified and corrected before they impact end users.
- **Ethical and Responsible AI:** Production AI applications must address fairness, transparency, accountability, and privacy — incorporating bias audits, explainability tools (SHAP, LIME), and compliance with regulations like GDPR.

**Practical Applications:** AI applications in production include autonomous vehicle perception systems, medical imaging diagnostic tools, conversational AI assistants for customer service, and algorithmic trading systems that execute decisions in milliseconds.

---

