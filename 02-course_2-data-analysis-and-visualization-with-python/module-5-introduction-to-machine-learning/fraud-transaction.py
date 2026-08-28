import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE

np.random.seed(42)

n_samples = 10000

normal_amounts = np.random.exponential(scale=50, size=int(n_samples * 0.98))
normal_hours = np.random.randint(6, 23, size=int(n_samples * 0.98))
normal_distance = np.random.normal(loc=5, scale=2, size=int(n_samples * 0.98))

fraud_amounts = np.random.exponential(scale=300, size=int(n_samples * 0.02))
fraud_hours = np.random.choice([0, 1, 2, 3, 4, 23], size=int(n_samples * 0.02))
fraud_distance = np.random.normal(loc=50, scale=15, size=int(n_samples * 0.02))

df_normal = pd.DataFrame({
    'amount': normal_amounts,
    'hour': normal_hours,
    'distance_from_home': np.abs(normal_distance),
    'is_fraud': 0
})

df_fraud = pd.DataFrame({
    'amount': fraud_amounts,
    'hour': fraud_hours,
    'distance_from_home': np.abs(fraud_distance),
    'is_fraud': 1
})

df = pd.concat([df_normal, df_fraud]).sample(frac=1).reset_index(drop=True)

X = df[['amount', 'hour', 'distance_from_home']]
y = df['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.05,
    max_depth=4,
    random_state=42,
    eval_metric='logloss'
)

model.fit(X_train_resampled, y_train_resampled)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print("--- Classification Report ---")
print(classification_report(y_test, y_pred))

print("\n--- Confusion Matrix ---")
print(confusion_matrix(y_test, y_pred))

print(f"\nROC-AUC Score: {roc_auc_score(y_test, y_prob):.4f}")