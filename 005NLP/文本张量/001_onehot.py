"""
@Author:xuyinglai
@Date:2026/9/1
@DESC:演示复杂版 简单版

"""
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import jieba
from tensorflow.keras.preprocessing.text import Tokenizer
import joblib
# todo 1.定义函数
def dm01_onehot_gen():
    # 1准备语料，切词后的内容
    vocabs={'周杰伦','陈奕迅','王力宏','蔡徐坤','李宗盛','吴亦凡'}

    # 2 实例化词汇映射器
    my_tokenizer = Tokenizer()
    # 3.通过 词汇映射器 在语料库上训练
    my_tokenizer.fit_on_texts(vocabs)
    # 4.打印woed_index字典，key value
    print(my_tokenizer.word_index)
    # 5.对每个词进行one-hot编码
    for word in vocabs:
        # 5.1 先创建长度=语料库的长度
        zreo_list=[0]*len(vocabs)
        # print(zreo_list)
        # 5.2
        idx=my_tokenizer.word_index[word]-1
        # 5.3
        zreo_list[idx]=1
        print(zreo_list)
    # 6保存 词汇映射对象
    joblib.dump(my_tokenizer,'./model/onehot.pkl')
    print('保存成功')

# todo 2.定义函数演示one-hot编码
def use_one_hot():
    # 1.加载我训练好的 词汇映射器
    my_tokenizer = joblib.load('./model/onehot.pkl')
    # 2.打印 查看Kv关系
    print(my_tokenizer.word_index)
    # 3.对指定词汇进行one hot
    token='蔡徐坤'
    # 4.创建长度=字典的list，全0
    zero_list=[0]*len(my_tokenizer.word_index)
    print(zero_list)
    # 5.获取指定词汇在word_index的索引
    idx=my_tokenizer.word_index[token]-1
    # 6.对应位置修改为1
    zero_list[idx]=1
    # 7.打印结果
    print(zero_list)

# todo 3.one-hot简单版
def simple_one_hot():
    # 准备语料库
    vocabs = {'周杰伦', '陈奕迅', '王力宏', '蔡徐坤', '李宗盛', '吴亦凡'}
    # 构建词汇 到 索引的映射关系 字典
    word2index={vocab:index for index, vocab in enumerate(vocabs)}
    print(word2index)
    # 对每个词进行one-hot
    for word in vocabs:
        zreo_list=[0]*len(vocabs)
        idx=word2index[word]
        zreo_list[idx]=1
        print(zreo_list)
        print(word)









# todo 4.测试代码
if __name__ == '__main__':
    # 1.测试one-hot编码
    # dm01_onehot_gen()
    # 2.测试one-hot编码
    # use_one_hot()
    # 3.简单版的one-hot
    simple_one_hot()