#!/usr/bin/python

import os, glob, Image

pic_list = []

pic_list = glob.glob('*.JPG')
pic_list.sort()

print (len(pic_list), 'images found...')
for temp in pic_list:
    print (temp)


cmd = 'fulla -g 0.0216776:-0.0799067:0.0566601:1 '
for temp in pic_list:
    repair = cmd + temp
    os.popen(repair).read()


