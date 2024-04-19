import pyscreenshot as ImageGrab
import pygetwindow as gw
import os
from PIL import Image

class Screenshot():
    
    def __init__(self, grid=5):
        self.window = gw.getWindowsWithTitle("BlueStacks App Player")[0]
        self.grid = grid

    def getWindowCoordinates(self):
        self.x1, self.y1, self.x2, self.y2 = self.window.left, self.window.top, self.window.left + self.window.width, self.window.top + self.window.height

    def takeScreenshot(self):
        # Capture the specified window
        im = ImageGrab.grab(bbox=(int(self.x1+self.window.width*0.04), int(self.y1+self.window.height*0.31), int(self.x2-self.window.width*0.075), int(self.y2-self.window.height*0.18)))
        
        image_save_path = os.getcwd() + '\Images\\'
        im.save(image_save_path + 'Torus.PNG')

    def takeScreenshotParts(self):
        image_save_path = os.getcwd() + '\Images\\Torus.PNG'

        im = Image.open(image_save_path)
        
        width, height = im.size

        part_width = width // self.grid
        part_height = height // self.grid

        coordinates = []
        for i in range(0, self.grid):
            for j in range(0, self.grid):
                x1 = j * part_width + part_width*0.25
                y1 = i * part_height + part_height*0.25
                x2 = x1 + part_width - part_width*0.5
                y2 = y1 + part_height - part_height*0.5
                coordinates.append((x1, y1, x2, y2))

        for i, coord in enumerate(coordinates):
            x1, y1, x2, y2 = coord
            im.crop((x1, y1, x2, y2)).save(os.getcwd() + '\Images\\' + str(i+1) + '.PNG')
        