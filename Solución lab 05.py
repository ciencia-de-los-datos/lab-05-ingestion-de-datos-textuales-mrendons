#Solución lab 05
import os
import pandas as pd

def process_directory(directory_path):
    data = []

    for sentiment in os.listdir(directory_path):
        if os.path.isdir(os.path.join(directory_path, sentiment)):
            folder_path = os.path.join(directory_path, sentiment)
            for filename in os.listdir(folder_path):
                if filename.endswith('.txt'):
                    file_path = os.path.join(folder_path, filename)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        phrase = file.read().strip()
                        data.append({'phrase': phrase, 'sentiment': sentiment})

    return pd.DataFrame(data)

train_dataset = process_directory(os.path.join('data', 'train'))
test_dataset = process_directory(os.path.join('data', 'test'))

train_dataset.to_csv('train_dataset.csv', index=False)
test_dataset.to_csv('test_dataset.csv', index=False)