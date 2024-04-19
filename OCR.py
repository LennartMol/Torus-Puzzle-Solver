from PIL import Image
import os

import pytesseract

# get current working directory
path_to_image = os.getcwd() + '\Images\\'
grid = 6
path_to_image_list = []
for image_nr in range(1, grid*grid+1):
    path_to_image_list.append(path_to_image + str(image_nr) + '.PNG')

number_detected_list = []

for path in path_to_image_list:
    number_detected_list.append(pytesseract.image_to_string(Image.open(path), config="--psm 10"))

# print each detected number with each image path
for i in range(len(number_detected_list)):
    print(path_to_image_list[i] + ' : ' + number_detected_list[i])
