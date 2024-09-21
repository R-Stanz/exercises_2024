import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, transform
from skimage import filters
from skimage import color

def calculate_energy(image):
    gray_image = color.rgb2gray(image)
    energy = np.abs(filters.sobel_v(gray_image))
    return energy

def find_seam(energy):
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
            cum_energy[r, c] += min_energy

    return cum_energy, backtrack


def blank_a_col(blanks_by_rows, row, col, number_of_cols):
    image_col = col

    i = 0
    while i < len(blanks_by_rows[row]) and image_col >= blanks_by_rows[row][i] and \
        image_col < number_of_cols - 1:
        
            image_col += 1
            i += 1

    blanks_by_rows[row].insert(i, image_col)
    return image_col, blanks_by_rows

def remove_seam(images, cum_energy, backtrack):
    new_image, annotated_image, blanks_by_rows = images

    rows, cols = new_image.shape[:2]
    output = np.zeros((rows, cols - 1, 3), dtype=new_image.dtype)

    c = np.argmin(cum_energy[-1])
    for r in reversed(range(rows)):
        image_c, blanks_by_rows = blank_a_col(blanks_by_rows, r, c, cols)

        for i in range(3):
            output[r, :, i] = np.delete(new_image[r, :, i], [c])
            annotated_image[r, image_c, i] = 0
        c = backtrack[r, c]

    return (output, annotated_image, blanks_by_rows)

def seam_carving(image, num_seams):
    annotated_image = image.copy()

    rows = image.shape[0]
    blanks_by_rows = [[] for i in range(rows)]

    images = (image, annotated_image, blanks_by_rows)
    for _ in range(num_seams):
        energy = calculate_energy(images[0])
        cum_energy, backtrack = find_seam(energy)
        images = remove_seam(images, cum_energy, backtrack)

    return images[:2]


# Carregar a imagem
img = io.imread('images/balls.jpg')

# Aplicar o seam carving
new_image, new_img  = seam_carving(img, 130)  # Reduz 20 costuras verticais

# cv2.imshow('original_image', img)
# cv2.imshow('new_image', new_image)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Mostrar a imagem original e a modificada
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 5))
ax[0].imshow(img)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(new_image)
ax[1].set_title('Seam Carved Image')
ax[1].axis('off')

ax[2].imshow(new_img)
ax[2].set_title('Seam Carved Image - Paths')
ax[2].axis('off')

plt.tight_layout()
plt.show()
