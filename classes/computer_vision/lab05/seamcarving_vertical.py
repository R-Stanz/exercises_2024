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
    energy = np.abs(filters.sobel_v(gray_image))
    return energy

def find_seam(energy):
    # A energia acumulada ao longo do caminho mínimo
    rows, cols = energy.shape
    cum_energy = energy.copy()
    backtrack = np.zeros_like(cum_energy, dtype=int)

    # Preenchendo a matriz de energia acumulada
    for r in range(1, rows):
        for c in range(cols):
            # Bordas são tratadas separadamente
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

def remove_seam(image, cum_energy, backtrack, mask):
    rows, cols, _ = image.shape
    output = np.zeros((rows, cols - 1, 3), dtype=image.dtype)
    c = np.argmin(cum_energy[-1])
    for r in reversed(range(rows)):
        for i in range(3):
            output[r, :, i] = np.delete(image[r, :, i], [c])
        c = backtrack[r, c]

        if r not in mask:
            mask[r] = []
        mask[r] += [c]

    return mask, output

def seam_carving(image, num_seams):
    mask = {}
    for _ in range(num_seams):
        energy = calculate_energy(image)
        cum_energy, backtrack = find_seam(energy)
        mask, image = remove_seam(image, cum_energy, backtrack, mask)
    return mask, image

def apply_mask(mask, image):
    new_image = image.copy()
    for row, del_cols in mask.items():
        for col in del_cols:
            for i in range(3):
                new_image[row, col,i] = 0
    return new_image

# Carregar a imagem
img = io.imread('images/balls.jpg')

# Aplicar o seam carving
mask, new_image = seam_carving(img, 40)  # Reduz 20 costuras verticais

new_img = apply_mask(mask, img)

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
