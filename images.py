
from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')
filtered_image = img.convert('L')
crooked = filtered_image.rotate(90)
crooked.save('grey_pikachu.png', 'png')



print(dir(img))

