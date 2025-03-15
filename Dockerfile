FROM python:3.9-slim

# Set the working directory to /app inside the container
WORKDIR /app

# Copy the entire project into the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install pytest and httpx for testing
RUN pip install pytest httpx

# Expose FastAPI port (optional)
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
