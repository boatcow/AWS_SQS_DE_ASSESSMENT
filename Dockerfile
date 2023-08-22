# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR .

# Copy the current directory contents into the container at /app
COPY . .

# Install the required packages
RUN pip install -r ux_dashboard/requirements.txt

# Define environment variable
ENV FLASK_ENV=production

# Make port 5000 available to the world outside this container
EXPOSE 8080

# Define command to run the app using Flask's development server
CMD ["python", "ux_dashboard/app.py"]
