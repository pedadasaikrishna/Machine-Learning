# =====================================================
# DATA PREPROCESSING - FOUNDATION EXAMPLES
# =====================================================

import pandas as pd

# =====================================================
# SAMPLE DATA
# =====================================================

df = pd.DataFrame({
    "Age": [22, 25, None, 30, 28],
    "Salary": [30000, None, 45000, 50000, 55000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
})

print("Original Data")
print(df)

# =====================================================
# 1. REMOVE MISSING VALUES
# =====================================================

# Removes rows containing at least one null value
df_removed = df.dropna()

print("\nAfter Removing Missing Values")
print(df_removed)

# =====================================================
# 2. MEAN IMPUTATION
# =====================================================

# Replace missing Age with average Age
df_mean = df.copy()
df_mean["Age"] = df_mean["Age"].fillna(df_mean["Age"].mean())

print("\nMean Imputation")
print(df_mean)

# =====================================================
# 3. MEDIAN IMPUTATION
# =====================================================

# Replace missing Salary with median Salary
df_median = df.copy()
df_median["Salary"] = df_median["Salary"].fillna(df_median["Salary"].median())

print("\nMedian Imputation")
print(df_median)

# =====================================================
# 4. MODE IMPUTATION
# =====================================================

# Replace missing Department with most frequent value
df_mode = df.copy()
df_mode["Department"] = df_mode["Department"].fillna(
    df_mode["Department"].mode()[0]
)

print("\nMode Imputation")
print(df_mode)