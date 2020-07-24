# Pixelify 🎨 
This rudimentary nine line python script lowers the quality of your imagesby picking every other pixel, which is based on what you set the ```cubeWidth``` to, and reads that pixels rgb color. It then changes the color of every pixel around it to the orginal pixel's color. The only mutable value is the intensity at which you can decrease the quality of the image.

## Looking at the code

```python
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

What is not visible in this block of code isn't relevant to the algorithm, but what I basically did was import the numpy and PIL libraries and then loaded the image. This script uses only one external variable which is an integer that specifies the ```cubeWidth```. Following that I declared the ```cubeRange``` variable which is basically the radius of the cube. Odd numbers cant be divided by 2 so just in case the radius is odd it takes only the whole number of that float integer.

```python
for x in range(im.size[0] // 1):
    for y in range(im.size[1] // 1):
        cordinate = x, y = x, y
```
These two for loops allow the algorithm to loop through each pixel.

```python
if x % cubeWidth == 0 and y % cubeWidth == 0 and x != 0 and y != 0:  
```
This simple if-then statement makes sure that the only pixel colors being used are the correct ones relative to the declared ```cubeWidth```.

```python
            for a in range(x - cubeWidth, x + cubeWidth // 2):
                for b in range(y - cubeWidth, y + cubeWidth // 2):
                    if x - cubeRange > 0 and y - cubeRange > 0:
                        img[a, b - cubeRange] = img[cordinate]
```
These last two for loops make each pixel color around the center one, relative to the ```cubeWidth```, equal the color of the center pixel.

## Results
![GitHub Logo](/Screen Shot 2020-07-24 at 1.10.14 PM.png)
