import yfinance as yf
import pandas as pd
import threading
from concurrent.futures import ThreadPoolExecutor

# Define stock symbols
stocks = [
    "AAPL", "MSFT", "JNJ", "PG", "KO", "PEP", "WMT", "NSRGY", "UL", "BRK-B",  # Blue-Chip Stocks
    "MCD", "CL", "MMM", "ABBV", "T", "VZ", "CAT", "IBM", "HD", "MDT",  # Dividend Aristocrats
    "PFE", "MRK", "KMB", "DUK", "SO", "AWK", "WM", "GIS", "KHC", "CLX",  # Defensive Sector Stocks
    "SPY", "VIG", "USMV", "SPLV", "DVY", "VDC", "VPU", "SCHD", "IYH", "FDLO",  # Stable ETFs
    "O", "AMT", "PSA", "EQIX", "PLD", "AVB", "VTR", "SPG", "WELL", "CCI"  # REITs
]

# Define timeframes and max historical data allowed
intervals = {
    "1m": "8d",
    "2m": "60d",
    "5m": "60d",
    "15m": "60d",
    "30m": "60d",
    "1h": "730d",
    "4h": "730d",
    "1d": "max",
    "1wk": "max",
    "1mo": "max"
}

# Function to download data for a single stock
def fetch_stock_data(stock):
    for interval, period in intervals.items():
        try:
            print(f"Downloading {stock} data for {interval} timeframe...")
            data = yf.download(stock, interval=interval, period=period)
            if not data.empty:
                filename = f"{stock}_{interval}.csv"
                data.to_csv(filename)
                print(f"✅ Saved: {filename}")
            else:
                print(f"❌ No data available for {stock} at {interval} timeframe.")
        except Exception as e:
            print(f"❌ Error downloading {stock} at {interval}: {e}")

# Use ThreadPoolExecutor to parallelize downloads
max_threads = min(10, len(stocks))  # Limit number of threads to avoid overload
with ThreadPoolExecutor(max_threads) as executor:
    executor.map(fetch_stock_data, stocks)

print("✅ Data download complete.")

