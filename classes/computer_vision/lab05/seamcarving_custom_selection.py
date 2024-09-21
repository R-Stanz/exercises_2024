from handlers import Seamcarving
from skimage import io

seamcarving = Seamcarving('images/balls.jpg')
seamcarving.select_on_image()
img, new_img, img_annoted = seamcarving.remove_selection()
