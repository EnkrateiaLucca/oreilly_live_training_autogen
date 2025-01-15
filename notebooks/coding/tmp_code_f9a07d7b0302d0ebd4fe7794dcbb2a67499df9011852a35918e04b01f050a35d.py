import yfinance as yf
import matplotlib.pyplot as plt

# Download MSFT stock data
msft = yf.download('MSFT', start='2024-01-01', end='2024-12-31')

# Plotting the stock data
plt.figure(figsize=(10, 6))
plt.plot(msft['Close'], label='MSFT Closing Prices')
plt.title('MSFT Stock Prices in 2024')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('MSFT_Stock_Prices_2024.png')
plt.close()