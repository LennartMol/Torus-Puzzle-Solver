import pygetwindow as gw
import pyscreenshot as ImageGrab
import os
import pyautogui

class Mover():
    
    def __init__(self, grid=6):
        self.window = gw.getWindowsWithTitle("BlueStacks App Player")[0]
        self.height = 0
        self.width = 0
        self.bbox = 0
        self.grid = grid
        self.column_coordinates = []
        self.row_coordinates = []
        pyautogui.PAUSE = 0.01685

    def getWindowCoordinates(self):
        self.x1, self.y1, self.x2, self.y2 = self.window.left, self.window.top, self.window.left + self.window.width, self.window.top + self.window.height
        self.bbox = (int(self.x1+self.window.width*0.04), int(self.y1+self.window.height*0.31), int(self.x2-self.window.width*0.075), int(self.y2-self.window.height*0.18))
        self.height = self.bbox[3] - self.bbox[1]
        self.width = self.bbox[2] - self.bbox[0]

    def getColumnCoordinates(self):
        first_column_x = int(self.bbox[0] + self.width * 0.5)
        first_column_y = int(self.bbox[1] + self.height/self.grid/2)
        self.column_coordinates.append((first_column_x, first_column_y))
        for i in range(1, self.grid):
            column_x = first_column_x
            column_y = int(first_column_y + self.height/self.grid*i)
            self.column_coordinates.append((column_x, column_y))

    def getRowCoordinates(self):
        first_row_x = int(self.bbox[0] + self.width/self.grid/2)
        first_row_y = int(self.bbox[1] + self.height * 0.5)
        self.row_coordinates.append((first_row_x, first_row_y))

    def moveColumnLeft(self, column=0, moves=1):
        for noMoves in range(0, moves):
            pyautogui.moveTo(self.column_coordinates[column][0], self.column_coordinates[column][1])
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(self.column_coordinates[column][0] - (self.width/self.grid), self.column_coordinates[column][1])
            pyautogui.mouseUp(button='left')
    
    def moveColumnRight(self, column=0, moves=1):
        for noMoves in range(0, moves):
            pyautogui.moveTo(self.column_coordinates[column][0], self.column_coordinates[column][1])
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(self.column_coordinates[column][0] + (self.width/self.grid/2), self.column_coordinates[column][1])
            pyautogui.mouseUp(button='left')

    def moveRowUp(self, row=0, moves=1):
        for noMoves in range(0, moves):
            pyautogui.moveTo(self.row_coordinates[row][0], self.row_coordinates[row][1])
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(self.row_coordinates[row][0], self.row_coordinates[row][1] - (self.height/self.grid/2))
            pyautogui.mouseUp(button='left')
    
    def moveRowDown(self, row=0, moves=1):
        for noMoves in range(0, moves):
            pyautogui.moveTo(self.row_coordinates[row][0], self.row_coordinates[row][1])
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(self.row_coordinates[row][0], self.row_coordinates[row][1] + (self.height/self.grid))
            pyautogui.mouseUp(button='left')
    
    def checkCoordinates(self):
        image = 1
        image_save_path = os.getcwd() + '\Images\\'

        for coord in self.column_coordinates:
            # from coord, take screenshot by create a small box around the coordinate (2318, 483), go up 1/6th of the box and down 1/6th of the box, left 1/6th of the box and right 1/6th of the box
            x1 = int(coord[0] - self.width / 6)
            y1 = int(coord[1] - self.height / 6)
            x2 = int(coord[0] + self.width / 6)
            y2 = int(coord[1] + self.height / 6)
            im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            
            im.save(image_save_path + 'Test_column' + str(image) + '.PNG')
            image = image + 1
        image = 1
        for coord in self.row_coordinates:
            # from coord, take screenshot by create a small box around the coordinate (2318, 483), go up 1/6th of the box and down 1/6th of the box, left 1/6th of the box and right 1/6th of the box
            x1 = int(coord[0] - self.width / 6)
            y1 = int(coord[1] - self.height / 6)
            x2 = int(coord[0] + self.width / 6)
            y2 = int(coord[1] + self.height / 6)
            im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            
            im.save(image_save_path + 'Test_row' + str(image) + '.PNG')
            image = image + 1
        