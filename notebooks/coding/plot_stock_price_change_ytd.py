# filename: plot_stock_price_change_ytd.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Step 1: Define a function to get the closing prices and YTD change
def get_ytd_change(ticker):
    stock_data = yf.Ticker(ticker)
    hist_data = stock_data.history(period="ytd")

    # Get the closing prices
    hist_data['Close'] = hist_data['Close']
    
    # Calculate the YTD change in percentage
    start_price = hist_data.iloc[0]['Close']
    hist_data['YTD Change'] = (hist_data['Close'] / start_price - 1) * 100

    return hist_data['YTD Change']

# Step 2: Get YTD change data for NVDA and TSLA
nvda_ytd_change = get_ytd_change('NVDA')
tsla_ytd_change = get_ytd_change('TSLA')

# Step 3: Plot the data
plt.figure(figsize=(12, 6))
plt.plot(nvda_ytd_change, label='NVDA YTD Change')
plt.plot(tsla_ytd_change, label='TSLA YTD Change')

# Plot styling
plt.title('NVDA and TSLA Stock Price YTD Change')
plt.xlabel('Date')
plt.ylabel('YTD Change (%)')
plt.legend()
plt.grid(True)

# Step 4: Save the plot as a .png file
plt.savefig('stock_price_change_ytd.png')

print("Plot saved as stock_price_change_ytd.png")