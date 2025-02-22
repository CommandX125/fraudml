import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score


df = pd.read_csv("fraudTest.csv")
df["is_fraud"] = df["is_fraud"].astype(int)  
features = ["amt", "unix_time", "category"]  
X = pd.get_dummies(df[features], drop_first=True)  
y = df["is_fraud"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]


report = classification_report(y_test, y_pred, output_dict=True)
auc_roc = roc_auc_score(y_test, y_prob)
conf_matrix = confusion_matrix(y_test, y_pred)


report_df = pd.DataFrame(report).transpose()


import joblib
joblib.dump(model, "fraud_model.pkl")