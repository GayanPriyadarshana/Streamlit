import streamlit as st
import plotly.express as px
import pandas as pd

# Sample data for monthly average, high, and low temperatures
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] * 3,
    'Temperature': [50, 55, 65, 70, 80, 90, 95, 90, 85, 75, 60, 50] +
                   [40, 45, 55, 60, 70, 80, 85, 80, 75, 65, 50, 40] +
                   [30, 35, 45, 50, 60, 70, 75, 70, 65, 55, 40, 30],
    'Type': ['High'] * 12 + ['Average'] * 12 + ['Low'] * 12
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Create the line chart using Plotly Express
fig = px.line(df, x="Month", y="Temperature", color='Type', 
              title='Average temperature in Fahrenheit',
              labels={'Temperature': 'Temperature (°F)'})

# Update layout for the figure
fig.update_layout(
    xaxis_title='',
    yaxis_title='',
    legend_title='',
    hovermode="x",
    yaxis=dict(
        title='Temperature (°F)',
        side='right',  # Position the y-axis tick labels to the right
        ticksuffix='°'
    ),
    xaxis=dict(
        ticks= 'outside',
        ticklen=6,
        tickwidth=2,
        showline=True,
        linecolor="lightgray"
    ),
     legend=dict(
        orientation="h",  # Set the legend to horizontal
        yanchor="bottom",
        y=-0.3,  # Position the legend at the bottom
        xanchor="left",
        x=-0.01   # Center the legend
    )
)

# Streamlit command to display the plot
st.plotly_chart(fig)
