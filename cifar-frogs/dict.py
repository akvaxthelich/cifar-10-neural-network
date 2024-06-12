import numpy as np
import os
from PIL import Image

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
         #print its data
        fraugs.append(decoded_dict['data'][i])                #append this index to the list


 #one row/array, 1024r -> 1024g -> 1024b, makes one image

# rgbIdx = 0 #value 0, 1, 2, to set the parts of the pixel

reds = []
greens = []
blues = []
images = []


#len(fraugs)
for fraugRow in range(len(fraugs)): #for all 1030 fraugs in batch 1 
    print("Loading fraug image data...")
    for j in range(3072):         #for each item in a fraug (color value)
        if(j < 1024):               #append the first 1024
            reds.append(fraugs[fraugRow][j])  #add the reds from this image to one array
        if(j >= 1024 and j < 2048):
            greens.append(fraugs[fraugRow][j])#the greens to another
        if(j >= 2048 and j < 3072):
            blues.append(fraugs[fraugRow][j])#the blues to another

    print("Loading color values into pixel array...")
    image = []
    for z in range(1024):
        pixel = ((reds[z], greens[z], blues[z]))
        image.append(pixel)
    reds = []
    greens = []
    blues = []

    print("Loading formatted tuple array into image array.")
    images.append(image)
    print("Cleared color cache, looping.")
print("Done.")


imgIdx = 4
print("Loading and showing image.")
img = Image.new("RGB", (32,32))
pixels = img.load()
test = images[imgIdx]
for y in range(32):
    for x in range (32):
        index = y * 32 + x
        pixels[x, y] = test[index]
img.show()

# print(len(reds))
# for fraugRow in range(len(fraugs)):
#     for pixelColor in range(1024): #each array should be length 1024
#         pixel = ((reds[pixelColor], greens[pixelColor], blues[pixelColor]))
#         image.append(pixel)

# #pixels is an array of 3d tuples -> this should be called image
# print(image[0]) #all of the pixels in item 1
