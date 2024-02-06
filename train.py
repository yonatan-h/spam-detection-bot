import pandas as pd
from logistic_regression import LogisticRegression
import re 
import numpy as np
import json 
from extract_features import extract_features
import os 



def shuffle(X, y, message_indexes):
    length = X.shape[0]
    indices = np.arange(length)
    np.random.shuffle(indices)
    return (X[indices], y[indices], message_indexes[indices])

def extract_X_and_y( train_data, preprocess_data):

    length = train_data.shape[0]
    message_indexes = []
    X = []
    y = []
    for i in range(length):
        row = train_data.iloc[i]
        message_indexes.append(i)
        X.append(extract_features(row.text, preprocess_data))
        y.append(int(row.label))
        # print(row.label, type(row.label), int(row.label))
        # return
    
    message_indexes = np.array(message_indexes)
    X = np.array(X)
    y = np.array(y)

    X,y,message_indexes = shuffle(X, y, message_indexes)
    print('ys are', y[:10])
    print(f'{X.shape[1]} Features have been extracted from each sample')
    return X, y, message_indexes


 
def train():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    train_data = pd.read_csv(os.path.join(dir_path, "data","train.csv"))
    preprocess_data = json.load(open(os.path.join(dir_path,"data","preprocess.json")))

    X, y, message_indexes = extract_X_and_y(train_data, preprocess_data)
    train_length = int(y.size * 0.8)
    train_X, train_y, train_mi = X[:train_length], y[:train_length], message_indexes[:train_length]
    test_X, test_y, test_mi = X[train_length:], y[train_length:], message_indexes[train_length:]

    print(f'Data has been split into {train_length} training and {y.size - train_length} testing data' )

    lr = LogisticRegression(num_features=X.shape[1])
    lr.fit(train_X, train_y)

    with open(os.path.join(dir_path,"data","model.json"), "w") as f:
        f.write(json.dumps({ "weights":lr.w.tolist() }))
        print('Model has been saved in model.json')

    real_spam_as_spam = 0
    real_spam_as_not_spam = 0
    real_not_spam_as_spam = 0
    real_not_spam_as_not_spam = 0

    false_negatives = []
    false_positives = []

    yp = lr.predict_solid(test_X)

    for i in range(yp.size):
        m_index = test_mi[i]
        if yp[i] == 1 and test_y[i] == 1:
            real_spam_as_spam += 1
        elif yp[i] == 1 and test_y[i] == 0:
            real_not_spam_as_spam += 1
            false_positives.append(train_data.iloc[m_index].text)
        elif yp[i] == 0 and test_y[i] == 1:
            real_spam_as_not_spam += 1
            false_negatives.append(train_data.iloc[m_index].text)
        else:
            real_not_spam_as_not_spam += 1
    
    print('confusion matrix')
    print(f'           Spam Ham')
    print(f'Actual-Spam {real_spam_as_spam} {real_spam_as_not_spam}')
    print(f'Actual-Ham {real_not_spam_as_spam} {real_not_spam_as_not_spam}\n')
    # return
    print('FALSE NEGATIVES:\n', false_negatives and "\n".join(false_negatives[:10]))
    print('FALSE POSITIVES:\n', false_negatives and "\n".join(false_positives[:10]))


train()





