import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Generate a sample dataset
dates = [datetime(2023, 3, 1) + timedelta(days=i) for i in range(31)]
impressions_this_month = [i * 10 + 500 for i in range(31)]
clicks_this_month = [i * 5 + 200 for i in range(31)]
impressions_last_month = [i * 8 + 400 for i in range(31)]
clicks_last_month = [i * 3 + 150 for i in range(31)]

# Create traces for the figure
fig = go.Figure()
fig.add_trace(go.Scatter(x=dates, y=impressions_this_month, mode='lines', name='Impressions', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=dates, y=clicks_this_month, mode='lines', name='Clicks', line=dict(color='purple')))
fig.add_trace(go.Scatter(x=dates, y=impressions_last_month, mode='lines', name='This month', line=dict(dash='dot', color='blue')))
fig.add_trace(go.Scatter(x=dates, y=clicks_last_month, mode='lines', name='Last month', line=dict(dash='dot', color='purple')))

# Create a dual-axis layout
fig.update_layout(
    title='All Campaigns',
    xaxis_title='Date',
    yaxis=dict(
        title='Impressions',
        side='left',
        color='blue',
    ),
    yaxis2=dict(
        title='Clicks',
        side='right',
        overlaying='y',
        color='purple',
    ),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
    )
)

# Format x-axis tick marks to show Mar 1, Mar 15, Mar 31
fig.update_xaxes(
    tickvals=[dates[0], dates[14], dates[-1]],
    tickformat='%b %d'
)

# Streamlit command to display the plot
st.plotly_chart(fig)
