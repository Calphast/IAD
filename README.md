# Internet Usage and Political Stability Analysis

This project analyzes global internet usage patterns using **World Bank's
World Development Indicators** (https://cmustatistics.github.io/data-repository/politics/world-bank.html). The analysis focuses on two statistical approaches:

-   **ANOVA** to determine whether internet usage differs across
    income groups
-   **Linear Regression** to explore the relationship between
    internet usage and political stability

The goal is to better understand how **economic classification and
political conditions relate to internet adoption worldwide**.

# Dataset

The analysis uses **World Bank data** on global internet usage.

## Key Variables

- **Internet** – Percentage of individuals using the internet
- **Income Group** – Country income classification (High, Upper Middle, Lower Middle, Low)
- **PoliticalStability** – Political stability and absence of violence/terrorism score (z-score)

The analysis focuses on data from 2016.

# Methods

## ANOVA Analysis

A **one-way ANOVA test** evaluates whether mean internet usage differs
between income groups. 

The ANOVA test produced a **statistically significant result**,
indicating that internet usage differs across income groups.

Post-hoc Tukey tests identify which income groups differ significantly
from one another.

### Visualization

A **boxplot** compares internet usage distributions across:

-   High Income
-   Upper Middle Income
-   Lower Middle Income
-   Low Income

## Regression Analysis

A **linear regression model** examines the relationship between:

**Predictor Variable** - Political Stability

**Response Variable** - Internet Usage

The regression evaluates whether countries with **higher political
stability tend to have higher internet adoption rates**.

The regression analysis indicates a **relationship between political
stability and internet usage**, suggesting that countries with greater
political stability tend to have higher internet penetration.

### Visualization

The regression analysis includes:

-   Scatter plot of the relationship
-   Fitted regression line
-   Estimated regression coefficients

# Requirements

Python libraries used in this project:

    pandas
    numpy
    scipy
    matplotlib
    seaborn
    statsmodels

Install dependencies:

``` bash
pip install pandas numpy scipy matplotlib seaborn statsmodels
```
