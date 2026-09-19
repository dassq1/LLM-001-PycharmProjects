"""
@Author:xuyinglai
@Date:2026/9/8
@DESC:
"""
import math

import pandas as pd
import torch
import torch.nn as nn

from src.config import DIM_MODEL, NUM_HEADS, NUM_ENCODER_LAYERS, NUM_DECODER_LAYERS

class PositionalEncoding(nn.Module):
    def __init__(self,max_len=500):
        super().__init__()
        self.pe=torch.zeros(size=[max_len,DIM_MODEL],dtype=torch.float)
        for pos in range(max_len):
            for _2i in range(0,DIM_MODEL,2):
                self.pe[pos,_2i]=math.sin(pos/10000**(_2i/DIM_MODEL))
                self.pe[pos,_2i+1]=math.cos(pos/10000**(_2i/DIM_MODEL))
        self.register_buffer('pe',self.pe)

    def forward(self,embed): # embed.shape=[batch_size,seq_len,dim_model]
        seq_len=embed.shape[1]
        part_pe= self.pe[0:seq_len,:] # part_pe=[seq_len,dim_model]
        return embed+part_pe

class TraansLation(nn.Module):
    def __init__(self,zh_vocab_size,zh_padding_id,en_vocab_size,en_padding_id):
        super().__init__()
        self.transformer = nn.Transformer(
            d_model=DIM_MODEL,
            num_heads=NUM_HEADS,
            num_decoder_layers=NUM_DECODER_LAYERS,
            num_encoder_layers=NUM_ENCODER_LAYERS,
            dim_feedforward=4*DIM_MODEL,
            batch_first=True,
            dropout=0.1,
            activation="relu",
        )
        self.zh_embedding = nn.Embedding(num_embeddings=zh_vocab_size, embedding_dim=DIM_MODEL,padding_idx=0)
        self.enembedding = nn.Embedding(num_embeddings=en_vocab_size, embedding_dim=DIM_MODEL,padding_idx=0)
        self.position_encoding=None
        self.linear = nn.Linear(in_features=DIM_MODEL, out_features=en_vocab_size)
    def forward(self,x): # 只用作训练
        pass
    def encode(self,src,src_key_padding_mask):# 我自己定义的encode
        src_embed = self.zh_embedding(src)
        src_embed=self.position_encoding(src_embed)
        # todo
        memory=self.transformer.encoder(src=src_embed,src_key_padding_mask=src_key_padding_mask)
        return memory # [batch_size,src_len,dim_model]
    def decode(self,tgt,memory,tgt_mask,memory_key_padding_mask):
         tgt_embed= self.enembedding(tgt)
         tgt_embed= self.position_encoding(tgt_embed)
         hidden= self.transformer.encoder(
             tgt=tgt_embed,
             memory=memory,
             tgt_mask=tgt_mask,
             memory_key_padding_mask=memory_key_padding_mask,
         )
         output=self.linear(hidden)  #[batch_size,tgt_len,en_vocab_size]
         return output


