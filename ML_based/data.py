import pandas as pd
from pandas import DataFrame, Series
import pandas_datareader.data as web
from datetime import datetime
from dateutil import parser
import tushare as ts

def getStock_C(ticker):
	"""
	Get daily Chinese stock data from TuShare.
	"""
	df = ts.get_h_data(ticker, index=True)
	df = df.iloc[::-1]
	df = df[['open', 'high', 'low', 'volume', 'close']]
	df.columns = ['Open', 'High', 'Low', 'Volume', 'AdjClose']
	return df

