## 角点

1. 信息更丰富
2. 边界与角点


#### 角点检测基本原理

![title](images/harris_2.png)

1. 平面时，上下左右移动 灰度值基本相似
2. 边界时，上下/左右移动时，有一组灰度基本相似
3. 角点时, 任何一方向都有明显变化



### 图像尺寸空间

人类眼睛中， 离得远也能清楚判断物体。因此是一种特征提取的方式。


##### 模拟 

1. 高斯模糊
2. 多分辨率金字塔
3. 高斯差分金字塔(DOG)



依赖 'opencv-contrib-python'



`SIFT` 存在专利无法运行  

https://zhuanlan.zhihu.com/p/109152430?from_voters_page=true

## 创建指定的

```bash
conda create --name py3.6 python=3.6 numpy

pip install opencv-python==3.4.2.16 
pip install opencv-contrib-python==3.4.2.16

 conda activate py3.6
```
