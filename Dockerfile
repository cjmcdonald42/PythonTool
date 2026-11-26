# Use the official Python 3.14 slim image
FROM python:3.14-slim

# Prevent Python from writing .pyc files and ensure stdout/stderr are unbuffered
# (Unbuffered output ensures input() prompts display immediately in the terminal)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy your script into the container
COPY pythonTool.py .

# Run the script when the container starts
CMD ["python", "pythonTool.py"]