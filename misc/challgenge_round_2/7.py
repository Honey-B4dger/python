from PIL import Image
import re

im = Image.open('resources/oxygen.png', 'r')

#print(type(im))
#print(im.getdata())

print(im.size)
width, height = im.size
#print(width)
#print(height)

pixels = []
for x in range(width):
    pixels.append(im.getpixel((x,height / 2)))

#print(pixels)

pixels = [r for r,g,b,l in pixels if r == g and g == b]


pixels_refined = [chr(r) for r in pixels]

pixels_condensed = []
for i in range(1,len(pixels_refined),7):
    #print(pixels_refined[i])
    pixels_condensed.append(pixels_refined[i])

print(type(pixels_condensed))

result = ''.join(pixels_condensed)
print(type(result))
print(result)

final = re.findall(r'\d{3}', result)

print(''.join([chr(int(num)) for num in final]))
