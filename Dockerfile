# Use the official Python base image
FROM python:3.8

# Set the working directory in the Docker container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY docker_requirements.txt /app/

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container at /app
COPY . /app

# Command to run on container start
CMD ["streamlit", "run", "air_quality_streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]