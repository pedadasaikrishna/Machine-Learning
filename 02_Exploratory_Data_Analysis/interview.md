# Exploratory Data Analysis (EDA) Interview Questions

## 1. What is EDA and why is it important?

Exploratory Data Analysis (EDA) is the process of understanding and analyzing data before building machine learning models.

Its objectives are:

- Understand data structure
- Detect missing values
- Find outliers
- Discover patterns
- Study relationships between variables

EDA is important because many machine learning failures occur due to poor understanding of data rather than poor model selection.

A common industry saying is:

"Spend 80% of the time understanding the data and 20% building the model."

---

## 2. What is the difference between Univariate, Bivariate and Multivariate Analysis?

### Univariate Analysis

Analysis of one variable.

Examples:

- Age Distribution
- Salary Distribution

Common plots:

- Histogram
- Box Plot

### Bivariate Analysis

Analysis of two variables.

Examples:

- Salary vs Experience
- Age vs Income

Common plots:

- Scatter Plot
- Correlation Plot

### Multivariate Analysis

Analysis involving multiple variables simultaneously.

Examples:

- Correlation Matrix
- Pair Plot

Used for discovering complex relationships among features.

---

## 3. How do you detect outliers during EDA?

Outliers are observations significantly different from the majority of data.

Common methods:

### IQR Method

IQR = Q3 − Q1

Outlier Range:

Lower Bound = Q1 − 1.5(IQR)

Upper Bound = Q3 + 1.5(IQR)

### Z-Score Method

Values with:

|Z| > 3

are considered potential outliers.

### Visualization

- Box Plot
- Scatter Plot

Outliers should be investigated before removal because some may represent important business cases.

---

## 4. What is correlation and why is it useful?

Correlation measures the strength and direction of relationship between two numerical variables.

Range:

-1 to +1

Positive Correlation:

Experience ↑ Salary ↑

Negative Correlation:

Price ↑ Demand ↓

EDA uses correlation to:

- Find important features
- Remove redundant variables
- Detect multicollinearity

---

## 5. What is a correlation heatmap?

A correlation heatmap is a visual representation of correlation values between all numerical features.

Benefits:

- Quickly identify strongly related variables
- Detect multicollinearity
- Support feature selection

It is one of the most commonly used EDA visualizations in industry projects.

---

## 6. How do you handle class imbalance discovered during EDA?

Example:

99% Normal Transactions

1% Fraud Transactions

Problems:

- Accuracy becomes misleading
- Model may ignore minority class

Solutions:

- Oversampling
- Undersampling
- SMOTE
- Precision/Recall based evaluation

EDA helps identify class imbalance before model training.

---

## 7. What insights should you collect during EDA before building a model?

Before training a model, EDA should answer:

- Are there missing values?
- Are there outliers?
- What are the feature distributions?
- Which features are important?
- Are features correlated?
- Is the target variable balanced?
- Do we need feature engineering?

These insights guide preprocessing, feature selection and model choice.