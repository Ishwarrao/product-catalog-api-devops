# Use official lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy only requirements to cache dependencies first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY app.py .
COPY bulk_add.py .

# Copy any additional files if needed, e.g. models, migrations, etc.

# Expose the Flask default port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]