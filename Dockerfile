# Use official Python image as base
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy app code into container
COPY app/ .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the main.py script when container starts
CMD ["python", "-u", "main.py"]