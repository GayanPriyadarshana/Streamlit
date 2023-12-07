import streamlit as st
import plotly.express as px
import pandas as pd

# Sample dataset based on the provided image
data = pd.DataFrame({
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Positive Comments": [0.20, 0.30, 0.35, 0.40]
      # Values as proportions
})

# Creating the bar chart using Plotly
fig = px.bar(data, x='Quarter', 
             y='Positive Comments', 
              title='<b><br><span style="font-size: 22px;">Customer Feedback</b><br><span style="font-size: 12px;">Positive Comments</span>',
              text='Positive Comments'
             )

# Updating the layout to show the y-axis tick labels as percentages
fig.update_layout(yaxis_tickformat='.0%',
                  yaxis={'side': 'right'},
                  yaxis_title='')

# Convert the 'Positive Comments' column to percentage format for the bar text
fig.update_traces(texttemplate='%{text:.0%}', textposition='inside')

# Streamlit command to render the plot
st.plotly_chart(fig)
