FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy all files from the current directory to /app in the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the app on port 8000
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
