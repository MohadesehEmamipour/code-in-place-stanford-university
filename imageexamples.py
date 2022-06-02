"""
This program contains several examples of functions that
manipulate an image to show how the SimpleImage library works.
"""

from simpleimage import SimpleImage

def darker(image):
    """
    Makes image passed in darker by halving red, green, blue values.
    Note: changes in image persist after function ends.
    """
    # Demonstrate looping over all the pixels of an image,
    # changing each pixel to be half its original intensity.
    for pixel in image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2




def main():
    """
    Run your desired image manipulation functions here.
    You should store the return value (image) and then
    call .show() to visualize the output of your program.
    """
    flower = SimpleImage('flower.jpg')
    flower.show()

    darker(flower)
    flower.show()

 
if __name__ == '__main__':
    main()
