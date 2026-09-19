import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

# --------模拟数据集，如果你已有train_dataset就删掉这一段--------
X = torch.randn(1000, 10)
Y = torch.randint(0, 2, (1000,))
train_dataset = TensorDataset(X, Y)

# ✅实例化得到dataloader对象（小写d！！）
dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
# -----------------------------------------------------------

# 模型
model = nn.Sequential(
    nn.Linear(10, 32),
    nn.ReLU(),
    nn.Linear(32, 2)
)

# Loss
loss_fn = nn.CrossEntropyLoss()

# AdamW
optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=0.001,
    weight_decay=0.01
)

# 学习率调度器
scheduler = torch.optim.lr_scheduler.StepLR(
    optimizer,
    step_size=10,
    gamma=0.1
)

for epoch in range(30):
    model.train()
    total_loss = 0.0
    # ✅使用实例对象 dataloader，不是类名 DataLoader / Dataloader
    for x, y in dataloader:
        # 前向传播
        y_pred = model(x)
        # Loss
        loss = loss_fn(y_pred, y)
        # 清空梯度
        optimizer.zero_grad()
        # 反向传播
        loss.backward()
        # AdamW更新参数
        optimizer.step()

        total_loss += loss.item() * x.size(0)

    scheduler.step()
    avg_loss = total_loss / len(train_dataset)
    lr = optimizer.param_groups[0]["lr"]
    print(
        f"Epoch {epoch + 1:02d} | "
        f"Avg Loss = {avg_loss:.4f} | "
        f"LR = {lr:.6f}"
    )
