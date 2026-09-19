import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import torch
import pandas as pd
import torch.nn as nn
import matplotlib.pyplot as plt
from torch.utils.data import TensorDataset, Dataset
from tqdm import tqdm   # ✅导入进度条tqdm，不是keras


# 读取数据
fashion_mnist_train = pd.read_csv(r'C:\Users\23716\Desktop\PycharmProjects\004Deep-learning\data\fashion-mnist_train.csv')
fashion_mnist_test=pd.read_csv(r'C:\Users\23716\Desktop\PycharmProjects\004Deep-learning\data\fashion-mnist_test.csv')
# 将数据转成张量 n*1*784-->n*1*28*28
x_train=torch.tensor(fashion_mnist_train.iloc[:,1:].values,dtype=torch.float32).reshape(-1,1,28,28)
y_train=torch.tensor(fashion_mnist_train.iloc[:,0].values,dtype=torch.int32)

x_test=torch.tensor(fashion_mnist_test.iloc[:,1:].values,dtype=torch.float32)
y_test=torch.tensor(fashion_mnist_test.iloc[:,0].values,dtype=torch.int32)

# plt.imshow(x_train[12345,0,:,:],cmap='gray')
# plt.show()
#todo 构建数据集
train_dataset = TensorDataset(x_train, y_train)
test_dataset = TensorDataset(x_test, y_test)

# todo 搭建模型
model=nn.Sequential(
    nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, stride=1, padding=2),
    nn.Sigmoid(),
    nn.AvgPool2d(kernel_size=2, stride=2),
    nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1, padding=0),
    nn.Sigmoid(),
    nn.AvgPool2d(kernel_size=2, stride=2),
    nn.Flatten(),
    nn.Linear(in_features=16*5*5, out_features=120),
    nn.Sigmoid(),
    nn.Linear(in_features=120, out_features=84),
    nn.Sigmoid(),
    nn.Linear(in_features=84, out_features=10),

)
#todo 查看形状
# x=torch.rand(size=(1,1,28,28),dtype=torch.float32)
# for layer in model:
#     x=layer(x)
#     print(f"layer: {layer}, shape: {x.shape}")

# todo 训练模型
def train(model,train_dataset,test_dataset,lr,epoch_num,batch_size,device):
    def init_weights(layer):
        # 对线性层和卷积层使用Xavier均匀分布，初始化参数
        if type(layer) == nn.Linear or type(layer) == nn.Conv2d:
            nn.init.xavier_uniform(layer.weight)
    model.apply(init_weights)
    model.to(device)
    loss=nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    for epoch in range(epoch_num):
        model.train() # 设置为训练模式
        train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True,)
        loss_accumulate=0,
        # for batch_count,(x,y) in enumerate(train_loader):
