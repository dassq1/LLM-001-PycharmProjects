"""
@Author:xuyinglai
@Date:2026/9/1
@DESC:
"""
from gensim.models import Word2Vec
import jieba
import pandas as pd
df=pd.read_csv('./data/online_shopping_10_cats.csv')
df.dropna(inplace=True)
print(df.shape)
sentences=[jieba.lcut(text) for text in df ['review']]
model=Word2Vec(
    sentences=sentences,
    vector_size=100,
    window=2,
    min_count=1,
    workers=4,
    sg=1,
)