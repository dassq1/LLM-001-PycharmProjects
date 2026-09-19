# 必须放在所有import最最前面，解决OMP报错
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
import matplotlib.pyplot as plt

model = torch.nn.Linear(10, 2)

optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=0.001
)

scheduler = torch.optim.lr_scheduler.StepLR(
    optimizer,
    step_size=10,
    gamma=0.1
)

lrs = []

for epoch in range(40):
    # 1. 先记录当前epoch使用的学习率（本轮训练要用的lr）
    lrs.append(optimizer.param_groups[0]["lr"])

    # ----------------模拟训练过程----------------
    # 真实项目这里要跑dataloader循环：zero_grad→loss.backward()→optimizer.step()
    # 本demo没有训练数据，为消除警告，手动调用一次optimizer.step()（无梯度，仅满足API顺序）
    optimizer.step()
    # -------------------------------------------

    # ✅规则：optimizer.step()之后，再执行scheduler.step()更新下一轮的学习率
    scheduler.step()

plt.figure(figsize=(8, 4))
plt.plot(range(40), lrs, marker="o")
plt.xlabel("Epoch")
plt.ylabel("Learning Rate")
plt.title("StepLR Learning Rate")
plt.show()
