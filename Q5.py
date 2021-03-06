from simpleimage import SimpleImage
filename='flower.jpg'
rep=6
def main():
    getfile()
    image=SimpleImage(filename)
    image.show()
    final_image=SimpleImage.blank(image.width*rep,image.height*rep)
    for i in range(rep):
        start_x=i*image.width
        start_y=i*image.height
        repeat(start_x,start_y,image,final_image)
    final_image.show()
def repeat(start_x,start_y,image,final_image):
    
    for x in range(image.width):
        for y in range(image.height):
            pixel=image.get_pixel(x,y)
            final_image.set_pixel(start_x+x,start_y+y,pixel)
    return image

def getfile():
    file=input('Enter your default image(or press enter):')
    if file=='':
        file=filename
    return file

if __name__=='__main__':
    main()
