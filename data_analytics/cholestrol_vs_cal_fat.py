import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns


data = pd.read_csv("../data/recipes.csv")

trunc = ['low_cholesterol','calories','fat','protein']

cals = ['title','calories']

nd = data[cals]

#lc = nd[nd.low_cholesterol == 1]
#hc = nd[nd.low_cholesterol == 0]

dat = nd[nd.calories >= 1500]
print(dat)


#fig = plt.figure()
#graph1 = fig.add_subplot(1,2,1)
#graph1.scatter(lc['calories'], lc['fat'])
#graph2 = fig.add_subplot(1,2,2)
#graph2.scatter(hc['calories'], hc['fat'])
#
#plt.show()