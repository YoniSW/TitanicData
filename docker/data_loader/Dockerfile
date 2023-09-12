# Stage 1: Build stage with Python 3.9
FROM python:3.9.6

# Set the working directory
WORKDIR /app

RUN pip install loguru==0.7.0
RUN pip install psycopg2-binary==2.9.7

CMD ["python", "/data/data_loader.py"]