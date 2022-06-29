import time

temporaryBoard = [
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                ]

originalBoard = [
                [[4, 0, 0], [0, 0, 0], [0, 0, 1]],
                [[6, 8, 2], [0, 0, 1], [0, 9, 3]],
                [[0, 9, 7], [8, 0, 4], [0, 0, 2]],
                [[0, 0, 6], [0, 0, 0], [0, 0, 7]],
                [[3, 0, 0], [6, 0, 2], [0, 0, 0]],
                [[9, 0, 1], [0, 0, 0], [0, 2, 0]],
                [[0, 0, 9], [0, 0, 6], [0, 0, 0]],
                [[2, 0, 0], [0, 0, 0], [0, 0, 0]],
                [[7, 6, 3], [4, 1, 8], [0, 0, 9]]
                ]


numberOfMissingNumbers = -1

for line in originalBoard:
    for block in line:
        for number in block:
            if number == 0:
                numberOfMissingNumbers += 1

checksum = 0
efficiencyCounter = 0
solution = [0] * (numberOfMissingNumbers + 1)

start = time.time()

def checkBoard():
    
    #Function to check if the board is either unsolvabel (0), unfinished (1) or already solved(2)
    solutionIterator = 0
    for line in range(0, 9):
        for block in range(0, 3):
            for numberInBlock in range (0, 3):
                if originalBoard[line][block][numberInBlock] == 0:
                    temporaryBoard[line][block][numberInBlock] = solution[solutionIterator]
                    solutionIterator += 1
                else:
                    temporaryBoard[line][block][numberInBlock] = originalBoard[line][block][numberInBlock]
  

    checksum = 0
    stateOfBoard = 2

    #Lines
    checksum = 0
    for line in temporaryBoard:
        for uniqueNumber in range(1, 10):
            for block in line:
                checksum += block.count(uniqueNumber)

            if checksum > 1:
                return 0
            elif checksum < 1:
                stateOfBoard = 1
            checksum = 0

    #Rows  
    checksum = 0
    for numberInBlock in range(3):
        for block in range(3):
            for uniqueNumber in range(1, 10):
                for line in range (9):
                    if temporaryBoard[line][block][numberInBlock] == uniqueNumber:
                        checksum += 1

                if checksum > 1:
                    return 0
                elif checksum < 1:
                    stateOfBoard = 1
                checksum = 0

    #Blocks
    checksum = 0
    for lineBlock in range(0, 9, +3):
        for y in range(3):
            for uniqueNumber in range(1, 10):
                for line in range(lineBlock, (lineBlock + 3)):
                    checksum += temporaryBoard[line][y].count(uniqueNumber)
                    
                if checksum > 1:
                    return 0
                elif checksum < 1:
                    stateOfBoard = 1
                checksum = 0

    return stateOfBoard


#Function to check if the board is either unsolvabel (0), unfinished (1) or already solved(2)
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
    print("unlösbar")
else:
    solutionIterator = 0
    for line in range(0, 9):
        for block in range(0, 3):
            for numberInBlock in range (0, 3):
                if originalBoard[line][block][numberInBlock] == 0:
                    temporaryBoard[line][block][numberInBlock] = solution[solutionIterator]
                    solutionIterator += 1
                else:
                    temporaryBoard[line][block][numberInBlock] = originalBoard[line][block][numberInBlock]
    
    for line in temporaryBoard:
        print(line)
    print("Easy! Nume ", efficiencyCounter, " Versüech")
    print(diff)