import streamlit as st
import pandas as pd
import os

# Function to load data for a selected year and pollutant
@st.cache  # Cache the data to avoid reloading on every interaction
def load_data(data_folder, year, pollutant):
    # Construct the file path based on the year and pollutant
    file_name = f"{pollutant}_NM_{year}_AQS_edited.csv"
    file_path = os.path.join(data_folder, year, file_name)
    
    # Read the CSV file and parse the 'Date' column as datetime
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
    
    # Extract the relevant columns assuming 'Concentration' is a column in your CSV
    if 'Concentration' in data.columns:
        data = data[['Date', 'Concentration']]
    else:
        # Fallback if 'Concentration' column is not present, adjust as needed
        # Assuming 'Daily Max 8-hour CO Concentration' is the concentration column
        concentration_col = data.columns[1]
        data = data[['Date', concentration_col]]
        data.rename(columns={concentration_col: 'Concentration'}, inplace=True)
    
    return data

# Function to plot AQI data using Streamlit's line_chart
def plot_aqi_data(data, start_date, end_date):
    # Convert start_date and end_date to pandas.Timestamp to ensure correct comparison
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter data based on the selected date range
    mask = (data['Date'] >= start_date) & (data['Date'] <= end_date)
    filtered_data = data.loc[mask]

    # Aggregate data by day
    daily_data = filtered_data.groupby('Date')['Concentration'].mean().reset_index()

    # Plot using Streamlit's line_chart function
    st.line_chart(daily_data.set_index('Date')['Concentration'])

# Assuming the data folder is structured with subfolders named by year
DATA_FOLDER = './AirQualityDataEdited'

# Streamlit app layout
st.title('Air Quality Data Visualization')

# Get years based on the subfolders in the data directory
years = [folder for folder in os.listdir(DATA_FOLDER) if os.path.isdir(os.path.join(DATA_FOLDER, folder))]
year = st.sidebar.selectbox('Select a year', sorted(years))

# Assuming pollutants are the same for all years
# This should be dynamically loaded if different per year
pollutants = ['CO', 'NO2', 'Ozone', 'PM10', 'PM2.5', 'SO2']
pollutant = st.sidebar.selectbox('Select a pollutant', pollutants)

# Date range selector
start_date = st.sidebar.date_input('Start date')
end_date = st.sidebar.date_input('End date')

# Validate the date range
if start_date > end_date:
    st.sidebar.error('Error: End date must fall after start date.')
else:
    if start_date and end_date:  # Check if both dates are selected
        # Load and plot the data
        data = load_data(DATA_FOLDER, year, pollutant)
        st.subheader(f'Air Quality Index (AQI) for {pollutant} from {start_date.strftime("%m/%d/%Y")} to {end_date.strftime("%m/%d/%Y")}')
        plot_aqi_data(data, start_date, end_date)
