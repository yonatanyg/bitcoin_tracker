import time
from fetcher import get_btc_price
from db import init_db, insert_price, get_stats

def recommend(price, avg):
    # Basic recommendation based on last price vs average
    if price < avg:
        return "BUY"
    elif price > avg:
        return "SELL"
    return "HOLD"

def run():
    print("Starting bitcoin tracker...")
    init_db()

    while True:
        try:
            price = get_btc_price()
            insert_price(price)
            max_p, min_p, avg_p = get_stats()

            print(f"\nCurrent Price: ${price:.2f}")
            print(f"Max: ${max_p:.2f} | Min: ${min_p:.2f} | Avg: ${avg_p:.2f}")
            print("Recommendation:", recommend(price, avg_p))
        except Exception as e:
            print("Error:", e)
        
        time.sleep(60)

if __name__ == "__main__":
    run()
