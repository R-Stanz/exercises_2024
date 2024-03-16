import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

#abre imagem
filename = sys.argv[1]
im = cv2.imread(filename)

#converte cores
im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

#split
#im_r,im_g,im_b = cv2.split(im)
im_h = im[:,:,0]
im_s = im[:,:,1]
im_v = im[:,:,2]

#combina as imagens
im = cv2.merge([im_h,im_s,im_v])

#modicacoes na imagem
for row_index in range(len(im_h)):
    for line_index in range(len(im_h[row_index])):
        hue_val = im_h[row_index][line_index]

        if ((hue_val >= 94) and (hue_val <= 110) and (line_index < 570)):
            im_h[row_index][line_index] -= 40
            im_s[row_index][line_index] -= 110
        
        elif ((hue_val <= 80) and (line_index > 575)):

            if ((hue_val >= 24) and (hue_val <= 40)):
                im_h[row_index][line_index] += 50
            elif (hue_val >= 24):
                im_h[row_index][line_index] += 40

            im_s[row_index][line_index] += 90

#combina as imagens
new_im = cv2.merge([im_h,im_s,im_v])

#mostra imagens
imagens = [im_h,im_s,im_v]



x_values = np.arange(256)

plt.subplot(2,3,1),plt.imshow(imagens[0],cmap = 'gray')
plt.subplot(2,3,2),plt.imshow(imagens[1],cmap = 'gray')
plt.subplot(2,3,3),plt.imshow(imagens[2],cmap = 'gray')
plt.subplot(2,3,4),plt.imshow(cv2.cvtColor(im, cv2.COLOR_HSV2RGB))
plt.subplot(2,3,5),plt.imshow(cv2.cvtColor(new_im, cv2.COLOR_HSV2RGB))



plt.show()

cv2.imwrite("mod.jpg", cv2.cvtColor(new_im, cv2.COLOR_HSV2BGR))












