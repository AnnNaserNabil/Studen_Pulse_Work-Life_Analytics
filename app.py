import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎓 Student Pulse: Work-Life Analytics")

@st.cache_data
def load_data():
    return pd.read_csv("your_dataset.csv")

data = load_data()
st.write("✅ Data Loaded")

st.dataframe(data.head())

selected_job = st.sidebar.selectbox("Filter by Job Type", ["All"] + list(data['Job_Type'].unique()))

if selected_job != "All":
    filtered = data[data['Job_Type'] == selected_job]
else:
    filtered = data

st.write(f"Data shape: {filtered.shape}")

# Plot
if not filtered.empty:
    fig = px.scatter(filtered, x='Study_Hours', y='Academic_Performance', color='Stress_Level')
    st.plotly_chart(fig)
else:
    st.warning("No data available for this job type.")
