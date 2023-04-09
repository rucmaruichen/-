import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path1 = 'LassoNet_weight.csv'
path2 = 'RF_weight.csv'
path3 = '逐步回归_weights.csv'
data = pd.read_csv(path3,names=["权重"])
data = np.array(data)
data = np.pad(data,((0,29),(0,0)),'constant')
data = data.reshape(23,23)
data = np.abs(data)
sns.heatmap(data=data,square=True,cbar=False,
            cmap='gray',yticklabels=False,xticklabels=False)
plt.show()