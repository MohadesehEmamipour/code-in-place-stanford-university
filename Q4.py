from simpleimage import SimpleImage
filename='flower.jpg'
rep=6
def main():
    getfile()
    image=SimpleImage(filename)
    image.show()
    final_image=SimpleImage.blank(image.width*rep,image.height*rep)
    
    
    repeat()
    final_image.show()
def repeat():
    image=SimpleImage(filename)
    width=image.width
    height=image.height
    x=pixel.x
    y=pixel.y
    image=SimpleImage(filename)
    final_image=SimpleImage.blank(image.width*rep,image.height*rep)
    
    for x in range(image.width):
        for y in range(image.height):
            pixel=image.get_pixel(x,y)
            final_image.set_pixel(x*rep,y*rep,pixel)
    return image

def getfile():
    file=input('Enter your default image(or press enter):')
    if file=='':
        file=filename
    return file 

if __name__=='__main__':
    main()
