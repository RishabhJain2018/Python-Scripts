# Script to Import Images From subfolders to a single folder.

import os
from os import *
import cv2

folder_path = "/home/rishabh/Downloads/lfw2/"
destination_path="/home/rishabh/Downloads/images/"

images_folder = listdir(folder_path)
for folder in images_folder:
	for img in os.listdir(folder_path+folder):
		image = cv2.imread(folder_path +folder+"/"+ str(img))
		cv2.imwrite(destination_path+img,image)

print "All Files Moved."
