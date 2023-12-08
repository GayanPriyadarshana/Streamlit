import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

# Generate a sample dataset
dates = [datetime(2023, 3, 1) + timedelta(days=i) for i in range(31)]
data = {
    'Date': dates + dates + dates + dates,
    'Value': [i * 10 + 500 for i in range(31)] + [i * 5 + 200 for i in range(31)] +
             [i * 8 + 400 for i in range(31)] + [i * 3 + 150 for i in range(31)],
    'Type': ['Impressions'] * 31 + ['Clicks'] * 31 + ['Impressions'] * 31 + ['Clicks'] * 31,
    'Month': ['This Month'] * 62 + ['Last Month'] * 62
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create the line chart using Plotly Express
fig = px.line(df, x='Date', y='Value', color='Type', line_dash='Month',
              color_discrete_map={'Impressions': 'blue', 'Clicks': 'purple'})

# Update layout for dual y-axes
fig.update_layout(
    title='All Campaigns',
    xaxis_title='',
    yaxis=dict(
        title='',
        
        side='right',
        showgrid=True,
    ),
    yaxis2=dict(
        title='Clicks',
        overlaying='y',
        side='left',
        showgrid=False,
    ),
    xaxis=dict(
        ticks= 'outside',
        ticklen=6,
        tickwidth=2,
        showline=True,
        linecolor="lightgray"
    ),
    legend_title_text='',
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=-.3,
        xanchor='right',
        x=1
    )
)

# Streamlit command to display the plot
st.plotly_chart(fig)
