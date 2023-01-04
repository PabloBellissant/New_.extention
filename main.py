from PIL.Image import *

from findIndex import getValue

i = open("image.jpg")
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
        print(i,listValue)
        dndList.append(listValue)