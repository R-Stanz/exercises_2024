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

def remove_seam(image, cum_energy, backtrack, mask):
    rows, cols, _ = image.shape
    output = np.zeros((rows-1, cols, 3), dtype=image.dtype)
    r = np.argmin(cum_energy, axis=0)[-1]
    for c in reversed(range(cols)):
        for i in range(3):
            output[:, c, i] = np.delete(image[:, c, i], [r])
        r = backtrack[r, c]

        if c not in mask:
            mask[c] = []
        mask[c] += [r]

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
    for col, del_rows in mask.items():
        for row in del_rows:
            for i in range(3):
                new_image[row, col, i] = 0

    return new_image

# Carregar a imagem
img = io.imread('images/balls.jpg')

# Aplicar o seam carving
mask, new_image = seam_carving(img, 20)  # Reduz 20 costuras verticais

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
