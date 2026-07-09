import psycopg2
from logger_config import logger


def get_connection():

    try:
        connection = psycopg2.connect(
            host="localhost",
            database="dataforge",
            user="postgres",
            password="Tej@189",
            port="5432"
        )

        logger.info("PostgreSQL connection established")

        return connection

    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return None