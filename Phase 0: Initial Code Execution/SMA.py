import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV with correct column names
columns = ["Date", "Close", "High", "Low", "Open", "Volume"]
data = pd.read_csv("gold_daily_5y.csv", skiprows=2, names=columns, index_col=0, parse_dates=True)

# Calculate SMAs
short_window = 50
long_window = 200

data['SMA_50'] = data['Close'].rolling(window=short_window).mean()
data['SMA_200'] = data['Close'].rolling(window=long_window).mean()

# Generate Buy/Sell signals
data['Signal'] = 0
data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1  # Buy
data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = -1  # Sell

# Track profits
buy_price = None
profits = []

for index, row in data.iterrows():
    if row['Signal'] == 1 and buy_price is None:  
        buy_price = row['Close']  # Buy at this price
    elif row['Signal'] == -1 and buy_price is not None:  
        profit_percent = ((row['Close'] - buy_price) / buy_price) * 100
        profits.append(profit_percent)  # Store profit %
        buy_price = None  # Reset after selling

# Calculate total profit percentage
total_profit = sum(profits) if profits else 0

# Plot Results
plt.figure(figsize=(14,7))
plt.plot(data.index, data['Close'], label='Gold Price', color='blue')
plt.plot(data.index, data['SMA_50'], label='50-day SMA', color='green', linestyle='dashed')
plt.plot(data.index, data['SMA_200'], label='200-day SMA', color='red', linestyle='dashed')

# Plot Buy/Sell signals
plt.scatter(data.index[data['Signal'] == 1], data['Close'][data['Signal'] == 1], label='Buy Signal', marker='^', color='green', alpha=1)
plt.scatter(data.index[data['Signal'] == -1], data['Close'][data['Signal'] == -1], label='Sell Signal', marker='v', color='red', alpha=1)

plt.legend()
plt.title(f'Gold Price with SMA Crossover Strategy\nTotal Profit: {total_profit:.2f}%')  # Display profit percentage
plt.show()

# Print total profit
print(f"Total Profit from SMA Strategy: {total_profit:.2f}%")
