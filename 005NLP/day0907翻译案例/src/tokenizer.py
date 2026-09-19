from pathlib import Path

from nltk import word_tokenize, TreebankWordDetokenizer, TreebankWordTokenizer
from tqdm import tqdm

class BaseTokenizer:
  """
  分词器基类。
  """
  unk_token = '<unk>'
  pad_token = '<pad>'
  sos_token = '<sos>'
  eos_token = '<eos>'
  def __init__(self, vocab_list):
    self.vocab_list:list[str] = vocab_list # 词表
    self.word2id = {word:index for index,word in enumerate(self.vocab_list)}# 字典放着token和id对应
    self.id2word = {index:word for index,word in enumerate(self.vocab_list)} # 这也是一个字典
  @staticmethod

  def tokenize(self,text:str)->list[str]:
    pass


  def encode(self, text:str)->list[str]:
    """
    一步到位，先使用tokenize()分词,然后把token的列表转成id列表
    """
    tokens=self.tokenize(text)# 得到多个token组合形成的列表
    return [self.word2id.get(token,1) for token in tokens] # 返回一个数字列表，
  @classmethod
  def detokenize(cls, tokens:list[str])->str:
    # 子类实现
    pass

  def decode(self, token_ids:list[str])->str:
    """
    先把id列表转成token列表，然后把token列表传给detokenize()拼接成句子
    """
    # id->tokens
    tokens=[self.id2word[token_id] for token_id in token_ids]
    # tokends 拼接成句子
    return self.detokenize(tokens)

  # 类方法，通用构建词表
  @classmethod
  def build_vocab(cls,texts:list[str],vocab_file:Path):
    unique_tokens = set()
    for text in texts:
      tokens = cls.tokenize(text)
      unique_tokens.update(tokens)  # token的列表，整体转成set

    vocab_list = ['<pad>', '<unk>', '<sos>', '<eos>'] + list(unique_tokens)

    from day0907翻译案例.src import config
    vocab_file.write_text('\n'.join(vocab_list), encoding='utf-8')

  # 类方法 基于词表构建tokenizer对象
  @classmethod
  def from_vocab(cls,vocab_file:Path):
    vocab_list=vocab_file.read_text(encoding='utf-8').split('\n')
    return cls(vocab_list)
class ChineseTokenizer(BaseTokenizer):
  @classmethod
  def tokenize(cls,text:str)->list[str]:
    return list(text) # 现在返回的是个列表，一个一个汉语字
  def detokenize(self, tokens:list[str]) ->str:
    return ''.join(tokens) # 现在是把list[]拼接成汉语句子

class EnglishTokenizer(BaseTokenizer):
  tokenizer=TreebankWordTokenizer() # 创建一个对象
  detokenizer=TreebankWordDetokenizer()
  @classmethod
  def tokenize(cls,text:str)->list[str]:
    # return TreebankWordDetokenizer().tokenize(text)
    return cls.tokenizer.tokenize(text)

  def detokenize(self, tokens:list[str]) ->str:
    return self.detokenizer.detokenize(tokens)


if __name__=='__main__':
  print(EnglishTokenizer.tokenize("i love you'r $500,000"))