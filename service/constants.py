import os

DB_NAME = 'postgres'
TABLE_NAME = 'passenger_data'
if os.environ.get('IS_CONTAINER') is not None: HOST = 'database'
else: HOST = 'localhost'
PSWD = os.environ.get('POSTGRES_PASSWORD')