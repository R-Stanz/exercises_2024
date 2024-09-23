from handlers import Seamcarving
from skimage import io
import matplotlib.pyplot as plt

seamcarving = Seamcarving('images/balls.jpg')
seamcarving.select_on_image()
print(len(seamcarving.pixels_to_remove))
img, new_img, img_annotated = seamcarving.remove_selection()

io.imsave("img.png", img)
io.imsave("new_img.png", new_img)
io.imsave("annotated.png", img_annotated)
'''
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 5))
ax[0].imshow(img)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(img_annotated)
ax[1].set_title('Seam Carved Image')
ax[1].axis('off')

ax[2].imshow(new_img)
ax[2].set_title('Seam Carved Image - Paths')
ax[2].axis('off')

plt.tight_layout()
plt.show()
'''
