## README

base on: <https://www.lanqiao.cn/courses/370/learning/?id=1191>

### ENV

python 3.7
pillow 8.1

### script

```bash
# 输出到 console 中
python ascii.py ascii_dora.png

# 小羊
python ascii.py test.png -o sleep.txt
```


### KEY

1. 使用 argparse 解析参数
2. rgb => 灰度 => 映射字符
    -  首先将 RGB 值转为灰度值，然后使用灰度值映射到字符列表中的某个字符。