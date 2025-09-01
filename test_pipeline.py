import unittest
import pandas as pd
from pipeline import transform_data

class TestPipeline(unittest.TestCase):
    def test_transform_data_adds_column(self):
        """Kontrollerar att transform_data lägger till 'loaded_at'"""
        # Skapa en test-DataFrame som liknar API-data
        df = pd.DataFrame({
            "currency": ["EUR", "SEK"],
            "rate": [0.92, 10.53],
            "base": ["USD", "USD"],
            "date": ["2025-09-01", "2025-09-01"]
        })

        transformed = transform_data(df)
        self.assertIn("loaded_at", transformed.columns)
        self.assertEqual(len(transformed), 2)  # Antal rader ska vara samma

if __name__ == "__main__":
    unittest.main()

# python -m unittest test_pipeline.py
