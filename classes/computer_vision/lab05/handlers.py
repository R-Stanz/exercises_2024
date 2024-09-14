import cv2 
from skimage import io
from skimage import filters
from skimage import color
import numpy as np


class Seamcarving:
    def __init__(self, path):
        self.img = io.imread(path)
        self.img_cv = cv2.imread(path)

    mode = True # if True, draw rectangle. Press 'm' to toggle to curve
    def select_on_image(self):
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.draw)

        while True:
            cv2.imshow('image', self.img_cv)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('m'):
                self.mode = not self.mode
            elif k == 27:
                break

        cv2.destroyAllWindows()



    pixels_to_remove = set({})
    drawing = False # true if mouse is pressed
    ix,iy = -1,-1

    # mouse callback function
    def draw(self, event, x, y, flags, param):
        radius = 5
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix, self.iy = x,y

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing == True:
                if self.mode == True:
                    cv2.rectangle(self.img_cv, (self.ix,self.iy), (x,y), (255,0,0), -1)
                else:
                    cv2.circle(self.img_cv, (x,y), radius, (0,0,255), -1)
                    self.add_circle_coords(x, y, radius)

        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            if self.mode == True:
                cv2.rectangle(self.img_cv, (self.ix, self.iy), (x,y), (0,0,255), -1)
                self.add_rectangle_coords(x, y)
            else:
                cv2.circle(self.img_cv, (x,y), radius, (0,0,255), -1)
                self.add_circle_coords(x, y, radius)

    def add_circle_coords(self, x, y, radius):
        for row_increment in range(5):
            for col_increment in range(5):
                new_coord = (self.ix + row_increment, self.iy + col_increment)
                self.pixels_to_remove.add(new_coord)
    
    def add_rectangle_coords(self, x, y):
        row_limits, col_limits = self.get_rectangle_limits(x,y)

        row_lower_limit, row_upper_limit = row_limits
        col_lower_limit, col_upper_limit = col_limits

        for row in range(row_lower_limit, row_upper_limit+1, 1):
            for col in range(col_lower_limit, col_upper_limit+1, 1):
                new_coord = (row, col)
                self.pixels_to_remove.add(new_coord)

    def get_rectangle_limits(self, x, y):
        row_upper_limit = self.iy
        row_lower_limit = y
        if y >= self.iy:
            row_upper_limit = y
            row_lower_limit = self.iy

        col_upper_limit = self.ix
        col_lower_limit = x
        if x >= self.ix:
            col_upper_limit = x
            col_lower_limit = self.ix

        return ((row_lower_limit, row_upper_limit), (col_lower_limit, col_upper_limit))
