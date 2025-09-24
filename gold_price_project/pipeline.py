import requests
import pandas as pd
import sqlite3
from datetime import datetime
import logging
import os
from dotenv import load_dotenv

# -------------------------------
# Logging-inställning
# -------------------------------
logging.basicConfig(
    filename='pipeline.log',       # Loggfil i samma mapp
    level=logging.INFO,            # Loggnivå
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# -------------------------------
# Ladda miljövariabler från .env
# -------------------------------
load_dotenv()
API_KEY = os.getenv("GOLD_API_KEY")

# -------------------------------
# API-inställningar
# -------------------------------
URL = "https://www.goldapi.io/api/XAU/USD"
headers = {
    "x-access-token": API_KEY,
    "Content-Type": "application/json"
}

# -------------------------------
# Hämta data och spara i DB
# -------------------------------
try:
    response = requests.get(URL, headers=headers)
    data = response.json()
    
    if "price" in data:
        price = data["price"]
        loaded_at = datetime.now()
        
        df = pd.DataFrame({
            "base": ["USD"],
            "target": ["XAU"],
            "price": [price],
            "loaded_at": [loaded_at]
        })
        
        conn = sqlite3.connect("gold_prices.db")
        df.to_sql("gold_prices", conn, if_exists="append", index=False)
        conn.close()
        
        logging.info(f"Successfully fetched and stored gold price: {price}")
        print(f"Successfully fetched and stored gold price: {price}")
    else:
        logging.error(f"Price missing in API response: {data}")
        print(f"Price missing in API response: {data}")

except Exception as e:
    logging.error(f"Error fetching data: {e}")
    print(f"Error fetching data: {e}")

# python pipeline.py