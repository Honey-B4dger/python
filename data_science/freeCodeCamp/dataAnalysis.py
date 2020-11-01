# https://www.youtube.com/watch?v=r-uOLxNrNk8

"""
Extraction, Cleaning, Wrangling, Analysis, Action

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

def plot(dataField, column, kind, xlabel, ylabel):
    dataField[column].plot(kind = kind)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

sales = pd.read_csv('data/sales_data.csv', parse_dates = ['Date'])

pd.set_option('display.max_columns', None)

print(f"The type of sales is: {type(sales)}")
print(f"The shape of sales is: {sales.shape}")

#print('What follows is the header.')
#print(sales.head(1))

print(f"Customer_Age_mean is: {sales['Customer_Age'].mean()}")
print(sales.info())
print(sales['Revenue'].describe())

"""
sales['Customer_Age'].plot(kind = 'kde', title = 'KDE')
plt.xlabel('Customer_Age')
plt.show()
plot(sales, 'Customer_Age', 'kde', 'x', 'Customer_Age')
plot(sales, 'Order_Quantity', 'kde', 'x', 'Order_Quantity')
"""
