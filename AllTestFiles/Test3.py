import yfinance as yf
import pandas as pd

# Define the stock symbol and intervals
symbol = "AAPL"  # Change this to your desired stock
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

# Loop through each interval and fetch data
for interval, period in intervals.items():
    print(f"Fetching data for {interval} interval...")
    
    try:
        data = yf.download(symbol, interval=interval, period=period)
        
        # Check if data is available
        if data.empty:
            print(f"❌ No data available for {interval} interval.")
            continue

        # Save to CSV
        filename = f"{symbol}_{interval}.csv"
        data.to_csv(filename)
        print(f"✅ Saved {interval} data to {filename}")

    except Exception as e:
        print(f"❌ Error fetching {interval} data: {e}")

print("✅ Data download complete.")

