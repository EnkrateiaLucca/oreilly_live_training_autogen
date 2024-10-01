# filename: stock_price_change_ytd.py

import yfinance as yf
import matplotlib.pyplot as plt
import datetime

# Get the current date
end_date = datetime.datetime.now().date()
# Get the first trading day of the current year
start_date = datetime.date(end_date.year, 1, 1)

# Fetch the YTD stock data for NVDA and TSLA
nvda_data = yf.download('NVDA', start=start_date, end=end_date)
tsla_data = yf.download('TSLA', start=start_date, end=end_date)

# Calculate the percentage change in stock price
nvda_price_change = ((nvda_data['Close'] / nvda_data['Close'].iloc[0]) - 1) * 100
tsla_price_change = ((tsla_data['Close'] / tsla_data['Close'].iloc[0]) - 1) * 100

# Plot the stock price change
plt.figure(figsize=(10, 6))
plt.plot(nvda_data.index, nvda_price_change, label='NVDA')
plt.plot(tsla_data.index, tsla_price_change, label='TSLA')
plt.xlabel('Date')
plt.ylabel('Price Change %')
plt.title('Year-to-Date Stock Price Change for NVDA and TSLA')
plt.legend()
plt.grid(True)
plt.savefig('stock_price_change_ytd.png')
print('Stock price change chart has been saved as stock_price_change_ytd.png.')