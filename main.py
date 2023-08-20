import random as random

# generate 6x6 matrix
row1 = ["01", "02", "03", "04", "05", "06"]
row2 = ["07", "08", "09", "10", "11", "12"]
row3 = ["13", "14", "15", "16", "17", "18"]
row4 = ["19", "20", "21", "22", "23", "24"]
row5 = ["25", "26", "27", "28", "29", "30"]
row6 = ["31", "32", "33", "34", "35", "36"]
matrix = [row1, row2, row3, row4, row5, row6]

def randomizeMatrix():
    # randomize columns
    for i in range(0, len(matrix)):     
        matrix[i] = random.sample(matrix[i], len(matrix[i]))

    # randomize rows
    for column in range(0, len(matrix)):
        # move a rows down by random amount (1-5)
        moveDowns = random.randint(1, len(matrix)-1)
        for moves in range(0, moveDowns):
            temp = matrix[0][column]
            for i in range(0, len(matrix)-1):
                matrix[i][column] = matrix[i+1][column]
            matrix[len(matrix)-1][column] = temp

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
            print("2 found at: ", i, j)