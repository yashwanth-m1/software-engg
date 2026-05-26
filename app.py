import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Create app
app = Dash(__name__)

# App layout
app.layout = html.Div([

    html.H1(
        "Soul Foods Pink Morsel Sales Dashboard",
        id="header"
    ),

    html.Div([

        dcc.RadioItems(
            id="region-picker",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True
        )

    ], className="radio-group"),

    html.Div([
        dcc.Graph(id="sales-chart")
    ], className="chart-container")

])
# Callback for interactive filtering
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-picker", "value")
)
def update_chart(selected_region):

    # Filter data
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Group by date
    sales_by_date = filtered_df.groupby("date")["sales"].sum().reset_index()

    # Create line chart
    fig = px.line(
        sales_by_date,
        x="date",
        y="sales",
        title=f"Sales Data for {selected_region.title()} Region",
        labels={
            "date": "Date",
            "sales": "Sales"
        }
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)