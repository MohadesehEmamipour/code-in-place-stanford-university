from simpleimage import SimpleImage
filename='doctor.jpg'
a=500
def main():
    getfile()
    image=SimpleImage(filename)
    image.show()
    center=SimpleImage.blank(a,a)
    start_x=(image.width-a)//2
    start_y=(image.height-a)//2
    for x in range(a):
        for y in range(a):
            pixel=image.get_pixel(start_x+x,start_y+y)
            center.set_pixel(x,y,pixel)
    center.show()
def getfile():
    file=input('Enter image file ( or press enter for default):')
    if file=='':
        file=filename
    return file

if __name__=='__main__':
    main()
        
