from PIL.Image import *

i = open("image.jpg")
(largeur, hauteur)= i.size
print(largeur, hauteur)
listPixel = []
for y in range(hauteur):
    for x in range(largeur):
        (rouge, vert, bleu) = i.getpixel((x, y))
        listPixel.append([rouge, vert, bleu])

print(listPixel)