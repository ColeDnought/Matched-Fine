from DataReader import get_tickers, get_historical_data

tickers = get_tickers() # This function will return a DataFrame of tickers
ticker_data = get_historical_data() # This function will return a DataFrame of historical data for every ticker

print("\nGot all the data!")