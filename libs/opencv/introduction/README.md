# 入门

1. 图像处理基本操作
    - `retval = cv2.imread(filename[,flags])`
    - `cv2.imshow("before",img)`
    - `cv2.waitKey()`
    - `cv2.destroyAllWindows()`
2. 像素处理
    - `BGR`
    - `img[0,0]`
    - `img[0, 0, 0]`
3. numpy 访问像素 
    - `np_arr.itemset((1,0,2),255)`
    - `np_arr.itemset((1,2),255)`
    - `np_arr.item(1,2)`
4. 感兴趣区域(ROI) region of Interest
    - 部分像素的截取复制
    - `img[200:400, 200:400]`
    - `dollar[160:340,200:300]=face`
5. 通道操作
    - 通道拆分
        - `b=img[:,:,0]`
        - `g=img[:,:,1]`
        - `r=img[:,:,2]`
        - `lena[:,:,0]=0` 将图片的b通道设置为0
        - `b,g,r = cv2.split(img)`
    - 通道合并
        - `rgb=cv2.merge([r,g,b])`
    - 获取图像属性
        - 大小、类型 
        - shape
            - 彩色 `color.shape= (512, 512, 3)`
            - 黑白 `gray.shape= (256, 256)`
        - size 像素数目
        - dtype 数据类型

## 图像处理基本操作

```bash
retval = cv2.imread(filename[,flags])
```

- retval: 读取到的图像，未读取到则返回 `<class 'NoneType'>None`
- flags: 读取标记
    - cv2.IMREAD_UNCHANGED -1 原图保持不变
    - cv2.IMREAD_GRAPYSCALE 0 灰度图像
    - cv2.IMREAD_COLOR 1  BGR图像
    - 等
- 支持多种图像格式

