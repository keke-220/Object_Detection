import sys 
import os
import shutil
from PIL import Image


path_in = '/home/xiaohan/Desktop/objectDetection/YOLOv3/output/'
path_out_1 = '/home/xiaohan/Desktop/objectDetection/YOLOv3/output_1/'

for filename in os.listdir(path_in):
    file_end = filename.split('_')[1]
    if file_end == '_1.png':
        shutil.move("path_in"+filename, "path_out_1"+filename)

    if file_end == '_2.png':
        shutil.move("path_in"+filename, "path_out_2"+filename)
    if file_end == '_3.png':
        shutil.move("path_in"+filename, "path_out_3"+filename)
    if file_end == '_3.png':
        shutil.move("path_in"+filename, "path_out_3"+filename)
