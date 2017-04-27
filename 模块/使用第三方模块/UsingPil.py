# coding=utf-8
from PIL import Image, ImageFilter

# thumbnail a image
im = Image.open("avatar.jpg")
w, h = im.size
print("width: ", w, " height: ", h)
im.thumbnail((w // 2, h // 2))
im.save("thumbnail.jpg", "jpeg")


# dim an image
dim_image = Image.open("avatar.jpg")
dim_image = dim_image.filter(ImageFilter.BLUR)
dim_image.save("dim_image.jpg", "jpeg")

