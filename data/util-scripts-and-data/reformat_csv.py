import pandas as pd
import os


def main():
    # Category,Message
    # ham, text...
    # spam, text...

    # reformat to
    #text,label
    # "text...
    #",0

    csv_file_names = ['amh.csv', 'amh2.csv', 'mix.csv', 'org.csv']
    with open('reformatted.csv', 'w') as f:
        f.write(f'text,label\n')

    # csv_file_names = ['mini-amh.csv']

    for file_name in csv_file_names:
        print('reformatting', file_name)
        data = pd.read_csv(file_name)
        length = data.shape[0]
        for i in range(length):
            # print('reformatting row', i)
            row = data.iloc[i]

            #get category
            if row.Category == 'ham': label = 0
            elif row.Category == 'spam': label = 1
            else: raise ValueError('Invalid label ' + str(row.Category) + 'in line ' +str(i+1) + 'in file ' + file_name )

            #get message
            text = row.Message
            if type (text) != str:
                print('skipping '+str(text)+' row', i, 'in file', file_name, 'because it is not a string')
                continue

            text  = "".join(text.split('"'))
            text  = "".join(text.split(','))
            text  = "".join(text.split('/'))

            #write to reformatted.csv
            with open('reformatted.csv', 'a') as f:
                f.write(f'"{text}",{label}\n')
           

main()