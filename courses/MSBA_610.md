# MSBA 610: Time Series Analysis and Optimization for Business Decisions

**Credits:** 3  
**Level:** graduate  
**Prerequisites:** ISA 510, ISA 530

## Course Description
Time series analysis and optimization techniques applied to business decision-making.

## Key Topics
- Time series analysis
- Optimization
- Business decisions
- Forecasting

---

## Information Bank
*Research and supplementary materials for each key topic below.*

### Time series analysis

Time series analysis is the set of statistical and computational methods for extracting meaningful patterns from data collected sequentially over time. It involves decomposing temporal data into its constituent components and modeling dependencies between observations to understand past behavior and forecast future values.

- **Components:** Trend (long-term directional movement), seasonality (fixed-period repeating patterns), cyclicality (variable-period oscillations driven by economic or business cycles), irregular/residual (random noise)
- **Key methods:** Decomposition (additive and multiplicative), autocorrelation and partial autocorrelation analysis (ACF/PACF), stationarity testing (Augmented Dickey-Fuller test), differencing and transformations
- **Models:** ARIMA/SARIMA (classical statistical models), exponential smoothing (Holt-Winters), VAR (vector autoregression for multivariate series), state space models
- **Modern approaches:** Prophet (handles holidays and missing data), LSTM neural networks, temporal fusion transformers, ensemble methods combining multiple forecasting models
- **Practical relevance:** Time series analysis is applied in financial market analysis, demand planning, energy consumption forecasting, web traffic analysis, and economic indicator monitoring. Mastering both classical and modern methods allows analysts to select the best approach for each business context.

---

### Optimization

Optimization is the mathematical discipline of finding the best solution from a set of feasible alternatives, typically by maximizing or minimizing an objective function subject to constraints. In business analytics, optimization transforms data-driven insights into actionable decisions that allocate resources most effectively.

- **Key concepts:** Objective function (what to maximize/minimize), decision variables (what can be controlled), constraints (limitations and requirements), feasible region (set of valid solutions)
- **Types:** Linear programming (LP -- linear objectives and constraints), integer programming (IP -- discrete decision variables), nonlinear programming, mixed-integer programming, stochastic optimization (incorporating uncertainty)
- **Algorithms:** Simplex method, interior point methods, branch and bound, gradient descent, genetic algorithms, simulated annealing
- **Tools:** Python PuLP and SciPy.optimize, Gurobi, CPLEX, Excel Solver; these enable formulating and solving optimization problems programmatically
- **Practical relevance:** Optimization drives decisions in supply chain management (routing, scheduling), portfolio allocation, pricing strategies, workforce scheduling, and production planning. Combining forecasting with optimization creates powerful decision-support systems that predict future states and prescribe optimal actions.

---

### Business decisions

Business decisions in the analytics context refers to the application of quantitative methods, data analysis, and modeling to support and improve organizational decision-making. It bridges the gap between analytical outputs and strategic actions, ensuring that data insights translate into measurable business outcomes.

- **Decision frameworks:** Decision trees and payoff matrices, expected value analysis, sensitivity analysis (what-if scenarios), Monte Carlo simulation for risk quantification
- **Prescriptive analytics:** Goes beyond prediction to recommend specific actions; combines optimization models with forecasting to suggest the best course of action given constraints and objectives
- **Decision-making under uncertainty:** Scenario planning, robust optimization, probabilistic forecasting with confidence intervals, risk-reward tradeoff analysis
- **Stakeholder alignment:** Framing analytical results in business terms (revenue impact, cost savings, risk reduction), presenting multiple options with tradeoffs, supporting decisions with clear assumptions and limitations
- **Practical relevance:** The ultimate goal of business analytics is better decisions. Organizations that embed analytics into decision processes see improved outcomes in pricing, inventory management, capital allocation, and strategic planning. The ability to connect analytical methods to business impact is what distinguishes impactful analysts.

---

### Forecasting

Forecasting is the process of making predictions about future events based on historical data and analytical models. In business contexts, forecasting provides the forward-looking intelligence needed for planning, budgeting, resource allocation, and risk management across all organizational functions.

- **Quantitative methods:** Time series models (ARIMA, exponential smoothing, Prophet), causal/regression models (using external predictors), machine learning approaches (gradient boosting, neural networks), ensemble methods (combining multiple models)
- **Qualitative methods:** Expert judgment (Delphi method), market research, scenario planning; used when historical data is limited or structural changes are expected
- **Evaluation metrics:** MAE (Mean Absolute Error), MAPE (Mean Absolute Percentage Error), RMSE (Root Mean Squared Error), forecast bias; backtesting with holdout periods validates model performance
- **Best practices:** Using multiple models and comparing performance, accounting for seasonality and external factors, communicating uncertainty through prediction intervals, regularly retraining models as new data arrives
- **Practical relevance:** Accurate forecasting directly impacts profitability -- overforecasting leads to excess inventory and waste, while underforecasting causes stockouts and lost revenue. Companies that implement systematic forecasting processes consistently outperform those relying on intuition alone.

---

