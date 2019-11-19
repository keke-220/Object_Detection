from PIL import Image
import os
path = '/home/xiaohan/Desktop/objectDetection/360-Dataset/images/'
path_out = '/home/xiaohan/Desktop/objectDetection/360-Dataset/split_to_2/'
for filename in os.listdir(path):
	im = Image.open(path + filename)
	width, height = im.size   # Get dimensions

	left = 0
	top = 0
	right = width/2
	bottom = height

	# Crop the center of the image
	newIm_l = im.crop((left, top, right, bottom))
	newIm_l.save(path_out + os.path.splitext(filename)[0] + '_l' + '.jpg')
	newIm_r = im.crop((right, top, width, bottom))
	newIm_r.save(path_out + os.path.splitext(filename)[0] + '_r' + '.jpg')






