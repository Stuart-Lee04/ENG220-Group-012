import streamlit as st
import pandas as pd
import pydeck as pdk

# Load data
site_data = pd.read_csv('./data/AirQualityData/aqs_sites.csv') 

# Streamlit app setup
st.title('Air Quality Visualization App')

# Sidebar for user selections
year = st.sidebar.selectbox('Select Year', range(2010, 2022)) 
state = st.sidebar.selectbox('Select State', site_data['State Name'].unique())
county = st.sidebar.selectbox('Select County', site_data[site_data['State Name'] == state]['County Name'].unique())
monitor_site = st.sidebar.selectbox('Select Monitor Site', site_data['Local Site Name'].unique())

# Load the corresponding year's data
monitor_data_path = f'./data/AirQualityData/annual_conc_by_monitor_{year}.csv'
monitor_data = pd.read_csv(monitor_data_path)

pollutant = st.sidebar.selectbox('Select Pollutant', monitor_data['Parameter Name'].unique())

# Filter data based on selections
filtered_site_data = site_data[(site_data['State Name'] == state) & (site_data['County Name'] == county) & (site_data['Local Site Name'] == monitor_site)]
filtered_monitor_data = monitor_data[(monitor_data['Parameter Name'] == pollutant)]

# Display map
if not filtered_site_data.empty:
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=filtered_site_data['Latitude'].iloc[0],
            longitude=filtered_site_data['Longitude'].iloc[0],
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=filtered_site_data,
                get_position='[Longitude, Latitude]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))

# Display line chart and raw data
if not filtered_monitor_data.empty:
    # Assuming the monitor data contains a time and measurement column, replace these with your actual column names
    st.line_chart(filtered_monitor_data[['time_column', 'measurement_column']])
    st.write(filtered_monitor_data)
else:
    st.write("No data available for the selected criteria.")
