import os
from PIL import Image
import sys
import os

# specify the img directory path

# list files in img directory

args = sys.argv
if len(args) > 1:
    imgpath = sys.argv[1]
    print(imgpath)
    if not os.path.exists(imgpath):
        print("path doesnt exist")
        quit()
else:
    print("No path")
    quit()


files = os.listdir(imgpath)
partcut = 9.1

for file in files:
    print(file)
    # make sure file is an image
    if file.endswith(('.png')):
        im = Image.open(imgpath + '/' + file)
        width, height = im.size
        left = width / partcut
        top = height / partcut
        right = (partcut-1) * width / partcut
        bottom = (partcut-1) * height / partcut
        im1 = im.crop((left, top, right, bottom))

        im1.save(f"{imgpath}/cropped-{file}") 
