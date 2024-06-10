import numpy as np

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

filepath = "batches/data/data_batch_1"

dict = unpickle(filepath)


decoded_dict = {key.decode('utf-8'): value for key, value in dict.items()}

#print(decoded_dict.keys())

rows = len(decoded_dict['data']) 

for i in range(rows):
    if(decoded_dict['labels'][i] == 6): #is she a fraug?
        print(decoded_dict['filenames'][i])
        print(decoded_dict['data'][i])