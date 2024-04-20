from PIL import Image
import os
import pytesseract

class OCR():
    
    def __init__(self, grid=6):
        self.grid = grid
        self.number_detected_list = []
        self.debug = True

    def detectNumbers(self):
        path_to_image_parts = os.getcwd() + '\Images\\'

        path_to_image_list = []
        for image_nr in range(1, self.grid*self.grid+1):
            path_to_image_list.append(path_to_image_parts + str(image_nr) + '.PNG')

        if(self.debug):print("Detecting numbers from images...")
        
        image = 1
        for path in path_to_image_list:
            self.number_detected_list.append(pytesseract.image_to_string(Image.open(path), config="--psm 10"))
            if(self.debug):print("In image {} detected number: {}".format(image, self.number_detected_list[image-1]))
            image += 1

    def createMatrix(self):
        matrix = []
        for i in range(0, self.grid):
            column = []
            for j in range(0, self.grid):
                column.append(self.number_detected_list[i*self.grid+j])
            matrix.append(column)
        # remove \n from each element
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                matrix[i][j] = matrix[i][j].replace('\n', '')
        return matrix


