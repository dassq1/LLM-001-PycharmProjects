"""
@Author:xuyinglai
@Date:2026/9/16
@DESC:
"""
import os
os.environ['HF_ENDPOINT']='https://hf-mirror.com'
import time
from torch.utils.tensorboard import SummaryWriter

from tqdm import tqdm

from src.config import LR, LOGS_PATH, MODELS_PATH, EPOCHS, SAVE_STEPS
from src.dataset import get_dataloader
from transformers import get_linear_schedule_with_warmup



import torch
from transformers import AutoModelForSequenceClassification


current_step=1
total_loss=0
best_loss=float('inf') #极大值
def train_one_epoch(model,dataloader,optimizer,scheduler,device,writer):
    global current_step
    global total_loss
    global best_loss
    # total_loss=0 不能放在这里，因为不一定是整倍数
    # model=train()
    for batch in tqdm(dataloader):
        inputs={k:v.to(device) for k,v in batch.items()}
        outputs=model(**inputs)
        loss=outputs.loss
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)# 裁剪
        optimizer.step()
        scheduler.step()# 更新学习率
        optimizer.zero_grad()
        total_loss+=loss.item()
        if current_step %SAVE_STEPS==0:
            avg_loss=total_loss/SAVE_STEPS
            writer.add_scalar('loss',avg_loss,current_step)

            if avg_loss < best_loss:
                best_loss=avg_loss
                model.save_pretrained(str(MODELS_PATH))


            total_loss=0
        current_step+=1

def train():
    # 设备
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(device)

    # 模型
    model = AutoModelForSequenceClassification.from_pretrained("google-bert/bert-base-chinese",num_labels=2).to(device)

    # 数据
    dataloader=get_dataloader()
    # 优化器
    optimizer=torch.optim.AdamW(model.parameters(),lr=LR)
    # 计算总训练步数
    total_steps = len(dataloader) * EPOCHS
    warmup_steps = int(0.1 * total_steps)  # 10% 的步数用于预热

    # 创建 scheduler
    scheduler = get_linear_schedule_with_warmup(
        optimizer,
        num_warmup_steps=warmup_steps,
        num_training_steps=total_steps
    )
    # writer
    writer=SummaryWriter(LOGS_PATH/time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime()))
    for epoch in range(1,1+EPOCHS):
        print(f'#############Epoch{epoch}/{EPOCHS}#################')
        train_one_epoch(model,dataloader,optimizer,scheduler,device,writer) #实参
if __name__ == '__main__':
    train()


