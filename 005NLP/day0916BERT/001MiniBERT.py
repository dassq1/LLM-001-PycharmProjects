"""
@Author:xuyinglai
@Date:2026/9/16
@DESC:
"""
import torch
import torch.nn as nn
# 参数
vocab_size=1000
hidden_size=128
num_heads = 4
num_layers = 2
max_position_embeddings = 128

class MiniBERT(nn.Module):
    def __init__(self,):
        super().__init__()
        # token Embedding
        self.token_embeddings = nn.Embedding(vocab_size,
                                             hidden_size)
        # position Embedding
        self.pos_embeddings = nn.Embedding(max_position_embeddings, hidden_size)

        # Segment Embedding
        self.segment_embeddings = nn.Embedding(2, hidden_size)

        # Transformer Encoder layer
        encoder_layer = nn.TransformerEncoderLayer(d_model=hidden_size,nhead=num_heads,dim_feedforward=hidden_size*4,batch_first=True)

        # Transformer Encoder
        self.encoder = nn.TransformerEncoder(encoder_layer,num_layers=num_layers)

    def forward(self,input_ids,token_type_ids,attention_mask):
        token_emb=self.token_embeddings(input_ids)
        seq_len=input_ids.size(1)
        position_ids=torch.arange(seq_len,dtype=torch.long,device=input_ids.device).unsqueeze(0)
        position_emb=self.pos_embeddings(position_ids)
        segment_emb=self.segment_embeddings(token_type_ids)
        x=token_emb+position_emb+segment_emb
        src_key_padding_mask=attention_mask==0
        hidden_states=self.encoder(x,src_key_padding_mask=src_key_padding_mask)
        return hidden_states


input_ids = torch.tensor([
    [101, 10, 20, 30, 40, 102],
    [101, 10, 20, 102,  0,   0]
])
token_type_ids = torch.zeros_like(input_ids)
attention_mask = torch.tensor([
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0]
])

if __name__=="__main__":
    model = MiniBERT()
    hidden_states = model(
        input_ids,
        token_type_ids,
        attention_mask
    )
    print(hidden_states.shape)


