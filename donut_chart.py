import streamlit as st
import plotly.graph_objects as go

# Sample data for the donut chart
categories = ['Photos & Videos', 'Music & Audio', 'Games', 'Movies & TV', 'Other apps', 'Free Space']
values = [40, 15, 10, 10, 19, 16]  # Adding 'Not Used' category

# Create the donut chart
fig = go.Figure(data=[go.Pie(labels=categories, values=values, hole=.7, sort=False, textinfo='none')])

# Update the layout of the chart
fig.update_layout(
    title_text='Phone storage',
    # Add annotations in the center of the donut pies
    #annotations=[dict(text='84%<br>used', x=0.5, y=0.5, font_size=20, showarrow=False)],

    annotations=[
        dict(text='used', x=0.5, y=0.45, font_size=15, showarrow=False, font_color='grey'),
        dict(text='<b>84%</b>', x=0.5, y=0.55, font_size=20, showarrow=False, font_color='black')
    ],
    legend_title_text='',
    showlegend=True
)

# Customize the legend position
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-0.15,
    xanchor="center",
    x=0.5
))

# Customize the pie chart colors, setting 'Not Used' to a light grey to distinguish it
fig.update_traces(marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#D3D3D3'], 
                              line=dict(color='#FFFFFF', width=2)))

# Streamlit command to display the plot
st.plotly_chart(fig)
