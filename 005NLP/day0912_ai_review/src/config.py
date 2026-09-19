"""
@Author:xuyinglai
@Date:2026/9/16
@DESC:
"""
from pathlib import Path
# 路径参数
"""
.parents[0]` = `.parent` → 当前 py 文件直接所在文件夹
.parents[1]` → 再往上再上一级文件夹（父目录的父目录）
"""
ROOT_PATH=Path(__file__).parents[1]
DATA_PATH=ROOT_PATH / "data"
# LOGS_PATH=ROOT_PATH / "logs"
LOGS_PATH=Path('/root/tf-logs')
MODELS_PATH=ROOT_PATH / "models"

# todo 训练参数
BATCH_SIZE=18

LR=1e-6
EPOCHS=5
SAVE_STEPS=100