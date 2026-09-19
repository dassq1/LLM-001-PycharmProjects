"""
@Author:xuyinglai
@Date:2026/9/1
@DESC:
"""
import jieba
text='小明毕业于北京大学计算机系'
text2='南京市长江大桥'
# todo 精确模式(默认)
print(jieba.cut(text))
for word in  jieba.cut(text):
    print(word)

for word in  jieba.cut(text2):
    print(word)

words=jieba.lcut(text)
print(words)
print('*'*100)
# todo 全模式
for word in  jieba.cut(text,cut_all=True):
    print(word)
print('*'*100)
words=jieba.lcut(text,cut_all=True)
print(words)
print('*'*100)
# todo 搜索引擎模式
# for word in  jieba.cut_for_search(text):
#     print(word)
words=jieba.lcut_for_search(text)
print(words)

# todo 自定义词典
print('*'*100)
text=('随着云计算技术的普及，'
      '越来越多企业开始采用云原生架构来部署服务，'
      '并借助大模型能力提升智能化水平，'
      '实现业务流程的自动化与智能决策。')
# print(jieba.lcut(text))
# 加载自定义的词典
jieba.load_userdict('data/user_dict')
words=jieba.lcut(text)
print(words)
# todo 添加新词
print('*'*100)
jieba.add_word('越来越多',15)
jieba.load_userdict('data/user_dict')
words=jieba.lcut(text)
print(words)
