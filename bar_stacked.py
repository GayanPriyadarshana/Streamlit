import streamlit as st
import plotly.express as px
import pandas as pd

# Create a sample dataset that represents the graph in the image
data = {
    'Decade': ['1990', '2000', '2010', '2020', '1990', '2000', '2010', '2020', '1990', '2000', '2010', '2020'],
    'Category': ['Fiction', 'Fiction', 'Fiction', 'Fiction',
                 'Non-fiction', 'Non-fiction', 'Non-fiction', 'Non-fiction',
                 'Literature', 'Literature', 'Literature', 'Literature'],
    'Sales': [50, 80, 90, 120, 70, 90, 110, 130, 20, 30, 40, 50]  # Sample sales data
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Convert 'Decade' to string to make sure Plotly treats it as categorical
df['Decade'] = df['Decade'].astype(str)

# Create the stacked bar chart using Plotly Express
fig = px.bar(
    df,
    x='Decade',
    y='Sales',
    color='Category',
    title='Book sales by decade'
)

# Customize the legend to be horizontal and adjust the layout
fig.update_layout(
    legend_title_text='',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.23,
        xanchor="center",
        x=0.5
    ),
    xaxis=dict(title='',
               type='category'),

    yaxis=dict(title='')
)



# Streamlit command to display the plot
st.plotly_chart(fig)
