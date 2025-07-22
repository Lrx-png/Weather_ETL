import psycopg2
import logging

from dotenv import load_dotenv
import os

load_dotenv()

# create an instance of the logger
logger = logging.getLogger()

# loggin set up
log_format = logging.Formatter('%(asctime)-15s - %(levelname)-2s - %(message)s')
sh = logging.StreamHandler()
sh.setFormatter(log_format)

# add the handler to the logger
logger.addHandler(sh)
logger.setLevel(logging.INFO)
"""
conn = psycopg2.connect(
    dbname=os.getenv('dbname'),
    user=os.getenv('user'),
    password=os.getenv('password'),
    host=os.getenv('host'),
    port=os.getenv('port')
)
"""

try:
    # Veritabanına bağlanma
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    logger.info("Database connection established successfully.")
    
except Exception as e:
    logger.error(f"Failed to connect to database: {repr(e)}")

finally:
    try:
        conn.close()
        logger.info("ℹDatabase connection closed.")
    except:
        pass