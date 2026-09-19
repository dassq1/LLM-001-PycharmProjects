# process.py
# 数据预处理
import pandas as pd
from sklearn.model_selection import train_test_split
from tokenizer import ChineseTokenizer, EnglishTokenizer
import config

def process():
  """
  数据预处理主函数。
  """
  print('开始处理数据')

  df = pd.read_csv(
    config.DATA_PATH /'raw' /'cmn.txt',
    sep='\t',
    header=None,# 没有标题 列名
    usecols=[0, 1],# 只要0 ，1 列
    names=['en', 'zh'],
    encoding='utf8',
  )

  df = df.dropna()
  df = df[df['en'].str.strip().ne('') & df['zh'].str.strip().ne('')]

  train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

  # todo 构建中文词表
  # zh_texts=train_df['zh'].tolist()
  # zh_unique_tokens=set()
  # for zh_text in zh_texts:
  #     zh_tokens=ChineseTokenizer.tokenize(zh_text)
  #     zh_unique_tokens.update(zh_tokens)# token的列表，整体转成set
  #
  # zh_vocab_list = ['<pad>','<unk>','<sos>','<eos>']+list(zh_unique_tokens)
  #
  # (config.MODELS_PATH / 'zh_vocab.txt').write_text('\n'.join(zh_vocab_list), encoding='utf-8')
  ChineseTokenizer.build_vocab(train_df['zh'].tolist(), config.MODELS_PATH / 'zh_vocab.txt')
  # todo 构建英文词表
  # en_texts = train_df['en'].tolist()
  # en_unique_tokens = set()
  # for en_text in en_texts:
  #   en_tokens = EnglishTokenizer.tokenize(en_text)
  #   en_unique_tokens.update(en_tokens)  # token的列表，整体转成set
  #
  # en_vocab_list = ['<pad>', '<unk>', '<sos>', '<eos>'] + list(en_unique_tokens)
  #
  # (config.MODELS_PATH / 'en_vocab.txt').write_text('\n'.join(en_vocab_list), encoding='utf-8')
  EnglishTokenizer.build_vocab(train_df['en'].tolist(), config.MODELS_PATH / 'en_vocab.txt')

  # todo 编码数据集
  # zh_vocab_list =(config.MODELS_PATH / 'zh_vocab.txt').read_text(encoding='utf8').split('\n')
  # zh_tokenizer=ChineseTokenizer(vocab_list=zh_vocab_list)
  zh_tokenizer=ChineseTokenizer.from_vocab(config.MODELS_PATH / 'zh_vocab.txt')
  train_df['zh']=train_df['zh'].apply(lambda x: zh_tokenizer.encode(x))

  en_tokenizer=EnglishTokenizer.from_vocab(config.MODELS_PATH / 'en_vocab.txt')
  train_df['en']=train_df['en'].apply(lambda x:[2]+ en_tokenizer.encode(x)+[3])
  # 测试集
  test_df['zh']=test_df['zh'].apply(lambda x: zh_tokenizer.encode(x))
  test_df['en']=test_df['en'].apply(lambda x:[2]+ en_tokenizer.encode(x)+[3])

  train_df.to_json(config.DATA_PATH /'processed'/ 'train.json', orient='records', lines=True)
  test_df.to_json(config.DATA_PATH /'processed'/ 'test.json', orient='records', lines=True)
  print(train_df.head())

if __name__ == '__main__':
  process()
