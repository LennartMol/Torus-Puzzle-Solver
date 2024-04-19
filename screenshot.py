import pyscreenshot as ImageGrab
import pygetwindow as gw
import os

class Screenshot():
    
    def __init__(self):
        self.window = gw.getWindowsWithTitle("BlueStacks App Player")[0]

    def getWindowCoordinates(self):
        self.x1, self.y1, self.x2, self.y2 = self.window.left, self.window.top, self.window.left + self.window.width, self.window.top + self.window.height

    def takeScreenshot(self):
        # Capture the specified window
        im = ImageGrab.grab(bbox=(int(self.x1+self.window.width*0.04), int(self.y1+self.window.height*0.31), int(self.x2-self.window.width*0.075), int(self.y2-self.window.height*0.18)))
        
        image_save_path = os.getcwd() + '\Images\\'
        im.save(image_save_path + 'Torus.PNG')