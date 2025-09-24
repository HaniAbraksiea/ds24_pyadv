import unittest
import sqlite3
import os
from datetime import datetime
import pipeline  # importera din pipeline-fil (pipeline.py)

DB_FILE = "gold_prices.db"

class TestGoldPricePipeline(unittest.TestCase):

    def test_database_exists(self):
        """Kontrollerar att databasen finns efter pipeline körning"""
        pipeline  # kör pipeline.py
        self.assertTrue(os.path.exists(DB_FILE), f"{DB_FILE} does not exist")

    def test_table_has_data(self):
        """Kontrollerar att tabellen gold_prices innehåller minst en rad"""
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM gold_prices")
        count = cursor.fetchone()[0]
        conn.close()
        self.assertGreater(count, 0, "gold_prices table is empty")

    def test_price_column(self):
        """Kontrollerar att kolumnen price har värden"""
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT price FROM gold_prices ORDER BY loaded_at DESC LIMIT 1")
        price = cursor.fetchone()[0]
        conn.close()
        self.assertIsInstance(price, float, "Price is not a float")

if __name__ == "__main__":
    unittest.main()

# pytest test_pipeline.py -v
