# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code and model file to the container
COPY app.py .
COPY best_model.joblib .

# Install FastAPI and other dependencies
RUN pip install fastapi uvicorn joblib

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
