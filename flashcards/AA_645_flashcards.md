# AA 645: Data Mining and Predictive Analytics - Flashcard Reference Bank

---

## Predictive Analytics

### Key Terms & Definitions
- **Predictive Analytics**: Branch of advanced analytics using historical data, statistical modeling, and machine learning to forecast future outcomes
- **Descriptive Analytics**: Backward-looking analysis that summarizes what has already happened in the data
- **Prescriptive Analytics**: Goes beyond prediction to recommend specific actions and optimize decisions
- **Overfitting**: When a model fits the training data too closely, capturing noise rather than the true underlying pattern, resulting in poor generalization
- **Underfitting**: When a model is too simple to capture the underlying structure of the data, performing poorly on both training and test data
- **Training Set**: The portion of data used to build and fit the model
- **Test Set**: The held-out portion of data used to evaluate model performance on unseen data
- **Cross-Validation**: A resampling technique that splits data into multiple folds to estimate model performance more reliably than a single train/test split
- **Feature Engineering**: The process of creating new input variables from raw data to improve model predictive power
- **AUC-ROC**: Area Under the Receiver Operating Characteristic Curve; measures a classification model's ability to distinguish between classes (1.0 = perfect, 0.5 = random)
- **RMSE**: Root Mean Squared Error; measures average prediction error for regression models, penalizing larger errors more heavily
- **F1-Score**: Harmonic mean of precision and recall, providing a balanced measure of classification performance

### Core Concepts (Q&A Format)
- Q: What is the difference between descriptive, predictive, and prescriptive analytics?
- A: Descriptive analytics explains what happened (summaries, dashboards); predictive analytics forecasts what will happen (models, probabilities); prescriptive analytics recommends what to do (optimization, decision support).

- Q: What are the main steps in the predictive analytics pipeline?
- A: (1) Define the problem, (2) Collect data, (3) Clean and preprocess, (4) Explore and visualize, (5) Build models, (6) Validate and evaluate, (7) Deploy into production.

- Q: Why is data preprocessing critical in predictive analytics?
- A: Raw data often contains missing values, outliers, inconsistent formats, and irrelevant features. Without cleaning and transformation, models will learn from noise and produce unreliable predictions.

- Q: How does predictive analytics differ from data mining?
- A: Data mining discovers hidden patterns and relationships in historical data; predictive analytics leverages those discovered patterns to forecast future events and outcomes.

- Q: What is the bias-variance tradeoff?
- A: Bias is error from oversimplified models (underfitting); variance is error from overly complex models (overfitting). The goal is to find the model complexity that minimizes total error by balancing both.

- Q: When would you use classification vs. regression in predictive analytics?
- A: Use classification when the target variable is categorical (e.g., yes/no, fraud/not fraud). Use regression when the target variable is continuous (e.g., price, temperature, revenue).

- Q: What role do evaluation metrics play in predictive analytics?
- A: They quantify how well a model performs. Different metrics suit different tasks: accuracy, precision, recall, F1, and AUC-ROC for classification; RMSE, MAE, and R-squared for regression.

### Important Facts & Figures
- Predictive analytics market valued at over $14 billion globally and growing rapidly
- The standard process model for data mining is CRISP-DM (Cross-Industry Standard Process for Data Mining), with six phases
- Approximately 80% of a data scientist's time is spent on data preparation and cleaning
- AUC-ROC of 0.5 indicates a model performing no better than random chance; 1.0 is perfect classification
- An R-squared of 1.0 means the model explains 100% of variance; 0 means it explains none
- Key industries: healthcare, finance, marketing, supply chain, insurance, telecommunications
- Common platforms: Python (scikit-learn), R, SAS, SPSS, AWS SageMaker, Google AutoML

### Common Exam Questions
- Q: Explain the predictive analytics lifecycle and why each step matters.
- A: Problem definition sets scope; data collection gathers inputs; preprocessing ensures quality; exploration reveals patterns; modeling builds predictive functions; evaluation validates performance; deployment puts the model into production use.

- Q: What is overfitting and how can it be prevented?
- A: Overfitting occurs when a model memorizes training data noise. Prevention techniques include cross-validation, regularization, pruning, early stopping, and using simpler models.

- Q: Compare supervised and unsupervised learning with examples.
- A: Supervised learning uses labeled data to predict outcomes (e.g., regression, classification). Unsupervised learning finds hidden patterns in unlabeled data (e.g., clustering, association analysis).

- Q: Why might a model with high training accuracy perform poorly on new data?
- A: The model has overfit to the training data, capturing noise and idiosyncrasies rather than generalizable patterns. It lacks the ability to generalize to unseen observations.

---

## Regression

### Key Terms & Definitions
- **Linear Regression**: Statistical method modeling a straight-line relationship between one or more predictors and a continuous outcome using ordinary least squares (OLS)
- **Multiple Linear Regression**: Extension of simple linear regression with two or more independent variables predicting one dependent variable
- **Logistic Regression**: Classification method that models the probability of a binary outcome using the sigmoid function
- **Sigmoid Function**: S-shaped function that maps any real number to a value between 0 and 1; formula: 1 / (1 + e^(-z))
- **Ordinary Least Squares (OLS)**: Estimation method that minimizes the sum of squared differences between observed and predicted values
- **Ridge Regression (L2)**: Regularization technique that adds a penalty equal to the squared magnitude of coefficients, shrinking them toward zero but never to exactly zero
- **Lasso Regression (L1)**: Regularization technique that adds a penalty equal to the absolute value of coefficients, capable of shrinking some coefficients to exactly zero (feature selection)
- **Elastic Net**: Combines both L1 (Lasso) and L2 (Ridge) penalties, balancing feature selection with coefficient shrinkage
- **R-squared (R2)**: Proportion of variance in the dependent variable explained by the model; ranges from 0 to 1
- **Adjusted R-squared**: Modified R-squared that penalizes for the number of predictors, preventing artificial inflation from adding irrelevant variables
- **Residual**: The difference between an observed value and the predicted value (observed - predicted)
- **Multicollinearity**: When two or more independent variables are highly correlated, making it difficult to isolate their individual effects

### Core Concepts (Q&A Format)
- Q: What are the four key assumptions of linear regression?
- A: (1) Linearity between predictors and outcome, (2) Independence of errors, (3) Homoscedasticity (constant variance of residuals), (4) Normality of residual distribution.

- Q: What is the difference between Ridge and Lasso regression?
- A: Ridge (L2) shrinks all coefficients toward zero but keeps all variables in the model. Lasso (L1) can shrink coefficients to exactly zero, effectively performing automatic feature selection by eliminating irrelevant predictors.

- Q: When should you use logistic regression instead of linear regression?
- A: When the dependent variable is binary/categorical (e.g., pass/fail, yes/no). Linear regression is for continuous outcomes; logistic regression models the probability of class membership.

- Q: What does a high R-squared value indicate, and what are its limitations?
- A: High R-squared means the model explains a large proportion of variance. Limitations: it always increases when adding more predictors (use adjusted R-squared instead), does not indicate causation, and can be misleadingly high in overfit models.

- Q: How do you detect multicollinearity and why does it matter?
- A: Detect using Variance Inflation Factor (VIF); VIF > 5-10 suggests problematic multicollinearity. It matters because it inflates standard errors, making coefficient estimates unreliable and statistical tests invalid.

- Q: What is the purpose of regularization in regression?
- A: Regularization adds a penalty term to the loss function to constrain model complexity, preventing overfitting and improving generalization to unseen data.

- Q: What is the difference between MAE and RMSE?
- A: MAE (Mean Absolute Error) treats all errors equally. RMSE (Root Mean Squared Error) penalizes larger errors more heavily due to squaring. RMSE is always greater than or equal to MAE.

### Important Facts & Figures
- OLS minimizes the sum of squared residuals: min Sum(yi - y_hat_i)^2
- Lasso was introduced by Robert Tibshirani in 1996
- VIF (Variance Inflation Factor) > 10 is a common threshold indicating severe multicollinearity
- Logistic regression decision boundary is typically set at probability = 0.5
- Polynomial regression with degree > 3-4 risks severe overfitting
- The F-test evaluates whether the overall regression model is statistically significant
- Adjusted R-squared can decrease when adding an irrelevant predictor, unlike regular R-squared

### Common Exam Questions
- Q: Write and interpret the equation for simple linear regression.
- A: y = b0 + b1*x + e, where b0 is the y-intercept, b1 is the slope (change in y per unit change in x), and e is the error term.

- Q: Explain how Lasso regression performs feature selection.
- A: Lasso's L1 penalty forces some coefficients to exactly zero as the regularization parameter (lambda) increases. Variables with zero coefficients are effectively removed from the model, performing automatic feature selection.

- Q: A model has R-squared of 0.95 on training data but 0.60 on test data. What is happening?
- A: The model is overfitting. The large gap between training and test performance indicates it has memorized training data patterns that do not generalize. Solutions include regularization, reducing model complexity, or gathering more training data.

- Q: What happens when you violate the homoscedasticity assumption?
- A: Coefficient estimates remain unbiased but standard errors become unreliable, leading to invalid hypothesis tests and confidence intervals. Solutions include weighted least squares or robust standard errors.

---

## Decision Trees

### Key Terms & Definitions
- **Decision Tree**: Non-parametric supervised learning algorithm that recursively splits data into subsets based on feature values, creating a tree-shaped model for classification or regression
- **Root Node**: The topmost node in the tree representing the first and most important split of the entire dataset
- **Internal Node (Decision Node)**: A node that tests a feature condition and branches into child nodes based on the outcome
- **Leaf Node (Terminal Node)**: A node with no children that holds the final prediction (class label or value)
- **Gini Impurity**: Measure of how often a randomly chosen element would be misclassified; ranges from 0 (pure) to 0.5 (maximum impurity for binary classification)
- **Entropy**: Measure of disorder/uncertainty in a dataset from information theory; ranges from 0 (pure) to 1 (maximum impurity for binary classification)
- **Information Gain**: Reduction in entropy achieved by splitting on a given attribute; attribute with highest information gain is chosen for the split
- **CART**: Classification and Regression Trees algorithm; produces binary splits using Gini impurity for classification and variance reduction for regression
- **ID3**: Iterative Dichotomiser 3; uses information gain (entropy) to select splitting attributes; works primarily with categorical features
- **C4.5**: Improvement over ID3 that uses gain ratio instead of information gain, handles continuous attributes, and deals with missing values
- **Pruning**: Technique to reduce tree size and prevent overfitting by removing branches that provide little predictive power
- **Pre-pruning (Early Stopping)**: Stopping tree growth before it fully fits the training data by setting constraints like maximum depth or minimum samples per leaf

### Core Concepts (Q&A Format)
- Q: How does a decision tree make a prediction for a new data point?
- A: The data point starts at the root node. At each internal node, the relevant feature is tested and the data point follows the appropriate branch. This continues until it reaches a leaf node, which provides the predicted class or value.

- Q: What is the difference between Gini impurity and entropy as splitting criteria?
- A: Both measure node impurity. Gini impurity measures misclassification probability; entropy measures information uncertainty. Gini is slightly faster to compute (no logarithm). They generally produce similar trees; CART uses Gini while ID3/C4.5 use entropy.

- Q: Why are decision trees prone to overfitting?
- A: Without constraints, a tree can grow until each leaf contains a single training example, perfectly memorizing the data including noise. This deep tree has high variance and generalizes poorly to new data.

- Q: What is the difference between pre-pruning and post-pruning?
- A: Pre-pruning stops tree growth early by setting limits (max depth, min samples). Post-pruning grows the full tree first, then removes branches that do not significantly improve performance using techniques like cost-complexity pruning.

- Q: How does CART differ from ID3?
- A: CART creates binary splits only, uses Gini impurity, and handles both classification and regression. ID3 can create multi-way splits, uses information gain (entropy), and only handles classification with categorical features.

- Q: What are the advantages of decision trees over other algorithms?
- A: Highly interpretable and easy to visualize, require minimal data preprocessing (no scaling/normalization needed), handle both numerical and categorical data, and capture nonlinear relationships naturally.

### Important Facts & Figures
- Gini impurity formula: Gini = 1 - Sum(pi^2) where pi is the proportion of class i
- Entropy formula: H = -Sum(pi * log2(pi))
- Information Gain = Entropy(parent) - weighted average Entropy(children)
- CART was introduced by Breiman, Friedman, Olshen, and Stone in 1984
- ID3 was developed by Ross Quinlan in 1986; C4.5 is Quinlan's 1993 improvement
- A fully grown tree on n training samples can have up to n leaf nodes
- Decision trees have O(n * m * log(n)) training complexity where n = samples, m = features
- Cost-complexity pruning parameter (alpha/ccp_alpha) controls the tradeoff between tree size and training accuracy

### Common Exam Questions
- Q: Given a dataset, calculate Gini impurity for a node with 30 class-A and 70 class-B samples.
- A: Gini = 1 - (0.3^2 + 0.7^2) = 1 - (0.09 + 0.49) = 1 - 0.58 = 0.42

- Q: Why might a decision tree with 100% training accuracy be a poor model?
- A: It has likely overfit by memorizing every training example including noise. It will have high variance and perform poorly on unseen data. Pruning or ensemble methods should be applied.

- Q: Explain the concept of information gain and how it is used in ID3.
- A: Information gain measures the reduction in entropy after splitting on a feature. ID3 calculates information gain for every feature and selects the one with the highest gain for the split. This greedy process repeats recursively until stopping criteria are met.

- Q: Compare decision trees and logistic regression for a binary classification problem.
- A: Decision trees capture nonlinear relationships and feature interactions naturally without feature engineering, but are prone to overfitting. Logistic regression assumes a linear decision boundary, is more stable, and provides probability estimates with interpretable coefficients.

---

## Random Forests

### Key Terms & Definitions
- **Random Forest**: Ensemble learning method that constructs multiple decision trees and aggregates their predictions through majority voting (classification) or averaging (regression)
- **Ensemble Learning**: Strategy of combining multiple models to produce a single, stronger predictive model with better performance than any individual model
- **Bagging (Bootstrap Aggregating)**: Technique where each tree is trained on a random bootstrap sample drawn with replacement from the original training data
- **Bootstrap Sample**: A sample of size n drawn with replacement from the original dataset of size n; on average includes about 63.2% of unique original observations
- **Out-of-Bag (OOB) Samples**: The approximately 36.8% of observations not included in a given bootstrap sample; used as a built-in validation set
- **OOB Error**: Generalization error estimate computed by predicting each observation using only trees that did not include it in their bootstrap sample
- **Feature Randomness (Feature Subsampling)**: At each split, only a random subset of features is considered, decorrelating the trees in the ensemble
- **Feature Importance**: Measure of each feature's contribution to prediction; computed by tracking the total decrease in impurity (Gini/entropy) across all trees
- **Permutation Importance**: Feature importance measured by randomly shuffling a feature's values and observing the decrease in model accuracy
- **n_estimators**: Hyperparameter controlling the number of trees in the forest
- **max_features**: Hyperparameter controlling the number of features considered at each split; default is sqrt(total features) for classification, total_features/3 for regression

### Core Concepts (Q&A Format)
- Q: How does a random forest reduce overfitting compared to a single decision tree?
- A: By averaging predictions across many diverse trees trained on different bootstrap samples with random feature subsets. This reduces variance (the main source of error in decision trees) without significantly increasing bias.

- Q: Why is feature randomness important in random forests?
- A: Without feature randomness, if one feature is very strong, most trees would split on it first, making the trees highly correlated. Feature subsampling decorrelates the trees, which is essential for variance reduction through averaging.

- Q: What is the OOB error and why is it useful?
- A: OOB error estimates generalization performance using samples not included in each tree's bootstrap sample. It is useful because it provides a reliable validation estimate without needing a separate holdout set, similar to leave-one-out cross-validation.

- Q: How does a random forest make a final prediction?
- A: For classification, each tree votes for a class and the majority vote wins. For regression, the prediction is the average of all individual tree predictions.

- Q: What are the key hyperparameters to tune in a random forest?
- A: n_estimators (number of trees), max_depth (tree depth limit), max_features (features per split), min_samples_split (minimum samples to split a node), and min_samples_leaf (minimum samples in a leaf).

- Q: When would you prefer a random forest over a single decision tree?
- A: Almost always when prediction accuracy matters more than interpretability. Random forests are more accurate, more robust to noise, and less prone to overfitting, though they sacrifice the easy visual interpretability of a single tree.

### Important Facts & Figures
- Random forests were formalized by Leo Breiman in 2001
- Default max_features for classification: sqrt(p); for regression: p/3, where p = total features
- Each bootstrap sample contains approximately 63.2% unique observations (1 - 1/e)
- OOB error is analogous to leave-one-out cross-validation and is computed at no additional cost
- Random forests are embarrassingly parallel -- each tree can be trained independently
- More trees generally improve performance but with diminishing returns; typically 100-500 trees suffice
- Random forests handle high-dimensional data well and are robust to irrelevant features
- Two types of feature importance: mean decrease in impurity (MDI) and mean decrease in accuracy (MDA/permutation importance)

### Common Exam Questions
- Q: Explain why bagging reduces variance but not bias.
- A: Each bootstrapped tree has similar bias to a single tree. However, averaging many predictions reduces the variance of the overall estimate (by the law of large numbers). Since bias is a systematic error inherent to the model structure, averaging does not reduce it.

- Q: A random forest has 500 trees. Approximately how many unique samples does each tree train on?
- A: Each bootstrap sample contains approximately 63.2% of unique observations from the original dataset (since each observation has a (1-1/n)^n probability of being excluded, which approaches 1/e as n grows large).

- Q: Compare random forests and gradient boosting.
- A: Random forests build trees independently in parallel (bagging), reducing variance. Gradient boosting builds trees sequentially, where each new tree corrects errors of the previous ones, reducing bias. Gradient boosting often achieves higher accuracy but is more prone to overfitting and slower to train.

- Q: What is the relationship between the number of trees and overfitting in random forests?
- A: Unlike single decision trees, adding more trees to a random forest does not cause overfitting. Performance improves and then plateaus. The OOB error converges as more trees are added.

---

## Association Analysis

### Key Terms & Definitions
- **Association Analysis (Association Rule Mining)**: Unsupervised data mining technique that discovers co-occurrence relationships among items in transactional datasets
- **Market Basket Analysis**: The most common application of association analysis; identifies products frequently purchased together
- **Itemset**: A collection of one or more items (e.g., {bread, butter, milk})
- **Frequent Itemset**: An itemset whose support exceeds the minimum support threshold
- **Support**: The proportion of transactions containing an itemset; Support(A) = (Transactions containing A) / (Total transactions)
- **Confidence**: The conditional probability of finding item B given item A; Confidence(A->B) = Support(A and B) / Support(A)
- **Lift**: Ratio of observed co-occurrence to expected co-occurrence if independent; Lift(A->B) = Confidence(A->B) / Support(B); lift > 1 = positive association, lift = 1 = independent, lift < 1 = negative association
- **Apriori Algorithm**: Level-wise algorithm that generates candidate itemsets of increasing size and prunes those below minimum support; based on the downward closure property
- **Apriori Principle (Downward Closure)**: If an itemset is infrequent, all its supersets must also be infrequent; allows pruning of the search space
- **FP-Growth**: Alternative algorithm that compresses data into a Frequent Pattern tree (FP-tree) and mines patterns without candidate generation, offering better scalability
- **Antecedent (LHS)**: The "if" part of an association rule (e.g., {bread} in {bread} -> {butter})
- **Consequent (RHS)**: The "then" part of an association rule (e.g., {butter} in {bread} -> {butter})

### Core Concepts (Q&A Format)
- Q: What do support, confidence, and lift each measure?
- A: Support measures how frequently an itemset appears overall. Confidence measures the reliability of the rule (probability of consequent given antecedent). Lift measures whether the association is stronger than chance (>1 means positive association).

- Q: Explain the Apriori principle and why it is important for efficiency.
- A: The Apriori principle states that all subsets of a frequent itemset must also be frequent. This allows the algorithm to prune candidate itemsets whose subsets are infrequent, dramatically reducing the search space and computation time.

- Q: How does FP-Growth improve upon the Apriori algorithm?
- A: FP-Growth avoids the costly candidate generation step by compressing the transaction database into a compact FP-tree structure and mining frequent patterns directly from it. This makes it significantly faster on large datasets.

- Q: A rule has high confidence but lift of 1.0. Should you act on it?
- A: No. A lift of 1.0 means the items are statistically independent -- the association is no stronger than random chance. High confidence alone can be misleading if the consequent item is already very popular.

- Q: What is the difference between association rules and correlation?
- A: Association rules identify co-occurrence patterns in transactional data (A->B) with directionality. Correlation measures the linear relationship strength between two numerical variables. Association rules can capture complex, non-linear basket-level relationships.

- Q: What challenges arise when setting support and confidence thresholds?
- A: Setting thresholds too high misses rare but valuable patterns. Setting them too low produces a flood of trivial, redundant rules. The thresholds must be tuned to balance rule quality, quantity, and computational cost.

### Important Facts & Figures
- The Apriori algorithm was introduced by Agrawal and Srikant in 1994
- FP-Growth was introduced by Han, Pei, and Yin in 2000
- Apriori computational complexity grows exponentially with the number of items
- Lift = 1 means statistical independence; lift > 1 means positive association; lift < 1 means negative association
- A rule {A} -> {B} with confidence of 0.8 means 80% of transactions containing A also contain B
- The classic example: "customers who buy diapers also buy beer" (apocryphal but illustrative)
- Association analysis extends beyond retail: web usage mining, medical diagnosis, genomics, fraud detection
- The number of possible itemsets for n items is 2^n - 1

### Common Exam Questions
- Q: Given 1000 transactions where {bread} appears in 400, {butter} in 300, and {bread, butter} together in 200, calculate support, confidence, and lift for {bread} -> {butter}.
- A: Support({bread, butter}) = 200/1000 = 0.20. Confidence = 200/400 = 0.50. Lift = 0.50 / 0.30 = 1.67. Since lift > 1, there is a positive association.

- Q: Why can Apriori be computationally expensive and how does the Apriori principle help?
- A: Apriori generates all candidate itemsets at each level and scans the database for each. The Apriori principle prunes candidates by eliminating any whose subsets are infrequent, avoiding exponential explosion.

- Q: Distinguish between actionable and trivial association rules.
- A: Actionable rules reveal non-obvious, commercially useful associations (e.g., diapers and beer). Trivial rules state obvious relationships (e.g., ketchup and mustard). Lift, domain knowledge, and business context help filter trivial rules.

- Q: A retailer finds that {coffee} -> {sugar} has lift = 2.5 and {coffee} -> {laptop} has lift = 0.3. Interpret both.
- A: Coffee and sugar are purchased together 2.5x more than expected by chance (strong positive association). Coffee and laptop are purchased together less than expected (negative association or no practical relationship).

---

## Clustering

### Key Terms & Definitions
- **Clustering**: Unsupervised machine learning technique that groups data points into clusters where intra-cluster similarity is maximized and inter-cluster similarity is minimized
- **K-Means Clustering**: Partitioning algorithm that assigns n observations to K clusters by iteratively updating cluster centroids until convergence
- **Centroid**: The center point of a cluster, computed as the mean of all data points assigned to that cluster
- **Hierarchical Clustering**: Algorithm that builds a nested hierarchy of clusters; agglomerative (bottom-up) or divisive (top-down)
- **Dendrogram**: Tree-like diagram that visualizes the hierarchical clustering process, showing the order and distance at which clusters are merged or split
- **DBSCAN**: Density-Based Spatial Clustering of Applications with Noise; groups dense regions and marks low-density points as outliers
- **Epsilon (eps)**: DBSCAN parameter defining the maximum radius of a neighborhood around a point
- **MinPts**: DBSCAN parameter specifying the minimum number of points required within epsilon radius to form a dense region
- **Silhouette Score**: Measures how similar a point is to its own cluster vs. the nearest neighboring cluster; ranges from -1 (wrong cluster) to +1 (well-clustered)
- **Elbow Method**: Technique for selecting optimal K by plotting within-cluster sum of squares (WCSS) against K and identifying the "elbow" point where improvement diminishes
- **Inertia (WCSS)**: Within-Cluster Sum of Squares; total distance of all points to their assigned centroid; lower is better

### Core Concepts (Q&A Format)
- Q: How does the K-Means algorithm work step by step?
- A: (1) Choose K and initialize K centroids randomly, (2) Assign each point to nearest centroid, (3) Recalculate centroids as mean of assigned points, (4) Repeat steps 2-3 until centroids no longer change (convergence).

- Q: What are the limitations of K-Means?
- A: Requires specifying K in advance, assumes spherical and equally-sized clusters, sensitive to initialization (solved by K-Means++), sensitive to outliers, and struggles with non-convex cluster shapes.

- Q: How does DBSCAN differ from K-Means?
- A: DBSCAN does not require pre-specifying the number of clusters, can find arbitrarily shaped clusters, naturally identifies outliers/noise, and is density-based rather than centroid-based. However, it struggles with clusters of varying densities.

- Q: What does the silhouette score tell you about clustering quality?
- A: A silhouette score close to +1 means points are well-matched to their own cluster and far from others. Near 0 means points are on cluster boundaries. Negative values mean points may be assigned to the wrong cluster.

- Q: Why is feature scaling critical before clustering?
- A: Most clustering algorithms use distance metrics (e.g., Euclidean). Features with larger scales dominate the distance calculation, biasing the clustering. Standardization ensures all features contribute equally.

- Q: When would you choose hierarchical clustering over K-Means?
- A: When you do not know K in advance and want to explore different numbers of clusters via the dendrogram, when you need nested cluster relationships, or when the dataset is small enough (hierarchical is O(n^3) vs K-Means O(n*K*t)).

- Q: What are core points, border points, and noise points in DBSCAN?
- A: Core points have at least MinPts neighbors within epsilon. Border points are within epsilon of a core point but have fewer than MinPts neighbors themselves. Noise points are not within epsilon of any core point.

### Important Facts & Figures
- K-Means converges in O(n * K * t * d) where n=samples, K=clusters, t=iterations, d=dimensions
- K-Means++ initialization improves convergence by choosing initial centroids that are spread apart
- Hierarchical clustering time complexity is O(n^3) for agglomerative, making it impractical for large datasets
- DBSCAN has two key parameters: epsilon (neighborhood radius) and MinPts (minimum density)
- Silhouette score formula: s(i) = (b(i) - a(i)) / max(a(i), b(i)) where a = mean intra-cluster distance, b = mean nearest-cluster distance
- Common linkage methods in hierarchical clustering: single (minimum distance), complete (maximum distance), average, and Ward's (minimizes total within-cluster variance)
- PCA (Principal Component Analysis) is often applied before clustering to reduce dimensionality

### Common Exam Questions
- Q: You run K-Means with K=3 and K=5. How do you decide which is better?
- A: Use the elbow method (plot WCSS vs K and look for the bend), silhouette score (higher average is better), or domain knowledge about the expected number of groups.

- Q: Why might K-Means produce different results on different runs?
- A: K-Means uses random initialization of centroids. Different starting positions can lead to different local optima. K-Means++ or running the algorithm multiple times with different seeds helps mitigate this.

- Q: A dataset contains customers with two features: income ($0-$200K) and age (0-100). Why might clustering fail without preprocessing?
- A: Income has a much larger scale, so Euclidean distance would be dominated by income differences. Age would have almost no influence. Standardizing both features to mean=0, std=1 ensures equal contribution.

- Q: Compare agglomerative and divisive hierarchical clustering.
- A: Agglomerative (bottom-up) starts with each point as its own cluster and merges the closest pairs step by step. Divisive (top-down) starts with all points in one cluster and recursively splits. Agglomerative is more common because divisive is computationally more expensive.

---

## Python

### Key Terms & Definitions
- **Pandas**: Primary Python library for data manipulation; provides DataFrame (2D table) and Series (1D array) data structures for loading, cleaning, transforming, and analyzing structured data
- **DataFrame**: Two-dimensional labeled data structure in Pandas with rows and columns, similar to a spreadsheet or SQL table
- **Series**: One-dimensional labeled array in Pandas, essentially a single column of a DataFrame
- **NumPy**: Foundational numerical computing library providing efficient multi-dimensional arrays (ndarrays) and mathematical operations
- **ndarray**: NumPy's core data structure; a homogeneous, fixed-size multi-dimensional array optimized for numerical computation
- **Scikit-learn (sklearn)**: Most widely used Python machine learning library; provides a consistent API for classification, regression, clustering, preprocessing, and model evaluation
- **Matplotlib**: Low-level Python plotting library for creating static, animated, and interactive visualizations (line charts, bar charts, scatter plots, histograms)
- **Seaborn**: Statistical visualization library built on Matplotlib; provides higher-level, attractive default plots like heatmaps, pair plots, violin plots, and box plots
- **Statsmodels**: Library for classical statistical models (OLS, logistic regression, ARIMA) with detailed summary tables including p-values and confidence intervals
- **Jupyter Notebook**: Interactive development environment that combines executable code, visualizations, and markdown text in a single document for reproducible analysis
- **fit/predict/score**: Scikit-learn's consistent API pattern; fit() trains the model, predict() generates predictions, score() evaluates performance
- **Pipeline**: Scikit-learn object that chains preprocessing steps and a model into a single reproducible workflow

### Core Concepts (Q&A Format)
- Q: What is the difference between Pandas and NumPy?
- A: NumPy provides fast numerical array operations for homogeneous data. Pandas builds on NumPy to provide DataFrames for heterogeneous tabular data with labeled rows/columns, built-in handling of missing values, and convenient I/O functions.

- Q: Why is scikit-learn's consistent API (fit/predict/score) important?
- A: It allows seamless swapping of algorithms. You can replace a decision tree with a random forest or logistic regression by changing one line of code, since all models follow the same interface. This enables easy model comparison.

- Q: What is the purpose of train_test_split in scikit-learn?
- A: It splits data into training and test sets to evaluate how well a model generalizes to unseen data. Typical splits are 70-30 or 80-20. The test set is kept separate during training to provide an unbiased performance estimate.

- Q: When would you use Statsmodels over scikit-learn for regression?
- A: When you need detailed statistical inference: p-values, confidence intervals, R-squared, F-statistics, and residual diagnostics. Scikit-learn focuses on prediction accuracy; Statsmodels focuses on statistical significance and model interpretation.

- Q: What are the key Pandas operations for data preprocessing?
- A: dropna()/fillna() for missing values, groupby() for aggregation, merge()/concat() for combining datasets, apply() for custom transformations, get_dummies() for one-hot encoding, and describe() for summary statistics.

- Q: Why are Jupyter Notebooks the standard for data science workflows?
- A: They allow mixing code, output, visualizations, and explanatory text in one document. This supports iterative exploration, immediate feedback, documentation, and reproducibility -- all essential for analytics workflows.

### Important Facts & Figures
- Pandas can read from CSV, Excel, SQL, JSON, Parquet, and many other file formats
- NumPy arrays are up to 50x faster than Python lists for numerical operations due to contiguous memory and vectorized operations
- Scikit-learn provides 30+ classification algorithms, 20+ regression algorithms, and 10+ clustering algorithms
- Key scikit-learn modules: sklearn.model_selection, sklearn.preprocessing, sklearn.metrics, sklearn.ensemble, sklearn.linear_model
- Seaborn's heatmap() is commonly used to visualize correlation matrices
- GridSearchCV and RandomizedSearchCV in scikit-learn automate hyperparameter tuning with cross-validation
- The Python data science stack (NumPy, Pandas, scikit-learn, Matplotlib) is open-source and free
- Jupyter Notebooks use .ipynb file format and can be converted to HTML, PDF, or Python scripts

### Common Exam Questions
- Q: Write Python code to load a CSV, check for missing values, and display summary statistics.
- A: `import pandas as pd; df = pd.read_csv('data.csv'); print(df.isnull().sum()); print(df.describe())`

- Q: What scikit-learn function would you use to evaluate a model using 5-fold cross-validation?
- A: `from sklearn.model_selection import cross_val_score; scores = cross_val_score(model, X, y, cv=5)` -- This trains and evaluates the model 5 times, each time using a different fold as the test set.

- Q: Explain the difference between Matplotlib and Seaborn.
- A: Matplotlib is low-level and highly customizable but requires more code for attractive plots. Seaborn is high-level, produces publication-quality statistical visualizations with less code, and integrates well with Pandas DataFrames.

- Q: How would you build a complete machine learning pipeline in scikit-learn?
- A: Use `from sklearn.pipeline import Pipeline` to chain steps: e.g., `Pipeline([('scaler', StandardScaler()), ('model', RandomForestClassifier())])`. The pipeline applies preprocessing and modeling sequentially, ensuring consistent treatment of training and test data.

---

## Tableau

### Key Terms & Definitions
- **Tableau**: Leading business intelligence and data visualization platform using drag-and-drop interface to create interactive visualizations and dashboards
- **Dimension**: Qualitative/categorical field (e.g., name, region, date) used to categorize and segment data; typically displayed as row/column headers
- **Measure**: Quantitative/numerical field (e.g., sales, profit, count) that can be aggregated (sum, average, count) in visualizations
- **Dashboard**: A collection of multiple visualizations, filters, and interactive elements combined on a single canvas to tell a cohesive data story
- **Worksheet**: A single visualization or chart within Tableau; dashboards are composed of one or more worksheets
- **Calculated Field**: A new field created by writing a formula using existing fields, enabling custom metrics, ratios, and logic
- **Filter**: A control that limits the data displayed in a visualization based on specific criteria (dimension values, measure ranges, dates)
- **Parameter**: A dynamic variable that can be controlled by the user to change calculations, filters, or reference lines interactively
- **Mark**: The visual element that represents data in a chart (bar, point, line, shape); controlled by the Marks card (color, size, label, detail, tooltip)
- **Tableau Prep**: Data cleaning and transformation tool for preparing data before visualization in Tableau Desktop
- **TabPy**: Tableau Python Server integration that allows Python scripts to be executed within Tableau calculated fields for advanced analytics
- **Data Blending**: Technique for combining data from multiple sources at the visualization level without creating a formal join

### Core Concepts (Q&A Format)
- Q: What is the difference between dimensions and measures in Tableau?
- A: Dimensions are categorical/qualitative fields (names, dates, categories) that define the granularity of the view. Measures are numerical fields (sales, profit) that are aggregated (summed, averaged) within the dimensional context.

- Q: How do you create an interactive dashboard in Tableau?
- A: Create individual worksheets with visualizations, then combine them on a Dashboard canvas. Add filters, parameters, and actions (filter, highlight, URL) that allow users to interact with and drill down into the data dynamically.

- Q: What are the benefits of Tableau over Python for data visualization?
- A: Tableau is faster for non-programmers (drag-and-drop), creates interactive dashboards easily, connects to many data sources natively, and is designed for sharing with business stakeholders. Python offers more customization but requires coding.

- Q: When would you use a calculated field in Tableau?
- A: When you need to create new metrics not in the raw data, such as profit margin (Profit/Sales), year-over-year growth, running totals, conditional logic (IF/THEN), or custom aggregations.

- Q: How does TabPy extend Tableau's capabilities?
- A: TabPy allows Tableau to execute Python scripts within calculated fields, enabling advanced statistical modeling, machine learning predictions, sentiment analysis, and other computations that are beyond Tableau's built-in analytics.

- Q: What visualization type would you use for comparing parts of a whole?
- A: Stacked bar charts, tree maps, or pie charts (though pie charts are generally discouraged for more than a few categories). Tree maps are effective for hierarchical part-to-whole relationships.

### Important Facts & Figures
- Tableau was founded in 2003 and acquired by Salesforce in 2019 for $15.7 billion
- Tableau product family: Desktop (authoring), Server/Cloud (publishing/sharing), Prep (data cleaning), Public (free public sharing)
- Dashboard best practice: most important content goes at the top-left (users read in Z-pattern or F-pattern)
- Tableau supports live connections (real-time queries) and extracts (snapshot cached locally for speed)
- LOD (Level of Detail) expressions: FIXED, INCLUDE, EXCLUDE -- control the granularity of calculations independent of the view
- Common chart selection: bar chart for comparisons, line chart for trends, scatter plot for correlations, map for geographic data, heatmap for density
- Tableau Public is free but all workbooks are publicly visible
- Tableau can connect to 75+ data sources including SQL databases, cloud platforms, spreadsheets, and web APIs

### Common Exam Questions
- Q: A manager wants to see sales by region with the ability to filter by product category and time period. How would you build this in Tableau?
- A: Create a bar chart or map worksheet with Region on the axis and SUM(Sales) as the measure. Add Product Category and Date as Quick Filters. Combine into a dashboard and add filter actions so clicking one visualization filters the others.

- Q: What is the difference between a live connection and an extract in Tableau?
- A: A live connection queries the database in real-time for up-to-date data but can be slow with large datasets. An extract creates a local snapshot of the data that loads faster but must be refreshed to reflect new data.

- Q: Explain the concept of Level of Detail (LOD) expressions in Tableau.
- A: LOD expressions compute aggregations at a specified granularity regardless of what dimensions are in the view. FIXED computes at a specified dimension level, INCLUDE adds a dimension to the view level, and EXCLUDE removes a dimension from the view level.

- Q: Why is Tableau important in a predictive analytics workflow?
- A: Tableau communicates analytical findings to non-technical stakeholders through interactive, visual dashboards. Even the best predictive model has no business value unless its results are understood and acted upon by decision-makers.

---
