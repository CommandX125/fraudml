import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore
from sklearn.ensemble import IsolationForest


df = pd.read_csv("fraudTest.csv") 
df.columns = df.columns.str.lower()  
df["time"] = range(len(df))  


fraud_counts = df["is_fraud"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    fraud_counts, 
    labels=["Non-Fraud", "Fraud"], 
    autopct='%1.1f%%', 
    colors=["green", "red"],
    startangle=90, 
    explode=[0, 0.1]
)
plt.title("Fraud vs Non-Fraud Transactions (Pie Chart)")
plt.show()


df['amount_zscore'] = zscore(df['amount'])
anomalies = df[df['amount_zscore'].abs() > 3]
print("🔹 Transactions Marked as Anomalies (Z-Score > 3):")
print(anomalies[['amt', 'amount_zscore']])

plt.figure(figsize=(10,6))
sns.scatterplot(x=df.index, y=df['amt'], hue=(df['amount_zscore'].abs() > 3), palette={True: "red", False: "blue"})
plt.title("Anomalous Transactions (Red = Anomaly)")
plt.show()


model = IsolationForest(contamination=0.01, random_state=42)
df['Anomaly'] = model.fit_predict(df[['amt', 'time']])


anomaly_counts = df['Anomaly'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    anomaly_counts, 
    labels=["Normal Transactions", "Anomalies"], 
    autopct='%1.1f%%', 
    colors=["blue", "red"],
    startangle=90, 
    explode=[0, 0.1]
)
plt.title("Anomalies Detected Using Isolation Forest (Pie Chart)")
plt.show()