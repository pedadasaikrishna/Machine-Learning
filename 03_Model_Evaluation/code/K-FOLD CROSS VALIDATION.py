# =====================================================
# K-FOLD CROSS VALIDATION
# GRID SEARCH CV
# =====================================================

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import (
    cross_val_score,
    GridSearchCV
)

# =====================================================
# LOAD DATASET
# =====================================================

iris = load_iris()

X = iris.data
y = iris.target

# =====================================================
# MODEL
# =====================================================

model = DecisionTreeClassifier()

# =====================================================
# K-FOLD CROSS VALIDATION
# =====================================================

scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)

print("K-Fold Scores:")
print(scores)

print("\nAverage Score:")
print(scores.mean())

# =====================================================
# GRID SEARCH CV
# =====================================================

params = {
    "max_depth": [2, 3, 4, 5],
    "criterion": ["gini", "entropy"]
}

grid = GridSearchCV(
    estimator=model,
    param_grid=params,
    cv=5
)

grid.fit(X, y)

print("\nBest Parameters:")
print(grid.best_params_)

print("\nBest Score:")
print(grid.best_score_)