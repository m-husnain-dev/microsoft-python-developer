import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = {
    'Experience_Years': [1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7],
    'Education_Level': [1, 1, 1, 2, 2, 2, 3, 3, 3, 3],
    'Salary': [39343, 46205, 37731, 43525, 39891, 56642, 60150, 54445, 64445, 57189]
}

df = pd.DataFrame(data)

print("--- DataFrame Head ---")
print(df.head())

X = df[['Experience_Years', 'Education_Level']]  # Input Features (DataFrame)
y = df['Salary']                                   # Target Variable (Series)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print(f"\nR2 Score: {r2:.4f}")

results_df = pd.DataFrame({
    'Actual Salary': y_test,
    'Predicted Salary': np.round(y_pred, 2),
    'Difference': np.round(y_test - y_pred, 2)
})

print("\n--- Predictions Table ---")
print(results_df)