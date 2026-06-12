# =====================================================
# EDA VISUALIZATIONS CHEAT SHEET
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv("data.csv")

# =====================================================
# 1. HISTOGRAM
# Shows Distribution
# =====================================================

df["Age"].hist()

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

# =====================================================
# 2. BOX PLOT
# Shows Outliers
# =====================================================

df.boxplot(column="Salary")

plt.title("Salary Box Plot")

plt.show()

# =====================================================
# 3. BAR CHART
# Category Comparison
# =====================================================

df["Department"].value_counts().plot(
    kind="bar"
)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")

plt.show()

# =====================================================
# 4. PIE CHART
# Percentage Distribution
# =====================================================

df["Department"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Department Distribution")

plt.show()

# =====================================================
# 5. SCATTER PLOT
# Relationship Between Variables
# =====================================================

plt.scatter(
    df["Age"],
    df["Salary"]
)

plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")

plt.show()

# =====================================================
# 6. LINE PLOT
# Trend Analysis
# =====================================================

plt.plot(
    df["Age"],
    df["Salary"]
)

plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")

plt.show()

# =====================================================
# 7. HEATMAP
# Correlation Visualization
# =====================================================

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()

# =====================================================
# 8. PAIR PLOT
# Relationship Between Numerical Columns
# =====================================================

sns.pairplot(df)

plt.show()

# =====================================================
# 9. COUNT PLOT
# Count of Categories
# =====================================================

sns.countplot(
    x="Department",
    data=df
)

plt.title("Department Count")

plt.show()

# =====================================================
# 10. DISTRIBUTION PLOT
# Histogram + KDE Curve
# =====================================================

sns.histplot(
    df["Salary"],
    kde=True
)

plt.title("Salary Distribution")

plt.show()