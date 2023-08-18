# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir uvicorn fastapi pymongo redis

# Expose the port on which the FastAPI app runs
EXPOSE 80

# Run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
