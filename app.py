import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Header
st.header('Car Sales Dashboard')

# Histogram for the 'price' column
fig_histogram = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_histogram)

fig_odometer = px.histogram(df, x='odometer', nbins=50, title='Odometer Reading Distribution')
fig_odometer.show()

# Scatter plot of 'price' vs 'odometer'
fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
show_scatter = st.checkbox('Show Scatter Plot')

fig_year_price = px.scatter(df, x='model_year', y='price', color='model', title='Year vs Price by Make')
fig_year_price.show()

if show_scatter:
    st.plotly_chart(fig_scatter)