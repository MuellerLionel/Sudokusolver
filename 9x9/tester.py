"""temporaryBoard = [
                [[4, 3, 5], [2, 6, 9], [7, 8, 1]],
                [[6, 8, 2], [5, 7, 1], [4, 9, 3]],
                [[1, 9, 7], [8, 3, 4], [5, 6, 2]],
                [[8, 2, 6], [1, 9, 5], [3, 4, 7]],
                [[3, 7, 4], [6, 8, 2], [9, 1, 5]],
                [[9, 5, 1], [7, 4, 3], [6, 2, 8]],
                [[5, 1, 9], [3, 2, 6], [1, 0, 0]],
                [[2, 4, 8], [9, 5, 7], [0, 0, 6]],
                [[7, 6, 3], [4, 1, 8], [2, 0, 9]]
                ]
originalBoard = [
                [[4, 3, 5], [2, 6, 9], [7, 8, 1]],
                [[6, 8, 2], [5, 7, 1], [4, 9, 3]],
                [[1, 9, 7], [8, 3, 4], [5, 6, 2]],
                [[8, 2, 6], [1, 9, 5], [3, 4, 7]],
                [[3, 7, 4], [6, 8, 2], [9, 1, 5]],
                [[9, 5, 1], [7, 4, 3], [6, 2, 8]],
                [[5, 1, 9], [3, 2, 6], [0, 0, 0]],
                [[2, 4, 8], [9, 5, 7], [0, 0, 6]],
                [[7, 6, 3], [4, 1, 8], [2, 0, 9]]
                ]

originalBoard = [
                [[4, 0, 0], [0, 0, 0], [0, 0, 1]],
                [[6, 8, 2], [0, 0, 1], [0, 9, 3]],
                [[0, 9, 7], [8, 0, 4], [0, 0, 2]],
                [[0, 0, 6], [0, 0, 5], [0, 4, 7]],
                [[3, 7, 0], [6, 0, 2], [0, 0, 0]],
                [[9, 5, 1], [0, 0, 0], [0, 2, 0]],
                [[0, 0, 9], [0, 0, 6], [0, 0, 0]],
                [[2, 0, 0], [0, 0, 7], [0, 0, 0]],
                [[7, 6, 3], [4, 1, 8], [0, 0, 9]]
                ]
originalBoard = [
                [[4, 3, 5], [2, 6, 9], [7, 8, 1]],
                [[6, 8, 2], [5, 7, 1], [4, 9, 3]],
                [[1, 9, 7], [8, 3, 4], [5, 6, 2]],
                [[8, 2, 6], [1, 9, 5], [3, 4, 7]],
                [[3, 7, 4], [6, 8, 2], [9, 1, 5]],
                [[9, 5, 1], [7, 4, 3], [6, 2, 8]],
                [[5, 1, 9], [3, 2, 6], [1, 0, 0]],
                [[2, 4, 8], [9, 5, 7], [0, 0, 6]],
                [[7, 6, 3], [4, 1, 8], [2, 0, 9]]
                ]
"""
originalBoard = [
                [4, 3, 5, 2, 6, 9, 7, 8, 1],
                [6, 8, 2, 5, 7, 1, 4, 9, 3],
                [1, 9, 7, 8, 3, 4, 5, 6, 2],
                [8, 2, 6, 1, 9, 5, 3, 4, 7],
                [3, 7, 4, 6, 8, 2, 9, 1, 0],
                [9, 5, 1, 7, 4, 3, 6, 2, 8],
                [5, 1, 9, 3, 2, 6, 8, 7, 4],
                [2, 4, 8, 9, 5, 7, 1, 3, 6],
                [7, 6, 3, 4, 1, 8, 2, 0, 0]
                ]

temporaryBoard = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]

numberOfMissingNumbers = -1

for line in originalBoard:
    for number in line:
        if number == 0:
            numberOfMissingNumbers += 1

checksum = 0
efficiencyCounter = 0
solution = [5, 5, 9]
########
def checkBoard():
    
    #Function to check if the board is either unsolvabel (0), unfinished (1) or already solved(2)

    checkLines = 0
    checkRows = 0
    checkBlocks = 0


    solutionIterator = 0
    for line in range (0, 9):
        for number in range (0, 9):
            if originalBoard[line][number] == 0:
                temporaryBoard[line][number] = solution[solutionIterator]
                solutionIterator += 1
            else:
                temporaryBoard[line][number] = originalBoard[line][number]

    checksum = 0
    stateOfBoard = 2

    for uniqueNumber in range(1, 10):
        for row in range(0, 9):
            for line in range(0, 9):
                if temporaryBoard[line][row] == uniqueNumber:
                        checkRows += 1

                checkLines = temporaryBoard[line].count(uniqueNumber)

                if checkLines > 1:
                    print("lines", uniqueNumber, line, row)
                    return 0
                elif checkLines < 1:
                    stateOfBoard = 1
                checkLines = 0
            

            if checkRows > 1:
                print("rows", uniqueNumber, line, row, checkRows)
                return 0
            elif checkRows< 1:
                stateOfBoard = 1
                print("lines not happy")
            checkRows = 0


    #Blocks
    checksum = 0
    for uniqueNumber in range(1, 10):
        for lineBlock in range(0, 9, +3):
            for rowBlock in range(0, 9, +3):
                for line in range(lineBlock, (lineBlock + 3)):
                    for row in range(rowBlock, (rowBlock + 3)):
                        if temporaryBoard[line][row] == uniqueNumber:
                            checkBlocks += 1
                            
                if checkBlocks > 1:
                    print("blocks")
                    return 0
                elif checkBlocks < 1:
                    print("block not happy")
                    stateOfBoard = 1
                checkBlocks = 0

    

    return stateOfBoard

print(checkBoard())

