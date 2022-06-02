''' Written and made by Mohadeseh Emamipour from Iran. '''
''' A preset image is Repeats 10 times diagonally on a blank page. '''

#import simpleimage library
from simpleimage import SimpleImage

#Read image file 
filename='download.jpg'

# The number of times a photo is repeated,here a photo is repeated 3 times.
rep=10

def main():
    # Get file and load image
    getfile()

    #Read an image from a filename
    image=SimpleImage(filename)

    # Show the image before the transform
    image.show()

    #Create a blank image with specified dimensions
    final_image=SimpleImage.blank(image.width*rep,image.height*rep)

    #A for-loop repeats code for a specified number of times. 
    for i in range(rep):

        #Accessing Image Size
        start_x=i*image.width
        start_y=i*image.height

        repeat(start_x,start_y,image,final_image)

    # Show the image after the transform
    final_image.show()

def repeat(start_x,start_y,image,final_image):

    #Nested Loop over pixels in an image
    '''
    Nested Loops
    Sometimes you will see for loops put inside other for loops. This is called a "nested" loop.
    When this happens we refer to the first for loop as the "outer" loop and the second
    for loop as the "inner" loop.
    These loops operate much like you would expect. It is very good practice
    (and quite helpful) to make sure that the index variable is different for each loop.
    A standard choice is to use x for the outer loop and y for the inner loop. 
    '''
    for x in range(image.width):
        for y in range(image.height):

            #Accessing pixel from coordinates
            pixel=image.get_pixel(x,y)

            #Set a pixel with coordinates
            final_image.set_pixel(start_x+x,start_y+y,pixel)

    return image

def getfile():
    # Read image file path from user, or use the default file
    # input means takes in a prompt, returns user response
    file=input('Enter your default image(or press enter):')

    # this return statement only happens if the condition in the if-statement is true
    if file=='':
        file=filename
    return file

if __name__=='__main__':
    main()

''' Thank you so much indeed to all the colleagues for this course ( Code In Place ) is excellent and very useful and valuable. '''
