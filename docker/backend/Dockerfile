# Stage 1: Build stage with Python 3.9
FROM python:3.9.6

# Set the working directory
WORKDIR /app

# Install any additional packages or perform other configurations as needed for PostgreSQL
RUN pip install jsonify
RUN pip install Flask==2.3.2
RUN pip install flask-restx==1.1.0
RUN pip install loguru==0.7.0
RUN pip install matplotlib==3.7.1
RUN pip install numpy==1.24.2
RUN pip install psycopg2-binary==2.9.7

# Run the data_loader.py script when the container starts
CMD ["python", "/data/data_loader.py"]
CMD ["python", "/service/app_factory.py"]