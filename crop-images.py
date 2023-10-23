import os
from PIL import Image

# specify the img directory path
path = "."

# list files in img directory
files = os.listdir(path)

partcut = 9.1

for file in files:
    # make sure file is an image
    if file.endswith(('.png')):
        im = Image.open(file)
        width, height = im.size
        left = width / partcut
        top = height / partcut
        right = (partcut-1) * width / partcut
        bottom = (partcut-1) * height / partcut
        im1 = im.crop((left, top, right, bottom))

        im1.save(f"cropped-{file}") 
