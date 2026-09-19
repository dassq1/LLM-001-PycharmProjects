"""
@Author:xuyinglai
@Date:2026/9/9
@DESC:
"""
import pandas as pd
dfjo=pd.DataFrame(
    dict(A=range(1,4),B=range(4,7),C=range(7,10)),
    columns=['A','B','C'],
    index=list('xyz'),
)
print(dfjo)
print(dfjo.to_json('test1.json', orient='records'))
print(dfjo.to_json('test2.json', orient='records', lines=True))

print(dfjo.to_dict(orient='records'))

