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

for index, file in enumerate(files):
    print(file)
    # make sure file is an image
    if file.endswith(('.png')):
        im = Image.open(imgpath + '/' + file)
        width, height = im.size

        new_height = 640
        new_width  = int(new_height * width / height)


        img2 = im.resize((new_width, new_height), Image.ANTIALIAS)
        #img3 = img2.crop((300,0, 940, new_height))

        img2.save(f"{imgpath}/{index}.png") 
