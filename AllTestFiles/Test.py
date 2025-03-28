import yfinance as yf
import pandas as pd

# Define the asset
asset = "AAPL"

# Define the different timeframes to test
intervals = {
    "1m": "9d",
    "2m": "61d",
    "5m": "61d",
    "15m": "61d",
    "30m": "61d",
    "1h": "731d",
    "4h": "731d",
    "1d": "max",
    "1wk": "max",
    "1mo": "max"
}

# Store results
results = {}

# Loop through each timeframe
for interval, period in intervals.items():
    try:
        print(f"Fetching data for {interval} interval...")

        # Download market data
        data = yf.download(asset, period=period, interval=interval)

        if not data.empty:
            earliest_date = data.index[0]  # Get the first available date
            latest_date = data.index[-1]   # Get the last available date
            results[interval] = (earliest_date, latest_date)
            print(f"✅ {interval} | Data available from {earliest_date} to {latest_date}")
        else:
            print(f"❌ {interval} | No data available.")
            results[interval] = "No Data"
    
    except Exception as e:
        print(f"❌ {interval} | Error: {e}")
        results[interval] = str(e)

# Convert results to a DataFrame and save as CSV
df_results = pd.DataFrame.from_dict(results, orient='index', columns=['Start Date', 'End Date'])
df_results.to_csv("yahoo_finance_timeframe_limits.csv")

print("\n✅ Test complete. Results saved to 'yahoo_finance_timeframe_limits.csv'")

