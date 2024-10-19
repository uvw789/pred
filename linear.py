# -*- coding: utf-8 -*-
"""E01_MLL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ugnYsMhOL6D5lrWqC46x55gjY_qCSjk4
"""

import pandas as pd
import numpy as np

file_path = 'BostonHousing.csv'  # Update this if your file path is different
data = pd.read_csv(file_path)

print(data.head())

# Display information about the dataset
print(data.info())

# Check for missing values
print(data.isnull().sum())

data = data.dropna()

# Initial linear regression with all parameters
X_all = data.drop(columns=['medv'])
y_all = data['medv']

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X_train_all, X_test_all, y_train_all, y_test_all = train_test_split(X_all, y_all, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model_all = LinearRegression()

# Train the model
model_all.fit(X_train_all, y_train_all)

y_pred_all = model_all.predict(X_test_all)

mse_all = mean_squared_error(y_test_all, y_pred_all)
rmse_all = np.sqrt(mse_all)
r2_all = r2_score(y_test_all, y_pred_all)

print(f"All Parameters - Mean Squared Error: {mse_all}")
print(f"All Parameters - Root Mean Squared Error: {rmse_all}")
print(f"All Parameters - R-squared: {r2_all}")

# Plotting actual vs predicted values for all parameters
plt.figure(figsize=(10, 6))
plt.scatter(y_test_all, y_pred_all, edgecolor='k', alpha=0.7)
plt.plot([y_test_all.min(), y_test_all.max()], [y_test_all.min(), y_test_all.max()], 'r--', lw=3)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('All Parameters - Actual vs Predicted Values')
plt.show()

# Draw a heatmap of correlations
plt.figure(figsize=(12, 10))
corr_matrix = data.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

relevant_features = corr_matrix.index[abs(corr_matrix["medv"]) > 0.5].tolist()
relevant_features.remove('medv')
print("Selected relevant features:", relevant_features)

# Linear regression with selected parameters
X_relevant = data[relevant_features]
y_relevant = data['medv']

# Split the data into training and testing sets
X_train_rel, X_test_rel, y_train_rel, y_test_rel = train_test_split(X_relevant, y_relevant, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model_rel = LinearRegression()

# Train the model
model_rel.fit(X_train_rel, y_train_rel)

y_pred_rel = model_rel.predict(X_test_rel)

# Evaluate the model
mse_rel = mean_squared_error(y_test_rel, y_pred_rel)
rmse_rel = np.sqrt(mse_rel)
r2_rel = r2_score(y_test_rel, y_pred_rel)

print(f"Selected Parameters - Mean Squared Error: {mse_rel}")
print(f"Selected Parameters - Root Mean Squared Error: {rmse_rel}")
print(f"Selected Parameters - R-squared: {r2_rel}")

# Plotting actual vs predicted values for selected parameters
plt.figure(figsize=(10, 6))
plt.scatter(y_test_rel, y_pred_rel, edgecolor='k', alpha=0.7)
plt.plot([y_test_rel.min(), y_test_rel.max()], [y_test_rel.min(), y_test_rel.max()], 'r--', lw=3)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Selected Parameters - Actual vs Predicted Values')
plt.show()

# Compare results
print("\nComparison:")
print(f"All Parameters - RMSE: {rmse_all}, R-squared: {r2_all}")
print(f"Selected Parameters - RMSE: {rmse_rel}, R-squared: {r2_rel}")