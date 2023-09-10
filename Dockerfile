# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code and requirements file into the container
COPY main.py .
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Expose the port your FastAPI application will run on (default is 8000)
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
