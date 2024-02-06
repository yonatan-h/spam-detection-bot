import pandas as pd

df = pd.read_csv('spam_collected.csv', encoding='ISO-8859-1')
print(df.shape)


df = pd.read_csv('ham_collected.csv', encoding='ISO-8859-1')
print(df.shape)
