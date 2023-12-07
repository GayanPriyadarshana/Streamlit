import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Sample data to represent stock price behavior over a week
data = {
    'Date': ['2022-08-22', '2022-08-23', '2022-08-24', '2022-08-25', '2022-08-26'],
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Open': [10, 15, 20, 35, 50],
    'High': [15, 20, 30, 40, 60],
    'Low': [5, 10, 15, 30, 40],
    'Close': [15, 18, 25, 30, 45],
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=df['Day'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    increasing_line_color='green',
    decreasing_line_color='red'
)])

# Update the layout to match the image
fig.update_layout(
    title='Stock behavior<br>August 22 - 26',
    xaxis_title='',
    yaxis_title='',
    xaxis=dict(
        rangeslider=dict(
            visible=False  # Disable the range slider
        ),
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204,204,204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
    ),
    autosize=False,
    showlegend=False
)

# Streamlit command to display the plot
st.plotly_chart(fig)
