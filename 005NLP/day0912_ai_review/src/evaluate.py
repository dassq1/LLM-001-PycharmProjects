"""
@Author:xuyinglai
@Date:2026/9/16
@DESC:
"""
from src.dataset import get_dataloader
import torch
from tqdm import tqdm
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification


from src.config import MODELS_PATH

from sklearn.metrics import accuracy_score


def evaluate():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = AutoModelForSequenceClassification.from_pretrained(MODELS_PATH).to(device)

    dataloader=get_dataloader(train=False)

    all_labels=[]
    all_predictions=[]
    for batch in tqdm(dataloader): # batch是一个字典
        batch={k:v.to(device) for k,v in batch.items()}
        labels= batch.pop('labels') # labels.shape  [batch_size]
        with torch.no_grad():
            outputs=model(**batch)
        logits=outputs.logits
        predictions=torch.argmax(logits,dim=-1)

        all_labels.extend(labels.tolist())
        all_predictions.extend(predictions.tolist())
    print(accuracy_score(all_labels, all_predictions))
    return accuracy_score(all_labels, all_predictions)




if __name__ == '__main__':
    pass