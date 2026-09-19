import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def get_digit_data():
    # 加载数据集
    dataset = pd.read_csv('../data/train.csv')
    x=dataset.drop('label',axis=1)
    y=dataset['label']

    train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.2,random_state=7)

    # 归一化
    scaler = MinMaxScaler()
    train_x = scaler.fit_transform(train_x)
    test_x = scaler.transform(test_x)

    train_x = torch.from_numpy(train_x).float()
    test_x = torch.from_numpy(test_x).float()
    train_y = torch.from_numpy(train_y.to_numpy()).long()
    test_y = torch.from_numpy(test_y.to_numpy()).long()

    return train_x,train_y,test_x,test_y
