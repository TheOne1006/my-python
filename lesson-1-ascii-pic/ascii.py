# -*- coding=utf-8 -*-

from PIL import Image
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')  # 输出文件
parser.add_argument('--width', type=int, default=80)  # 输出字符画宽
parser.add_argument('--height', type=int, default=80)  # 输出字符画高

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '

    # 获取字符集的长度，这里为 70, 
    # TODO: len 长度固定，怎么简化 运算？
    length = len(ascii_char)

    # 简化的灰度值公式
    # 将 RGB 值转为灰度值 gray，灰度值范围为 0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # 灰度值范围为 0-255，而字符集只有 70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


# 被当作 模块 import 的时候不会执行

if __name__ == '__main__':

    #  使用 PIL 的 Image.open 打开图片文件，获得对象 im
    im = Image.open(IMG)

    # 使用 resize 调整 宽高, NEAREST 表示低质量画质
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    # 逐个像素 写入 txt
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    # 输出到 控制台
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
