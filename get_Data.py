import pandas as pd

"""
Get the API key for alphavantage (www.alphavantage.co) API.

:returns: the API key

:rtype: str
"""
def get_key():
    key_file = open("API_key.txt")
    key = key_file.read()
    return key

"""
Read a stock daily information (all the time) form given the stock name and return it in the form of a dataframe. The dataframe
    will have the following attributes: timestamp, open, high, low, close, volume.

:param stock_name: the name of the stock (e.g. MSFT)
:param key: the API key for alphavantage

:type stock_name: the daily information of a specific stock
:type key: 

:returns stock_info: return the dataframe after read the data.

:rtype stock_info: pandas.DataFrame
"""
def get_data(stock_name, key):
    website = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol={ticker}&apikey={key}&datatype=csv".format(ticker = stock_name, key = key)
    stock_info = pd.read_csv(website)
    return stock_info