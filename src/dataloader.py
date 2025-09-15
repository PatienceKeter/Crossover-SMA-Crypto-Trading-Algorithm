# Fetch cryptocurrency market prices and data
# Import necessary libraries

import yfinance as yf
import pandas as pd

# Retrieve Bitcoin to USD exchange rates with a 1 day interval and save the dataframe to a variable.
def get_bitcoin_data(start='2025-01-01', end='2025-08-31', interval='1d'):
    BTC_USD = yf.download("BTC-USD", start=start, end=end, interval=interval)
    return BTC_USD




