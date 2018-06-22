import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Administrator/Desktop/show.jpg')

GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(GrayImage, 200, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(GrayImage, 127, 255, cv2.THRESH_TOZERO_INV)
titles = ['Gray Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
cv2.imshow("test",thresh1)
cv2.imwrite("C:/Users/Administrator/Desktop/show_grey.jpg",thresh1)
cv2.waitKey(0)
images = [GrayImage, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(6):
#     plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()

