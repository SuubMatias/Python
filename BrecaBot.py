from PIL import ImageGrab, Image


img = ImageGrab.grab()
print(type(img))
img.save('C:/Users/Vitor Lucas/Desktop/teste.png')
#ESSE PIXEL É BASEADO NO SEU MONITOR
print(img.getpixel((55, 122)))
cor = (240, 71, 71)
if img.getpixel((56, 122)) == cor:
    print("opa")