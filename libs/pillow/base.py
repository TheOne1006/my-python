from PIL import Image

# 从文件加载图像，使用 Image 模块中的 open 函数
# 返回 一个Image 对象，可以展示实例属性
im = Image.open("test.png")
# 格式, 宽、高, 模式
print(im.format, im.size, im.mode)  # PNG (800, 731) RGBA
print(im)

# 显示图像, 系统展示图片
im.show()


