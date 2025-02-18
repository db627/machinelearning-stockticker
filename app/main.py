import yfinance as yf
import pandas as pd
import os
import string
import matplotlib.pyplot as plt

def sanitize_ticker(ticker):
    valid_chars = f"-_.{string.ascii_letters}{string.digits}"
    return ''.join(c for c in ticker if c in valid_chars).lower()

def getStock(ticker):
    tick = yf.Ticker(ticker)
    tick_hist = tick.history(period="max")
    return tick_hist

def tickerToCSV(ticker):
    global DATA_PATH
    sanitized_ticker = sanitize_ticker(ticker)
    DATA_PATH = f"{sanitized_ticker}_data.csv"

    if os.path.exists(DATA_PATH):
        print(f"Loading data from {DATA_PATH}...")
        data = pd.read_csv(DATA_PATH, index_col=0) 
    else:
        print(f"Fetching data for {ticker}...")
        data = getStock(ticker)
        data.to_csv(DATA_PATH) 
        print(f"Data saved to {DATA_PATH}")

    return data

ticker = input("Enter a stock ticker symbol: ").strip()
data = tickerToCSV(ticker)
data.plot.line(y="Close", use_index=True)
plt.show()