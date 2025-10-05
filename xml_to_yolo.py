import xml.etree.ElementTree as ET
import os
import sys
from PIL import Image

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

tags = {}

tree = ET.parse(imgpath)
root = tree.getroot()

for inx, tag in enumerate(root.find('tags')):
    tags.update({tag.attrib['name']: inx})


for img in root.find('images'):
    newname = img.attrib['file'].split(".")[0]
    im = Image.open(img.attrib['file'])
    with open(newname + ".txt" , 'w') as writer:
        boxes = ""
        for box in img.findall('box'):
            top = int(box.attrib['top'])
            left = int(box.attrib['left'])
            width = int(box.attrib['width'])
            height = int(box.attrib['height'])

            x = (left+(width/2))/im.size[0]
            y = (top+(height/2))/im.size[1]
            newwidth = width/im.size[0]
            newheight = height/im.size[1]
            
            blep = box.find('label')
            boxes += f"{tags[blep.text]} {x:.5f} {y:.5f} {newwidth:.5f} {newheight:.5f} \n"
    
        writer.write(boxes)
        
