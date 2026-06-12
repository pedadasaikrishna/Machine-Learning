# Data Preprocessing Interview Questions

## 1. What is Data Preprocessing and why is it important?

Data preprocessing is the process of cleaning and transforming raw data before training a machine learning model.

Real-world data often contains:

- Missing values
- Duplicate records
- Outliers
- Inconsistent formats

Machine learning models learn from data. If the data is poor, the model's performance will also be poor.

A common saying:

"Garbage In = Garbage Out"

Therefore, preprocessing is one of the most important stages in the ML pipeline.

---

## 2. How do you handle missing values?

The approach depends on the data.

Methods:

1. Remove rows (if very few values are missing)
2. Mean Imputation (for numerical data)
3. Median Imputation (when outliers exist)
4. Mode Imputation (for categorical data)

Example:

Age:

20, 25, NULL, 30

Mean = 25

Replace NULL with 25.

The choice depends on data distribution.

---

## 3. What is the difference between Standardization and Normalization?

### Standardization

Formula:

Z = (X - Mean) / Standard Deviation

Output:

- Mean = 0
- Std = 1

Used for:

- Logistic Regression
- SVM
- PCA
- KNN

### Normalization

Formula:

(X - Min)/(Max - Min)

Output:

Values between 0 and 1.

Used for:

- Neural Networks
- Deep Learning
- Distance-based models

---

## 4. What are Outliers and how do you detect them?

Outliers are observations significantly different from the majority of the data.

Example:

25000
30000
35000
5000000

Methods:

1. IQR Method
2. Z-Score Method
3. Boxplots

Outliers can distort averages and negatively affect model performance.

---

## 5. What is One-Hot Encoding and when should it be used?

One-Hot Encoding converts categorical values into binary columns.

Example:

Color:

Red
Blue
Green

Converted into:

Red Blue Green

1    0    0

0    1    0

0    0    1

Used when categories have no natural order.

Example:

Country
Gender
City

---

## 6. What is Data Leakage?

Data leakage occurs when information unavailable during prediction is accidentally used during training.

Example:

Using test data statistics while preprocessing.

Result:

Model appears highly accurate during testing but performs poorly in production.

Data leakage is one of the most common causes of unrealistic ML results.

---

## 7. Why is Feature Scaling important?

Many ML algorithms use distance calculations.

Examples:

- KNN
- SVM
- PCA

Suppose:

Age = 25

Salary = 500000

Without scaling, Salary dominates the calculations.

Feature scaling ensures all features contribute fairly to the model.