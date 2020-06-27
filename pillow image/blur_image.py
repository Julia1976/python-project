from PIL import Image,ImageFilter
image=Image.open("D:/python/pillow image/ha.png")
blur_image=image.filter(ImageFilter.BLUR)
blur_image.save("D:/python/pillow image/ha.png","png")
