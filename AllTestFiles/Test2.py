import yfinance as yf
import pandas as pd

# Define asset (Apple stock)
asset = "AAPL"

# Define timeframes to test
timeframes = ["1m", "2m", "5m", "15m", "30m", "1h", "4h", "1d", "1wk", "1mo"]

# Dictionary to store results
results = {}

print("Starting Yahoo Finance max historical data test...\n")

for tf in timeframes:
    print(f"Fetching data for {tf} interval...")
    
    try:
        # Try to fetch the maximum amount of data for each timeframe
        data = yf.download(asset, period="max", interval=tf)
        
        if not data.empty:
            start_date = data.index[0]
            end_date = data.index[-1]
            results[tf] = [start_date, end_date]
            print(f"✅ {tf} | Data available from {start_date} to {end_date}")
        else:
            results[tf] = ["No Data", "No Data"]
            print(f"❌ {tf} | No data available.")

    except Exception as e:
        results[tf] = ["Error", str(e)]
        print(f"❌ {tf} | Error: {e}")

# Convert results to DataFrame
df_results = pd.DataFrame.from_dict(results, orient='index', columns=['Start Date', 'End Date'])

# Save to CSV
df_results.to_csv("yahoo_finance_timeframe_limits.csv")

print("\n✅ Test complete. Results saved to 'yahoo_finance_timeframe_limits.csv'")

