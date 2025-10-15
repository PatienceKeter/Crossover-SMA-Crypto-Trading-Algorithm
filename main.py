#Import libraries
import os
import sys

# Fetching Bitcoin data
from src.dataloader import get_bitcoin_data
from src.analysis import add_sma, generate_trade_signals
from src.visualization import plot_price, plot_moving_averages, plot_trade_signals, plot_backtest
from src.backtest import backtest

def main():
    # Load data
    BTC_USD = get_bitcoin_data()
    print(BTC_USD.head())

    # Plot basic price chart
    plot_price(BTC_USD)

    # Calculate and plot SMAs
    BTC_USD = add_sma(BTC_USD)
    plot_moving_averages(BTC_USD)

    # Generate and plot trading signals
    signals = generate_trade_signals(BTC_USD)
    plot_trade_signals(BTC_USD, signals)

    # Backtest
    initial_balance = 10000.0
    backtest_results = backtest(BTC_USD, signals, initial_balance)
    plot_backtest(backtest_results, initial_balance)

if __name__ == "__main__":
    main()
