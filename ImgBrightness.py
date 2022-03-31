from PIL import Image,ImageEnhance

myimage = Image.open("testImg.jpg")
print(myimage.size)
newsize = (800,570)
myResizedImg = myimage.resize(newsize)
print(myResizedImg.size)
myResizedImg.save("ResizedTestImg.jpg")

#defining enhancer for image
myenhancer = ImageEnhance.Brightness(myimage)

# to Bright the image
brightImage = myenhancer.enhance(1.6)
brightImage.save("MyBrightImg.jpg")

# to Dark the image
darkImg = myenhancer.enhance(.5)
darkImg.save("MyDarkImg.jpg")