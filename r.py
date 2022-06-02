from simpleimage import SimpleImage

DEFAULT_FILE = 'flower.jpg'
NUM_REPEATS = 2

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Create new SimpleImage of correct width
    final_image = SimpleImage.blank(image.width * NUM_REPEATS, image.height)

    for i in range(NUM_REPEATS):
        start_x = i * image.width # x coordinate in final_image where image will be applied
        put_image(start_x, image, final_image)
        
    # Show the repeated image
    final_image.show()


def put_image(start_x, image, final_image):
    """
    Helper function to apply the image to final_image at the correct position
    """
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.get_pixel(x, y)
            final_image.set_pixel(start_x + x, y, pixel)


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()


