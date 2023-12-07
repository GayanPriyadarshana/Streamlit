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

average_popularity = df['Popularity'].mean()

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


# Add a shape for the average line to appear behind the bars
fig.add_shape(
    type="line",
    x0=-0.5,  # x0 is set to -0.5 to start the line a bit before the first bar
    y0=average_popularity,
    x1=len(df['Time']) - 0.5,  # x1 is set to the length of Time data minus 0.5 to end the line a bit after the last bar
    y1=average_popularity,
    line=dict(
        color="gray",
        width=2,
        dash="dash",
    ),
    layer="below",  # Places the line below the bars
)

#fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.update_layout(
    xaxis=dict(title='Time', tickmode='array', tickvals=df['Time']),
    yaxis=dict(title=''),
    showlegend=False
)

# Add a horizontal line for the average popularity
#fig.add_hline(y=average_popularity, line_dash="dash", line_color="gray", )
# Streamlit command to display the plot
st.plotly_chart(fig)
