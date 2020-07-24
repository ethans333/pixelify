#created by @ethans33 7/24/2020

from PIL import Image
from numpy import random

im = Image.open("/Users/ethan/Documents/Python/goldenlab.jpg")
img = im.load()
im.show() 

cubeWidth = 4
cubeRange = cubeWidth // 2

for x in range(im.size[0] // 1):
    for y in range(im.size[1] // 1):
        cordinate = x, y = x, y

        if x % cubeWidth == 0 and y % cubeWidth == 0 and x != 0 and y != 0:     
            for a in range(x - cubeWidth, x + cubeWidth // 2):
                for b in range(y - cubeWidth, y + cubeWidth // 2):
                    if x - cubeRange > 0 and y - cubeRange > 0:
                        img[a, b - cubeRange] = img[cordinate]

im.show()