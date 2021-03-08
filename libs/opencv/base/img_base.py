import numpy as numpy
import cv2 as cv

# cv.IMREAD_COLOR： 加载彩色图像。任何图像的透明度都会被忽视。它是默认标志。
# cv.IMREAD_GRAYSCALE：以灰度模式加载图像
# cv.IMREAD_UNCHANGED：加载图像，包括alpha通道
# 注意 除了这三个标志，你可以分别简单地传递整数1、0或-1。

# 灰色图片
img = cv.imread('dora.png', 0)

# 在窗口中显示图片， 窗口大小自适应
cv.imshow('image', img)

# cv.waitKey()是一个键盘绑定函数。
# 其参数是以毫秒为单位的时间。该函数等待任何键盘事件指定的毫秒。
# 如果您在这段时间内按下任何键，程序将继续运行。
# 如果**0**被传递，它将无限期地等待一次敲击键。它也可以设置为检测特定的按键，例如，如果按下键 a 等，我们将在下面讨论。

# 任意键 退出
cv.waitKey(0)


# 写入图像

# k = cv.waitKey(0)
# if k == 27:         # 等待ESC退出
#     cv.destroyAllWindows()
# elif k == ord('s'): # 等待关键字，保存和退出
#     cv.imwrite('messigray.png',img)
#     cv.destroyAllWindows()


# 只会破坏我们创建的所有窗口。
# 如果要销毁任何特定的窗口，cv.destroyWindow(win_name)
cv.destroyAllWindows()
