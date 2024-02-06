from collections import Counter
import pandas as pd
import json
import re
import numpy as np
import os



def top_tokens(train_data, split, top_count):
    tokens = set()
    spam_frequency = Counter()
    not_spam_frequency = Counter()
    num_spams = 0
    num_not_spams = 0

    print(train_data.iloc[0]['label'])
    for i in range(train_data.shape[0]):
        message = train_data.iloc[i].text.lower()
        is_spam = train_data.iloc[i].label == 1

        if is_spam: num_spams += 1
        else : num_not_spams += 1

        for token in list(set(split(message))):
            tokens.add(token)
            if is_spam: spam_frequency[token] += 1
            else : not_spam_frequency[token] += 1
    
    chi_token_pairs = []
    for token in list(tokens):
        #chi test
        #_        | spam | not spam
        #present  |  a   |    b
        #absent   |  c   |    d

        #actuals d
        a = spam_frequency[token]
        b = not_spam_frequency[token]
        c = num_spams - a
        d = num_not_spams - b

        #expecteds 
        total = a + b + c + d
        row1 = a + b
        row2 = c + d
        col1 = a + c
        col2 = b + d

        #redistribute (e means expected)
        e_a = (row1 * col1 / total) + 0.1
        e_b = (row1 * col2 / total) + 0.1
        e_c = (row2 * col1 / total) + 0.1
        e_d = (row2 * col2 / total) + 0.1

        #deviations
        # adding 0.5 to avoid division by zero

        dev_a = (a - e_a)**2 / (e_a )
        dev_b = (b - e_b)**2 / (e_b )
        dev_c = (c - e_c)**2 / (e_c )
        dev_d = (d - e_d)**2 / (e_d )

        chi = dev_a + dev_b + dev_c + dev_d
        chi_token_pairs.append((chi, token))

    chi_token_pairs.sort()
    chi_token_pairs.reverse()
    # print(len(chi_token_pairs))

    important_tokens = []
    for i in range(min(len(chi_token_pairs),top_count)):
        important_tokens.append(chi_token_pairs[i][1])
    
    return important_tokens

def average_msg_length(train_data):
    total_length = 0
    message_count = 0

    size = train_data.shape[0]

    for i in range(size):
        row = train_data.iloc[i]
        if row.label == 1: continue
        total_length += len(row.text)
        message_count += 1
    
    return total_length/message_count

def split_words(message):
    # all chars except numbers, spaces, comma, question, colon, brackets, slashes, dashes, underscores, equal signs, plus signs, tildes, backticks, at signs, hashtags etc
    return re.split(r"[\d\.\s\,\?\!\:\;\(\)\[\]\{\}\/\-\_\=\+\~\`\@\#\$\%\^\&\*\|\<\>\"\'\’\‘\“\”\—]+", message)

def split_characters(message):
    return list(message)

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    train_data = pd.read_csv(os.path.join(dir_path, "data","train.csv"))

    print('Preprocessing data...')
    top_words = top_tokens(train_data, split_words, 500)
    print('Top words done have been extracted...', top_words[:10])
    top_characters = top_tokens(train_data, split_characters, 500)
    print('Top characters have been extracted...', top_characters[:10])
    average_length = average_msg_length(train_data)
    print('Average length has been calculated...', average_length)

    # add to preprocess.json
    train_data = {
        "top_words": top_words,
        "top_characters": top_characters,
        "average_length": average_length
    }

    with open(os.path.join(dir_path, "data","preprocess.json"), "w") as file:
        json.dump(train_data, file, ensure_ascii=False)
        print('Preprocess data has been saved to preprocess.json')
    
main()