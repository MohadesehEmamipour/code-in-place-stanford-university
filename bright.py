from simpleimage import SimpleImage
filename='leaves.jpg'
bright=100

def main():
    getfile()
    image=SimpleImage(filename)
    image.show()
    for pixel in image:
        pixel.red=pixel.red+bright
        pixel.green=pixel.green+bright
        pixel.blue=pixel.blue+bright
    image.show()
def getfile():
    file=input('Enter image file(or press enter for default):')
    if file=='':
        file=filename
    return file
'''
def turncate(val):
    if val<0:
        val=0
    elif val>255:
        val=255
    return val
'''
if __name__=='__main__':
    main()
