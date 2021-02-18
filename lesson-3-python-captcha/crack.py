from PIL import Image

im = Image.open('captcha.gif')

# 将图片转换为8位像素模式
im.convert("P")

# print(im.histogram())

his = im.histogram()
values = {}

for i in range(256):
    values[i] = his[i]

for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:
    print(j, k)