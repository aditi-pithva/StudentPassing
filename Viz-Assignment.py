#!/usr/bin/env python
# coding: utf-8

# In[2]:


from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load the CSV file
df2 = pd.read_csv('df2_data.csv')

# Create the Dash app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Student Grade Analysis", style={'textAlign': 'center'}),

    # Dropdown for Residency Slicer
    html.Label("Slicer:"),
    dcc.Dropdown(
        id="residency-slicer",
        options=[{"label": res, "value": res} for res in df2["Residency"].unique()],
        value=df2["Residency"].unique()[0],  # Default value
        clearable=False
    ),

    # Subplots for visualizations
    html.Div([
        dcc.Graph(id="visual-1", style={"display": "inline-block", "width": "48%"}),
        dcc.Graph(id="visual-2", style={"display": "inline-block", "width": "48%"}),
        dcc.Graph(id="visual-3", style={"display": "inline-block", "width": "48%"}),
        dcc.Graph(id="visual-4", style={"display": "inline-block", "width": "48%"})
    ])
])

# Define the callback to update the graphs based on the Residency selection
@app.callback(
    [
        Output("visual-1", "figure"),
        Output("visual-2", "figure"),
        Output("visual-3", "figure"),
        Output("visual-4", "figure")
    ],
    Input("residency-slicer", "value")
)
def update_graphs(selected_residency):
    # Filter the DataFrame based on the selected Residency
    filtered_df = df2[df2["Residency"] == selected_residency]

    # Create individual visualizations
    fig1 = px.histogram(
        filtered_df,
        x="First Language",
        title="First Language Distribution",
        color_discrete_sequence=["#636EFA"]
    )

    fig2 = px.histogram(
        filtered_df,
        x="Age Group",
        title="Age Group Distribution",
        color_discrete_sequence=["#EF553B"]
    )

    fig3 = px.histogram(
        filtered_df,
        x="Gender",
        title="Gender Distribution",
        color_discrete_sequence=["#00CC96"]
    )

    fig4 = px.histogram(
        filtered_df,
        x="English Grade",
        title="English Grade Distribution",
        color_discrete_sequence=["#AB63FA"]
    )

    return fig1, fig2, fig3, fig4

# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)


# In[ ]:




