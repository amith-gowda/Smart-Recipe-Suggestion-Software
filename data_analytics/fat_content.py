"""
Created on Tue Jul 16 11:23:19 2019

@author: Amith
"""


import json

#create an empty list to store the fat content of the recipes
fatness = list()
count_yes = 0
count_no = 0


#open json file
with open('../data/rec.json') as json_file:  
    dataset = json.load(json_file)
    for recipe in dataset:
        try:
            fatness.append(recipe['fat'])
        except:
            continue
        
    for i in fatness:
        if (i == 'none'):
            count_no += 1
        else:
            count_yes += 1
            
    print(fatness)