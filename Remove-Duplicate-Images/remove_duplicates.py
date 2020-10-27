import hashlib
import os
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from hashlib import md5
import numpy as np


path = input('Drop your folder here')



def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return md5(f.read()).hexdigest()
filenames = list()
for root,dirs,filename in os.walk(path):
    for img in filename:
        filenames.append(os.path.join(root,img))

print(f'Total files in folder: {len(filenames)}')

duplicates = []
hash_keys = dict()
for index, filename in  enumerate(filenames):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys: 
            hash_keys[filehash] = index
        else:
            duplicates.append((index,hash_keys[filehash]))

print(f'Total duplicates: {len(duplicates)}')

#To random 3 show images uncomment the code below.

# for file_indexes in duplicates[0:3]:
#     try:

#         img=mpimg.imread(filenames[file_indexes[1]])
#         plt.subplot(121),plt.imshow(img)
#         plt.title(file_indexes[1]), plt.xticks([]), plt.yticks([])

#         img=mpimg.imread(filenames[file_indexes[0]])
#         plt.subplot(122),plt.imshow(img)
#         plt.title(str(file_indexes[0]) + ' duplicate'), plt.xticks([]), plt.yticks([])
#         plt.show()
    
#     except OSError as e:
#         continue

for index in duplicates:
    os.remove(filenames[index[0]])