import streamlit as st
import plotly.express as px
import pandas as pd

# Creating a sample dataset that mimics the structure of the graph in the image
data = {
    'Units': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95],
    'Revenue': [1.5, 2, 3, 5, 6, 7, 8, 9, 10, 12, 2, 3, 4, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11, 1, 2.5, 3.5, 4.2, 5.2, 6.1, 7.2, 8.2, 9.1, 10.5],
    'Product': ['Product A'] * 10 + ['Product B'] * 10 + ['Product C'] * 10
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Create the scatter plot using Plotly Express
fig = px.scatter(df, x="Units", y="Revenue", color="Product", symbol="Product")

# Customize the axes and layout to add dollar sign to y-axis ticks
fig.update_layout(
    title='Revenue by product',
    xaxis_title="Units",
    
    yaxis=dict(
        #title='Revenue',
        title='',
        tickprefix="$",  # Add dollar sign prefix to y-axis ticks
        ticksuffix="M  ",  # Assuming the values are in millions
        showline=True,
        zeroline=True,
        linecolor='lightgray'
    ),
    xaxis=dict(
        showgrid=True,   # Show vertical grid lines
        showline=True,
        zeroline=True,
        linecolor='lightgray'
    ),
    legend_title_text='',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.35,
        xanchor="right",
        x=0.7,
        
    ),
    
)
#fig.update_yaxes(ticksuffix = "  ")
# Show the figure in a Streamlit app
st.plotly_chart(fig)
