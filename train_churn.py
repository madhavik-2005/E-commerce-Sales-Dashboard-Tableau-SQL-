import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from imblearn.over_sampling import SMOTE
import joblib

# --------------------------
# Database connection
# --------------------------
engine = create_engine('postgresql://postgres:Maha#1415@localhost:5432/ecommerce')

# Load RFM data
rfm = pd.read_sql("SELECT * FROM vw_rfm", engine)
rfm['last_order_date'] = pd.to_datetime(rfm['last_order_date'])

# --------------------------
# Auto-adjust reference date
# --------------------------
# Pick a reference date 10% before the max last_order_date
max_date = rfm['last_order_date'].max()
reference_date = max_date - pd.Timedelta(days=90)  # 90 days before latest order
print(f"Reference date used: {reference_date}")

# Create churn label
rfm['churn'] = (reference_date - rfm['last_order_date']).dt.days > 90
print("Churn value counts:\n", rfm['churn'].value_counts())

# Check if we have both classes
if rfm['churn'].nunique() < 2:
    raise ValueError("Not enough classes in churn. Adjust reference date or check your RFM data.")

# --------------------------
# Features & target
# --------------------------
X = rfm[['recency_score', 'frequency_score', 'monetary_score']]
y = rfm['churn']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --------------------------
# Handle imbalance with SMOTE
# --------------------------
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# --------------------------
# Train model
# --------------------------
clf = GradientBoostingClassifier()
clf.fit(X_train_res, y_train_res)

# --------------------------
# Evaluate
# --------------------------
y_pred = clf.predict(X_test)
y_prob = clf.predict_proba(X_test)[:, 1]

print("Classification report:")
print(classification_report(y_test, y_pred, zero_division=0))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

# --------------------------
# Save model
# --------------------------
joblib.dump(clf, 'models/churn_model.pkl')
print("Churn model saved!")
