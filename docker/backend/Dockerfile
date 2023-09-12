# Stage 1: Build stage with Python 3.9
FROM python:3.9.6

# Set the working directory
WORKDIR /app

# Install relevant packages
RUN pip install jsonify Flask>=2.3.0 flask-restx>=1.0.0 loguru>=0.6.0 matplotlib>=3.4.0 numpy>=1.21.0 psycopg2-binary>=2.6.0

# Run the data_loader.py script when the container starts
CMD ["python", "/service/app_factory.py"]
