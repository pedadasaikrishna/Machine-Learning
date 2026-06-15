# Regression Algorithms

## What is Regression?

Regression is a supervised learning technique used to predict continuous numerical values.

The objective is to learn the relationship between independent variables (features) and a dependent variable (target).

Examples:

- House Price Prediction
- Salary Prediction
- Temperature Forecasting
- Sales Forecasting
- Demand Prediction

Output:

Continuous Numerical Value

Examples:

₹50,000
25.5°C
85.6%

---

# Types of Regression Algorithms

1. Simple Linear Regression
2. Multiple Linear Regression
3. Polynomial Regression
4. Decision Tree Regression
5. Random Forest Regression
6. Support Vector Regression (SVR)

---

# 1. Simple Linear Regression
![Simple Linear Regression](../assets/images/Simple%20Linear%20Regression.png)
## What is Simple Linear Regression?

Simple Linear Regression models the relationship between one independent variable and one dependent variable using a straight line.

Example:

Years of Experience → Salary

---

## Equation

```
Y = mX + c
```

Where:

Y = Predicted Value

X = Input Feature

m = Slope

c = Intercept

---

## Example

Experience = 5 Years

Predicted Salary = ₹50,000

The model learns a straight-line relationship.

---

## Advantages

- Easy to understand
- Fast training
- Highly interpretable

---

## Disadvantages

- Assumes linear relationship
- Poor performance on complex datasets

---

## Use Cases

- Salary Prediction
- Sales Prediction
- Revenue Forecasting

---

# 2. Multiple Linear Regression
![Multiple Linear Regression](../assets/images/Multiple%20Linear%20Regression.png)
## What is Multiple Linear Regression?

Extension of Simple Linear Regression.

Uses multiple independent variables(features) to predict one dependent variable.

---

## Equation

```
Y = b0 + b1X1 + b2X2 + b3X3 + ... + bnXn
```

---

## Example

House Price Prediction

Features:

- Area
- Bedrooms
- Bathrooms
- Location Score

Target:

House Price

---

## Why Use It?

Real-world problems rarely depend on only one feature.

---

## Advantages

- Handles multiple factors
- More realistic than simple regression

---

## Disadvantages

- Sensitive to multicollinearity
- More complex interpretation

---

## Use Cases

- House Price Prediction
- Loan Amount Prediction
- Insurance Cost Prediction

---

# 3. Polynomial Regression
![Polynomial Regression](../assets/images/Polynomial%20Regression.png)
## What is Polynomial Regression?

Polynomial Regression models non-linear relationships by introducing polynomial terms.

Instead of fitting a straight line, it fits a curve.

---

## Equation

```
Y = b0 + b1X + b2X² + b3X³ + ...
```

---

## Example

Study Hours vs Marks

Initially increases rapidly.

Later growth slows.

Straight line cannot capture this behavior.

Polynomial curve can.

---

## Advantages

- Captures non-linear patterns
- Better flexibility

---

## Disadvantages

- High degree may overfit
- Harder to interpret

---

## Use Cases

- Growth Curves
- Demand Forecasting
- Population Prediction

---

# 4. Decision Tree Regression
![Decision Tree Regression](../assets/images/Decision%20Tree%20Regression.png)
## What is Decision Tree Regression?

Decision tree regression is a supervised machine learning Regression algorithm that predicts continuous numerical outcomes by recursively partitioning data into smaller, distinct subsets based on feature thresholds

---

## Working

Example:

House Prices

Area > 2000 sqft?

YES → Luxury Segment

NO → Standard Segment

Further splits continue.

---

## Advantages

- Handles non-linear data
- No feature scaling required
- Easy visualization

---

## Disadvantages

- Can overfit easily
- Sensitive to data variations

---

## Use Cases

- Real Estate Pricing
- Customer Spending Prediction
- Risk Analysis

---

# 5. Random Forest Regression
![Random Forest Regression](../assets/images/Random%20Forest%20Regression.png)
## What is Random Forest Regression?

Random Forest Regression is a supervised machine learning algorithm that combines multiple independent decision trees during training and combines their individual predictions by averaging them to  final output(continuous numerical value).

It is an ensemble learning algorithm.

---

## Working

Tree 1 → 500000

Tree 2 → 520000

Tree 3 → 510000

Final Prediction:

Average = 510000

---

## Advantages

- High accuracy
- Reduces overfitting
- Handles non-linear relationships

---

## Disadvantages

- Slower training
- Less interpretable

---

## Use Cases

- Stock Forecasting
- House Price Prediction
- Demand Forecasting

---

# 6. Support Vector Regression (SVR)
![Support Vector Regression (SVR)](https://i0.wp.com/spotintelligence.com/wp-content/uploads/2024/05/support-vector-regression-svr.jpg?resize=1024%2C576&ssl=1)

## What is Support Vector Regression?

SVR is the regression version of Support Vector Machine (SVM).

Instead of minimizing prediction errors directly, SVR tries to fit a line within an acceptable error margin called epsilon (ε).

---

## Idea

Allow small errors.

Focus only on important points near the decision boundary.

---

## Advantages

- Works well on high-dimensional data
- Handles non-linear relationships using kernels
- Strong generalization

---

## Disadvantages

- Computationally expensive
- Difficult hyperparameter tuning

---

## Use Cases

- Financial Forecasting
- Energy Consumption Prediction
- Demand Prediction

---

# Comparison of Regression Algorithms

| Algorithm | Linear Data | Non-Linear Data | Interpretability | Overfitting Risk |
|------------|------------|----------------|------------------|------------------|
| Simple Linear Regression | Excellent | Poor | High | Low |
| Multiple Linear Regression | Excellent | Poor | Medium | Medium |
| Polynomial Regression | Good | Excellent | Medium | High |
| Decision Tree Regression | Good | Excellent | High | High |
| Random Forest Regression | Excellent | Excellent | Low | Low |
| SVR | Good | Excellent | Low | Medium |

---

# Algorithm Selection Guide

Use Simple Linear Regression:

- One feature
- Linear relationship

Use Multiple Linear Regression:

- Multiple features
- Linear relationship

Use Polynomial Regression:

- Curved relationship

Use Decision Tree Regression:

- Complex decision boundaries

Use Random Forest Regression:

- High accuracy required

Use SVR:

- Small to medium datasets
- High-dimensional data

---
