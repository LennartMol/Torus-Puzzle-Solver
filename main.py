import screenshot
import OCR
import algorithm
import mover



if __name__ == "__main__":
    grid = 6
    screenshotter = screenshot.Screenshot(grid)
    screenshotter.getWindowCoordinates()
    screenshotter.takeScreenshot()
    screenshotter.takeScreenshotParts()
    ocr = OCR.OCR(grid)
    ocr.detectNumbers()
    matrix = ocr.createMatrix()
    algorithm_t = algorithm.TorusAlgorithm(matrix, grid=6)
    algorithm_t.solveTorus()
    test = 1

    mover = mover.Mover()
    mover.getWindowCoordinates()
    mover.getColumnCoordinates()  
    mover.getRowCoordinates() 

    for move in algorithm_t.moves_list:
        if 'moveColumnLeft' in move:
            column = int(move.split(',')[1].split(' ')[2])
            moves = int(move.split(',')[2].split(' ')[2])
            mover.moveColumnLeft(column, moves)
        elif 'moveColumnRight' in move:
            column = int(move.split(',')[1].split(' ')[2])
            moves = int(move.split(',')[2].split(' ')[2])
            mover.moveColumnRight(column, moves)
        elif 'moveRowUp' in move:
            row = int(move.split(',')[1].split(' ')[2])
            moves = int(move.split(',')[2].split(' ')[2])
            mover.moveRowUp(row, moves)
        elif 'moveRowDown' in move:
            row = int(move.split(',')[1].split(' ')[2])
            moves = int(move.split(',')[2].split(' ')[2])
            mover.moveRowDown(row, moves)