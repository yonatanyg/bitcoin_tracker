Bitcoin Tracker:
A minimal, Dockerized Python app that tracks Bitcoin's price in real-time. Every minute, it fetches the latest BTC price from the CoinGecko API, stores it in a PostgreSQL database, and prints live stats — including max, min, average price, and a basic BUY/SELL/HOLD recommendation.

Tech Stack:
Python 3.10
PostgreSQL 13
Docker & Docker Compose

How It Works:
Fetches the current Bitcoin price (in USD) every 60 seconds.
Saves it in a PostgreSQL database with a timestamp.
Displays the following stats in the console:
 Max price
 Min price
 Average price
 Recommendation: BUY / SELL / HOLD

Run Using:
ansible-playbook deploy.yml


