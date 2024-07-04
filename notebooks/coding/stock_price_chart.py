# filename: stock_price_chart.py

import yfinance as yf
import matplotlib.pyplot as plt
import datetime

# Use the datetime library to get the today's date and the date one year ago
today = datetime.date.today()
start_of_year = datetime.date(today.year, 1, 1)

# Define the ticker symbols for the stocks we are interested in
tickers = ['NVDA', 'TSLA']

# Download the YTD stock data
data = yf.download(tickers, start=start_of_year, end=today)

# Get the daily closing prices
closing_prices = data['Close']

# Plot the data
plt.figure(figsize=(14, 7))
for i in closing_prices.columns.values:
    plt.plot(closing_prices.index, closing_prices[i], lw=3, alpha=0.8,label=i)
plt.legend(loc='upper left', fontsize=12)
plt.title('NVDA and TESLA stock price change YTD')
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid()
plt.show()