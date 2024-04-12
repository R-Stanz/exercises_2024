import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

def find_first_black_pixel_index(image):
    first_black_pixel_index = np.where(image == 0)
    first_black_pixel_line = first_black_pixel_index[0][0]
    first_black_pixel_col = first_black_pixel_index[1][0]
    return (first_black_pixel_line, first_black_pixel_col)

head_filename = sys.argv[1]
stick_filename = sys.argv[2]

im_height = 300
im_width = 300

im = np.full((im_height, im_width), 255).astype('uint8')

# Stickman's Head
head_img = cv2.imread(head_filename)
head_im = cv2.cvtColor(head_img, cv2.COLOR_RGB2GRAY)

head_width = head_im.shape[1] 
head_height = head_im.shape[0]

first_black_pixel_line, first_black_pixel_col = find_first_black_pixel_index(head_im)

last_black_pixel_line_reversed, last_black_pixel_col_reversed = find_first_black_pixel_index(np.fliplr(head_im[::-1]))

last_black_pixel_line = head_height - 1 - last_black_pixel_line_reversed
last_black_pixel_col  = head_width  - 1 - last_black_pixel_col_reversed

head_height = last_black_pixel_line - first_black_pixel_line

left_padding = int((im_width - 1 - head_width) / 2) 

for h in range(first_black_pixel_line, last_black_pixel_line + 1):
    for w in range(head_width):
        im[h - first_black_pixel_line][left_padding + w] = head_im[h][w]


# Stickman's Body

stick_img = cv2.imread(stick_filename)
stick_im = cv2.cvtColor(stick_img, cv2.COLOR_RGB2GRAY)

body_width = head_im.shape[1] 
body_height = head_im.shape[0]

first_black_pixel_line, first_black_pixel_col = find_first_black_pixel_index(stick_im)

last_black_pixel_line_reversed, last_black_pixel_col_reversed = find_first_black_pixel_index(np.fliplr(stick_im[::-1]))

last_black_pixel_line = body_height - 1 - last_black_pixel_line_reversed
last_black_pixel_col  = body_width  - 1 - last_black_pixel_col_reversed

body_height = last_black_pixel_col - first_black_pixel_col
stickman_height = head_height + body_height * (1 + 2 * 0.75 / np.sqrt(2))
top_padding = int((im_height - 1 - stickman_height) / 2)

for i in range(head_height + 1):
    im[i + top_padding] = im[i]
    im[i].fill(255)


body_start_line = head_height + top_padding + 1
body_width = last_black_pixel_line - first_black_pixel_line
left_padding = int((im_width - 1 - body_width) / 2) 

for h in range(body_height + 1):
    body_line   = body_start_line + h 
    stick_col   = first_black_pixel_col + h

    for w in range(body_width + 1):
        body_col    = left_padding + w
        stick_line  = first_black_pixel_line + w 

        im[body_line][body_col] = stick_im[stick_line][stick_col]


# Arms

arm_length = int((last_black_pixel_col - first_black_pixel_col) * 0.75)
arm_thickness = last_black_pixel_line - first_black_pixel_line
left_padding = int((im_width - 1 - 2 * arm_length - body_width) / 2) + 1

for i in range(2): 
    for l in range(arm_length + 1):
        arm_len  = left_padding + l 
        stick_col   = first_black_pixel_col + l

        for t in range(arm_thickness + 1):
            arm_thick   = body_start_line + t
            stick_line  = first_black_pixel_line + t

            im[arm_thick][arm_len] = stick_im[stick_line][stick_col]

    left_padding += arm_length + body_width


# Legs

#translation (180,100)
#M_translation = np.float32([[1,0,-10],[0,1,-10]])
#head_im = cv2.warpAffine(head_im,M_translation,(width,height))

stick_img = cv2.imread(stick_filename)
stick_im = cv2.cvtColor(stick_img, cv2.COLOR_RGB2GRAY)
stick_im_dst = cv2.imread(stick_filename,0)

print(stick_im)
print(stick_im.shape)

'''
width = im.shape[1]
height = im.shape[0]

#ler todos os pixels da imagem
for c in range(0, width-1):
	for l in range(0, height-1):
		px = im.item(l,c)

		#negativo
		#im_dst.itemset(l,c,255-px)

#		if px > 100:
#			im.itemset(l,c,255)


#redimensiona a imagem
new_width = int(im.shape[1] * .5)
new_height = int(im.shape[0] * .5)
dim = (new_width, new_height)
im_resized = cv2.resize(im, dim, interpolation = cv2.INTER_AREA)


#threshold
ret,im_thresh = cv2.threshold(im,127,255,cv2.THRESH_BINARY)

#mostra imagem com opencv
cv2.imshow('threashold',im_thresh)
cv2.imshow('resized',im_resized)
'''
cv2.imshow('image',im)
cv2.imshow('circle',head_im)
cv2.imshow('line',stick_im)
cv2.waitKey(0)
cv2.destroyAllWindows()







