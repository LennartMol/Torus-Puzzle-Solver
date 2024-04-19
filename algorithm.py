import random as random

class TorusAlgorithm(): 

    def __init__(self, matrix, grid):
        self.grid = grid
        if matrix is None:
            self.matrix = self.createExampleMatrix(self.grid)
            self.matrix = self.randomizeMatrix(self.matrix)
        else:
            self.matrix = self.addZerosToMatrix(matrix)

        

    def createExampleMatrix(self, grid):
        # generate 6x6 matrix based on grid size
        matrix = []
        for i in range(0, grid):
            column = []
            for j in range(0, grid):
                column.append(str(i*grid+j+1))
            matrix.append(column)
        matrix = self.addZerosToMatrix(matrix)

        return matrix
    
    def addZerosToMatrix(self, matrix):
        # if number is less than 10, add 0 in front
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if int(matrix[i][j]) < 10:
                    matrix[i][j] = "0" + matrix[i][j]
        return matrix
    
    def moveRowUp(self, row, moves):
        for noMoves in range(0, moves):
            temp = self.matrix[0][row]
            for i in range(0, len(self.matrix)-1):
                self.matrix[i][row] = self.matrix[i+1][row]
            self.matrix[len(self.matrix)-1][row] = temp
    
    def moveRowDown(self, row, moves):
        for noMoves in range(0, moves):
            temp = self.matrix[len(self.matrix)-1][row]
            for i in range(len(self.matrix)-1, 0, -1):
                self.matrix[i][row] = self.matrix[i-1][row]
            self.matrix[0][row] = temp
    
    def moveColumnLeft(self, column, moves):
        for noMoves in range(0, moves):
            temp = self.matrix[column][0]
            for i in range(0, len(self.matrix)-1):
                self.matrix[column][i] = self.matrix[column][i+1]
            self.matrix[column][len(self.matrix)-1] = temp

    def moveColumnRight(self, column, moves):
        for noMoves in range(0, moves):
            temp = self.matrix[column][len(self.matrix)-1]
            for i in range(len(self.matrix)-1, 0, -1):
                self.matrix[column][i] = self.matrix[column][i-1]
            self.matrix[column][0] = temp


    def randomizeMatrix(self, matrix):
        # randomize columns
        for i in range(0, len(matrix)):     
            matrix[i] = random.sample(matrix[i], len(matrix[i]))

        # randomize rows
        for row in range(0, len(matrix)):
            # move a rows down by random amount (1-5)
            moveDowns = random.randint(1, len(matrix)-1)
            self.moveRowUp(row, moveDowns)
        
        return matrix
        
            

    def printMatrix(self):
        for i in range(0, len(self.matrix)):
            print(self.matrix[i])
        print()

    def findNumber(self, numberToFind):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if self.matrix[i][j] == numberToFind:
                    foundX = j
                    foundY = i
                    print(numberToFind + " found at: ["+str(foundX+1) +","+ str(foundY+1) + "]\n")
                    return foundX, foundY
 
    def rotateAroundColumn(self, columnToRotateAround):
        
        # rotate around column x
        self.moveColumnRight(columnToRotateAround, 1)
        self.moveRowDown(0, 1)
        self.moveColumnLeft(columnToRotateAround, 1)
        self.moveRowUp(0, 1)
        self.moveRowUp(0, 1)
        self.moveColumnRight(columnToRotateAround, 1)
        self.moveRowDown(0, 1)
        self.moveColumnLeft(columnToRotateAround, 1)

    def moveToCorrectColumn(self, numberToMove, correctColumn):
        foundX, foundY = self.findNumber(numberToMove)

        # if number is not in correct column
        if foundY != correctColumn:
            stepsToMoveY = foundY - correctColumn

            # rotate to correct column
            while stepsToMoveY > 1:
                columnToRotateAround = foundY - 1 
                self.rotateAroundColumn(columnToRotateAround)
                print("Moved "+numberToMove+" up 1 step")
                self.printMatrix()
                foundX, foundY = self.findNumber(numberToMove)
                stepsToMoveY = foundY - correctColumn

            # rotate to correct column
            columnToRotateAround = foundY
            self.rotateAroundColumn(columnToRotateAround)
            print("Moved "+numberToMove+" to final position")
            self.printMatrix()

    def solveTorus(self):
        
        print("\nBegin matrix:")
        self.printMatrix()

        fixRow1 = range(2,7)
        fixRow2 = range(8,13)
        fixRow3 = range(14,19)
        fixRow4 = range(20,25)
        fixRow5 = range(26,31)
        fixRow6 = range(32,37)

        fixRows = [fixRow1, fixRow2, fixRow3, fixRow4, fixRow5, fixRow6]
        for fixRow in range(0, len(fixRows)):

            for numbers in fixRows[fixRow]:
                if numbers < 10:
                    numberToFind = "0" + str(numbers)
                else:
                    numberToFind = str(numbers)
                
                foundX = -1
                foundY = -1

                for i in range(0, len(self.matrix)):
                    for j in range(0, len(self.matrix[i])):
                        if self.matrix[i][j] == numberToFind:
                            foundX = j
                            foundY = i
                            print(numberToFind + " found at: ["+str(foundX+1) +","+ str(foundY+1) + "]\n")
                            break

                # move to correct column

                if foundX != 0:
                    self.moveColumnLeft(foundY, foundX)
                    print("Moved "+numberToFind+" to: [1,"+ str(foundY+1) + "]\n")
                    self.printMatrix()

                # move to correct row

                if foundY > fixRow:
                    self.moveRowUp(0, foundY-fixRow)
                    print("Moved "+numberToFind+" to: [1,"+str(fixRow+1)+"]\n")
                    self.printMatrix()
                elif foundY < fixRow:
                    self.moveRowDown(0, fixRow-foundY)
                    print("Moved "+numberToFind+" to: [1,"+str(fixRow+1)+"]\n")
                    self.printMatrix()
                else:
                    self.moveRowUp(0, 1)
                    print("Moved "+numberToFind+" to: [1,"+str(fixRow)+"]\n")
                    self.printMatrix()

                    self.moveColumnRight(foundY, foundX)
                    print("Moved column "+str(fixRow+1)+" back\n")
                    self.printMatrix()

                    self.moveRowDown(0, 1)
                    print("Moved "+numberToFind+" to: [1,"+str(fixRow+1)+"]\n")
                    self.printMatrix()

                # move 1 left
                self.moveColumnLeft(fixRow, 1)
                print("Moved "+numberToFind+" to: [6,"+str(fixRow+1)+"]\n")
                self.printMatrix()

        # find 1
        foundX, foundY = self.findNumber("01")

        # move to correct row
        if foundY != 0:
            self.moveRowUp(0, foundY)
            print("Moved 01 to: [1,1]\n")
            self.printMatrix()

        # move 7 to correct column 
        self.moveToCorrectColumn("07", 1) 

        # move 13 to correct column
        self.moveToCorrectColumn("13", 2)      

        # move 19 to correct column
        self.moveToCorrectColumn("19", 3)

        # switch last two columns
        def switchLastTwoColumns():
            self.moveColumnRight(5, 1)
            self.printMatrix()
            self.moveRowDown(0, 1)
            self.printMatrix()
            self.moveColumnRight(5, 1)
            self.printMatrix()
            self.moveRowUp(0, 1)
            self.printMatrix()
            self.moveColumnRight(5, 1)
            self.printMatrix()
            self.moveRowDown(0, 1)
            self.printMatrix()
            self.moveColumnRight(5, 1)
            self.printMatrix()
            self.moveRowUp(0, 1)
            self.printMatrix()
            self.moveColumnRight(5, 1)
            self.printMatrix()
            self.moveRowDown(0, 1)
            self.printMatrix()
            self.moveColumnRight(5, 1)	
            self.printMatrix()
            self.moveRowUp(0, 1)
            self.printMatrix()
            self.moveColumnRight(5, 1)

        # print error message when 31 is not in correct column
        foundX, foundY = self.findNumber("31")
        if foundY != 5:
            print("this bug needs to be fixed")
            self.printMatrix()
            switchLastTwoColumns()

        print("Matrix has been solved.")
        self.printMatrix()