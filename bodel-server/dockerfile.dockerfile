# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 3000

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "fastapi:app", "--host", "127.0.0.1", "--port", "8080", "--ssl_certfile", "cert.pem", "ssl_keyfile", "key.pem"]