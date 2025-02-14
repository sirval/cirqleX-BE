# Use the latest Python version
FROM python:3.12

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file first
COPY requirements.txt .

# Install virtualenv if it's not already included in the base image
RUN pip install --no-cache-dir virtualenv

# Create a virtual environment inside the container
RUN python -m venv /venv

# Install dependencies in the virtual environment
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run migrations and start FastAPI
CMD ["sh", "-c", "/venv/bin/alembic upgrade head && /venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000"]