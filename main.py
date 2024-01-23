import random as random

# generate 6x6 matrix
column1 = ["01", "02", "03", "04", "05", "06"]
column2 = ["07", "08", "09", "10", "11", "12"]
column3 = ["13", "14", "15", "16", "17", "18"]
column4 = ["19", "20", "21", "22", "23", "24"]
column5 = ["25", "26", "27", "28", "29", "30"]
column6 = ["31", "32", "33", "34", "35", "36"]
matrix = [column1, column2, column3, column4, column5, column6]

def moveRowUp(row, moves):
    for noMoves in range(0, moves):
        temp = matrix[0][row]
        for i in range(0, len(matrix)-1):
            matrix[i][row] = matrix[i+1][row]
        matrix[len(matrix)-1][row] = temp

def moveRowDown(row, moves):
    for noMoves in range(0, moves):
        temp = matrix[len(matrix)-1][row]
        for i in range(len(matrix)-1, 0, -1):
            matrix[i][row] = matrix[i-1][row]
        matrix[0][row] = temp

def moveColumnLeft(column, moves):
    for noMoves in range(0, moves):
        temp = matrix[column][0]
        for i in range(0, len(matrix)-1):
            matrix[column][i] = matrix[column][i+1]
        matrix[column][len(matrix)-1] = temp

def moveColumnRight(column, moves):
    for noMoves in range(0, moves):
        temp = matrix[column][len(matrix)-1]
        for i in range(len(matrix)-1, 0, -1):
            matrix[column][i] = matrix[column][i-1]
        matrix[column][0] = temp


def randomizeMatrix():
    # randomize columns
    for i in range(0, len(matrix)):     
        matrix[i] = random.sample(matrix[i], len(matrix[i]))

    # randomize rows
    for row in range(0, len(matrix)):
        # move a rows down by random amount (1-5)
        moveDowns = random.randint(1, len(matrix)-1)
        moveRowUp(row, moveDowns)
        
            

randomizeMatrix()

def printMatrix():
    for i in range(0, len(matrix)):
        print(matrix[i])
    print()
print("\nBegin matrix:")
printMatrix()


# find 2 to 6

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

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == numberToFind:
                    foundX = j
                    foundY = i
                    print(numberToFind + " found at: ["+str(foundX+1) +","+ str(foundY+1) + "]\n")
                    break

        # move to correct column

        if foundX != 0:
            moveColumnLeft(foundY, foundX)
            print("Moved "+numberToFind+" to: [1,"+ str(foundY+1) + "]\n")
            printMatrix()

        # move to correct row

        if foundY > fixRow:
            moveRowUp(0, foundY-fixRow)
            print("Moved "+numberToFind+" to: [1,"+str(fixRow+1)+"]\n")
            printMatrix()
        elif foundY < fixRow:
            moveRowDown(0, fixRow-foundY)
            print("Moved "+numberToFind+" to: [1,"+str(fixRow+1)+"]\n")
            printMatrix()
        else:
            moveRowUp(0, 1)
            print("Moved "+numberToFind+" to: [1,"+str(fixRow)+"]\n")
            printMatrix()

            moveColumnRight(foundY, foundX)
            print("Moved column "+str(fixRow+1)+" back\n")
            printMatrix()

            moveRowDown(0, 1)
            print("Moved "+numberToFind+" to: [1,"+str(fixRow+1)+"]\n")
            printMatrix()

        # move 1 left
        moveColumnLeft(fixRow, 1)
        print("Moved "+numberToFind+" to: [6,"+str(fixRow+1)+"]\n")
        printMatrix()

def findNumber(numberToFind):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == numberToFind:
                foundX = j
                foundY = i
                print(numberToFind + " found at: ["+str(foundX+1) +","+ str(foundY+1) + "]\n")
                return foundX, foundY

# find 1
foundX, foundY = findNumber("01")

# move to correct row
if foundY != 0:
    moveRowUp(0, foundY)
    print("Moved 01 to: [1,1]\n")
    printMatrix()

def rotateAroundColumn(columnToRotateAround):
    
    # rotate around column x
    moveColumnRight(columnToRotateAround, 1)
    moveRowDown(0, 1)
    moveColumnLeft(columnToRotateAround, 1)
    moveRowUp(0, 1)
    moveRowUp(0, 1)
    moveColumnRight(columnToRotateAround, 1)
    moveRowDown(0, 1)
    moveColumnLeft(columnToRotateAround, 1)

# find 7
foundX, foundY = findNumber("07")
positionOf1 = [0,0] 

# if 7 is not in correct place 
if foundY != 1:

    # pos of 1 is always [0,0]
    stepsToMoveY = foundY - positionOf1[1]

    # rotate to correct column + 1
    while stepsToMoveY > 2:
        columnToRotateAround = foundY - 1 
        rotateAroundColumn(columnToRotateAround)
        print("Moved 7 up 1 step")
        printMatrix()
        foundX, foundY = findNumber("07")
        stepsToMoveY = foundY - positionOf1[1]
    
    # rotate to correct column
    columnToRotateAround = foundY
    rotateAroundColumn(columnToRotateAround)
    print("Moved 7 to final position")
    printMatrix()
