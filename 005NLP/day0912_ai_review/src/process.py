"""
@Author:xuyinglai
@Date:2026/9/16
@DESC:
"""
import os
os.environ['HF_ENDPOINT']='https://hf-mirror.com'

from datasets import load_dataset
from torch.utils.data import dataset
from transformers import AutoTokenizer

from src.config import DATA_PATH


def process():
    # 读文件
    dataset=load_dataset('csv',data_files=str(DATA_PATH/'raw'/'online_shopping_10_cats.csv'))['train']
    # 过滤数据
    dataset=dataset.remove_columns(['cat'])
    dataset=dataset.filter(lambda x:x['review'] is not None )
    # 划分数据集
    dataset_dict=dataset.train_test_split(test_size=0.2)
    # 处理数据
    tokenizer=AutoTokenizer.from_pretrained("google-bert/bert-base-chinese")
    def map_function(batch):
        return tokenizer(batch['review'],padding=False,truncation=True)

    dataset_dict=dataset_dict.map(function=map_function, batched=True, remove_columns=['review'])
    dataset_dict.rename_column(original_column_name='label',new_column_name='labels') # 原地修改
    # 保存处理好的数据集
    dataset_dict.save_to_disk(str(DATA_PATH/'processed'))


if __name__ == '__main__':
    process()