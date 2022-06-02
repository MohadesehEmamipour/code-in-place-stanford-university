from simpleimage import SimpleImage
filename='doctor.jpg'
r=6
def main():
    getfile()
    image=SimpleImage(filename)
    image.show()
    final_image=SimpleImage.blank(image.width*r,image.height*r)
    for i in range(r):
        for i in range(r):
            start_x=i*image.width
            start_y=i*image.height
            put_image(start_x,start_y,image,final_image)
    final_image.show()
def put_image(start_x,start_y,image,final_image):
    for x in range(image.width):
        for y in range(image.height):
            pixel=image.get_pixel(x,y)
            final_image.set_pixel(start_x+x,start_y+y,pixel)

def getfile():
    file=input('Enter default image(or press enter):')
    if file=='':
        file=filename
    return file

if __name__=='__main__':
    main()
