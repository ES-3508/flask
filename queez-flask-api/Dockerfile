# Use the official Python Alpine image
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /app


RUN apt-get update && apt-get install -y \
    pkg-config \
    libmysqlclient-dev \
    build-essential \
    cython

# Install build tools and dependencies
# RUN apk add --no-cache pkgconfig mysql-dev build-base cython

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Copy the application files to the container
COPY . /app/

# Create and activate a virtual environment
RUN python -m venv venv
RUN source venv/bin/activate

# Install Cython explicitly
RUN pip install cython

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt -v

# Expose the required port
EXPOSE 5000

# Command to run the application
CMD ["python", "./server.py"]
