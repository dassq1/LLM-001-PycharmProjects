import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
import torch.nn as nn
import matplotlib.pyplot as plt

x = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0]
])

y = torch.tensor([
    [5.0],
    [8.0],
    [11.0],
    [14.0]
])

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

weight_history = []
loss_history = []

for epoch in range(40):
    optimizer.zero_grad()
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    loss.backward()
    optimizer.step()
    weight_history.append(model.weight.item())
    loss_history.append(loss.item())


# ========== 1行2列，左右分布 ==========
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# 左图：weight变化
ax1.plot(weight_history)
ax1.axhline(3, linestyle="--", color="red")
ax1.set_xlabel("Epoch")
ax1.set_ylabel("Weight")
ax1.set_title("Weight Updating")

# 右图：loss变化
ax2.plot(loss_history)
ax2.set_xlabel("Epoch")
ax2.set_ylabel("Loss")
ax2.set_title("Loss Decreasing")

plt.tight_layout()   # 自动调整子图间距，防止文字重叠
plt.show()
