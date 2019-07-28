import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("../data/recipes.csv")

nutrients = [['fat', 'protein'],['fat','calories']]   


dairy_comp = data.groupby(["dairy free"])["title"].count()
plt.figure(figsize=(5,5))
plt.pie(dairy_comp,labels=["Dairy","Dairy-Free"],autopct='%1.1f%%', startangle=90, colors=["blue","white"])
plt.axis("equal")

print(dairy_comp)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              



fig, ax = plt.subplots(6, 2, sharex=True, sharey=True, figsize = (8, 20))
plt.suptitle('Dairy v Dairy-Free', fontsize = 25, fontweight='bold', y = 0.95)

counter_x = 0
counter_y = 0

scaler = MinMaxScaler()

for i in nutrients:
    temp = data[data['dairy'] == 1].copy()
    temp = temp[i]
    temp = temp.dropna()
    x_scaled = scaler.fit_transform(temp[i[0]].values.reshape(-1, 1))
    y_scaled = scaler.fit_transform(temp[i[1]].values.reshape(-1, 1))

    ax[counter_x, counter_y].scatter(x_scaled,
                                     y_scaled,
                                     color = 'skyblue',
                                     s = 50,
                                    alpha = 0.25,
                                    label = 'dairy')
    ax[counter_x, counter_y].set_xlabel(i[0].title())
    ax[counter_x, counter_y].set_ylabel(i[1].title())
    current_title = " v ".join([i[0].title(), i[1].title()])
    ax[counter_x, counter_y].set_title(current_title)
    ax[counter_x, counter_y].legend()
    
    counter_x += 1


counter_y = 1
counter_x = 0


for i in nutrients:
    temp = data[data['dairy free'] == 1].copy()
    temp = temp.dropna()
    temp = temp[i]
    x_scaled = scaler.fit_transform(temp[i[0]].values.reshape(-1, 1))
    y_scaled = scaler.fit_transform(temp[i[1]].values.reshape(-1, 1))

    ax[counter_x, counter_y].scatter(x_scaled,
                                     y_scaled,
                                     color = 'blue',
                                     s = 50,
                                    alpha = 0.25,
                                    label = 'dairy-free')
    ax[counter_x, counter_y].set_xlabel(i[0].title())
    ax[counter_x, counter_y].set_ylabel(i[1].title())
    current_title = " v ".join([i[0].title(), i[1].title()])
    ax[counter_x, counter_y].set_title(current_title)
    ax[counter_x, counter_y].legend()
    counter_x += 1