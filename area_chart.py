import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Sample data for the area chart
data = {
    'Year': [2013, 2014, 2015, 2016],
    'Sales': [1000, 1170, 660, 1030],
    'Expenses': [400, 460, 1120, 540],
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create traces for the area chart
sales_trace = go.Scatter(
    x=df['Year'], 
    y=df['Sales'], 
    fill='tozeroy', 
    mode='lines+markers',
    name='Sales',
    line=dict(color='royalblue'), 
    marker=dict(color='royalblue'),
    fillcolor='rgba(65, 105, 225, 0.2)' 
)

expenses_trace = go.Scatter(
    x=df['Year'], 
    y=df['Expenses'], 
    fill='tozeroy', 
    mode='lines+markers',
    name='Expenses',
    line=dict(color='crimson'), 
    marker=dict(color='crimson'),
    fillcolor='rgba(220, 20, 60, 0.2)'
)

# Combine traces
fig = go.Figure(data=[sales_trace, expenses_trace])

# Update the layout to match the image
fig.update_layout(
    title='Company performance',
    xaxis=dict(title='Year', tickvals=df['Year']),
    yaxis=dict(title=''),
    showlegend=True,
    plot_bgcolor='white',
    legend=dict(
        orientation="h",
        yanchor="top",
        y=-0.15,
        xanchor="left",
        x=0.01
    )
)

# Streamlit command to display the plot
st.plotly_chart(fig)
