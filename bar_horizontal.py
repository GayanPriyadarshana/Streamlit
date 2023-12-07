import streamlit as st
import plotly.express as px
import pandas as pd

# Sample dataset to match the provided image
data = pd.DataFrame({
    "Product": ["alpha", "beta", "gamma", "delta"],
    "Sales Percentage": [.1, .2, .3, .4]  # Assuming these are the percentages shown in the bars
})

# Creating the horizontal bar chart using Plotly
fig = px.bar(
    data,
    x='Sales Percentage',
    y='Product',
    orientation='h',
    title='<b>Sales by region</b>'
)

# Customizing the chart to match the image's appearance
fig.update_layout(
    xaxis_tickformat='.0%',
    yaxis_title='',
    xaxis_title='',
    showlegend=False
)

fig.update_traces(marker_color='#6200EE')
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#e0e0e0')

# Streamlit command to render the plot
st.plotly_chart(fig)
