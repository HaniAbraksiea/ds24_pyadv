import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# Skapa en undermapp för figurer om den inte redan finns
if not os.path.exists("figures"):
    os.makedirs("figures")

# Läs data från databasen
conn = sqlite3.connect("gold_prices.db")
df = pd.read_sql("SELECT * FROM gold_prices", conn)
conn.close()

# Konvertera till datumformat (om det inte redan är rätt)
df["loaded_at"] = pd.to_datetime(df["loaded_at"])
df["date"] = df["loaded_at"].dt.date

# Gruppera per dag (medelvärde om flera mätningar samma dag)
daily_df = df.groupby("date")["price"].mean().reset_index()

# --- Skapa linjediagram ---
plt.figure(figsize=(10, 6))
plt.plot(daily_df["date"], daily_df["price"], marker="o", linestyle="-", color="gold")
plt.title("Gold Price Over Time (USD per Ounce)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.xticks(rotation=45)
plt.grid(True)

# Spara grafen i undermappen figures/
plt.savefig("figures/gold_price_over_time.png", dpi=300, bbox_inches="tight")
plt.close()

print("✅ Analys klar! Graf sparad i figures/gold_price_over_time.png")


# python analyze.py
