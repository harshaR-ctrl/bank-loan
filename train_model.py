import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Load the dataset
df = pd.read_csv('loan_dataset.csv')

print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

# Prepare features and target
X = df.drop('LoanApproved', axis=1)
y = df['LoanApproved']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
model.fit(X_train_scaled, y_train)

# Evaluate the model
train_score = model.score(X_train_scaled, y_train)
test_score = model.score(X_test_scaled, y_test)

print(f"\nModel Training Accuracy: {train_score:.4f}")
print(f"Model Testing Accuracy: {test_score:.4f}")

# Save the model and scaler
pickle.dump(model, open('loan_model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

print("\nModel and scaler saved successfully!")
print("Feature names:", list(X.columns))
