"""
@Author:xuyinglai
@Date:2026/9/16
@DESC:
"""
import os

os.environ['HF_ENDPOINT']='https://hf-mirror.com'
from datasets import load_from_disk
from torch.utils.data import DataLoader
from transformers import DataCollatorWithPadding, AutoTokenizer
# ✅ 标准写法
from src.config import DATA_PATH, BATCH_SIZE


def get_dataset(train:bool=True):
    data_path=DATA_PATH/'processed'/('train' if train else 'test')

    return load_from_disk(str(data_path))


tokenizer=AutoTokenizer.from_pretrained("google-bert/bert-base-chinese")
collate_fn=DataCollatorWithPadding(tokenizer=tokenizer,return_tensors='pt',padding=True)


def get_dataloader(train:bool=True):
    dataset=get_dataset(train)
    dataset.set_format(type='torch')# 原地修改
    return DataLoader(dataset,batch_size=BATCH_SIZE,shuffle=train,collate_fn=collate_fn)

if __name__ == '__main__':
    dataloader=get_dataloader()# 返回字典
    for batch in dataloader:
        for k,v in batch.items():
            print(k,v.shape)
        break


