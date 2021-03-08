# cv.line()，cv.circle()，cv.rectangle()，cv.ellipse()，cv.putText()

import numpy as np
import cv2 as cv

# 创建黑色图像

img = np.zeros((512, 512, 3), np.uint8)

# 绘制一条厚度为5的蓝色对角线,
cv.line(img,(0,0),(511,511),(255,0,0),5)

# 矩形  左上角 和 右下角, 颜色， 宽度
cv.rectangle(img,(384,0),(510,128),(0,255,0), 3)


# 原型, 圆心半径
cv.circle(img,(447,63), 63, (0,0,255), -1)

# 椭圆
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)


# 多边形 
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

# 添加文本信息
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()