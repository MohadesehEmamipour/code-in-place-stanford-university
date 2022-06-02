from simpleimage import SimpleImage
def blue_channel(filename):
    image=SimpleImage(filename)
    for pixel in image:
        pixel.red=0
        pixel.gree=0
    return image
def main():
    leaves=blue_channel('leaves.jpg')
    leaves.show()
if __name__=='__main__':
    main()
