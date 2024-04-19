import screenshot
import OCR
import algorithm

algorithm_t = algorithm.TorusAlgorithm(None, grid=6)

if __name__ == "__main__":
    # grid = 5
    # screenshotter = screenshot.Screenshot(grid)
    # screenshotter.getWindowCoordinates()
    # screenshotter.takeScreenshot()
    # screenshotter.takeScreenshotParts()
    # ocr = OCR.OCR(grid)
    # ocr.detectNumbers()
    # matrix = ocr.createMatrix(grid=5)
    # test = 1

    algorithm_t.solveTorus()
    test = 1