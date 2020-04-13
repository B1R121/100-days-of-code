# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:12:24 2020
This is program was made by following 

"Python for Finance Stock Data with Pandas and NumPy"
tutorial on youtube by shane lee


"""

from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

START_DATE = '2005-01-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))

UK_STOCK = 'UU.L'
USA_STOCK = 'AMZN'

def get_stats(stock_data):
    return {'last': np.mean(stock_data.tail(1)),
            'short_mean' : np.mean(stock_data.tail(20)),
            'long_mean': np.mean(stock_data.tail(200)),
            'short_rolling': stock_data.rolling(window=20).mean(),
            'long_rolling': stock_data.rolling(window=200).mean(),}
    

def clean_data(stock_data, col):
    weekdays = pd.date_range(start=START_DATE, end=END_DATE)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')

def create_plt(stock_data, ticker):
    stats = get_stats(stock_data)
    
    #choose style
    plt.style.use('default')
    #plt.style.use('dark_background')
    #plt.style.use('fivethirtyeight')
    #plt.style.use('ggplot')
    
    #for other styles look here https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html
    
    plt.subplots(figsize=(12,8))
    plt.plot(stock_data, label=ticker)
    plt.plot(stats['short_rolling'], label='short rolling mean - 20 days')
    plt.plot(stats['long_rolling'], label='long rolling mean - 200 days')
    plt.xlabel('Date')
    plt.ylabel('stck price')
    plt.title('stock Pricer over time')
    plt.legend()
    
    plt.show()
    
def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker, 'yahoo', START_DATE,END_DATE)
        adj_close = clean_data(stock_data, 'Adj Close')
        create_plt(adj_close, ticker)
        
    except RemoteDataError:
        print('No datya found for {t}'.format(t=ticker))
        
get_data(UK_STOCK)
    
    
    
