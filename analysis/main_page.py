# write a streamlit app for the main page
import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="NM WAQHE Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

pg = st.sidebar.selectbox('Select a page', ['Main', 'Water', 'Air'])

def main_page():
    st.title("Main Page")
    st.write("Welcome to the NM WAQHE Dashboard Main Page")

def water_page():
    st.title("Water Page")
    st.write("Welcome to the NM WAQHE Dashboard Water Page")

def air_page():
    st.title("Air Page")
    st.write("Welcome to the NM WAQHE Dashboard Air Page")

if pg == 'Main':
    main_page()
elif pg == 'Water':
    water_page()
elif pg == 'Air':
    air_page()