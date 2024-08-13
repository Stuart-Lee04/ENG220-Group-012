import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="NM WAQHE Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to load data, using the new caching mechanism
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
    st.title('NM WAQHE Dashboard')

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

# Data filtering based on the sidebar's inputs
filtered_data = df[
    (df['Well Name'] == selected_well) &
    (df['Measurement Date'].dt.date >= start_date) &
    (df['Measurement Date'].dt.date <= end_date)
]

# Layout for chart and map with padding
col1, col2 = st.columns([6, 5])  # Adjust the column width ratio if necessary
with col1:
    if not filtered_data.empty:
        # Plotting
        fig = px.line(filtered_data, x='Measurement Date', y='Depth to Water', title=f'Depth to Water for {selected_well} Over Time')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No data available for the selected criteria.")

with col2:
    # Create a new DataFrame for the well location to display on the map
    if not well_data.empty:
        well_location_df = pd.DataFrame({
            'latitude': [well_data.iloc[0]['Lat_DD']],
            'longitude': [well_data.iloc[0]['Long_DD']]
        })
        st.map(well_location_df)

# Displaying the data table at the bottom
if not filtered_data.empty:
    st.write("Depth to Water Data Table")
    st.dataframe(filtered_data[['Well Name', 'Measurement Date', 'Depth to Water']], height=300)

# Adding a placeholder for spacing
st.markdown("""---""")  # This creates a horizontal line for visual separation
