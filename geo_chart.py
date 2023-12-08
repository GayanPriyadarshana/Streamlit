import streamlit as st
import plotly.express as px
import pandas as pd

# Sample dataset of user counts by country using ISO Alpha-3 country codes
data = {
    'iso_alpha': ['USA', 'BRA', 'RUS', 'IND', 'CHN', 'ZAF', 'NGA', 'EGY', 'SAU', 'IRN', 'CAN', 'MEX', 'FRA', 'DEU', 'GBR', 'AUS'],
    'users': [800000, 210000, 150000, 600000, 900000, 120000, 115000, 130000, 95000, 85000, 300000, 160000, 250000, 300000, 350000, 150000]
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Create the choropleth map using Plotly Express
fig = px.choropleth(
    df,
    locations='iso_alpha',
    color='users',
    hover_name='iso_alpha',
    color_continuous_scale=px.colors.sequential.Purples,  # Purple color scale
    title='Users by region',
    scope='world',
    projection='natural earth'
)

# Update the layout of the map to have a light grey color for countries with no data
fig.update_geos(
    showframe=False,
    showcoastlines=True,
    showland=True,
    landcolor='lightgrey',  # Set land color to light grey for countries with no data
)

# Customize the layout
fig.update_layout(
    coloraxis_colorbar=dict(
        title='Number of Users',
        tickvals=[200000, 350000, 500000, 750000],
    )
    # legend=dict(
    #     orientation="h",  # Horizontal legend
    #     yanchor="bottom",
    #     y=-0.2,  # Position of the legend (below the chart)
    #     xanchor="center",
    #     x=0.5  # Center the legend
    # )
)

# Streamlit command to display the plot
st.plotly_chart(fig)
