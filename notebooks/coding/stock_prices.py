# filename: stock_prices.py
import yfinance as yf
from datetime import datetime, timedelta

# Define the stock tickers
tickers = ['META', 'TSLA']

# Define the nearest trading dates
start_date = '2024-01-02'
end_date = '2024-07-05'

# Function to find the nearest previous trading day
def get_nearest_previous_trading_day(date, data):
    while date not in data.index:
        date -= timedelta(days=1)
        if date < data.index[0]:
            raise ValueError("No trading day found before the specified date")
    return date

try:
    # Fetch the stock prices
    data = yf.download(tickers, start=start_date, end=end_date)
    print("Data fetched successfully")
    print(f"Available dates in dataset: {data.index}")

    # Convert start_date and end_date to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Convert datetime objects to strings in the correct format
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    # Find the nearest previous trading day for the end date
    end_date = get_nearest_previous_trading_day(end_date, data)
    end_date_str = end_date.strftime('%Y-%m-%d')
    print(f"Nearest previous trading day for end date: {end_date_str}")

    # Get the opening prices on the start date and the closing prices on the end date
    start_prices = data['Open'].loc[start_date_str]
    end_prices = data['Close'].loc[end_date_str]

    # Calculate the year-to-date gain
    gains = ((end_prices - start_prices) / start_prices) * 100

    # Print the results
    print(f"Start Prices on {start_date_str}:\n{start_prices}\n")
    print(f"End Prices on {end_date_str}:\n{end_prices}\n")
    print(f"Year-to-Date Gains:\n{gains}\n")

except Exception as e:
    print(f"An error occurred: {e}")