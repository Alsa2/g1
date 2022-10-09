#make a program that takes all the .jpg files in a folder and converts them to one pdf file

import os
from PIL import Image

#make a list of all the files in the folder
files = os.listdir()

#make a list of all the .jpg files in the folder
jpgs = []
for file in files:
    if file.endswith('.jpg'):
        jpgs.append(file)

# sort the list of .jpg files
jpgs.sort()

#convert the .jpg files to .pdf files
for jpg in jpgs:
    im = Image.open(jpg)
    im.save(jpg[:-4] + '.pdf')
