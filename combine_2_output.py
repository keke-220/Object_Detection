from PIL import Image
import os
path = '/home/xiaohan/Desktop/objectDetection/360-Dataset/images/'
path_in = '/home/xiaohan/Desktop/objectDetection/YOLOv3/(2)out/'
path_out = '/home/xiaohan/Desktop/objectDetection/YOLOv3/output/'
for filename in os.listdir(path):
	im = Image.open(path + filename)
	width, height = im.size

	lfile = open(path_in + os.path.splitext(filename)[0] + '_l' + '.txt')
	rfile = open(path_in + os.path.splitext(filename)[0] + '_r' + '.txt')
	outfile = open(path_out + os.path.splitext(filename)[0] + '.txt', 'w+')
	for line in lfile:
		#split_line = line.split(' ')
		#print (split_line[2])
		outfile.write(line)
	for line in rfile:
		split_line = line.split(' ')
		split_line[2] = str(int(int(split_line[2]) + width/2))
		split_line[4] = str(int(int(split_line[4]) + width/2))
		new_line = ' '.join(split_line)
		#print(new_line)
		outfile.write(new_line)
	lfile.close()
	rfile.close()
	outfile.close()
