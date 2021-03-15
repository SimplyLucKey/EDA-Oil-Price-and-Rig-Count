# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:07:33 2020

@author: Will
"""

# import libraries
import pandas_datareader as pdr

# read data from Yahoo Finance
df_oil = pdr.DataReader('CL=F', data_source='yahoo', start='2001-01-01', end='2021-02-27').reset_index(drop=False)


# extract year from 'Date'
df_oil['year'] = df_oil['Date'].dt.year

# extract csv
for i in range(2000, 2022):
    df_oil.loc[df_oil['year'] == i].to_csv(f'df_{i}.csv')