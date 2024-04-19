import pyscreenshot as ImageGrab
import pygetwindow as gw

if __name__ == "__main__": 
    # Get the window with the title "Your Window Title"
    window = gw.getWindowsWithTitle("BlueStacks App Player")[0]

    # Get the window coordinates
    x1, y1, x2, y2 = window.left, window.top, window.left + window.width, window.top + window.height

    # Capture the specified window
    im = ImageGrab.grab(bbox=(int(x1+window.width*0.04), int(y1+window.height*0.31), int(x2-window.width*0.075), int(y2-window.height*0.18)))
    im.show()