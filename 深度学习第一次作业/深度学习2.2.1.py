import os

os.makedirs(os.path.join('..', 'data'), exist_ok=True)
data_file = os.path.join('..', 'data', 'shenduxuexi.csv')
with open(data_file, 'w') as f:
    f.write('x1,x2,x3,x4,x5\n')  # 列名
    f.write('NA,143,127,5,13\n')  # 每行表示一个数据样本
    f.write('2,NA,106,3,11\n')
    f.write('4,NA,178,4,12\n')
    f.write('NA,152,140,3,12\n')
    f.write('NA,124,NA,NA,13\n')

import pandas as pd

data = pd.read_csv(data_file)
print(data)
print("\n")

#删除缺失值最多的列
data = data.drop(columns=data.isna().sum(axis=0).idxmax())
print(data) 
print("\n")

inputs, outputs = data.iloc[:, 0:3], data.iloc[:, 3]
#将data分成inputs和outputs，其中前者为data剩余的前三列，而后者为data的最后一列。
inputs = inputs.fillna(inputs.mean())
print(inputs)
#用同一列的均值替换“NaN”项
print("\n")

#转换为张量格式
import torch
X, y = torch.tensor(inputs.values), torch.tensor(outputs.values)
print(X,y)
print("\n")

