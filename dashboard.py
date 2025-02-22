import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import joblib
from model import report_df, auc_roc, conf_matrix

model = joblib.load("fraud_model.pkl")


app = dash.Dash(_name_)


app.layout = html.Div([
    html.H1("Fraud Detection Model Performance", style={'textAlign': 'center'}),
    

    html.H3(f"AUC-ROC Score: {auc_roc:.2f}"),
    
    
    dcc.Graph(
        figure=px.imshow(conf_matrix, labels=dict(x="Predicted", y="Actual"), 
                         x=["Not Fraud", "Fraud"], y=["Not Fraud", "Fraud"],
                         title="Confusion Matrix", color_continuous_scale="blues")
    ),
    
    
    dcc.Graph(
        figure=px.bar(report_df, x=report_df.index, y="f1-score", title="F1-Score by Class")
    ),
])


if _name_ == "_main_":
    app.run_server(debug=True)