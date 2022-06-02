from simpleimage import SimpleImage

DEFAULT_FILE = 'flower.jpg'
BRIGHTNESS_TOGGLE = 100

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    # Apply the filter
    # TODO: your code here

    # Show the image after the transform
    image.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()


from simpleimage import SimpleImage

DEFAULT_FILE = 'flower.jpg'
BRIGHTNESS_TOGGLE = 100

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    # Apply the filter
    for pixel in image:
        pixel.red = truncate(pixel.red + BRIGHTNESS_TOGGLE)
        pixel.green = truncate(pixel.green + BRIGHTNESS_TOGGLE)
        pixel.blue = truncate(pixel.blue + BRIGHTNESS_TOGGLE)

    # Show the image after the transform
    image.show()

def truncate(val):
    """ Truncates a value so that it is between 0 and 255 """
    if val < 0:
        val = 0
    elif val > 255:
        val = 255
    return val

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
