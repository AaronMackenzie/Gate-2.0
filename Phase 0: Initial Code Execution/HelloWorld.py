import yfinance as yf
import pandas as pd

# Define asset and time period
asset = "GC=F"  # Gold Futures (XAU/USD)
start_date = "2019-03-27"  # 5 years ago
end_date = "2024-03-27"

# Fetch data
gold_data = yf.download(asset, start=start_date, end=end_date, interval="1d")

# Save to CSV
gold_data.to_csv("gold_daily_5y.csv")

# Display first few rows
print(gold_data.head())

