import pyscreenshot as ImageGrab
import pygetwindow as gw
import os
from PIL import Image
import PIL.ImageOps
import time

class Screenshot():
    
    def __init__(self, grid=6):
        self.window = gw.getWindowsWithTitle("BlueStacks App Player")[0]
        self.grid = grid
        self.debug = True

    def getWindowCoordinates(self):
        if(self.debug):print("Getting BlueStacks window coordinates...")
        self.x1, self.y1, self.x2, self.y2 = self.window.left, self.window.top, self.window.left + self.window.width, self.window.top + self.window.height
        time.sleep(0.5)
        if(self.debug):print("Left x coordinate: {}, \nTop y coordinate: {}, \nRight x coordinate: {}, \nBottom y coordinate: {}\n".format(self.x1, self.y1, self.x2, self.y2))
        time.sleep(0.5)

    def takeScreenshot(self):
        if(self.debug):print("Taking screenshot of Torus puzzle...")
        im = ImageGrab.grab(bbox=(int(self.x1+self.window.width*0.04), int(self.y1+self.window.height*0.31), int(self.x2-self.window.width*0.075), int(self.y2-self.window.height*0.18)))
        image_save_path = os.getcwd() + '\Images\\Torus.PNG'
        if(self.debug):print("Saving screenshot at: {}\n".format(image_save_path))
        im.save(image_save_path)

    def takeScreenshotParts(self):
        image_save_path = os.getcwd() + '\Images\\Torus.PNG'

        if(self.debug):print("Opening Torus puzzle image...")
        im = Image.open(image_save_path)
        if(self.debug):print("Inverting colors of image...")
        im = PIL.ImageOps.invert(im)
        
        width, height = im.size

        part_width = width // self.grid
        part_height = height // self.grid

        coordinates = []
        for i in range(0, self.grid):
            for j in range(0, self.grid):
                x1 = j * part_width + part_width*0.37
                y1 = i * part_height + part_height*0.37
                x2 = x1 + part_width - part_width*0.7
                y2 = y1 + part_height - part_height*0.7
                coordinates.append((x1, y1, x2, y2))

        for i, coord in enumerate(coordinates):
            x1, y1, x2, y2 = coord
            if(self.debug):print("Cropping and saving number at place {} in seperate image...".format(i+1))
            im.crop((x1, y1, x2, y2)).save(os.getcwd() + '\Images\\' + str(i+1) + '.PNG')
            if(self.debug):print("Saved image at: {}\n".format(os.getcwd() + '\Images\\' + str(i+1) + '.PNG'))
            time.sleep(0.05)
        