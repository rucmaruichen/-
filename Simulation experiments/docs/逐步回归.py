import pandas as pd
import numpy as np
data = np.zeros(500)
df = pd.DataFrame(data) # 将列表数据转化为 一列
# df.iloc[1,[0]]=1
# print(df.iloc[1,[0]])
with open('逐步回归_weights.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n').strip(' ')      #去除文本中的换行符
        data = line.split(' ')
        data = list(filter(None, data))
        index = int(data[0].split('V')[1])
        value = float(data[1])
        df.iloc[index-1,[0]]=value
df.to_csv('逐步回归_weights.csv')