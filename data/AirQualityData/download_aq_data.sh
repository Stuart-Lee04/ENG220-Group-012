#!/bin/bash

# Base URL without the year
BASE_URL="https://aqs.epa.gov/aqsweb/airdata/annual_conc_by_monitor_"

# Define the range of years
START_YEAR=2010
END_YEAR=2022

# Loop over each year
for YEAR in $(seq $START_YEAR $END_YEAR)
do
    # Construct the full URL with the year
    FULL_URL="${BASE_URL}${YEAR}.zip"

    # Define the local file name to save the downloaded file
    FILE_NAME="data_${YEAR}.zip"

    # Download the file
    curl -o "$FILE_NAME" "$FULL_URL" || wget -O "$FILE_NAME" "$FULL_URL"

    # Check if the download was successful
    if [ -f "$FILE_NAME" ]; then
        echo "Downloaded data for year $YEAR. Extracting the file..."

        # Extract the file
        unzip "$FILE_NAME"

        echo "Extraction completed for year $YEAR."
    else
        echo "Failed to download data for year $YEAR."
    fi
done

