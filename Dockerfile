FROM python:3.10

# Update and install python3-pip
RUN apt-get update && \
    apt-get install -y python3-pip

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory into the container
COPY . /app

