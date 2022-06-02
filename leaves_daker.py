from simpleimage import SimpleImage
def darker(image):
    
    for pixel in image:
        pixel.red=pixel.red//2
        pixel.green=pixel.green//2
        pixel.blue=pixel.blue//2
    
def main():
    leaves=SimpleImage('leaves.jpg')
    leaves.show()
    darker(leaves)
    leaves.show()
if __name__ == '__main__':
    main()
