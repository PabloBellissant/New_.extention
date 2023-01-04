from PIL.Image import *

from findIndex import getValue
from listSimplifier import simplify

i = open("imagebis.jpg")
(largeur, hauteur)= i.size
listPixel = []
for y in range(hauteur):
    for x in range(largeur):
        (rouge, vert, bleu) = i.getpixel((x, y))
        listPixel.append([rouge, vert, bleu])


dndList = []
for rgb in range(3):
    for i in range(255):
        listValue = getValue(listPixel, rgb, i)
        if(listValue != []):
            dndList.append([rgb, i, listValue])
for i in range(len(dndList)):
    dndList[i][2] = simplify(dndList[i][2])



print(dndList)
