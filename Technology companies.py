# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:20:44 2024

@author: Computer
"""
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Company": ["Apple", "Google", "Microsoft", "Amazon", "Facebook"],
    "Revenue": [274.5, 182.5, 143.0, 386.1, 85.9],  # Revenue in billion USD
    "profit": [57.4, 40.3, 44.3, 21.3, 29.1],  # Profit in billion USD
    "Market_Cap": [2000, 1500, 1800, 1600, 800]  # Market cap in billion USD
}

df = pd.DataFrame(data)



print(df.describe())#Show descriptive statistics
print(df.info())#Show data information and check for missing values


#Analyze data to determine the relationship between profits and returns
df.plot(x='Revenue', y='profit', kind='scatter', title='Revenue vs Profit')
plt.show()

#Graphs
df.set_index('Company')['Market_Cap'].plot(kind='bar', title='Market Cap of Tech Companies')
plt.ylabel('Market Cap(in billion USD)')
plt.show()