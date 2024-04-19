import screenshot
import OCR
import algorithm
import mover



if __name__ == "__main__":
    # grid = 6
    # screenshotter = screenshot.Screenshot(grid)
    # screenshotter.getWindowCoordinates()
    # screenshotter.takeScreenshot()
    # screenshotter.takeScreenshotParts()
    # ocr = OCR.OCR(grid)
    # ocr.detectNumbers()
    # matrix = ocr.createMatrix()
    # algorithm_t = algorithm.TorusAlgorithm(matrix, grid=6)
    # algorithm_t.solveTorus()
    # test = 1

    mover = mover.Mover()
    mover.getWindowCoordinates()
    mover.getColumnCoordinates()  
    mover.getRowCoordinates() 
    # mover.checkCoordinates()
    mover.moveColumnLeft(column=1, moves=2)
    mover.moveColumnRight(column=0, moves=2)
    mover.moveRowUp(row=0, moves=3)
    mover.moveRowDown(row=0, moves=2)
    one = 1