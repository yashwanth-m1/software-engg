import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Group sales by date
sales_by_date = df.groupby("date")["sales"].sum().reset_index()

# Create line chart
fig = px.line(
    sales_by_date,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Sales"
    }
)

# Create Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualizer"),

    dcc.Graph(
        figure=fig
    )
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)