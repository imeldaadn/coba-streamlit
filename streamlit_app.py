#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

#######################
# Page configuration
st.set_page_config(
    page_title="Data Visualization Dashboard",
    page_icon="🎢",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")


#######################
# Load data



#######################
# Sidebar
with st.sidebar:
    st.title('🏂 Data Visualization Dashboard')
    

    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)


#######################
# Data AW
## Dashboard
st.header('Hi, Welcome to the :red[***Data Visualization Dashboard!***]', divider='rainbow')
st.subheader('We are here to showcase your data :yellow[in] a cool and engaging way :sunglasses:')
