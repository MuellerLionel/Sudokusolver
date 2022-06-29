import time



"""
originalBoard = [
                [4, 3, 5, 2, 6, 9, 7, 8, 1],
                [6, 8, 2, 5, 7, 1, 4, 9, 3],
                [1, 9, 7, 8, 3, 4, 5, 6, 2],
                [8, 2, 6, 1, 9, 5, 3, 4, 7],
                [3, 7, 4, 6, 8, 2, 9, 1, 5],
                [9, 5, 1, 7, 4, 3, 6, 2, 8],
                [5, 1, 9, 3, 2, 6, 8, 7, 4],
                [2, 4, 8, 9, 5, 7, 1, 3, 6],
                [7, 6, 3, 4, 1, 8, 2, 5, 0]
                ]
"""

temporaryBoard = [0] * 9 * 9

originalBoard = [
                4, 0, 0, 0, 0, 0, 0, 0, 1,
                6, 8, 2, 0, 0, 1, 0, 9, 3,
                0, 9, 7, 8, 0, 4, 0, 0, 2,
                0, 0, 6, 0, 0, 0, 0, 0, 7,
                3, 0, 0, 6, 0, 2, 0, 0, 0,
                9, 0, 1, 0, 0, 0, 0, 2, 0,
                0, 0, 9, 0, 0, 6, 0, 0, 0,
                2, 0, 0, 0, 0, 0, 0, 0, 0,
                7, 6, 3, 4, 1, 8, 0, 0, 9
                ]




numberOfMissingNumbers = -1

for line in originalBoard:
    for number in line:
        if number == 0:
            numberOfMissingNumbers += 1

checksum = 0
efficiencyCounter = 0
solution = [0] * (numberOfMissingNumbers + 1)


start = time.time()

def checkBoard():
    #Function to check if the board is either unsolvabel (0), unfinished (1) or already solved(2)
    checkLines = 0
    checkRows = 0
    checkBlocks = 0

    solutionIterator = 0
    for number in range (0, 9):
        if originalBoard[number] == 0:
            temporaryBoard[number] = solution[solutionIterator]
            solutionIterator += 1
        else:
            temporaryBoard[number] = originalBoard[number]
  
    stateOfBoard = 2

    for uniqueNumber in range(1, 10):
        for line in range(0,8):
            if temporaryBoard[line*9:(line+1)*9].count(uniqueNumber) > 1:
                return 0
            elif temporaryBoard[line*9:(line+1)*9].count(uniqueNumber) < 1:
                return 1



        for row in range(0, 9):
            for line in range(0, 9):
                if temporaryBoard[line][row] == uniqueNumber:
                        checkRows += 1
            if checkRows > 1:
                return 0
            elif checkRows < 1:
                stateOfBoard = 1
            checkRows = 0

        for line in temporaryBoard:
            checkLines = line.count(uniqueNumber)

            if checkLines > 1:
                return 0
            elif checkLines < 1:
                stateOfBoard = 1
            checkLines = 0

        for lineBlock in range(0, 9, +3):
            for rowBlock in range(0, 9, +3):
                for line in range(lineBlock, (lineBlock + 3)):
                    for row in range(rowBlock, (rowBlock + 3)):
                        if temporaryBoard[line][row] == uniqueNumber:
                            checkBlocks += 1
                            
                if checkBlocks > 1:
                    return 0
                elif checkBlocks < 1:
                    stateOfBoard = 1
                checkBlocks = 0


    return stateOfBoard

def explore (level, me):
    global efficiencyCounter
    efficiencyCounter += 1

    if level != -1:
        solution[level] = me
        
    state = checkBoard()

    if state == 2:
        return 2

    elif state == 0:
        solution[level] = 0
        return 0

    elif level < numberOfMissingNumbers:
        for child in range(1, 10):
            level = level + 1
            state = explore(level, child)
            level = level - 1
            if state == 2:
                return 2
            
    solution[level] = 0
    return 1


explore (-1, 1)
end = time.time()
diff = end - start

if solution.count(0) > 0:
    print("unsolvable")
else:
    solutionIterator = 0
    for line in range (0, 9):
        for number in range (0, 9):
            if originalBoard[line][number] == 0:
                temporaryBoard[line][number] = solution[solutionIterator]
                solutionIterator += 1
            else:
                temporaryBoard[line][number] = originalBoard[line][number]
    
    for line in temporaryBoard:
        print(line)
    print("Solved in ", efficiencyCounter, " tries")
    print(diff)
