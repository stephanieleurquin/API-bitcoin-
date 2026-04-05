from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="Crypto API")

COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"

@app.get("/")
def home():
    return {"message": "Bienvenue sur mon API Crypto 🚀"}

@app.get("/crypto/{coin}")
def get_crypto(coin: str):
    url = f"{COINGECKO_BASE_URL}/simple/price"
    params = {
        "ids": coin.lower(),
        "vs_currencies": "usd,eur",
        "include_24hr_change": "true",
        "include_market_cap": "true"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Erreur API externe")

    data = response.json()

    if coin.lower() not in data:
        raise HTTPException(status_code=404, detail="Crypto non trouvée")

    crypto_data = data[coin.lower()]

    return {
        "coin": coin.lower(),
        "price_usd": crypto_data.get("usd"),
        "price_eur": crypto_data.get("eur"),
        "market_cap_usd": crypto_data.get("usd_market_cap"),
        "change_24h_percent": crypto_data.get("usd_24h_change")
    }

@app.get("/top")
def get_top_cryptos():
    url = f"{COINGECKO_BASE_URL}/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": "false"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Erreur API externe")

    data = response.json()

    result = []
    for coin in data:
        result.append({
            "name": coin["name"],
            "symbol": coin["symbol"],
            "price_usd": coin["current_price"],
            "market_cap": coin["market_cap"],
            "change_24h": coin["price_change_percentage_24h"]
        })

    return result