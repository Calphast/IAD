# Internet Usage and Political Stability Analysis

This project analyzes global internet usage patterns using **World Bank's World Development Indicators** (https://cmustatistics.github.io/data-repository/politics/world-bank.html). The analysis focuses on three statistical and machine learning approaches:

- **ANOVA** to determine whether internet usage differs across income groups
- **Linear Regression** to explore the relationship between internet usage and political stability
- **Random Forest Regression** to model internet usage using multiple predictors and capture more complex relationships

The goal is to better understand how **economic classification and political conditions relate to internet adoption worldwide**. Plans to integrate different datasets and study other correlations are underway.

# Dataset

The analysis uses **World Bank data** on global internet usage.

## Key Variables

- **Internet** – Percentage of individuals using the internet
- **Income Group** – Country income classification (High, Upper Middle, Lower Middle, Low)
- **PoliticalStability** – Political stability and absence of violence/terrorism score (z-score)
- **GDP** – Economic output used as an additional predictor in the Random Forest model

The ANOVA and linear regression analyses focus on data from **2016**. The **Random Forest Regression** model utilizes data from **all available years** in the dataset.

# Methods

## ANOVA Analysis

A **one-way ANOVA test** evaluates whether mean internet usage differs between income groups.

The ANOVA test produced a **statistically significant result**, indicating that internet usage differs across income groups.

Post-hoc Tukey tests identify which income groups differ significantly from one another.

### Visualization

A **boxplot** compares internet usage distributions across:

- High Income
- Upper Middle Income
- Lower Middle Income
- Low Income

## Linear Regression Analysis

A **linear regression model** examines the relationship between:

**Predictor Variable** - Political Stability

**Response Variable** - Internet Usage

The regression evaluates whether countries with **higher political stability tend to have higher internet adoption rates**.

The regression analysis indicates a **relationship between political stability and internet usage**, suggesting that countries with greater political stability tend to have higher internet penetration.

### Visualization

The linear regression analysis includes:

- Scatter plot of the relationship
- Fitted regression line
- Estimated regression coefficients

## Random Forest Regression Analysis

A **Random Forest Regressor** is used to predict internet usage from multiple variables, including political stability and GDP.

The Random Forest model produced the following evaluation metrics:

- **Out-of-Bag Score:** 0.673
- **Mean Squared Error:** 324.085
- **R-squared:** 0.585

These results suggest that the model explains a **substantial portion of the variance** in internet usage and performs reasonably well on unseen data.

### Visualization

The Random Forest analysis includes:

- **Actual vs Predicted scatter plot** to compare model predictions with observed values
- **Feature importance plot** to show which predictors contribute most to the model

# Requirements

Python libraries used in this project:

    pandas
    numpy
    scipy
    matplotlib
    seaborn
    statsmodels
    scikit-learn

Install dependencies:

```bash
pip install pandas numpy scipy matplotlib seaborn statsmodels scikit-learn
