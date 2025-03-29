import yfinance as yf
import pandas as pd
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

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

# Lock for file writing
file_lock = threading.Lock()

# Function to download stock data with retries
def fetch_stock_data(stock):
    for interval, period in intervals.items():
        attempts = 3  # Retry up to 3 times
        for attempt in range(attempts):
            try:
                print(f"📥 Downloading {stock} data for {interval} timeframe (Attempt {attempt+1})...")
                data = yf.download(stock, interval=interval, period=period)

                if not data.empty:
                    filename = f"{stock}_{interval}.csv"

                    # Ensure thread safety while writing files
                    with file_lock:
                        data.to_csv(filename)

                    print(f"✅ Saved: {filename}")
                    break  # Exit retry loop on success
                else:
                    print(f"⚠️ No data for {stock} at {interval} timeframe.")

            except Exception as e:
                print(f"❌ Error downloading {stock} at {interval}: {e}")

            if attempt < attempts - 1:
                time.sleep(2)  # Wait before retrying

# Use ThreadPoolExecutor with controlled parallelism
max_threads = 5  # Reduce thread count to prevent overload
with ThreadPoolExecutor(max_threads) as executor:
    futures = {executor.submit(fetch_stock_data, stock): stock for stock in stocks}

    # Wait for all downloads to complete
    for future in as_completed(futures):
        stock = futures[future]
        try:
            future.result()  # Raise exception if any
        except Exception as e:
            print(f"⚠️ Error processing {stock}: {e}")

print("✅ Data download complete.")

