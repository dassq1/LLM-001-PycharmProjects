"""
@Author:xuyinglai
@Date:2026/9/8
@DESC:
"""
from pathlib import Path

import pandas as pd
import torch
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset,DataLoader
import config

class TranslationDataset(Dataset):
    def __init__(self,file_path:Path):

        self.data= pd.read_json(str(file_path),orient='records',lines=True).to_dict(orient='records')

    def __len__(self):

        return len(self.data)# 数据集一共多少条数据





    def __getitem__(self,index):

       # 根据索引拿到数

        item=self.data[index]
        encoder_input =torch.tensor( item['zh'],dtype=torch.long)
        decoder_input =torch.tensor( item['en'][:-1],dtype=torch.long)
        label=torch.tensor( item['en'][1:],dtype=torch.long)
        return encoder_input,decoder_input,label

def get_dataset(train:bool=True):
    data_file= config.DATA_PATH /'processed'/ ( 'train.json' if train else  'test.json')
    return TranslationDataset(data_file)


def collect_fn(batch):
    # pad
    encoder_inputs=[item[0] for item in batch]
    decoder_inputs=[item[1] for item in batch]
    labels=[item[2] for item in batch]
    encoder_inputs_tensor=pad_sequence(encoder_inputs,batch_first=True,padding_value=0) #[batch_size,src_len]
    decoder_inputs_tensor=pad_sequence(decoder_inputs,batch_first=True,padding_value=0) #[batch_size,tgt_len]
    labels_tensor=pad_sequence(labels,batch_first=True,padding_value=0) #[batch_size,tgt_len]
    return encoder_inputs_tensor,decoder_inputs_tensor,labels_tensor
def get_dataloader(train:bool=True):
    dataset=get_dataset(train)
    return DataLoader(
        dataset,batch_size=config.BATCH_SIZE,shuffle=True,num_workers=0,
        collate_fn=collect_fn)



if __name__=='__main__':
    dataloader=get_dataloader()
    for encoder_inputs,decoder_inputs,labels in dataloader:
        # print(encoder_inputs)
        # print(decoder_inputs)
        # print(labels )
        print(encoder_inputs.shape)
        # print(decoder_inputs.shape)
        # print(labels.shape)
