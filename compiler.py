from PIL.Image import *

from findIndex import getValue
from listSimplifier import simplify
from compacting import compacty



def Imagecompiler(i):
    (largeur, hauteur) = i.size
    listPixel = []
    print("launched")
    for y in range(hauteur):
        for x in range(largeur):
            (rouge, vert, bleu) = i.getpixel((x, y))
            listPixel.append([rouge, vert, bleu])

    dndList = []
    print("has image 1")
    for rgb in range(3):
        for i in range(255):
            listValue = getValue(listPixel, rgb, i)
            if (listValue != []):
                dndList.append([rgb, i, listValue])

    print("has image 2")
    for i in range(len(dndList)):
        dndList[i][2] = simplify(dndList[i][2])
        dndList[i][2] = compacty(dndList[i][2])

    return dndList

