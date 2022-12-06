import pandas as pd
import tensorflow as tf
from reco_utils.dataset import movielens
from reco_utils.common.constants import SEED as DEFAULT_SEED
from reco_utils.dataset.python_splitters import python_chrono_split

print('Digite o tamanho do dataset:100k, 1m, 10m, ou 20m')
MOVIELENS_DATA_SIZE = input()
print('Digite no formato float a porcentagem de dados para treino')
PERCENTAGE = input()
print(MOVIELENS_DATA_SIZE,PERCENTAGE)
PERCENTAGE = float(PERCENTAGE)
# Loading movie leans data
df = movielens.load_pandas_df(size=MOVIELENS_DATA_SIZE,header=["userID", "itemID", "rating", "timestamp"])
train, test = python_chrono_split(df, PERCENTAGE)
df.to_csv('./movielens'+MOVIELENS_DATA_SIZE+'.csv')
train.to_csv('../features/train_'+MOVIELENS_DATA_SIZE+'.csv')
test.to_csv('../features/test_'+MOVIELENS_DATA_SIZE+'.csv')