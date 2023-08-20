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

def moveColumnLeft(column, moves):
    for noMoves in range(0, moves):
        temp = matrix[column][0]
        for i in range(0, len(matrix)-1):
            matrix[column][i] = matrix[column][i+1]
        matrix[column][len(matrix)-1] = temp


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
    print()
    for i in range(0, len(matrix)):
        print(matrix[i])

printMatrix()


# find 2 and move to right spot
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] == "02":
            print("2 found at: ", i+1, j+1)