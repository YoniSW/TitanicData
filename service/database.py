from loguru import logger
import psycopg2
from psycopg2 import sql

import constants as c

db_params = {
    'dbname': c.DB_NAME,
    'user': c.DB_NAME,
    'password': c.PSWD,
    'host': c.HOST,
    'port': '5432',
    'sslmode': 'disable'
}

def get_database_connection():
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except Exception as e:
        logger.error(f"Error: {e}")
        return None

def fetch_passengers():
    conn = get_database_connection()
    if conn:
        try:
            cur = conn.cursor()
            query = f"SELECT * FROM {c.TABLE_NAME}"
            logger.info(f'query: {query}')
            cur.execute(query)
            data=cur.fetchall()
            passengers = []
            for row in data:
                passenger = {column.name: value for column, value in zip(cur.description, row)}
                passengers.append(passenger)
            
            cur.close()
            conn.close()
            return passengers
        except Exception as e:
            logger.error(f"Error: {e}")
            conn.close()
    
    return []


def fetch_passenger_by_id(passenger_id):
    conn = get_database_connection()
    if conn:
        try:
            cur = conn.cursor()
            query = f"SELECT * FROM {c.TABLE_NAME} WHERE PassengerId = {passenger_id}"
            logger.info(f'query: {query}')
            cur.execute(query)
            passenger = cur.fetchone()
            data = {column.name: value for column, value in zip(cur.description, passenger)}
            cur.close()
            conn.close()
            return data

        except Exception as e:
            logger.error(f"Error: {e}")
            conn.close()
            
    
    return None