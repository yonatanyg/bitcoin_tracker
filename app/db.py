import psycopg2
from datetime import datetime
import os

def connect():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "btc"),
        user=os.getenv("DB_USER", "btcuser"),
        password=os.getenv("DB_PASS", "btcpass")
    )

def init_db():
    # Create the btc_prices table if not exists
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS btc_prices (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP,
                    price FLOAT
                );
            """)
            conn.commit()

def insert_price(price):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO btc_prices (timestamp, price) VALUES (%s, %s);",
                (datetime.utcnow(), price)
            )
            conn.commit()

def get_stats():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT MAX(price), MIN(price), AVG(price) FROM btc_prices;")
            return cur.fetchone()
