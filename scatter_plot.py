import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Generate a sample dataset
np.random.seed(42)  # For reproducible random results
num_points = 50
data = {
    'Revenue': np.random.uniform(0, 1000, num_points),  # Revenue between $0 and $1000
    'Users': np.random.randint(0, 15, num_points)  # User count between 0 and 15k
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Create the scatter plot
fig = px.scatter(
    df,
    x='Revenue',
    y='Users',
    labels={
        'Revenue': 'Revenue ($)',
        'Users': 'Users (k)'
    },
    title='Revenue analysis'
)

# Customize the scatter plot
fig.update_layout(
    xaxis=dict(
        tickvals=[0, 250, 500, 750, 1000],  # Custom x-axis tick values
        title='Revenue',
        tickprefix="$",
        showgrid=True
        
    ),
    yaxis=dict(
        title='Users'
    ),
    showlegend=False
)

# Streamlit command to display the plot
st.plotly_chart(fig)
