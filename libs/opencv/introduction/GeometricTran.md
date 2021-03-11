# 几何变换

- 缩放 `cv2.resize()`
    - `dst = cv2.resize(src, dsize [,fx[,fy[,interpolation]]])`
    - dst 输出图像
    - src 原始图像
    - dsize 输出图像大小
        - 如果指定，无论是否指定参数 fx,fy 都由参数 dsize 决定图像大小
    - fx 水平缩放比例
    - fy 垂直缩放比例
    - interpolation 代表插值方式
- 翻转 `cv2.flip()`
    - `dst = cv2.flip(src, flipCode)`
    - flipCode 旋转类型
        - 0 绕着x轴翻转
        - 正数 绕着y轴旋转
        - 负数 绕着 x和 y 轴旋转
- 仿射
    - 图像通过一些列几何变化来保持图像的平直性和平行性
    - `cv2.warpAffine()` 
    - 通过变换矩阵 M 实现变换, 
    - 通过 `cv2.getRotationMatrix2D(center, angle, scale)` 获取转换矩阵
        - center 中心点
        - angle 旋转角度
        - scale 缩放大小
    - `cv2.getAffineTransform(p1, p2)` 定义两个平行四边形
        - p1 和 p2 [左上, 右上, 左下]
- 透视
    - `dst = cv2.warpPerspective(src, M, dsize [,flags [,borderMode [,borderVale]]])`
    - M 代表 3x3 变化矩阵
    - dsize 输出图像的尺寸大小
    - flags 插值方法, 默认为 `INTER_LINEAR` 
    - borderMode 边类型, 默认为 `BORDER_CONSTANT`
    - borderValue 边界值, 默认为 0
    - `M = cv2.getPerspectiveTransform(src, dst)`
        - src, dist 代表图像的四个顶点的坐标
- 重映射: 把图像内的像素点放置到另一幅图像内指定位置。
    - `dst = cv2.remap(src, map1, map2, interpolation [,borderMode [,borderValue]])`
        - dst 和 src 具有相同大小和类型
        - map1 参数有两种可能的值
            - 表示`(x,y)` 映射
            - 表示 `CV_16SC2, CV_32FCI, CV_32FC2`
        - map2 根据 map1 变化
        - interpolation 插值方式
        - borderModel 边界模式


## 常量

- `cv2.INTER_NEAREST` 最邻近插值
- `cv2.INTER_LINEAR` 双线性插值 (默认)
- `cv2.INTER_CUBIC` 三次样条插值