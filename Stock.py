# Import libraries
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# Importing and reading the data
df = pd.read_csv('sphist.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values( by=['Date'], ascending=True, inplace=True)
df.reset_index( drop=True, inplace=True)

df.head(2)

# Data Aggregations on closing price
df['Avg_5'] = df['Close'].rolling(window=5, center=False).mean()
df['Avg_30'] = df['Close'].rolling(window=30, center=False).mean()
df['Avg_365'] = df['Close'].rolling(window=365, center=False).mean()

df['Std_5'] = df['Close'].rolling(window=5, center=False).std()
df['Std_365'] = df['Close'].rolling(window=365, center=False).std()
#df['Std_5'] = df['Close'].rolling(window = 5, min_periods = 5).apply( lambda x: np.std(x))
df['Avg_5/365'] = df['Avg_5']/df['Avg_365']
df['Std_5/365'] = df['Std_5']/df['Std_365']

df = df.shift( periods = 1)

# Remove Missing Values and Values not within a year
df_new = df[df['Date'] > datetime(year = 1951, month = 1, day = 2)]
df_new.dropna( how= 'any', axis = 0, inplace = True)

# Splitting Data to Training and Test sets
df_train = df_new[df_new['Date'] < datetime(year = 2013, month = 1, day = 1)]
df_test = df_new[df_new['Date'] >= datetime(year = 2013, month = 1, day = 1)]

# Linear Regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

