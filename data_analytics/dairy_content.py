import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("../data/recipes.csv")



dairy_comp = dataset.groupby(["dairy free"])["title"].count()
plt.figure(figsize=(10,10))
plt.pie(dairy_comp,labels=["Dairy","Dairy-Free"],autopct='%1.1f%%', startangle=90, colors=["blue","white"])
plt.axis("equal")

print(dairy_comp)