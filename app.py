import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Header
st.header('GSK Garage')

# Add a section for filtering and displaying data
st.subheader('Filter Cars by Year, Fuel Type, and Price')

# Year selection with an 'All' option
year_options = df['model_year'].dropna().unique()
year_options_sorted = sorted(year_options)
year_options_sorted.insert(0, 'All')
selected_years = st.multiselect('Select Year(s)', year_options_sorted)

# Fuel type selection with an 'All' option
fuel_options = df['fuel'].dropna().unique()
fuel_options_sorted = sorted(fuel_options)
fuel_options_sorted.insert(0, 'All')
selected_fuels = st.multiselect('Select Fuel Type(s)', fuel_options_sorted)

# Update selection logic to handle 'All' option
selected_years = [year for year in year_options_sorted if year != 'All'] if 'All' in selected_years else selected_years
selected_fuels = [fuel for fuel in fuel_options_sorted if fuel != 'All'] if 'All' in selected_fuels else selected_fuels

# Price range selection
min_price = 0
max_price = int(df['price'].max())
selected_price_range = st.slider('Select Price Range', min_price, max_price, (min_price, max_price))

# Filter the dataframe based on selections
filtered_df = df[(df['model_year'].isin(selected_years)) &
                 (df['fuel'].isin(selected_fuels)) &
                 (df['price'] >= selected_price_range[0]) &
                 (df['price'] <= selected_price_range[1])]

# Display the filtered dataframe
if not filtered_df.empty:
    st.subheader('Filtered Cars')
    st.write(filtered_df)
else:
    st.write('No cars match the selected criteria.')

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


