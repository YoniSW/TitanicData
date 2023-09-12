# Stage 1: Build stage with Python 3.9
FROM python:3.9.6

# Set the working directory
WORKDIR /app

# Install any additional packages or perform other configurations as needed for PostgreSQL
RUN pip install jsonify
RUN pip install Flask>=2.3.0
RUN pip install flask-restx>=1.0.0
RUN pip install loguru>=0.6.0
RUN pip install matplotlib>=3.4.0
RUN pip install numpy>=1.21.0
RUN pip install psycopg2-binary>=2.6.0


# Run the data_loader.py script when the container starts
CMD ["python", "/service/app_factory.py"]
