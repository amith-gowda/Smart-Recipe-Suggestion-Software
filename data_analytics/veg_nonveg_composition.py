#veg and non veg composition graph
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("../data/recipes.csv")


keep_col = ['title','vegetarian']
new_dataset = dataset[keep_col]

vnv_comp = dataset.groupby(["vegetarian"])["title"].count()
plt.figure(figsize=(4,4))
plt.pie(vnv_comp,labels=["Non-Vegetarian","Vegetarian"],autopct='%1.1f%%', startangle=90, colors=["red","lightgreen"])
plt.axis("equal")

print(vnv_comp)


"""
for i, j in new_dataset.iterrows(): 
    print(i, j) 
    print() """