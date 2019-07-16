"""
Created on Tue Jul 16 11:46:07 2019

@author: Amith
"""


import json

#create an empty list to store the fat content of the recipes
proteins = list()
count_yes = 0
count_no = 0


#open json file
with open('../data/rec.json') as json_file:  
    dataset = json.load(json_file)
    for recipe in dataset:
        try:
            proteins.append(recipe['protein'])
        except:
            continue
        
    for i in proteins:
        if (i == 'none'):
            count_no += 1
        else:
            count_yes += 1

    print(proteins)