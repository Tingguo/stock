import pandas as pd
from pandas import DataFrame, Series
import pandas_datareader.data as web
from datetime import datetime
from dateutil import parser
import tushare as ts

<<<<<<< HEAD
def getStock_C(ticker):
	"""
	Get daily Chinese stock data from TuShare.
	"""
	df = ts.get_h_data(ticker, index=True)
	df = df.iloc[::-1]
	df = df[['open', 'high', 'low', 'volume', 'close']]
	df.columns = ['Open', 'High', 'Low', 'Volume', 'AdjClose']
	return df
=======
def getStock_C(ticker, start='2005-01-01', end='2015-07-25'):
	"""
	Get daily Chinese stock data from TuShare.
	"""
	df = ts.get_h_data(ticker, index=True, start=start, end=end)
	df = df.iloc[::-1]
	df = df[['open', 'high', 'low', 'volume', 'close']]
	df.columns = ['Open', 'High', 'Low', 'Volume', 'AdjClose']
	return df
>>>>>>> bb4464858cd89f8ea2fde41416be812c0320d72c
