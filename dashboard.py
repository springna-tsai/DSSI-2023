# dashboard.py
import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("My Streamlit Dashboard")
    st.write("Welcome to my dashboard!")

    # Create sample data for the bar chart
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [4, 7, 1, 9]
    })

    # Display the bar chart
    st.bar_chart(data.set_index('Category')['Values'])

if __name__ == "__main__":
    main()
