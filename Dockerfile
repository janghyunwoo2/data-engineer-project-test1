# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
#RUN pip install -r requirements.txt

# Run the data processing script
CMD ["python", "data_processing.py"]