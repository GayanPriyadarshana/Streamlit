import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# Generate a date range for the last 30 days
dates = [datetime.today() - timedelta(days=i) for i in range(30)]
dates.sort()

# Create a sample dataset
data = {
    'Date': dates,
    'Category A': [i + 200 for i in range(30)],
    'Category B': [i + 100 for i in range(30)],
    'Category C': [i for i in range(30)],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create traces for each category
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df['Date'], y=df['Category A'],
    hoverinfo='x+y',
    mode='lines',
    stackgroup='one',
    name='Category A',
    line=dict(width=0.5, color='rgb(131, 90, 241)'),
    fillcolor='rgba(131, 90, 241, 0.6)'
))
fig.add_trace(go.Scatter(
    x=df['Date'], y=df['Category B'],
    hoverinfo='x+y',
    mode='lines',
    stackgroup='one',
    name='Category B',
    line=dict(width=0.5, color='rgb(111, 240, 219)'),
    fillcolor='rgba(111, 231, 219, 0.6)'
))
fig.add_trace(go.Scatter(
    x=df['Date'], y=df['Category C'],
    hoverinfo='x+y',
    mode='lines',
    stackgroup='one',
    name='Category C',
    line=dict(width=0.5, color='rgb(184, 247, 212)'),
    fillcolor='rgba(184, 247, 212, 0.6)'
))

# Customize the layout
fig.update_layout(
    title='Users in the last 30 days',
    showlegend=True,
    xaxis=dict(
        type='date',
        title=''
    ),
    yaxis=dict(
        title='Number of Users'
    ),
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
