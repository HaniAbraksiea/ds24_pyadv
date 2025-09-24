# Gold Price Pipeline

## Description
This project is a Python ETL pipeline (Extract – Transform – Load) that:
1. Fetches the current gold price in USD from an open API (GoldAPI).
2. Adds a timestamp (`loaded_at`) for when the data was fetched.
3. Saves the results into a SQLite database (`gold_prices.db`).
4. Logs all runs and any errors in `pipeline.log`.
5. Performs data analysis and visualization using `analyze.py`.
6. Uses a simple Machine Learning model in `forecast.py` to predict the next day's gold price.

The pipeline can be run manually or scheduled automatically using Windows Task Scheduler. It is designed to demonstrate a full data workflow from API extraction to analysis and prediction.

## Installation
Clone the repository or download the files:
git clone <your-repo-link>

Navigate to the project folder:
cd gold_price_pipeline

Install dependencies:
pip install -r requirements.txt

## Usage
Run the ETL pipeline:
python pipeline.py

Run analysis and visualization:
python analyze.py

Run next-day price forecast:
python forecast.py

Run tests:
pytest test_pipeline.py -v

## Files
pipeline.py: fetches gold prices and stores them in SQLite.
analyze.py: analyzes historical prices and generates graphs.
forecast.py: predicts the next day’s price using a simple ML model.
test_pipeline.py: unit tests for the pipeline.
gold_prices.db: SQLite database storing the prices.
pipeline.log: logs all runs and errors.
requirements.txt: Python dependencies.

## Notes
Make sure you have an active internet connection for the API.
You can schedule pipeline.py daily using Windows Task Scheduler.
The ML forecast is a simple example and can be improved with more data or advanced models.


## API Key
Create a `.env`-file in the project folder and add your personal API key:
GOLD_API_KEY=din-api-nyckel-här

## Author
Hani Abraksiea – Data Science Intern – EC Utbildning, Gothenburg