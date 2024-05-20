import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Data Visualization Dashboard",
    page_icon="🎢",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

# Initialize connection.
conn = st.connection('mysql', type='sql')


# Sidebar
def main():
    st.sidebar.title('🏂 Data Visualization Dashboard')
    option = st.sidebar.selectbox("Select Page", ("Data Warehouse Adventureworks", "Web Scrapping"))
    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

# Data AW
## Dashboard
st.header('Hi, Welcome to the :rainbow[***Data Visualization Dashboard!***]', divider='rainbow')
st.markdown('We are here to showcase your data :orange[in] a cool :orange[and] engaging way :sunglasses:')
st.subheader("Data Warehouse Adventureworks")

## Grafik

if __name__ == "__main__":
    main()
