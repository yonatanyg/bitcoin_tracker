import psycopg2
from datetime import datetime
import os

def connect():
    """Connect to the PostgreSQL database using environment variables or defaults."""
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "btc"),
        user=os.getenv("DB_USER", "btcuser"),
        password=os.getenv("DB_PASS", "btcpass")
    )

def init_db():
    """Make sure the btc_prices table exists before we start."""
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
    """Add a new price entry with the current UTC time."""
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO btc_prices (timestamp, price) VALUES (%s, %s);",
                (datetime.utcnow(), price)
            )
            conn.commit()

def get_stats():
    """Grab the max, min, and average price so far from the database."""
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT MAX(price), MIN(price), AVG(price) FROM btc_prices;")
            return cur.fetchone()
