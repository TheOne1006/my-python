from __future__ import print_function
import os, sys
from PIL import Image

# PIL 支持大量图格式，通过 save方法时， 保存文件名会作为格式参考

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpeg"
    if infile != outfile:
        try:
            # png 透明 需要特殊处理
            im = Image.open(infile)
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, im)
            bg.save(outfile)
        except IOError:
            print("cannot convert", infile)
