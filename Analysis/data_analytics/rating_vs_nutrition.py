import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

data = pd.read_csv("../data/recipes.csv")

recipes = data.iloc[:,:10]

cal_clean = recipes.loc[recipes['calories'].notnull()]

q1  = cal_clean['calories'].quantile(.25)
q3  = cal_clean['calories'].quantile(.75)
iqr = q3 - q1

for i in recipes.columns[1:6]:
    recipes[i].fillna(cal_clean.loc[(cal_clean['calories'] > q1) & (recipes['calories'] < q3)][i].mean(), inplace=True)
    
recipes = recipes.loc[(recipes['calories'] > q1-(iqr*3)) & (recipes['calories'] < q3+(iqr*3))]

dict_plt = {0:'calories',1:'protein',2:'fat',3:'sodium'}

sns.set(font_scale=.7)

fig, ax = plt.subplots(1,4, figsize=(10,5))


for i in range(4):
    sns.barplot(x='rating',y=dict_plt[i], data=recipes, ax=ax[i], errwidth=1)
    ax[i].set_title('rating by {}'.format(dict_plt[i]), size=15)
    ax[i].set_ylabel('')
    
plt.savefig('rating_vs_nutrition.png')