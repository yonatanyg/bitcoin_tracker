import requests

def get_btc_price():
    # Calls CoinGecko public API to get current BTC price in USD
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    response.raise_for_status()  # Raise error if request failed
    data = response.json()
    return data["bitcoin"]["usd"]
