import requests
import sqlite3
import pandas as pd
import logging
from datetime import datetime

# Loggkonfiguration
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fetch_data(api_url: str) -> pd.DataFrame:
    """Hämtar valutadata från API och returnerar som DataFrame"""
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        # Kontrollera att 'rates' finns
        if "rates" not in data:
            logging.error(f"Rates saknas i API-svaret: {data}")
            raise KeyError("'rates' saknas i API-svaret")

        rates = data["rates"]
        df = pd.DataFrame(rates.items(), columns=["currency", "rate"])
        df["base"] = data.get("base_code", "USD")
        df["date"] = data.get("time_last_update_utc", datetime.today().strftime("%Y-%m-%d"))
        logging.info(f"Hämtade {len(df)} valutor från API.")
        return df

    except Exception as e:
        logging.error(f"Fel vid hämtning från API: {e}")
        raise

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Transformera data genom att lägga till tidstämpel"""
    try:
        df["loaded_at"] = datetime.now()
        logging.info("Transformerade data.")
        return df
    except Exception as e:
        logging.error(f"Fel vid transformation: {e}")
        raise

def save_to_sql(df: pd.DataFrame, db_file: str, table_name: str):
    """Spara DataFrame till SQL-tabell (SQLite)"""
    try:
        conn = sqlite3.connect(db_file)
        df.to_sql(table_name, conn, if_exists="append", index=False)
        conn.close()
        logging.info(f"Sparade {len(df)} rader till tabell {table_name}.")
    except Exception as e:
        logging.error(f"Fel vid SQL-sparande: {e}")
        raise

def main():
    """Kör hela pipelinen"""
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        df = fetch_data(url)
        df = transform_data(df)
        save_to_sql(df, "currency.db", "exchange_rates")
        logging.info("Pipeline kördes klart utan fel.")
    except Exception as e:
        logging.error(f"Pipeline misslyckades: {e}")

if __name__ == "__main__":
    main()


# python pipeline.py
