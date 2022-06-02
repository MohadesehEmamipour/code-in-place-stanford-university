"""
This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.
"""

from simpleimage import SimpleImage

BRIGHT_THRESHOLD = 153

def main():
    image = SimpleImage('images/simba-sq.jpg')
    for pixel in image:
        pixel_avg = get_pixel_average(pixel)
        if pixel_avg > BRIGHT_THRESHOLD:
            # set to grayscale
            pixel.red = pixel_avg   
            pixel.blue = pixel_avg
            pixel.green = pixel_avg
    image.show()

def get_pixel_average(pixel):
    """
    Computes the average of the red, green, and blue
    components of this pixel.

    Inputs:
        - pixel: The pixel to compute the average on
    """
    return (pixel.red + pixel.blue + pixel.green) // 3

if __name__ == '__main__':
    main()
