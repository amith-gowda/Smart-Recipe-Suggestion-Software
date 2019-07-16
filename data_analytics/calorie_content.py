"""
Created on Tue Jul 16 11:48:46 2019

@author: Amith
"""


import json
import numpy as np
import pandas as pd

#import csv
dataset = pd.read_csv("../data/recipes.csv")

#create an empty list to store the fat content of the recipes
cals = list()
count_yes = 0
count_no = 0

print(dataset.head(10))


