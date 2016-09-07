from PIL import Image
import os


class ImageTools(object):
    def __init__(self, in_path, out_path, quality=75, im_format=".jpg", im_width=2048):
        self.im_width = im_width
        self.quality = quality
        self.out_path = out_path
        self.in_path = in_path
        self.im_format = im_format

    def resize(self):
        count = 0
        for fn in os.listdir(str(self.in_path)):
            namefile = fn.split(".")
            count += 1
            print fn
            try:
                with Image.open(str(self.in_path) + "/" + str(fn)) as im:
                    if im.width > self.im_width:
                        x = im.width
                        y = im.height
                        cons = float(y) / x
                        my_height = self.im_width * cons
                        im = im.resize((self.im_width, int(my_height)), resample=0)
                    im.save(str(self.out_path) + "/" + str(namefile[0]) + ".jpg", quality=self.quality)
            except IOError:
                pass

        print count


ImageTools("D:/DOWNLOAD/textures2", "D:/DOWNLOAD/reduced2").resize()
