import streamlit as st
import plotly.express as px
import pandas as pd

# Sample dataset to create a graph similar to the one in the image
data = {
    'Product': ['Alpha', 'Beta', 'Gamma', 'Delta'],
    'This Quarter': [400, 300, 200, 100],
    'Last Quarter': [350, 280, 150, 90]
}

# Transform the dataset into a format suitable for Plotly Express
df = pd.DataFrame(data)
df = pd.melt(df, id_vars=['Product'], value_vars=['This Quarter', 'Last Quarter'],
             var_name='Quarter', value_name='Sales')



# Create the bar chart using Plotly Express
fig = px.bar(df, y="Product", x="Sales", color='Quarter',
             barmode='group', orientation='h',
             height=400,
             category_orders={"Product": ["Delta", "Gamma", "Beta", "Alpha"]})  # Order the products as in the image

# Customizing the chart to match the image's appearance
fig.update_layout(
    title_text='<b>Sales by product</b>',  # Bold title text
    legend_title_text='',  # Empty legend title
    xaxis=dict(
        title='',  # No x-axis title
        tickmode='array',
        tickvals=[0, 100, 200, 300, 400],  # Custom tick values
        ticktext=['0', '100', '200', '300', '400'],  # Custom tick texts
        tickangle=0,  # Horizontal tick text
        showgrid=False,  # Show grid lines
        gridwidth=1,
        gridcolor='LightBlue'  # Light blue grid lines
    ),
    yaxis=dict(
        title='',  # No y-axis title
        showgrid=False  # No horizontal grid lines
    ),
    plot_bgcolor='white',  # White background color
    legend=dict(
        orientation="h",  # Horizontal legend
        yanchor="top",
        y=-0.2,  
        xanchor="right",
        x=0.3
    )
)

# Show labels on the bars
#fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

# Streamlit command to render the plot
st.plotly_chart(fig)
