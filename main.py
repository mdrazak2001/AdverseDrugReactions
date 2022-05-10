import numpy as np
import pandas as pd
def pattern(n):
    for i in range(1, n):
        for j in range(1, i + 1):
            print(j, end=" ")
        print('\n')

def Numpy():
    a = np.array([1, 2, 3, 4, 5]) 
    b = np.array([5, 4, 3, 2, 1])
    res = (a + b)
    res = np.square(res)
    print(res) 

def Dataset1():
    df = pd.read_csv ('Dataset- Qn 6.csv')
    print("First 6 Rows")
    print(df.head(6))
    print("Last 6 Rows")
    print(df.tail(6))

    mn_price = df['price'].idxmin()
    print(df['company'][mn_price])
    print(df['company'].value_counts())
    print(df.sort_values(by='price', ascending = False))

def Dataset2():
    df = pd.read_csv ('DatSet- Qn 7.csv')
    print(df.head())

# pattern(6)
# Numpy()
# Dataset1()
Dataset2()
