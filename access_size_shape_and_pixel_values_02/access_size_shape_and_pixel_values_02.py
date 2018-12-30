import numpy as np
import cv2
img = cv2.imread("images_to_test_scripts/opencv-logo.png", 1)
# img
print(type(img))
len(img)
# 739
len(img[0])
# 600
len(img[0][0])
#3
img.shape
#(739, 600, 3)
img.dtype
#dtype('uint8')

img[10, 5]
#array([255, 255, 255], dtype=uint8)
img[:, :, 0]
#array([[255, 255, 255, ..., 255, 255, 255],
#       [255, 255, 255, ..., 255, 255, 255],
#       [255, 255, 255, ..., 255, 255, 255],
#       ..., 
#       [255, 255, 255, ..., 255, 255, 255],
#       [255, 255, 255, ..., 255, 255, 255],
#       [255, 255, 255, ..., 255, 255, 255]], dtype=uint8)
img.size
#1330200
