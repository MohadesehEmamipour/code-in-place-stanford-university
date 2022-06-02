from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'
SQUARE_WIDTH = 200

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    center_square = SimpleImage.blank(SQUARE_WIDTH, SQUARE_WIDTH)

    # TODO: your code here

    # Show the image after the transform
    center_square.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()


from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'
SQUARE_WIDTH = 200

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    center_square = SimpleImage.blank(SQUARE_WIDTH, SQUARE_WIDTH)

    # calculate coordinates of top left corner of centered square
    start_x = (image.width - SQUARE_WIDTH) // 2
    start_y = (image.height - SQUARE_WIDTH) // 2

    for x in range(SQUARE_WIDTH):
        for y in range(SQUARE_WIDTH):
            pixel = image.get_pixel(start_x + x, start_y + y)
            center_square.set_pixel(x, y, pixel)

    # Show the image after the transform
    center_square.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
