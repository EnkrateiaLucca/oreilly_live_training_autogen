# filename: stock_plot.py

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Define the stock tickers and the date range
tickers = ['NVDA', 'TSLA']
start_date = '2023-01-01'
end_date = pd.Timestamp.now().strftime('%Y-%m-%d')

# Step 2: Download the stock data from Yahoo Finance
data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

# Step 3: Calculate the YTD change
ytd_change = (data / data.iloc[0]) - 1

# Step 4: Plot the data
plt.figure(figsize=(10, 6))
for ticker in tickers:
    plt.plot(ytd_change[ticker], label=ticker)

plt.title('YTD Stock Price Change for NVDA and TSLA')
plt.xlabel('Date')
plt.ylabel('YTD Change (%)')
plt.legend()
plt.grid(True)
plt.show()