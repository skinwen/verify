import os

from PIL import Image

import deal_img


class image_ocr:
    dict_image = []
    dict_str = []

    def __init__(self, lib_path):
        for i in os.listdir(lib_path):
            file_name = os.path.join(lib_path, i)
            image = Image.open(file_name, 'r')
            # image.show()
            self.dict_image.append(image)
            self.dict_str.append(i[5])

    def ocr(self, img_path):
        image = Image.open(img_path)
        grey_img = deal_img.change_to_grey(image)
        imgs = deal_img.spilt_img(grey_img)

        str = ''
        for i in range(len(imgs)):
            restlt = ''
            img_temp = imgs[i]
            width = img_temp.size[0]
            higth = img_temp.size[1]
            min_diff_count = width * higth
            for j in range(len(self.dict_image)):
                img_dict = self.dict_image[j]
                curr_diff_count = 0

                break_flag = False
                for k in range(0, width):
                    for l in range(0, higth):
                        rgb_img_dict = img_dict.getpixel((k, l))
                        r_dict = rgb_img_dict[0]
                        rgb_temp = img_temp.getpixel((k, l))
                        r_temp = rgb_temp[0]
                        if (r_dict != r_temp):
                            curr_diff_count = curr_diff_count + 1
                        if (curr_diff_count >= min_diff_count):
                            break_flag = True
                            break
                    if (break_flag):
                        break
                if (curr_diff_count < min_diff_count):
                    min_diff_count = curr_diff_count;
                    restlt = self.dict_str[j]
            str = str + restlt
        return str


if __name__ == '__main__':
    image_ocr = image_ocr("E:\img\gz_lib")
    result = image_ocr.ocr('e:\img\gz_fund_excption\\3d54cd1f28d94b7fa3eab6fec6585a8b.png')
    print(result)
