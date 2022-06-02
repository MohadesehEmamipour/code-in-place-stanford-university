from simpleimage import SimpleImage
a=1
def red_screen(main_filename,back_filename):
    image=SimpleImage(main_filename)
    back=SimpleImage(back_filename)
    for pixel in image:
       ave=(pixel.red+pixel.green+pixel.blue)//3
       if pixel.red<=ave*a:
           x=pixel.x
           y=pixel.y
           image.set_pixel(x,y,back.get_pixel(x,y))  
    return image
def main():
    leaves=SimpleImage('leaves.jpg')
    leaves.show()
    d=red_screen('stop.jpg','leaves.jpg')
    d.show()
if __name__=='__main__':
    main()
