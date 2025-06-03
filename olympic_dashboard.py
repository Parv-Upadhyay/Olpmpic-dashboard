import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("🏅 Olympic Games Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("athlete_events.csv")

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filters")
years = sorted(df['Year'].dropna().unique())
countries = sorted(df['Team'].dropna().unique())  # 'Team' is the correct column name

year = st.sidebar.selectbox("Select Year", years)
country = st.sidebar.selectbox("Select Country", countries)

# Filter data
filtered = df[(df['Year'] == year) & (df['Team'] == country)]

# Medal Count
st.subheader(f"🎖️ Medal Count for {country} in {year}")
medal_counts = filtered.dropna(subset=['Medal']).groupby('Medal').size().reset_index(name='Count')

if not medal_counts.empty:
    fig = px.bar(medal_counts, x='Medal', y='Count', color='Medal', title="Medals by Type")
    st.plotly_chart(fig)
else:
    st.warning("No medal data available for the selected filters.")

# Show Table
st.subheader("📊 Athlete Event Data")
st.dataframe(filtered)
