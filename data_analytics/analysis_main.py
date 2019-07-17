"""
Created on Tue Jul 16 11:48:46 2019

@author: Amith
"""

#init
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
count = 0

#import csv
dataset = pd.read_csv("../data/recipes.csv")


#truncate uneccesary columns
keep_col = ['title','calories']
new_dataset = dataset[keep_col]

#this is for debug only
short_db = new_dataset.head(10)
short_cols = list(short_db)


