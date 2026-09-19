from pathlib import Path

# 路径参数
ROOT_PATH = Path(__file__).parents[1]
DATA_PATH = ROOT_PATH / 'data'
LOGS_PATH = ROOT_PATH / 'logs'
MODELS_PATH = ROOT_PATH / 'models'

# 训练参数
BATCH_SIZE = 64
LR = 1e-3
EPOCHS = 30


# 模型参数
DIM_MODEL = 256
NUM_HEADS = 4
NUM_ENCODER_LAYERS = 2
NUM_DECODER_LAYERS = 2
