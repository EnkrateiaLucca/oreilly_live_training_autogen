import yfinance as yf
import matplotlib.pyplot as plt

# Fetch MSFT stock data for 2024
ticker = 'MSFT'
stock_data = yf.download(ticker, start='2024-01-01', end='2024-12-31')

# Plotting the stock price
dates = stock_data.index
prices = stock_data['Close']

plt.figure(figsize=(10, 5))
plt.plot(dates, prices, label='MSFT Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price in USD')
plt.title('Microsoft (MSFT) Stock Prices in 2024')
plt.legend()
plt.grid(True)

# Save to a file
plt.savefig('MSFT_2024_Stock_Prices.png')
plt.close()