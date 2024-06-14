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

# Scatter plot of 'price' vs 'odometer'
fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
show_scatter = st.checkbox('Show Scatter Plot')

if show_scatter:
    st.plotly_chart(fig_scatter)