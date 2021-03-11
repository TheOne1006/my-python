import cv2 as cv
import numpy as np


img1 = cv.imread('img.png')
img2 = cv.imread('dora.png')


width, height, other = img2.shape
offsetw = 200
offseth = 200
img3 = img1[offsetw:width+offsetw, offseth:height+offseth]

# 第一幅画权重为 0.7
# 大小一致才能合并
dst = cv.addWeighted(img2, 0.7, img3, 0.3, 0)
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()