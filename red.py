import random
from simpleimage import SimpleImage
DEFAULT_FILE='leaves.jpg'
def main():
    file_name=get_file()
    image=SimpleImage(DEFAULT_FILE)
    image.show()
    for pixel in image:
        pixel.red=random.randint(0,255)
    image.show()
def get_file():
    filename=input('Enter image file(or press enter for default):')
    if filename=='':
        filename=DEFAULT_FILE
    return filename
if __name__=='__main__':
    main()
