# filename: stock_ytd_gain.py

import datetime
import yfinance as yf

# Get the current date
current_date = datetime.date.today()
print("Today's date is:", current_date)

# Download stock data
meta_data = yf.download('META', start='2022-01-01', end=current_date)
tesla_data = yf.download('TSLA', start='2022-01-01', end=current_date)

# Calculate YTD gain
meta_ytd_gain = ((meta_data['Close'][-1] - meta_data['Close'][0]) / meta_data['Close'][0]) * 100
tesla_ytd_gain = ((tesla_data['Close'][-1] - tesla_data['Close'][0]) / tesla_data['Close'][0]) * 100

print("META YTD gain:", meta_ytd_gain)
print("TESLA YTD gain:", tesla_ytd_gain)