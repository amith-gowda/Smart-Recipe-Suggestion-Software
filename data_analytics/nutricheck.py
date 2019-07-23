import pandas as pd

#import csv using pandas
dataset = pd.read_csv("../data/recipes.csv")

ing = list()
while(1):
    get = input("Enter an ingredient: ")
    inp = get.strip()
    if (inp == 'done'):
        break
    else:
        temp = inp.lower()
        ing.append(temp)
    
print("\n----------------------------\n\nEntered ingredients are:")
print(ing)

for item in ing()
    for i, j in dataset.iterrows(): 
        if (i == item):
            print("here")
        else:
            print("not here")