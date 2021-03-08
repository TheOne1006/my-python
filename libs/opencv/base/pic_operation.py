import numpy as numpy
import cv2 as cv

img = cv.imread('dora.png')

# 获取像素点
# 你可以通过行和列坐标来访问像素值。
# 对于 BGR 图像，它返回一个由蓝色、绿色和红色值组成的数组。
# 对于灰度图像，只返回相应的灰度。
px  =  img[100, 100]

# [47 47 47]
print(px) 