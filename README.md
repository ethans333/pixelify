# Pixelify
This rudimentary python script lowers the quality of your images.

This 9 line algorithm basically picks every other pixel, which is based on what you set the cube width to, and reads that pixels rgb color. It then changes the color of every pixel around it to the orginal pixel's color. The only mutable value is the intensity at which you can decrease the quality of the image.

## Looking at the code

```
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
```
