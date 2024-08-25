# -*- coding: utf-8 -*-
"""MeanReverse.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13x7cx7d5wF-DWMzQre5av8WSyy-UygVm
"""

#Yahoo finance to DL closing prices
!pip install yfinance
!pip install hurst

from google.colab import drive



!pip install arch

import yfinance as yf
import numpy as np
from hurst import compute_Hc

# Download USD/CAD exchange rate data for the last 5 years
data = yf.download('CAD=X', start='2019-01-01', end='2024-01-01', interval='1d')

# Extract the 'Adj Close' column (adjusted closing prices)
y = data['Adj Close'].values

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(data.index, y, label='USD/CAD Exchange Rate')
plt.title('USD/CAD Exchange Rate over the Last 5 Years')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.grid(True)
plt.legend()
plt.show()

import numpy as np
import statsmodels.tsa.stattools as ts

# Example time series data
y = data['Adj Close'].sort_index(ascending=True).values

# Perform the Augmented Dickey-Fuller test
# 'maxlag=0' corresponds to the MATLAB's '0' lag and 'regression="c"' corresponds to the constant (like MATLAB's '1')
results = ts.adfuller(y, maxlag=1, regression='c')

# Print the results
print('ADF Statistic:', results)

log_y = np.log(y)

# Calculate the Hurst exponent
H, c, data_reg = compute_Hc(log_y, kind='price', simplified=True)

# Print the Hurst exponent
print(f"Hurst exponent (H): {H}")

from arch.unitroot import VarianceRatio

vr_test = VarianceRatio(log_y, lags=2)
h = vr_test.stat
pValue = vr_test.pvalue

# Print the results
print(f"Variance Ratio Test Statistic (h): {h}")
print(f"P-Value: {pValue}")

