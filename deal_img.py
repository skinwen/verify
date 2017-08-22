import os.path

from PIL import Image

rootdir = "E:\img\gz_fund"

save_patg = "E:\img\gz_fund\grey"

num = 0


def change_to_grey(img):
    box = (5, 1, img.size[0] - 5, img.size[1] - 3)
    region = img.crop(box)
    # region.show()
    width = region.size[0]
    higth = region.size[1]

    for i in range(0, width):
        for j in range(0, higth):
            rgb = region.getpixel((i, j))
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            if r > 128 and g > 128 and b > 128:
                region.putpixel((i, j), (255, 255, 255))
            else:
                region.putpixel((i, j), (0, 0, 0))
    return region


def spilt_img(img):
    width = 14
    higth = 13

    box1 = (0, 2, width, 2 + higth)
    box2 = (13, 2, 13 + width, 2 + higth)
    box3 = (27, 2, 27 + width, 2 + higth)
    box4 = (40, 2, 40 + width, 2 + higth)
    img1 = img.crop(box1)
    # img1.show()
    img2 = img.crop(box2)
    img2 = img.crop(box2)
    # img2.show()
    img3 = img.crop(box3)
    # img3.show()
    img4 = img.crop(box4)
    # img4.show()

    img_list = [img1, img2, img3, img4]

    return img_list

if __name__ == '__main__':
    for i in os.listdir(rootdir):
        if os.path.isfile(os.path.join(rootdir, i)):
            file_name = os.path.join(rootdir, i)
            image = Image.open(file_name)
            img = change_to_grey(image)
            # img.save(save_patg + "\\" + i, "PNG")
            img_list = spilt_img(img)
            for j in img_list:
                j.save("E:\img\gz_fund\lib" + "\\" + str(num) + ".png", "PNG")
                num = num + 1
