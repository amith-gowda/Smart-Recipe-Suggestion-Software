import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("../data/recipes.csv")





fruit = ["Apple","Apricot","Avocado","Banana","Bilberry","Blackberry","Blackcurrant","Blueberry","Boysenberry","Currant","Cherry","Cherimoya","Cloudberry","Coconut","Cranberry","Cucumber","Custard apple","Damson","Date","Dragonfruit","Durian","Elderberry","Feijoa","Fig","Goji berry","Gooseberry","Grape","Raisin","Grapefruit","Guava","Honeyberry","Huckleberry","Jabuticaba","Jackfruit","Jambul","Jujube","Juniper berry","Kiwifruit","Kumquat","Lemon","Lime","Loquat","Longan","Lychee","Mango","Marionberry","Melon","Cantaloupe","Honeydew","Watermelon","Miracle fruit","Mulberry","Nectarine","Nance","Olive","Orange","Blood orange","Clementine","Mandarine","Tangerine","Papaya","Passionfruit","Peach","Pear","Persimmon","Physalis","Plantain","Plum","Prune (dried plum)","Pineapple","Plumcot (or Pluot)","Pomegranate","Pomelo","Purple mangosteen","Quince","Raspberry","Salmonberry","Rambutan","Redcurrant","Salal berry","Salak","Satsuma","Star fruit","Strawberry","Tamarillo","Tamarind","Tomato","Ugli fruit","Yuzu"]
fruit = [x.lower() for x in fruit]
dd =dataset[dataset.vegetarian==0 ][list(set(fruit).intersection(dataset.columns.tolist()))].sum(axis=0).sort_values(ascending=False)
dx = dd[:20]
dx["others"]= dd[20:].sum()
plt.figure(figsize=(6,6))
plt.pie(dx,labels=dx.index,autopct='%1.1f%%', startangle=90)
plt.axis("equal")
plt.title("Composistion of usage of Fruits in recipes", y =1.08)