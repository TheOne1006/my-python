# 图片上的算术运算
import cv2 as cv
import numpy as np

x = np.uint8([250])


y = np.uint8([10])

print(f"x: {x}, y: {y}")

# OpenCV加法是饱和运算  260 => 250
print(cv.add(x, y))

# np求摩
# 250+10 = 260 % 256 = 4
print(x + y)