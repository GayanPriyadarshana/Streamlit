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
    color_continuous_scale=px.colors.sequential.Purples,
    title='Users by region'
)

# Update the layout of the map to ensure the entire map is visible
fig.update_geos(
    visible=True, 
    showcountries=True,
    showcoastlines=True,
    showland=True, 
    fitbounds="locations"
)

# Customize the layout
fig.update_layout(
    coloraxis_colorbar=dict(
        title='Number of Users',
        tickvals=[50000, 200000, 350000, 500000, 750000]
    ),
    geo=dict(
        projection_scale=1,  # this can be used to zoom in or out
        center=dict(lat=0, lon=180)  # this will center on the Pacific area
    )
)

# Streamlit command to display the plot
st.plotly_chart(fig)
