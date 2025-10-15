# Import necessary libraries
import pandas as pd
import numpy as np

#Fetching Bitcoin data
from src.dataloader import get_bitcoin_data
BTC_USD = get_bitcoin_data()
#Fetching trade signals
from src.analysis import trade_signals

# Backesting the algorithm's trading performance

# Defining how much money you will start with (in USD)
initial_balance = 10000.0 # ten thousand USD

# Creating dataframe containing all the dates considered
backtest = pd.DataFrame(index=trade_signals.index)

# Adding column containing the daily percent returns of Bitcoin
backtest['BTC_Return'] = BTC_USD['Close'] / BTC_USD['Close'].shift(1) # Current closing price / yesterday's closing price


# Adding column containing the daily percent returns of the Moving Average Crossover strategy
backtest['Alg_Return'] = np.where(trade_signals.Signal == 1, backtest.BTC_Return, 1.0)

# Adding column containing the daily value of the portfolio using the Crossover strategy
backtest['Balance'] = initial_balance * backtest.Alg_Return.cumprod() # cumulative product
