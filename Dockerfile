# Use an official Python runtime as a parent image
FROM python:3.11.6

# Set environment variables (optional)
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE Lab3.settings

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY . /app/
