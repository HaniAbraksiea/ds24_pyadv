import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# --- Hämta data ---
conn = sqlite3.connect("gold_prices.db")
df = pd.read_sql("SELECT * FROM gold_prices", conn)
conn.close()

# Konvertera loaded_at till datum och sortera
df["loaded_at"] = pd.to_datetime(df["loaded_at"])
df = df.sort_values("loaded_at")

# Skapa feature: föregående dags pris
df["previous_price"] = df["price"].shift(1)
df = df.dropna()

# Features och target
X = df[["previous_price"]]
y = df["price"]

# Dela upp i train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# --- Bygg modell ---
model = LinearRegression()
model.fit(X_train, y_train)

# Prognos på testdata
y_pred = model.predict(X_test)

# Utvärdera
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae:.2f} USD")

# Visa jämförelse
result = pd.DataFrame({"Actual": y_test.values, "Predicted": y_pred})
print(result.head())

# Prognos nästa dag
latest_price = df["price"].iloc[-1]
next_day_prediction = model.predict([[latest_price]])
print(f"Predicted next day price: {next_day_prediction[0]:.2f} USD")

# python forecast.py
