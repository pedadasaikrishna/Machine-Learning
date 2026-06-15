# Classification Algorithms Interview Questions

## 1. What is Classification in Machine Learning?

Classification is a supervised learning task where the objective is to predict discrete categories or classes based on input features.

The model learns from labeled data and assigns new observations to predefined classes.

Examples:

* Spam / Not Spam
* Fraud / Genuine
* Pass / Fail
* Disease / No Disease

Unlike regression, which predicts continuous numerical values, classification predicts categorical outcomes.

**Interview Follow-Up:**

How do you identify whether a problem is classification or regression?

If the output is a category → Classification

If the output is a number → Regression

---

## 2. What is the difference between Linear and Non-Linear Classifiers?

### Linear Classifiers

Linear classifiers separate classes using a straight-line decision boundary (or hyperplane in higher dimensions).

Examples:

* Logistic Regression
* Linear SVM
* Perceptron
* SGD Classifier

Advantages:

* Fast training
* Easy interpretation
* Works well on linearly separable data

Limitations:

* Cannot capture complex patterns

---

### Non-Linear Classifiers

Non-linear classifiers create complex decision boundaries.

Examples:

* KNN
* Kernel SVM
* Decision Tree
* Random Forest
* AdaBoost
* Neural Networks

Advantages:

* Capture complex relationships
* Higher predictive power

Limitations:

* Higher computational cost
* Greater overfitting risk

**Interview Rule:**

Simple Data → Linear Models

Complex Data → Non-Linear Models

---

## 3. Why is Logistic Regression called Regression even though it is used for Classification?

The name comes from its mathematical foundation.

Logistic Regression first computes a linear equation:

```
z = b0 + b1x1 + b2x2 + ...
```

Then applies the Sigmoid Function:

```
P(Y=1) = 1 / (1 + e^(-z))
```

This converts the output into a probability between 0 and 1.

The final prediction is obtained by applying a threshold (usually 0.5).

Therefore, despite its name, Logistic Regression is a classification algorithm.

**Interview Follow-Up:**

Output:

* Regression → Numerical Value
* Logistic Regression → Probability → Class Label

---

## 4. Why is Random Forest usually preferred over a single Decision Tree?

A Decision Tree can easily overfit because it learns very specific rules from training data.

Random Forest solves this problem by:

1. Creating multiple decision trees.
2. Training each tree on different samples.
3. Combining predictions through voting.

Benefits:

* Higher accuracy
* Better generalization
* Reduced overfitting
* More stable predictions

This is why Random Forest is one of the most widely used classification algorithms in industry.

---

## 5. When would you use KNN and when would you avoid it?

### Use KNN When:

* Dataset is small to medium sized.
* Relationships are complex.
* Fast training is required.
* Data is properly scaled.

### Avoid KNN When:

* Dataset is very large.
* Features are high-dimensional.
* Real-time prediction is required.

Reason:

KNN stores the entire training dataset and performs distance calculations during prediction, making prediction expensive.

**Interview Follow-Up:**

Why is feature scaling important in KNN?

Because KNN uses distance calculations.

Without scaling, large-valued features dominate the distance metric.

---

## 6. What is the difference between Bagging and Boosting?

### Bagging (Bootstrap Aggregating)

Models are trained independently.

Final prediction combines outputs from all models.

Goal:

Reduce Variance

Example:

Random Forest

---

### Boosting

Models are trained sequentially.

Each model focuses on mistakes made by previous models.

Goal:

Reduce Bias

Examples:

* AdaBoost
* Gradient Boosting
* XGBoost

---

### Simple Interview Statement

Bagging:

"Train Independently"

Boosting:

"Learn From Previous Mistakes"

---

## 7. Why are Neural Networks considered more powerful than traditional classifiers?

Artificial Neural Networks can learn highly complex and non-linear relationships.

Unlike Logistic Regression or Decision Trees, Neural Networks automatically learn useful representations from data through multiple hidden layers.

Advantages:

* Handle complex patterns
* Work with images, text and speech
* Foundation of Deep Learning
* State-of-the-art performance in many domains

Limitations:

* Require large datasets
* Computationally expensive
* Less interpretable

This is why Neural Networks dominate modern AI systems such as:

* ChatGPT
* Image Recognition Systems
* Speech Assistants
* Autonomous Vehicles
