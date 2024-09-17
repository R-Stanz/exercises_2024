import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, transform
from skimage import filters
from skimage import color

def calculate_energy(image):
    # Convertendo a imagem para escala de cinza
    gray_image = color.rgb2gray(image)
    # Calculando o gradiente da imagem
    energy = np.abs(filters.sobel_h(gray_image))
    return energy

def find_seam(energy):
    # A energia acumulada ao longo do caminho mínimo
    rows, cols = energy.shape
    cum_energy = energy.copy()
    backtrack = np.zeros_like(cum_energy, dtype=int)

    # Preenchendo a matriz de energia acumulada
    for c in range(1, cols):
        for r in range(rows):
            # Bordas são tratadas separadamente
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
            cum_energy[r, c] += min_energy

    return cum_energy, backtrack

def blank_a_row(blanks_by_cols, row, col, number_of_rows):
    image_row = row

    i = 0
    while i < len(blanks_by_cols[col]) and image_row >= blanks_by_cols[col][i] and \
        image_row < number_of_rows - 1:
        
            image_row += 1
            i += 1

    blanks_by_cols[col].insert(i, image_row)
    return image_row, blanks_by_cols


def remove_seam(images, cum_energy, backtrack):
    new_image, annotated_image, blanks_by_cols = images

    rows, cols = new_image.shape[:2]
    output = np.zeros((rows-1, cols, 3), dtype=new_image.dtype)

    r = np.argmin(cum_energy, axis=0)[-1]
    for c in reversed(range(cols)):
        image_r, blanks_by_cols = blank_a_row(blanks_by_cols, r, c, rows)

        for i in range(3):
            output[:, c, i] = np.delete(new_image[:, c, i], [r])
            annotated_image[image_r, c, i] = 0
        r = backtrack[r, c]

    return (output, annotated_image, blanks_by_cols)

def seam_carving(image, num_seams):
    annotated_image = image.copy()

    cols = image.shape[1]
    blanks_by_cols = [[] for i in range(cols)]

    images = (image, annotated_image, blanks_by_cols)
    for _ in range(num_seams):
        energy = calculate_energy(images[0])
        cum_energy, backtrack = find_seam(energy)
        images = remove_seam(images, cum_energy, backtrack)

    return images[:2]


# Carregar a imagem
img = io.imread('images/balls.jpg')

# Aplicar o seam carving
new_image, new_img = seam_carving(img, 130)  # Reduz 20 costuras verticais

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
