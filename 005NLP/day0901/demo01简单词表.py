"""
@Author:xuyinglai
@Date:2026/9/1
@DESC:
"""
import torch
vocab={
    '我':0,
    '喜欢':1,
    '学习':2,
    '人工智能':3
       }
tokens=['我','喜欢','学习','人工智能']
token_id=[vocab[token] for token in tokens]
print(token_id)
for x in tokens:
    print(x)






import torch
import torch.nn as nn
embedding=nn.Embedding(
    4,5)
print(embedding.weight)
print(embedding.weight.shape)
print(embedding)
print('*'*100)
token_ids=torch.tensor([0,1,2,3])
vector=embedding(token_ids)
print(vector)
print(vector.shape)
print('*'*100)
token_ids = torch.tensor([15, 28, 999])
print(token_ids.shape)
print('*'*100)
sentences = [
    ["我", "喜欢", "苹果"],
    ["我", "喜欢", "香蕉"],
    ["我", "吃", "苹果"],
    ["我", "吃", "香蕉"],
]
vocab = {
    "我": 0,
    "喜欢": 1,
    "苹果": 2,
    "香蕉": 3,
    "吃": 4
}
# todo 构建skip-gram 训练模型
# from gensim.models import KeyedVectors
# kv=KeyedVectors.load_word2vec_format('data/sg',binary=True)
