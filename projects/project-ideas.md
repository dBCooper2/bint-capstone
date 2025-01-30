# Project Ideas

## Hypothesis Tests for Teams

1. Testing the Relationship Between Player Scoring and All-Star Selection - SCOTT

    Null Hypothesis (H₀): There is no difference in the average points per game (PPG) between All-Star and non-All-Star players.
    Alternative Hypothesis (H₁): All-Star players have a significantly higher PPG than non-All-Star players.
    Test: Independent t-test or Mann-Whitney U test (if the data is not normally distributed).
    Why? If a strong relationship exists, logistic regression can be used to predict All-Star selection based on PPG and other stats.

2. Home vs. Away Performance Impact on Team Wins - JOHN

    Null Hypothesis (H₀): The average win percentage is the same for home and away games.
    Alternative Hypothesis (H₁): Teams win significantly more home games than away games.
    Test: Paired t-test (since each team plays both home and away games).
    Why? If significant, a logistic regression model can predict game outcomes based on home/away status.

3. Effect of Three-Point Shooting on Team Win Percentage - SHAKE

    Null Hypothesis (H₀): There is no correlation between a team’s three-point attempt rate and its win percentage.
    Alternative Hypothesis (H₁): Teams that attempt more three-pointers have a significantly higher win percentage.
    Test: Pearson correlation or Spearman rank correlation (if non-linear).
    Why? If the relationship is strong, multiple linear regression can be used to model how shooting efficiency affects wins.

4. Predicting Playoff Qualification Based on Regular Season Stats - TREVOR

    Null Hypothesis (H₀): Teams that make the playoffs and those that do not have the same average statistics (e.g., PPG, turnovers, defensive efficiency).
    Alternative Hypothesis (H₁): Teams that make the playoffs have significantly different average statistics compared to non-playoff teams.
    Test: MANOVA (Multivariate Analysis of Variance) to compare multiple team statistics at once.
    Why? If significant, classification models like Random Forest or XGBoost can predict playoff qualification based on team stats.

## ChatGPT Project Idea Vomit

These are ideas that ChatGPT gave for each topic we will cover in our capstone presentations.

### 1. Data Transformation and Preprocessing

    Handling missing values (e.g., filling missing player stats with the median)
    Feature scaling (e.g., normalizing points, assists, and rebounds for models that require scaling)
    Encoding categorical variables (e.g., converting team names into one-hot encoding)
    Feature engineering (e.g., creating advanced stats like "True Shooting Percentage" or "Assist-to-Turnover Ratio")

### 2. Hypothesis Testing

    Example: Testing whether the average points per game differs between two eras of basketball (e.g., pre-2010 vs. post-2010) using a t-test.
    Chi-square test: Checking if there’s a significant association between player positions and whether they make the All-Star team.

### 3. Linear and Multiple Linear Regression

    Predict total points per game (PPG) based on field goal attempts, free throw attempts, and three-point attempts.
    Predict team win percentage using various team statistics like turnovers, assists, and defensive efficiency.

### 4. Stepwise and Polynomial Regression

    Stepwise regression: Selecting the most relevant variables to predict player efficiency rating (PER).
    Polynomial regression: Modeling the non-linear relationship between age and player performance (e.g., quadratic regression for peak performance years).

### 5. KNN Regression

    Predicting player salaries based on nearest neighbors with similar performance metrics (e.g., PPG, rebounds, assists).

### 6. Decision Tree (DT) and Random Forest (RF) Regression

    Decision Tree: Predicting a player’s PPG based on various shooting metrics.
    Random Forest: Improving the accuracy of the PPG prediction by averaging multiple decision trees.

### 7. Ridge and Lasso Regression

    Predicting team wins per season while preventing overfitting by penalizing less important features.

### 8. Logistic Regression

    Classifying whether a player will make the All-Star team based on past performance stats.

### 9. Decision Trees for Classification

    Classifying players into positions (e.g., guard, forward, center) based on height, weight, and playing style.

### 10. Random Forests for Classification

    Predicting whether a team will make the playoffs based on season statistics.

### 11. XGBoost and Neural Networks

    XGBoost: Predicting MVP winners using advanced statistics and player historical performance.
    Neural Networks: Predicting game outcomes based on player and team stats.

### 12. KNN Classification

    Classifying playing style (e.g., scorer vs. playmaker vs. defender) based on player stats.

### 13. Support Vector Machines (SVMs)

    Predicting whether a player is a starter or bench player based on efficiency metrics.

## Sports Analytics (Hockey)

- Shots mapped on the rink/court/field/etc. and hypothesis testing on positions taking shots as well as locations of shots (Data Transformation and Hypothesis Testing)
  - testing group means: lefties vs righties, LW vs RW, FWDs vs Ds
- Forecasting Player Performance using Regression
- Win Probability Model (Logistic Regression and XGBoost, Classification Problems)

## Finance

- Portfolio Performance and Hypothesis Testing on Portfolio Strategies, Graphed (1st Project)
- Portfolio Backtesting and Forecasting using CAPM and Fama French Regression as well as Treynor, Sharpe, etc. Ratios for performance benchmarking (2nd Project)
- Fraud Detection for Credit Cards/Crypto (Classification Project)

## Webdev

- Graphing Page Views, Single Factor Hypothesis Testing for Web Analytics (Bounce Rates, time on page, etc)

- Forecasting Web Analytic Rates using Regression or K-Factor Experiments

- Classifying Users?