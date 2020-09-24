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

# Data Aggregations on closing price
df['Avg_5'] = df['Close'].rolling( window = 5, center = False).mean()
df['Avg_30'] = df['Close'].rolling( window = 30, center = False).mean()
df['Avg_365'] = df['Close'].rolling( window = 365, center = False).mean()

df['Std_5'] = df['Close'].rolling( window = 5, center = False).std()
df['Std_365'] = df['Close'].rolling( window = 365, center = False).std()
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

model = LinearRegression()
features = ['Avg_5', 'Avg_30', 'Avg_365', 'Std_5', 'Std_365', 'Avg_5/365', 'Std_5/365']
target = ['Close']
X = df_train[features]
X_test = df_test[features]
y = df_train[target]
y_test = df_test[target]

model.fit(X, y)
print("Coef: ", model.coef_)
print("Intercept: ", model.intercept_)
y_pred = model.predict(X_test)

mae = mean_absolute_error( y_test, y_pred)
mse = mean_squared_error( y_test, y_pred)

print("MAE: ", mae)
print("MSE: ", mse)
print("RMSE: ", np.sqrt(mse))
print("Score: ", model.score(X, y))

fig, ax = plt.subplots( figsize=( 8, 6))
plt.plot( df_test['Date'], y_pred, label = 'Predictions')
plt.plot( df_test['Date'], df_test['Close'], label = 'Real Data')

plt.xlabel('Date'), plt.ylabel('Price')
ax.tick_params( left = False, right = False, top = False, bottom = False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.xticks( rotation = 45)

plt.legend()
plt.show()