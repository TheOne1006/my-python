# 图像运算

将数据组的数值类型定义为`dtype=np.uint8`, 可以保证数组值的范围在`[0, 255]` 之间。

1. 加法运算 `+`
    - `像素a + 像素b = mod(a+b, 256)`
    - `cv2.add(图像a, 图像b), a + b > 255 则为 255` 
        - a 和 b 的大小 和类型 必须保持一致
    - `cv2.add(图像a, 数值c)`
2. 加权和 `cv2.addWeighted`
    - 计算两幅图像的像素值和，将每幅图形的像素值和，将权重考虑进来
    - `dst = saturate(src1 * α + src2 * β + γ)`
        - saturate 取饱和值最大值
        - src1 和 src2 两张图片大小，类型相同
    - `dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)`
        - alpha 和 beta 分别是 src1, src2 的系数
3. 位运算
    - `dst = cv2.bitwise_add(src1, src2 [,mask])` 与
        - dst 具有相同大小的array 输出
        - src1, src2 表示  array 或 scalar 类型
        - mask 可选操作掩码
    - `cv2.bitwise_or()`  或
    - `cv2.bitwise_xor()` 异或
    - `cv2.bitwise_not()` 取反
4. 掩摸
5. 图像与数值的运算
    - `cv2.add()`
6. 位平面解析
    - 




### 加法运算符

`a + b = mod(a+b, 256)`