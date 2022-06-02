import PIL
from simpleimage import SimpleImage
def daker(image):
    for pixel in image:
        pixel.red=pixel.red//2
        pixel.green=pixel.green//2
        pixel.blue=pixel.blue//2
def main():
    flower=SimpleImage('flower.jpg')
    daker(a)
    flower.show()
    

