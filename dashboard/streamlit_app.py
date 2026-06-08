import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

from database.db import engine


# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Weather Monitoring Dashboard",
    page_icon="🌦",
    layout="wide"
)

# ==================================
# AUTO REFRESH
# ==================================

st_autorefresh(
    interval=10000,
    key="weather_refresh"
)

# ==================================
# TITLE
# ==================================

st.title("🌦 Real-Time Weather Monitoring Dashboard")

st.markdown(
    """
    Multi-City Weather Monitoring System using
    PostgreSQL + SQLAlchemy + Alembic + APScheduler + Streamlit
    """
)

# ==================================
# LOAD DATA
# ==================================

query = """
SELECT *
FROM weather_data
ORDER BY fetched_at DESC
"""

df = pd.read_sql(query, engine)

if df.empty:
    st.warning("No weather data found.")
    st.stop()

# ==================================
# SIDEBAR
# ==================================

st.sidebar.header("Dashboard Filters")

cities = sorted(df["city"].unique())

selected_city = st.sidebar.selectbox(
    "Select City",
    cities
)

records_to_show = st.sidebar.slider(
    "Records To Display",
    min_value=5,
    max_value=100,
    value=20
)

# ==================================
# FILTER DATA
# ==================================

filtered_df = df[
    df["city"] == selected_city
]

latest = filtered_df.iloc[0]

# ==================================
# LAST UPDATED
# ==================================

st.caption(
    f"Last Updated : {latest['fetched_at']}"
)

# ==================================
# METRICS
# ==================================

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "🏙 City",
        latest["city"]
    )

with col2:
    st.metric(
        "🌡 Temperature",
        f"{latest['temperature']} °C"
    )

with col3:
    st.metric(
        "💧 Humidity",
        f"{latest['humidity']} %"
    )

with col4:
    st.metric(
        "☁ Weather",
        latest["weather"]
    )

with col5:
    st.metric(
        "📊 Records",
        len(filtered_df)
    )

st.divider()

# ==================================
# LATEST RECORDS
# ==================================

st.subheader("📋 Latest Weather Records")

st.dataframe(
    filtered_df.head(records_to_show),
    use_container_width=True
)

st.divider()

# ==================================
# CHART DATA
# ==================================

chart_df = filtered_df.sort_values(
    by="fetched_at"
)

# ==================================
# TEMPERATURE TREND
# ==================================

st.subheader(
    f"🌡 Temperature Trend - {selected_city}"
)

st.line_chart(
    chart_df.set_index("fetched_at")["temperature"]
)

# ==================================
# HUMIDITY TREND
# ==================================

st.subheader(
    f"💧 Humidity Trend - {selected_city}"
)

st.line_chart(
    chart_df.set_index("fetched_at")["humidity"]
)

st.divider()

# ==================================
# CITY COMPARISON
# ==================================

st.subheader(
    "🏆 Average Temperature Comparison"
)

avg_temp = (
    df.groupby("city")["temperature"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(avg_temp)

st.divider()

# ==================================
# CITY STATS
# ==================================

st.subheader("📈 City Statistics")

stats_df = (
    df.groupby("city")
    .agg(
        Avg_Temperature=("temperature", "mean"),
        Avg_Humidity=("humidity", "mean"),
        Records=("id", "count")
    )
    .round(2)
)

st.dataframe(
    stats_df,
    use_container_width=True
)

st.divider()

# ==================================
# FULL DATASET
# ==================================

with st.expander("View Full Dataset"):

    st.dataframe(
        df,
        use_container_width=True
    )