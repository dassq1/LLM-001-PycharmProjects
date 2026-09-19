"""
@Author:xuyinglai
@Date:2026/8/26
@DESC:
"""
import torch
import torch.nn as nn
from load_data import get_digit_data

# 加载数据
train_x,train_y,test_x,test_y = get_digit_data()

model = nn.Sequential(
    nn.Linear(784,50),
    nn.ReLU(),
    nn.Linear(50,100),
    nn.ReLU(),
    nn.Linear(100,10),
    )
    # 无需手动添加softmax()

# 加载训练好的参数
state_dict=torch.load('../data/nn_example.pt', map_location='cpu')
model.load_state_dict(state_dict)
# 前向传播
y_pred=model(test_x)
print("模型输出logits 原始得分:\n",y_pred)
print(y_pred.shape)

# 提取预测类别
y_pred_class=torch.argmax(y_pred,dim=1)
print('预测类别',y_pred_class)

# 计算准确率
acc_cnt=torch.sum(y_pred_class==test_y).item()
acc=acc_cnt/len(y_pred_class)
print("测试集准确率",acc)

