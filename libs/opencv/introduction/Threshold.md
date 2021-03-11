# 阈值处理

剔除图像内像素值高于一定的值 或者小于一定的像素值。

- `retval,dst = threshold(src, thresh, maxval, type)`
    - retval 阈值
    - dst 分割结果图像, 与原始图像 具有相同大小和类型
    - thresh 与设定的阈值
    - maxval
    - type
        - `cv2.THRESH_BINARY` 二值化, 127
        - `cv2.THRESH_BINARY_INV` 反二值化
        - `cv2.THRESH_TRUNC` 截断阈值化 超过  超过阈值 则赋值为阈值
        - `cv2.THRESH_TOZERO_INV` 超过阈值 则为 0
        - `cv2.THRESH_TOZERO` 低于阈值 赋值为 0

# 自适应阈值处理

改进阈值处理技术, 其使用变化的阈值完成对图像的阈值处理

- `dst = cv2.adaptiveThreshold(src, max Value, adaptiveMethod, thresholdType, blockSize, C)`
    - maxValue 最大值
    - adaptiveMethod 自适应方法
    - thresholdType
        - `cv2.ADAPTIVE_THRESH_MEAN_C` 邻域所有像素的权重一致
        - `cv2.ADAPTIVE_THRESH_GAUSSIAN_C` 与邻域各个像素点到中心点的距离有关，通过高斯方式得到各个权重值
    - blockSize 邻域尺寸，通常为 3，5，7
    - C 常量

# Otsu 处理

-  `t,otus = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)`
    - t 是 Otsu 方法计算并得到最优阈值
