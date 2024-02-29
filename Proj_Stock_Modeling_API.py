# For the sake of showcase, to hide warnings
import warnings
warnings.filterwarnings('ignore')

# Import libraries
import pandas as pd
import numpy as np
import time
from pandas_datareader import data as pdr
from datetime import datetime
import matplotlib.pyplot as plt

#New change to yahoo API
import yfinance as yf 
yf.pdr_override()

# Setting the Date
start = pd.to_datetime('2020-09-01')
end = pd.to_datetime('today')

# Pandas DataReader API (Quandl, Google, Yahoo, AlphaVantage, sooq ...)
Tickers = ['AAPL'] # ,'TSLA', 'MSFT', 'QQQ', 'AMZN', 'SPY'
Stock_df = pdr.get_data_yahoo(Tickers, start, end) #Previously data.DataReader(Tickers, 'yahoo', start, end)
print(Stock_df.head(10))

# 


# Data Aggregations on adjusted closing price
Stock_df['Avg_5'] = Stock_df['Adj Close'].rolling( window = 5, center = False).mean()
Stock_df['Avg_30'] = Stock_df['Adj Close'].rolling( window = 30, center = False).mean()
Stock_df['Avg_365'] = Stock_df['Adj Close'].rolling( window = 365, center = False).mean()
Stock_df['Std_5'] = Stock_df['Adj Close'].rolling( window = 5, center = False).std()
Stock_df['Std_30'] = Stock_df['Adj Close'].rolling( window = 365, center = False).std()
Stock_df['Std_365'] = Stock_df['Adj Close'].rolling( window = 365, center = False).std()
Stock_df['Avg_5/365'] = Stock_df['Avg_5']/Stock_df['Avg_365']
Stock_df['Std_5/365'] = Stock_df['Std_5']/Stock_df['Std_365']

Stock_df = Stock_df.shift( periods = 1)
Stock_df.dropna( how= 'any', axis = 0, inplace = True)

Stock_df.head()


# Splitting Data to Training and Test sets
 

# Importing Models
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


# Plot the adjusted close price
Stock_df['Adj Close'].plot( figsize = ( 10, 7))
# Define the label for the title of the figure
plt.title( "Adjusted Close Price of %s" % Tickers, fontsize = 18)
# Define the labels for x-axis and y-axis
plt.ylabel( 'Price', fontsize = 20)
plt.xlabel( 'Year', fontsize = 20)
# Plot the grid lines
plt.grid( which="major", color = 'k', linestyle = '-.', linewidth = 0.5)
# Show the plot
plt.show()