import numpy as np
import os
import PIL

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

filepath = "batches/data/data_batch_1" #remember to go through all
#os.chdir("cifar-10-neural-network/cifar-frogs")
dict = unpickle(filepath)

decoded_dict = {key.decode('utf-8'): value for key, value in dict.items()}

#print(decoded_dict.keys())

fraugs = []

rows = len(decoded_dict['data']) 

for i in range(rows):
    if(decoded_dict['labels'][i] == 6): #is this item labeled a fraug?
        print(decoded_dict['data'][i]) #print its data
        fraugs.append(i)                #append this index to the list


rgbIdx = 0 #value 0, 1, 2, to set the parts of the pixel
pixels = []

reds = []
greens = []
blues = []

for fraugRow in range(len(fraugs)):
    for color in range(0,3072):
        if(color < 1024):
            reds.append(decoded_dict['data'][color])
        if(color >= 1024 and color < 2048):
            greens.append(decoded_dict['data'][color])
        if(color >= 2048 and color < 3072):
            blues.append(decoded_dict['data'][color])
    
for pixelColor in range(1024):
    pixel = ((reds[pixelColor], greens[pixelColor], blues[pixelColor]))
    pixels.append(pixel)

print(pixels)
