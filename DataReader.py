import pandas as pd
import yfinance as yf
from functools import lru_cache
from pytickersymbols import PyTickerSymbols

def get_tickers(index="S&P 500"):
    """
    Get list of stocks in an index (default: S&P 500)
    
    Args:
        index (str): Index to get tickers from (default: 'S&P 500') see https://pypi.org/project/pytickersymbols/ for full list of indexes
    Returns:
        DataFrame: DataFrame of tickers
    """
    stock_reader = PyTickerSymbols()
    tickers = stock_reader.get_stocks_by_index(index)
    return pd.DataFrame(tickers)

@lru_cache(maxsize=None)
def download_data(tickers, interval) -> pd.DataFrame: 
    # Just a helper function so that you don't have to re-download data every time
    return yf.download(list(tickers), interval=interval, period="max", group_by='ticker')

def get_historical_data(index="S&P 500", interval="1d") -> pd.DataFrame:
    """
    Get historical data for a ticker
    
    Args:
        index (str): Index to get data for (default: 'S&P 500')
        interval (str): Time between each sample (default: '1d'). Options: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    Returns:
        DataFrame: DataFrame of historical data
    """
    ticker_df = get_tickers(index)
    ticker_symbols = tuple(ticker_df['symbol'])
    return download_data(ticker_symbols, interval)