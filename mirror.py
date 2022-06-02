from simpleimage import SimpleImage
def mirror_image(filename):
    image=SimpleImage(filename)
    width=image.width
    height=image.height
    mirror=SimpleImage.blank(width,height*2)
    for x in range(width):
        for y in range(height):
            pixel=image.get_pixel(x,y)
            mirror.set_pixel(x,y,pixel)
            mirror.set_pixel(x,(height*2)-(y+1),pixel)
    return mirror
def main():
    original=SimpleImage('leaves.jpg')
    original.show()
    mirrored=mirror_image('leaves.jpg')
    mirrored.show()
if __name__=='__main__':
    main()
