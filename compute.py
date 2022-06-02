from simpleimage import SimpleImage
def compute_luminosity(red,green,blue):
    a=(0.2*red)+(0.5*green)+(0.1*blue)
    return a
def gray_scale(filename):
    image=SimpleImage(filename)
    for pixel in image:
        luminosity=compute_luminosity(pixel.red,pixel.green,pixel.blue)
        pixel.red=luminosity
        pixel.green=luminosity
        pixel.blue=luminosity
    return image
def main():
    leaves=SimpleImage('leaves.jpg')
    leaves.show()
    gray_scale_leaves=gray_scale('leaves.jpg')
    gray_scale_leaves.show()
    
    
if __name__=='__main__':
    main()
    
