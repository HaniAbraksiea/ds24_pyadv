# Automated Python Pipeline

## Description
This project is a simple ETL pipeline (Extract – Transform – Load) in Python that:

- Fetches currency exchange rates from an open API: [https://open.er-api.com/v6/latest/USD](https://open.er-api.com/v6/latest/USD)  
  No API key is required.
- Transforms the data by adding a timestamp column `loaded_at`.
- Saves the results to an SQLite database (`currency.db`).
- Logs all runs and any errors in `pipeline.log`.

## Installation
1. Clone the repository or download the files.
2. Install dependencies:
```bash
pip install -r requirements.txt
