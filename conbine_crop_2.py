import sys
import os
from PIL import Image

path_l = '/home/xiaohan/Desktop/objectDetection/YOLOv3/output_l/'
path_r = '/home/xiaohan/Desktop/objectDetection/YOLOv3/output_r/'
path_out = '/home/xiaohan/Desktop/objectDetection/YOLOv3/output_l_r/'
for filename in os.listdir(path_l):
  fileroot = filename.split('_')[0]
  im_l = Image.open(path_l + filename)
  im_r = Image.open(path_r + fileroot + '_r' + '.png')
  images = [im_l, im_r]
  widths, heights = zip(*(i.size for i in images))
  total_width = sum(widths)
  max_height = max(heights)

  new_im = Image.new('RGB', (total_width, max_height))

  x_offset = 0
  for im in images:
    new_im.paste(im, (x_offset,0))
    x_offset += im.size[0]

  new_im.save(path_out + fileroot + '.jpg')
