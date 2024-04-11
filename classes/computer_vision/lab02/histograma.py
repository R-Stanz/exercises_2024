import sys

import cv2
import numpy as np
import matplotlib.pyplot as plt


filename = sys.argv[1]
im = cv2.imread(filename,0)

width = int(im.shape[1] * .5)
height = int(im.shape[0] * .5)
dim = (width, height)
im = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)



#Calcula o histograma
im_hist = cv2.calcHist([im],[0],None,[256],[0,256]) 

#equaliza histograma
im_hist_eq = cv2.equalizeHist(im)

#equaliza histograma por CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
im_hist_clahe = clahe.apply(im)



plt.subplot(321).set_ylabel("Original"), plt.imshow(im,'gray') #imagem original
plt.subplot(322), plt.plot(im_hist)                            #histograma

plt.subplot(323).set_ylabel("Equalizado"), plt.imshow(im_hist_eq, 'gray')   #imagem com histograna equalizado por CDF
plt.subplot(324).set_title(""), plt.hist(im_hist_eq.ravel(),256,[0,256])    #histograma

plt.subplot(325).set_ylabel("Eq. Clahe"), plt.imshow(im_hist_clahe, 'gray') #imagem com histograna equalizado por CLAHE
plt.subplot(326).set_title(""), plt.hist(im_hist_clahe.ravel(),256,[0,256]) #histograma




plt.xlim([0,256])
plt.show()




cv2.imshow('hist_eq_clahe',im_hist_clahe)
cv2.imshow('hist_eq',im_hist_eq)
cv2.imshow('imagem',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
