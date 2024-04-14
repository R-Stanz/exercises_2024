import cv2
import numpy as np

def find_first_black_pixel_index(image):  
    first_black_pixel_index = np.where(image < 50)
    first_black_pixel_line = first_black_pixel_index[0][0]
    first_black_pixel_col = first_black_pixel_index[1][0]
    return (first_black_pixel_line, first_black_pixel_col)



def fill_from(line, col, image):

    line_increment = 1
    if (line < 0):
        line_increment *= -1

    col_increment = 1
    if (col < 0):
        col_increment *= -1

    while (image[line][col] < 255):
        c = col
        while (image[line][c] < 255):
            image[line][c] = 255
            c += col_increment
        line += line_increment

    return image

def fill_the_blanks(image):

    image = fill_from(0,0,image)
    image = fill_from(-1,0,image)
    image = fill_from(0,-1,image)
    image = fill_from(-1,-1,image)

    return image
