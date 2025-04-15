import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("/data/female-labor-force-by-age.csv")  # Change to your file path

data = load_data()

st.title("📊 Student Work-Life Balance Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
selected_job = st.sidebar.selectbox(
    "Filter by Job Type",
    options=["All"] + list(data['Job_Type'].unique())
)

if selected_job != "All":
    filtered = data[data['Job_Type'] == selected_job]
else:
    filtered = data

st.markdown(f"### Showing data for: **{selected_job}**")
st.dataframe(filtered.head(10))

# Plot 1: Study Hours vs Academic Performance
st.subheader("🧠 Study Hours vs Academic Performance")
fig1 = px.scatter(filtered, x="Study_Hours", y="Academic_Performance",
                  color="Stress_Level", hover_data=['Work_Hours', 'Sleep_Hours'])
st.plotly_chart(fig1, use_container_width=True)

# Plot 2: Work Hours vs Stress Level
st.subheader("💼 Work Hours vs Stress Level")
fig2 = px.scatter(filtered, x="Work_Hours", y="Stress_Level",
                  color="Job_Type", hover_data=['Academic_Performance'])
st.plotly_chart(fig2, use_container_width=True)

# Plot 3: Academic Performance by Job Type
st.subheader("📚 Academic Performance by Job Type")
fig3 = px.box(data if selected_job == "All" else filtered,
              x="Job_Type", y="Academic_Performance", color="Job_Type")
st.plotly_chart(fig3, use_container_width=True)

# Plot 4: Correlation Heatmap
st.subheader("📈 Correlation Heatmap")
numeric_cols = ['Work_Hours', 'Sleep_Hours', 'Study_Hours',
                'Work_Life_Balance', 'Stress_Level', 'Academic_Performance',
                'Social_Activity', 'Job_Satisfaction']
corr = filtered[numeric_cols].corr()

fig4, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig4)

# Optional: Summary stats
st.subheader("🧾 Summary Statistics")
st.write(filtered[numeric_cols].describe())
