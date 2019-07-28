import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns


data = pd.read_csv("../data/recipes.csv")

trunc = ['low_cholesterol','calories','fat','protein']

nd = data[trunc]

dat = nd[nd.calories <= 1500]

lc = nd[nd.low_cholesterol == 1]
hc = nd[nd.low_cholesterol == 0]

fig = plt.figure()
fig.suptitle('High vs Low Cholestrol effects on calories and fat')
graph1 = fig.add_subplot(1,2,1)
graph1.scatter(lc['calories'], lc['fat'])
graph2 = fig.add_subplot(1,2,2)
graph2.scatter(hc['calories'], hc['fat'])


plt.show()
