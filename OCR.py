from PIL import Image
import os
import pytesseract

class OCR():
    
    def __init__(self, grid=6):
        self.grid = grid
        self.number_detected_list = []

    def detectNumbers(self):
        path_to_image_parts = os.getcwd() + '\Images\\'

        path_to_image_list = []
        for image_nr in range(1, self.grid*self.grid+1):
            path_to_image_list.append(path_to_image_parts + str(image_nr) + '.PNG')

        for path in path_to_image_list:
            self.number_detected_list.append(pytesseract.image_to_string(Image.open(path), config="--psm 10"))

        # print each detected number with each image path
        for i in range(len(self.number_detected_list)):
            print(path_to_image_list[i] + ' : ' + self.number_detected_list[i])

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


