from PIL import Image

image = Image.open('Images/ship.bmp')

print(image.size)

newImage = image.resize((70, 45))

newImage.save('Images/ship2.bmp')