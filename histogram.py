import streamlit as st
import plotly.express as px
import pandas as pd

# Sample dataset representing popularity at different times on Tuesdays
data = {
    'Time': ['9a', '10a', '11a', '12p', '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p'],
    'Popularity': [20, 25, 30, 50, 40, 45, 60, 55, 50, 40, 35, 30, 25]
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Create a bar chart
fig = px.bar(
    df,
    x='Time',
    y='Popularity',
    title='Popular times on Tuesdays',
    labels={'Popularity': 'peak'},
    #text='Popularity'
)

# Customize the bar chart
#fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.update_layout(
    xaxis=dict(title='Time', tickmode='array', tickvals=df['Time']),
    yaxis=dict(title=''),
    showlegend=False
)

# Streamlit command to display the plot
st.plotly_chart(fig)
