from snownlp import SnowNLP
from snownlp import normal
from snownlp import sentiment
import numpy as np

# 导⼊入包

def train(neg_file, pos_file, to):
    sentiment.train(neg_file, pos_file)

sentiment.save()
train("neg.txt", "pos.txt", "test_sentiment.marshal")