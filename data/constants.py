import os
from pathlib import Path

DB_NAME = 'postgres'
INPUT_CSV_NAME = 'titanic.csv'
PATH_TO_CSV = Path(__file__).resolve().parent / INPUT_CSV_NAME
TABLE_NAME = 'passenger_data'
if os.environ.get('IS_CONTAINER') is not None: HOST = 'database'
else: HOST = 'localhost'
PSWD = os.environ.get('POSTGRES_PASSWORD')