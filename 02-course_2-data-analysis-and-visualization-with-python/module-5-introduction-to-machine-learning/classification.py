import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    'Age': [25, 45, 35, 50, 23, 52, 40, 60, 48, 33],
    'Monthly_Bill': [50, 120, 80, 110, 40, 130, 90, 150, 105, 70],
    'Churn': [0, 1, 0, 1, 0, 1, 0, 1, 1, 0]  # 0 = Stayed, 1 = Left
}

df = pd.DataFrame(data)

print("--- DataFrame Head ---")
print(df.head())

X = df[['Age', 'Monthly_Bill']]  # Input Features
y = df['Churn']                  # Target Class (0 or 1)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("\n--- Model Evaluation ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
results_df = pd.DataFrame({
    'Actual_Churn': y_test.values,
    'Predicted_Churn': y_pred
})

print("\n--- Predictions Comparison ---")
print(results_df)