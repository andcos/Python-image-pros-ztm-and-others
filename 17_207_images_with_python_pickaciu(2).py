# images with python

from PIL import Image, ImageFilter
#https://pillow.readthedocs.io/en/3.3.x/reference/Image.html#examples

#from PIL.Image import core as _imaging

img = Image.open('./astro.jpg')
print(img)
img.thumbnail((400,400))
# the image is compressed -
img.save('thumbnail.jpg')


