# @Author:xuyinglai @Date:2026/8/31 @DESC:
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# 生成一个 batch
x = torch.randn(100, 1) * 10 + 50

bn = nn.BatchNorm1d(1)

# 训练模式
bn.train()

y = bn(x)

print("BatchNorm前：")
print("mean =", x.mean().item())
print("std  =", x.std().item())

print("\nBatchNorm后：")
print("mean =", y.mean().item())
print("std  =", y.std().item())

# 可视化
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(x.detach().numpy(), bins=20)
plt.title("Before BatchNorm")

plt.subplot(1, 2, 2)
plt.hist(y.detach().numpy(), bins=20)
plt.title("After BatchNorm")

plt.tight_layout()
plt.show()