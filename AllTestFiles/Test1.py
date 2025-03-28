import yfinance as yf
import pandas as pd

# Define asset and time period
asset = "AAPL"  # Apple stock
period = "8d"  # Yahoo Finance allows a max of 60 days for 1-minute data
interval = "1m"  # 1-minute timeframe

# Fetch data
apple_data = yf.download(asset, period=period, interval=interval)

# Save to CSV
apple_data.to_csv("apple_1min_8days.csv")

# Display first few rows
print(apple_data.head())

