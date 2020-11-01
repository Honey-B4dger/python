from PIL import Image

im = Image.open('resources/cave.jpg', 'r')
(width, height) = im.size

#print(width,height)

even = Image.new('RGB', (width//2, height//2))
odd = Image.new('RGB', (width//2, height//2))

print(str(even.size))

for x in range(width):
    for y in range(height):
        p = im.getpixel((x,y))
        if (x + y) % 2 == 1:
            odd.putpixel(((x//2),(y//2)), p)
        else:
            even.putpixel(((x//2),(y//2)), p)


odd.show()
even.show()
