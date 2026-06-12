# =====================================================
# EXPLORATORY DATA ANALYSIS (EDA) - BASIC CHEAT SHEET
# =====================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv("data.csv")

# =====================================================
# BASIC DATASET INFORMATION
# =====================================================

# Dataset Shape (Rows, Columns)
print("Shape:")
print(df.shape)

# Total Number of Elements
print("\nSize:")
print(df.size)

# Column Names
print("\nColumns:")
print(df.columns)

# Data Types
print("\nData Types:")
print(df.dtypes)

# First 5 Rows
print("\nHead:")
print(df.head())

# Last 5 Rows
print("\nTail:")
print(df.tail())

# Dataset Information
print("\nInfo:")
print(df.info())

# Statistical Summary
print("\nDescribe:")
print(df.describe())

# Missing Values Count
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Rows Count
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Unique Values Per Column
print("\nUnique Values:")
print(df.nunique())

# =====================================================
# CATEGORICAL COLUMN ANALYSIS
# =====================================================

# Replace 'Department' with your categorical column name

print("\nUnique Categories:")
print(df["Department"].unique())

print("\nCategory Counts:")
print(df["Department"].value_counts())

# =====================================================
# CORRELATION ANALYSIS
# =====================================================

print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# =====================================================
# HISTOGRAM
# Shows Distribution
# Replace 'Age' with your numerical column
# =====================================================

df["Age"].hist()
plt.title("Histogram")
plt.show()

# =====================================================
# BOX PLOT
# Shows Outliers
# Replace 'Salary' with your numerical column
# =====================================================

df.boxplot(column="Salary")
plt.title("Box Plot")
plt.show()

# =====================================================
# BAR CHART
# Shows Category Comparison
# Replace 'Department' with your categorical column
# =====================================================

df["Department"].value_counts().plot(kind="bar")
plt.title("Bar Chart")
plt.show()

# =====================================================
# PIE CHART
# Shows Percentage Distribution
# Replace 'Department' with your categorical column
# =====================================================

df["Department"].value_counts().plot(kind="pie")
plt.title("Pie Chart")
plt.show()

# =====================================================
# SCATTER PLOT
# Shows Relationship Between Variables
# Replace 'Age' and 'Salary'
# =====================================================

plt.scatter(df["Age"], df["Salary"])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Scatter Plot")
plt.show()

# =====================================================
# LINE PLOT
# Shows Trend
# Replace 'Age' and 'Salary'
# =====================================================

plt.plot(df["Age"], df["Salary"])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Line Plot")
plt.show()

# =====================================================
# HEATMAP
# Shows Correlation Between Numerical Columns
# =====================================================

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)

plt.title("Correlation Heatmap")
plt.show()