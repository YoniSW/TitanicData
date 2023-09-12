# Stage 1: Build stage with Python 3.9
FROM python:3.9.6

# Set the working directory
WORKDIR /app

# Install relevant packages
RUN pip install loguru>=0.6.0 psycopg2-binary>=2.6.0

CMD ["python", "/data/data_loader.py"]
