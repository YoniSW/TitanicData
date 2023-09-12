import csv
from loguru import logger
import psycopg2

import constants as c


# Define DB connection parameters
db_params = {
    'dbname': c.DB_NAME,
    'user': c.DB_NAME,
    'password': c.PSWD,
    'host': c.HOST,  # If running on the same machine
    'port': '5432', # used by the PostgreSQL DB server
    'sslmode': 'disable'
}

# Connect to DB
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Create schema 
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {c.TABLE_NAME} (
        PassengerId INT,
        Survived INT,
        Pclass INT,
        Name VARCHAR(255),
        Sex VARCHAR(10),
        Age FLOAT,
        SibSp INT,
        Parch INT,
        Ticket VARCHAR(50),
        Fare FLOAT,
        Cabin VARCHAR(50),
        Embarked VARCHAR(1)
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()

    # Load CSV data into the table
    with open(c.PATH_TO_CSV, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            row = [value if value != '' else None for value in row]
            cursor.execute('''
                INSERT INTO passenger_data
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            ''', row)

    conn.commit()
    logger.info("CSV data loaded successfully!")

except Exception as e:
    logger.error(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
