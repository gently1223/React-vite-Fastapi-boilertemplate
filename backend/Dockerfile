# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Set the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
