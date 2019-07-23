"""
Created on Tue Jul 16 11:48:46 2019

@author: Amith
"""

#init
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

count = 0

#import csv
dataset = pd.read_csv("../data/recipes.csv")
total_cal = 0
count = 0


#this is for debug only
short_db = dataset.head(10)
short_cols = list(short_db)
trunc = ['title','dairy']
nd = short_db[trunc]
dairy_dataset = dataset[trunc]
#print(nd)
#nd.fillna('', inplace = True)

temp = dairy_dataset[dairy_dataset['dairy'] == 1].copy()

for i in temp.iterrows():
    count += 1
    
print(count)
