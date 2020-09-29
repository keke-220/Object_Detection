# objectDetection
Code for detecting target objects using YOLO (pytorch)
Following preprocessing methods for 360-degree images are used:
1. Split original image from the middle, detect individually and combine the outputs
2. Cut top and bottom, split the rest to 4 square images, detect individually and combine the outputs
