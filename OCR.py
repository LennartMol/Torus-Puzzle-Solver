from PIL import Image
import os

import pytesseract

grid = 5

path_to_image_parts = os.getcwd() + '\Images\\'

path_to_image_list = []
for image_nr in range(1, grid*grid+1):
    path_to_image_list.append(path_to_image_parts + str(image_nr) + '.PNG')

number_detected_list = []

for path in path_to_image_list:
    number_detected_list.append(pytesseract.image_to_string(Image.open(path), config="--psm 0"))

# print each detected number with each image path
for i in range(len(number_detected_list)):
    print(path_to_image_list[i] + ' : ' + number_detected_list[i])
