from PIL import Image
import glob, os


def resize(dir,save_dir):
    count = 0
    for fn in os.listdir(str(dir)):
        namefile = fn.split(".")
        count +=1
        if namefile[1] in('db',''):
            continue
        print fn
        print count
        im = Image.open(str(dir) + "/" + str(fn))
        if im.width > 2048:
            x=im.width
            y=im.height
            cons= float(y)/x
            myheight = 2048*cons
            im = im.resize((2048, int(myheight)), resample=0)

        im.save(str(save_dir)+ "/" + str(namefile[0]) + ".jpg", "JPEG")

resize("D:/DOWNLOAD/textures2", "D:/DOWNLOAD/reduced2")