from simpleimage import SimpleImage
filename='flower.jpg'
def main():
    getfile()
    image=SimpleImage(filename)
    image.show()
    f=flame(filename)
    f.show()

def flame(filename):
    image=SimpleImage(filename)
    for pixel in image:
        ave=(pixel.red+pixel.green+pixel.blue)//3
        if pixel.red>=ave:
            pixel.red=255
            pixel.green=0
            pixel.blue=0
        else:
            pixel.red=ave
            pixel.green=ave
            pixel.blue=ave
    return image

def getfile():
    file=input('Enter your default image(or press enter):')
    if file=='':
        file=filename
    return file
if __name__=='__main__':
    main()
