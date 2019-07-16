"""
Created on Tue Jul 16 11:43:21 2019

@author: Amith
"""


import json

#create an empty list to store the fat content of the recipes
sodiums = list()
count_yes = 0
count_no = 0


#open json file
with open('../data/rec.json') as json_file:  
    dataset = json.load(json_file)
    for recipe in dataset:
        try:
            sodiums.append(recipe['sodium'])
        except:
            continue
        
    print(sodiums)
  