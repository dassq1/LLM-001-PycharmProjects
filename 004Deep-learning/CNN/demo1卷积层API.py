"""
@Author:xuyinglai
@Date:2026/8/31
@DESC:
"""
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
img=plt.imread("../data/duck.jpg")
# plt.imshow(img)
# plt.show()
print(img.shape) # (1080, 1080, 3)
# 转为张量，改变输入数据形状 卷积层要求：c w h
input = torch.tensor(img).permute(2,0,1).float()
print(input.shape) # torch.Size([3, 1080, 1080])
# 定义卷积层
conv = nn.Conv2d(
    in_channels=3, out_channels=3, kernel_size=3, stride=1, padding=1
)
# 前向传播
out=conv(input)
print(out.shape) # torch.Size([3, 1080, 1080])
# 转换输出图片格式
out_img=torch.clamp(out.int(),0,255)
# print(out_img.shape)
out_img=out_img.permute(1,2,0).detach().numpy()
# plt.imshow(out_img)
# plt.show()

# 显示图片
fig, ax = plt.subplots(1,2,figsize=(12,8))
ax[0].imshow(img)
ax[1].imshow(out_img)
plt.show()

