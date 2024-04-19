import screenshot
import OCR
import algorithm
import time



if __name__ == "__main__":
    grid = 6
    screenshotter = screenshot.Screenshot(grid)
    screenshotter.getWindowCoordinates()
    screenshotter.takeScreenshot()
    screenshotter.takeScreenshotParts()
    ocr = OCR.OCR(grid)
    ocr.detectNumbers()
    matrix = ocr.createMatrix()
    time.sleep(1)
    algorithm_t = algorithm.TorusAlgorithm(matrix, grid=6)
    algorithm_t.solveTorus()