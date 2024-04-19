import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load data
@st.cache_data
def load_data(filepath):
    df = pd.read_csv(filepath, parse_dates=['MSRMNT_Dat'])
    df.rename(columns={'MSRMNT_Dat': 'Measurement Date', 'Depth_To_W': 'Depth to Water', 'Well_Name': 'Well Name'}, inplace=True)
    df.sort_values('Measurement Date', inplace=True)
    return df

# Assuming your dataset file path
data_path = 'ce1d0932-1914-4de2-97b7-a13e034c6a4a.csv'  # Replace with your actual data file path
df = load_data(data_path)

st.title('Well Water Depth Visualization')

# Sidebar for inputs
with st.sidebar:
    # Well selection
    well_list = df['Well Name'].unique()
    selected_well = st.selectbox('Select a Well', well_list)

    # Date range selection
    well_data = df[df['Well Name'] == selected_well]
    min_date, max_date = well_data['Measurement Date'].min(), well_data['Measurement Date'].max()
    start_date, end_date = st.select_slider(
        'Select a date range',
        options=pd.to_datetime(well_data['Measurement Date']).dt.date.unique(),
        value=(min_date.date(), max_date.date())
    )

    # Based on the selected well, show the location of the well on a map
    well_location = well_data.iloc[0]
    st.write(f"Well Location: Latitude - {well_location['Lat_DD']} and Longitude - {well_location['Long_DD']}")

    # Displaying the selected well's date range and location outside the sidebar
    st.write(f"Data available from {min_date.date()} to {max_date.date()} for {selected_well}")

# Data filtering based on the sidebar's inputs
filtered_data = df[
    (df['Well Name'] == selected_well) &
    (df['Measurement Date'].dt.date >= start_date) &
    (df['Measurement Date'].dt.date <= end_date)
]

# Displaying filtered data and plotting
if not filtered_data.empty:
    st.write(filtered_data[['Well Name', 'Measurement Date', 'Depth to Water']])
    
    # Plotting
    fig = px.line(filtered_data, x='Measurement Date', y='Depth to Water', title=f'Depth to Water for {selected_well} Over Time')
    st.plotly_chart(fig)
else:
    st.write("No data available for the selected criteria.")

# Create a new DataFrame for the well location to display on the map
well_location_df = pd.DataFrame({
    'latitude': [well_location['Lat_DD']],
    'longitude': [well_location['Long_DD']]
})

st.map(well_location_df)