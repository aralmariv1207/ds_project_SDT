import pandas as pd
import streamlit as st
import plotly.express as px

st.title("My Streamlit App")
st.write("Here's my first ever app in Streamlit!")

df = pd.read_csv("vehicles_us.csv")

# Add a Header
st.header("Car Sales Analysis")

# Plotly Express Histogram
fig_hist = px.histogram(df, x='price')
st.plotly_chart(fig_hist, key="hist")

# Plotly Express Scatter Plot
fig_scatter = px.scatter(df, x='price', y='model_year')
st.plotly_chart(fig_scatter, key="scatter")

# Checkbox to Control Plot
if st.checkbox("Show Histogram"):
    st.plotly_chart(fig_hist, key="checkbox_hist")
