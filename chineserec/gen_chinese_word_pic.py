# -*-coding:utf-8-*-
import os
import pygame

chinese_dir = 'chinese'
if not os.path.exists(chinese_dir):
    os.mkdir(chinese_dir)

font_dir = 'C:/Windows/Fonts'

font_files = os.listdir(font_dir)

pygame.font.init()
start, end = (0x4E00, 0x9FA5)  # 汉字编码范围
for codepoint in range(int(start), int(end)):
    word = chr(codepoint)
    # for i in range(0, len(font_files)):
    font = pygame.font.SysFont('simhei', 64)
    # 当前目录下要有微软雅黑的字体文件msyh.ttc,或者去c:\Windows\Fonts目录下找
    # 64是生成汉字的字体大小
    rtext = font.render(word, True, (0, 0, 0), (255, 255, 255))

    print(word.encode("gbk"))
    # print(word.encode().decode('gbk'))
    path = chinese_dir + '/' + word + '_' + 'simhei' + '.png'
    path = path.encode('gbk')
    pygame.image.save(rtext, path)
