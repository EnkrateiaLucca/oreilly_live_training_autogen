# filename: plot_stock_price.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Fetch YTD stock data for NVDA and TSLA
nvda = yf.download('NVDA', start='2023-01-01', progress=False)
tsla = yf.download('TSLA', start='2023-01-01', progress=False)

# Normalize the data to compare the price changes from a common point
nvda_normalized = nvda['Close'] / nvda['Close'].iloc[0]
tsla_normalized = tsla['Close'] / tsla['Close'].iloc[0]

# Plot
plt.figure(figsize=(14, 7))
plt.plot(nvda_normalized, label='NVDA', linewidth=2)
plt.plot(tsla_normalized, label='TSLA', linewidth=2)
plt.title('YTD Stock Price Change of NVDA and TSLA')
plt.xlabel('Date')
plt.ylabel('Normalized Price')
plt.legend()
plt.grid(True)
plt.show()