import streamlit as st
import plotly.express as px
import pandas as pd

# Sample dataset
data = {
    'Country': ['IRQ', 'EGY', 'ISR', 'RUS', 'IRN', 'USA', 'GBR', 'DEU', 'CAN'],
    'Region': ['Middle East', 'Middle East', 'Middle East', 'Europe', 
               'Middle East', 'North America', 'Europe', 'Europe', 'North America'],
    'Life Expectancy': [68, 70, 82, 72, 75, 79, 81, 80, 84],
    'Fertility Rate': [6, 3, 2, 2, 2, 1, 1, 1, 1],
    'Live Births per 1000 Females': [60, 50, 20, 40, 30, 10, 10, 10, 10]
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Create the scatter plot
fig = px.scatter(
    df,
    x='Life Expectancy',
    y='Live Births per 1000 Females',
    size='Fertility Rate',
    color='Region',
    hover_name='Country',
    title='Fertility rates and life expectancies',
    labels={'Live Births per 1000 Females': 'live births per 1000 females'},
    size_max=60,
    height=400
)

# Customizing the chart to match the image's appearance
fig.update_traces(marker=dict(line=dict(width=2, color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

# Customize the legend
fig.update_layout(
    legend_title_text='',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.6,
        xanchor="right",
        x=1,
        
    ),
    yaxis=dict( title=''),
    xaxis=dict( showgrid=True )
)


# Streamlit command to display the plot
st.plotly_chart(fig)
