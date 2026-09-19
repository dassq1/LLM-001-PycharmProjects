"""
@Author:xuyinglai
@Date:2026/9/16
@DESC:
"""
import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification

from src.config import MODELS_PATH


def predict(text:str | list[str],model,tokenizer,device) ->int | list[int]:
    model.to(device)
    model.eval()

    is_str=isinstance(text,str)
    if is_str:
        text= [text]
    inputs = tokenizer(text,padding=True,truncation=True,return_tensors="pt")
    inputs={k:v.to(device) for k,v in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
    logits=outputs.logits #(batchsize,numlabels)
    predictions=torch.argmax(logits,dim=-1).tolist() # (batchasize)
    if is_str:
         return predictions[0]
    else:
        return predictions


if __name__ == '__main__':
    text=['太好了','这什么玩意儿', '这本书写的不错，下次别写了']
    model=AutoModelForSequenceClassification.from_pretrained(MODELS_PATH)
    tokenizer=AutoTokenizer.from_pretrained('google-bert/bert-base-chinese')
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    print(predict(text, model, tokenizer, device))
