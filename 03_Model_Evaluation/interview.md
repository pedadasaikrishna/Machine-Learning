# Model Evaluation Interview Questions

## 1. Why is model evaluation important in Machine Learning?

Model evaluation helps determine how well a model generalizes to unseen data.

A model may achieve 99% training accuracy by memorizing data, but if it performs poorly on new data, it is not useful.

Evaluation helps:

- Compare models
- Detect overfitting
- Detect underfitting
- Select deployment-ready models

The ultimate goal is not training accuracy but generalization.

---

## 2. What is a Confusion Matrix and why is it useful?

A Confusion Matrix summarizes classification performance.

![](https://www.simplilearn.com/ice9/free_resources_article_thumb/confusion-matrix.JPG)

It provides detailed insight into prediction errors.

From the confusion matrix we derive:

- Accuracy
- Precision
- Recall
- F1 Score

It is one of the most important evaluation tools for classification problems.

---

## 3. When would you choose Precision over Recall and vice versa?

### Precision

Focuses on minimizing False Positives.

Use Cases:

- Spam Detection
- Loan Approval
- Recommendation Systems

### Recall

Focuses on minimizing False Negatives.

Use Cases:

- Cancer Detection
- Fraud Detection
- Security Systems

Interview Rule:

False Positive Cost High → Precision

False Negative Cost High → Recall

---

## 4. Why can Accuracy be misleading?

Accuracy assumes balanced classes.

Example:

1000 Transactions

990 Normal

10 Fraud

Model predicts all transactions as Normal.

Accuracy:

990/1000 = 99%

Looks excellent.

Reality:

Detected 0 fraud cases.

Therefore accuracy should never be used alone for imbalanced datasets.

---

## 5. Explain Cross Validation.

Cross Validation evaluates model stability by repeatedly training and validating on different data subsets.

Most common:

K-Fold Cross Validation

Example:

K = 5

Dataset divided into 5 folds.

Each fold becomes validation data once.

Benefits:

- Better use of data
- More reliable estimates
- Reduced variance

It is preferred over a single train-test split.

---

## 6. What is ROC-AUC and why is it important?

ROC Curve plots:

True Positive Rate vs False Positive Rate

at different classification thresholds.

AUC measures overall classifier quality.

Interpretation:

1.0 = Perfect Model

0.5 = Random Guess

Higher AUC indicates better class separation.

ROC-AUC is commonly used for comparing multiple classification models.

---

## 7. What is Regularization and how does it prevent overfitting?

Regularization adds a penalty term to the loss function.

Purpose:

Prevent the model from learning overly complex patterns.

Types:

### L1 Regularization (Lasso)

Creates sparse models and performs feature selection.

### L2 Regularization (Ridge)

Shrinks large coefficients and improves stability.

Regularization is one of the most effective methods for controlling overfitting.