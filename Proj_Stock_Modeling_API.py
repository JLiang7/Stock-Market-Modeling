# Import libraries
import pandas as pd
import numpy as np
import time
from pandas_datareader import data, wb
from datetime import datetime
import matplotlib.pyplot as plt

# Setting the Date
start = pd.to_datetime('2020-09-01')
end = pd.to_datetime('today')

# Pandas DataReader API (Quandl, Google, Yahoo, AlphaVantage, sooq ...)
Tickers = ['AAPL'] # ,'TSLA', 'MSFT', 'QQQ', 'AMZN', 'SPY'
stock_df = data.DataReader(Tickers, 'yahoo', start, end)
print(stock_df.head(10))

# 


# Data Aggregations on closing price


# Splitting Data to Training and Test sets
 

# Importing Models
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


# Plot the adjusted close price
stock_df['Adj Close'].plot( figsize = ( 10, 7))
# Define the label for the title of the figure
plt.title( "Adjusted Close Price of %s" % Tickers, fontsize = 18)
# Define the labels for x-axis and y-axis
plt.ylabel( 'Price', fontsize = 20)
plt.xlabel( 'Year', fontsize = 20)
# Plot the grid lines
plt.grid( which="major", color = 'k', linestyle = '-.', linewidth = 0.5)
# Show the plot
plt.show()