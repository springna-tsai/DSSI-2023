# dashboard.py
import streamlit as st
import pandas as pd
import numpy as np

google_drive_link = "https://docs.google.com/spreadsheets/d/1HUngiEwcxpOi6xQ4b_Zqotv3kubdhvUE/edit?usp=share_link&ouid=106151830704109772809&rtpof=true&sd=true"

df = pd.read_csv(google_drive_link)
df['Time'] = pd.to_datetime(df['Time'])
df = df[df['Time'].dt.year >= 2018]
df.dropna(inplace=True)
df['Press'] = df['Press'].replace('Newslens', 'NewsLens')

st.sidebar.title("Dashboard Options")
chart_type = st.sidebar.radio("Select Chart Type", ["Press Clickbait Ratio", "Category Clickbait Ratio"])

st.title("Clickbait Analysis Dashboard")

if chart_type == "Press Clickbait Ratio":
    # Bar chart for press clickbait ratio
    press_ratios = df.groupby('Press')['IsClickbait'].mean()
    st.bar_chart(press_ratios)
    st.pyplot(plt)
    st.title('Clickbait Ratio for Each Press')

elif chart_type == "Category Clickbait Ratio":
    # Bar chart for category clickbait ratio
    category_ratios = df.groupby('Category')['IsClickbait'].mean()
    st.bar_chart(category_ratios)
    st.pyplot(plt)
    st.title('Clickbait Ratio for Each News Category')
