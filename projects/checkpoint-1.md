# Presentation 1, Checkpoint 1

## Data Transformation

Currently, the team is getting data from:
- [x] John's Shot Data Source (I need to get the github link for that for citations)
- [ ] nba_api
    - [x] team data
    - [x] player data
    - [ ] working on getting game data

We have data dictionaries for:
- [ ] shot data(?)
- [x] team and player data

## Hypothesis Testing

- [ ] 1. Testing the Relationship Between Player Scoring and All-Star Selection - SCOTT

    Null Hypothesis (H₀): There is no difference in the average points per game (PPG) between All-Star and non-All-Star players.
    Alternative Hypothesis (H₁): All-Star players have a significantly higher PPG than non-All-Star players.
    Test: Independent t-test or Mann-Whitney U test (if the data is not normally distributed).
    Why? If a strong relationship exists, logistic regression can be used to predict All-Star selection based on PPG and other stats.

    **Progress**: New relationship will be chosen using a correlation heatmap

- [ ] 2. Home vs. Away Performance Impact on Team Wins - JOHN

    Null Hypothesis (H₀): The average win percentage is the same for home and away games.
    Alternative Hypothesis (H₁): Teams win significantly more home games than away games.
    Test: Paired t-test (since each team plays both home and away games).
    Why? If significant, a logistic regression model can predict game outcomes based on home/away status.

    **Progress**: We need to get home and away classifications from `nba_api`

- [ ] 3. Effect of Three-Point Shooting on Team Win Percentage - SHAKE

    Null Hypothesis (H₀): There is no correlation between a team’s three-point attempt rate and its win percentage.
    Alternative Hypothesis (H₁): Teams that attempt more three-pointers have a significantly higher win percentage.
    Test: Pearson correlation or Spearman rank correlation (if non-linear).
    Why? If the relationship is strong, multiple linear regression can be used to model how shooting efficiency affects wins.

    **Progress**: Complete(?) Not sure if we need more work on the interpretation side

- [ ] 4. Predicting Playoff Qualification Based on Regular Season Stats - TREVOR

    Null Hypothesis (H₀): Teams that make the playoffs and those that do not have the same average statistics (e.g., PPG, turnovers, defensive efficiency).
    Alternative Hypothesis (H₁): Teams that make the playoffs have significantly different average statistics compared to non-playoff teams.
    Test: MANOVA (Multivariate Analysis of Variance) to compare multiple team statistics at once.
    Why? If significant, classification models like Random Forest or XGBoost can predict playoff qualification based on team stats.

    **Progress**: I have been down in the data scraping mines all day, I haven't touched this yet outside of watching videos about MANOVA.

## Data Visualization

For data visualizations we are looking at missingno to show NAs in data, and matplotlib + seaborn for time series charts. For NBA Shooting, sportyR will be used to plot shots on a basketball court.

### TODOS
- [ ] test missingno
- [ ] change missingno styling
- [ ] plot with sportyR
- [ ] figure out what we are charting with sportyR
- [ ] find mpl stylesheets
- [ ] find seaborn styles
- [ ] what are we charting with seaborn and mpl?
    - QQ Plots
    - Distributions
    - ???

## Slide Deck

The Slide will be broken into a 4x3 grid (4 rows, 3 columns). The first column will outline data transformations, with missingno to show data cleaning, matplotlib for summary statistics
