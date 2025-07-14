# Bitcoin Tracker

A simple Dockerized Python application that fetches the current Bitcoin price every minute, stores it in a PostgreSQL database, and prints statistics and buy/sell recommendations based on the average price so far.

## 🧱 Tech Stack

- Python 3.10
- PostgreSQL 13
- Docker & Docker Compose

## 🏁 How It Works

1. Fetches Bitcoin price (USD) from CoinGecko API every 60 seconds.
2. Stores each price along with a timestamp in the PostgreSQL database.
3. Calculates and prints:
   - Max price
   - Min price
   - Average price
   - Buy/Sell/Hold recommendation based on last price vs average.

## 🚀 Getting Started

> Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and running.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/bitcoin-tracker.git
cd bitcoin-tracker
