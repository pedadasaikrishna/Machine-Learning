# Regression Algorithms Interview Questions

## 1. What is Regression in Machine Learning?

Regression is a supervised learning technique used to predict continuous numerical values.

Examples:

- House Prices
- Salaries
- Sales Forecasting
- Temperature Prediction

The goal is to learn the relationship between input features and a numerical target variable.

A simple interview rule:

Categories → Classification

Numbers → Regression

---

## 2. What is the difference between Simple and Multiple Linear Regression?

### Simple Linear Regression

Uses only one independent variable.

Example:

Experience → Salary

Equation:

Y = mX + c

### Multiple Linear Regression

Uses multiple independent variables.

Example:

Area + Bedrooms + Bathrooms → House Price

Equation:

Y = b0 + b1X1 + b2X2 + ... + bnXn

Most real-world problems use Multiple Linear Regression because outcomes are usually influenced by multiple factors.

---

## 3. When would you use Polynomial Regression instead of Linear Regression?

Linear Regression assumes a straight-line relationship.

When data follows a curved pattern, Linear Regression performs poorly.

Polynomial Regression introduces higher-degree terms such as:

X², X³

allowing the model to learn non-linear relationships.

Example:

Study Hours vs Marks

Growth curves

Population growth

The trade-off is that high-degree polynomials may overfit.

---

## 4. Why is Random Forest Regression generally better than a single Decision Tree?

Decision Trees can easily overfit because they learn highly specific rules.

Random Forest solves this by:

- Building many trees
- Training them on different samples
- Averaging predictions

Benefits:

- Higher accuracy
- Better generalization
- Reduced overfitting

This is why Random Forest is one of the most popular regression algorithms in industry.

---

## 5. What is Support Vector Regression (SVR)?

SVR is the regression version of Support Vector Machine.

Instead of fitting every point exactly, SVR tries to fit a function within an acceptable error margin called epsilon (ε).

Advantages:

- Works well in high dimensions
- Handles non-linear data using kernels
- Strong generalization

Limitations:

- Slow on large datasets
- Hyperparameter tuning can be difficult

---

## 6. Which regression algorithm would you choose for a House Price Prediction problem?

The answer depends on the dataset.

Linear Relationship:
- Multiple Linear Regression

Complex Non-Linear Relationship:
- Decision Tree Regression

High Accuracy Requirement:
- Random Forest Regression

Large Complex Dataset:
- Gradient Boosting / XGBoost (advanced)

In practical projects, multiple models are trained and compared using evaluation metrics such as RMSE and R².

---

## 7. How do you evaluate Regression Models?

Common metrics:

### MAE

Average absolute error.

Easy to interpret.

### MSE

Squares errors before averaging.

Penalizes large mistakes.

### RMSE

Square root of MSE.

Most commonly used.

### R² Score

Measures how much variance the model explains.

R² = 1

Perfect model.

Higher R² and lower RMSE generally indicate a better regression model.