# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Clone the Git repository
RUN git clone https://github.com/JPanettieri/historic-weather-scraper.git .

# Install any necessary dependencies
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the application
CMD ["python", "main.py"]