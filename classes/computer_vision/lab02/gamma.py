import sys
import cv2
import numpy as np

from cv_utils import waitKey


def gamma_correction(img, gamma,c=1.0):
   i = img.copy()
   i[:,:,:] = 255*(c*(img[:,:,:]/255.0)**(1.0 / gamma))
   return i


def gamma_correction_LUT(img, gamma,c=1.0):

	#cria uma Lookup Table (LUT)
	GAMMA_LUT = np.array([c*((i / 255.0) ** (gamma)) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# aplica a transformação usando LUT
	return cv2.LUT(img, GAMMA_LUT)


def callback_trackbar(x):
    try:
        gamma = cv2.getTrackbarPos('gamma','image')
        im_gamma = gamma_correction_LUT(im, gamma*0.5)
        cv2.imshow('image',im_gamma)
    except:
        return

def new_image(*args):
    cv2.imwrite("mod_jet.jpg", cv2.cvtColor(im, cv2.COLOR_RGB2BGR))



#abre imagem
filename = sys.argv[1]
print(filename)
im = cv2.imread(filename)


cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.createTrackbar('gamma','image',0,100,callback_trackbar)
cv2.createButton("Generate Image", new_image, None, cv2.QT_PUSH_BUTTON,1)


cv2.imshow('image',im)
waitKey('image', 27) #27 = ESC	












