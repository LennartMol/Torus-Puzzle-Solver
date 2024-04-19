import screenshot

screenshotter = screenshot.Screenshot()

if __name__ == "__main__":
    screenshotter.getWindowCoordinates()
    screenshotter.takeScreenshot()