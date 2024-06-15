import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Header
st.header('Car Sales Dashboard')

# Histogram for the 'price' column
st.subheader('Price Distribution')
fig_histogram_price = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_histogram_price)

# Histogram for the 'odometer' column
st.subheader('Odometer Distribution')
fig_histogram_odometer = px.histogram(df, x='odometer', title='Odometer Distribution')
st.plotly_chart(fig_histogram_odometer)

# Histogram for the 'model_year' column
st.subheader('Model Year Distribution')
fig_histogram_model_year = px.histogram(df, x='model_year', title='Model Year Distribution')
st.plotly_chart(fig_histogram_model_year)

# Scatter plot of 'price' vs 'odometer'
st.subheader('Price vs Odometer')
fig_scatter_price_odometer = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
show_scatter_price_odometer = st.checkbox('Show Scatter Plot: Price vs Odometer')

if show_scatter_price_odometer:
    st.plotly_chart(fig_scatter_price_odometer)

# Scatter plot of 'price' vs 'model_year'
st.subheader('Price vs Model Year')
fig_scatter_price_model_year = px.scatter(df, x='model_year', y='price', title='Price vs Model Year')
show_scatter_price_model_year = st.checkbox('Show Scatter Plot: Price vs Model Year')

if show_scatter_price_model_year:
    st.plotly_chart(fig_scatter_price_model_year)

# Scatter plot of 'odometer' vs 'model_year'
st.subheader('Odometer vs Model Year')
fig_scatter_odometer_model_year = px.scatter(df, x='model_year', y='odometer', title='Odometer vs Model Year')
show_scatter_odometer_model_year = st.checkbox('Show Scatter Plot: Odometer vs Model Year')

if show_scatter_odometer_model_year:
    st.plotly_chart(fig_scatter_odometer_model_year)
