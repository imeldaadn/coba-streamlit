import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Konfigurasi halaman
st.set_page_config(
    page_title="Data Visualization Dashboard",
    page_icon="🎢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Memuat konfigurasi database dari secrets.toml
db_config = st.secrets["database"]

# Membuat string koneksi
db_connection_str = f'mysql+mysqlconnector://{db_config["username"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["name"]}'
db_connection = create_engine(db_connection_str)

# Query untuk mengambil data
def load_data():
    query = """
    SELECT p.name AS product_name, SUM(s.LineTotal) AS total_sales 
    FROM sales_fact s 
    JOIN product p ON s.product_key = p.id
    GROUP BY p.name 
    ORDER BY total_sales DESC;
    """
    return pd.read_sql(query, db_connection.connect())

# Fungsi utama untuk menampilkan aplikasi
def main():
    st.sidebar.title('🏂 Data Visualization Dashboard')
    option = st.sidebar.selectbox("Select Page", ("Data Warehouse Adventureworks", "Web Scraping"))
    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.sidebar.selectbox('Select a color theme', color_theme_list)

    # Data AW
    ## Dashboard
    st.header('Hi, Welcome to the :rainbow[***Data Visualization Dashboard!***]')
    st.markdown('We are here to showcase your data :orange[in] a cool :orange[and] engaging way :sunglasses:')
    st.subheader("Data Warehouse Adventureworks")

    ## Grafik
    data = load_data()
    st.write(data)

    # Membuat chart bar dengan Plotly
    fig = px.bar(
        data, 
        x='product_name', 
        y='total_sales', 
        title='Total Sales by Product',
        labels={'product_name': 'Product', 'total_sales': 'Total Sales'},
        color='total_sales',
        color_continuous_scale=selected_color_theme
    )

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
