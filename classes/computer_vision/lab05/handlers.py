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

        elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
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
                if self.iy + row_increment < rows and self.ix + col_increment < cols:
                    new_coord = (self.iy + row_increment, self.ix + col_increment)
                    self.pixels_to_remove.add(new_coord)
    
    def add_rectangle_coords(self, x, y):
        row_range, col_range = self.get_rectangle_ranges(x,y)

        for row in row_range:
            for col in col_range:
                new_coord = (row, col)
                self.pixels_to_remove.add(new_coord)

    def get_rectangle_ranges(self, x, y):
        row_range = range(y, self.iy, 1)
        if y >= self.iy:
            row_range = range(self.iy, y, 1)

        col_range = range(x, self.ix, 1)
        if x >= self.ix:
            col_range = range(self.ix, x, 1)

        return (row_range, col_range)
    



    def remove_selection(self):
        new_img = self.img.copy()
        img_annotated = self.img.copy()

        rows, cols = self.img.shape[:2]
        new_to_img = np.empty((rows, cols), dtype=object)
        for r in range(rows):
            for c in range(cols):
                new_to_img[r,c] = (r,c)

        images = (new_img, img_annotated, new_to_img)
        while self.pixels_to_remove and new_img.any():
            if self.has_less_ratio_than_img(new_img):
                images = self.vertical_seamcarving(images)
            else:
                images = self.horizontal_seamcarving(images)

            new_img, img_annotated, new_to_img = images

        return (self.img, new_img, img_annotated)

    def has_less_ratio_than_img(self, image):
        new_image_height, new_image_width, _ = image.shape
        new_image_ratio = new_image_width / new_image_height

        image_height, image_width, _ = self.img.shape
        image_ratio = image_width / image_height

        if new_image_ratio < image_ratio:
            return False
        return True



    def vertical_seamcarving(self, images):
        new_img, img_annotated, new_to_img = images

        energy = self.calculate_energy_v(new_img)
        cum_energy, backtrack = self.find_seam_v(energy, new_to_img)
        return self.remove_seam_v(images, cum_energy, backtrack)

    def calculate_energy_v(self, image):
        gray_image = color.rgb2gray(image)
        energy = np.abs(filters.sobel_v(gray_image))
        return energy

    def find_seam_v(self, energy, new_to_img):
        rows, cols = energy.shape
        cum_energy = energy.copy()
        backtrack = np.zeros_like(cum_energy, dtype=int)

        for r in range(1, rows):
            for c in range(cols):
                if c == 0:
                    idx = np.argmin(cum_energy[r-1, c:c+2])
                    backtrack[r, c] = idx + c
                    min_energy = energy[r-1, idx + c]
                else:
                    idx = np.argmin(cum_energy[r-1, c-1:c+2])
                    backtrack[r, c] = idx + c - 1
                    min_energy = cum_energy[r-1, idx + c - 1]

                img_coord = new_to_img[r,c]
                if img_coord in self.pixels_to_remove:
                    cum_energy[r,c] -= 10
                else:
                    cum_energy[r,c] += min_energy

        return (cum_energy, backtrack)

    def remove_seam_v(self, images, cum_energy, backtrack):
        new_image, annotated_image, new_to_img = images

        rows, cols = new_image.shape[:2]
        output = np.zeros((rows, cols - 1, 3), dtype=new_image.dtype)
        mod_new_to_img = np.zeros((rows, cols - 1), dtype=new_to_img.dtype)

        c = np.argmin(cum_energy[-1])
        for r in reversed(range(rows)):
            img_coord = new_to_img[r,c]
            mod_new_to_img = np.delete(new_to_img[r, :], [c])
            if img_coord in self.pixels_to_remove:
                self.pixels_to_remove.remove(img_coord)

            img_r, img_c = img_coord
            for i in range(3):
                output[r, :, i] = np.delete(new_image[r, :, i], [c])
                annotated_image[img_r, img_c, i] = 0

            c = backtrack[r, c]

        return (output, annotated_image, new_to_img)


    def horizontal_seamcarving(self, images):
        new_img, img_annotated, new_to_img = images

        energy = self.calculate_energy_h(new_img)
        cum_energy, backtrack = self.find_seam_h(energy, new_to_img)
        return self.remove_seam_h(images, cum_energy, backtrack)

    def calculate_energy_h(self, image):
        gray_image = color.rgb2gray(image)
        energy = np.abs(filters.sobel_h(gray_image))
        return energy

    def find_seam_h(self, energy, new_to_img):
        rows, cols = energy.shape
        cum_energy = energy.copy()
        backtrack = np.zeros_like(cum_energy, dtype=int)

        for c in range(1, cols):
            for r in range(rows):
                if r == 0:
                    idx = np.argmin([cum_energy[r+i, c-1] for i in range(2)])
                    backtrack[r, c] = idx + r
                    min_energy = cum_energy[idx + r, c-1]
                elif r == (rows-1):
                    idx = np.argmin([cum_energy[r+i, c-1] for i in range(-1, 1)])
                    backtrack[r, c] = idx + r - 1
                    min_energy = cum_energy[idx + r-1, c-1]
                else:
                    idx = np.argmin([cum_energy[r+i, c-1] for i in range(-1, 2)])
                    backtrack[r, c] = idx + r - 1
                    min_energy = cum_energy[idx + r-1, c-1]

                img_coord = new_to_img[r,c]
                if img_coord in self.pixels_to_remove:
                    cum_energy[r,c] -= 10000
                else:
                    cum_energy[r,c] += min_energy

        return (cum_energy, backtrack)

    def remove_seam_h(self, images, cum_energy, backtrack):
        new_image, annotated_image, new_to_img = images

        rows, cols = new_image.shape[:2]
        output = np.zeros((rows-1, cols, 3), dtype=new_image.dtype)
        mod_new_to_img = np.zeros((rows-1, cols, 3), dtype=new_to_img.dtype)

        r = np.argmin(cum_energy, axis=0)[-1]
        for c in reversed(range(cols)):
            img_coord = new_to_img[r,c]
            mod_new_to_img = np.delete(new_to_img[:, c], [r])
            if img_coord in self.pixels_to_remove:
                self.pixels_to_remove.remove(img_coord)

            img_r, img_c = img_coord
            for i in range(3):
                output[:, c, i] = np.delete(new_image[:, c, i], [r])
                annotated_image[img_r, img_c, i] = 0

            r = backtrack[r, c]

        return (output, annotated_image, new_to_img)
