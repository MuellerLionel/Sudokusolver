#originalBoard = [
#                [4, 3, 5, 2, 6, 9, 7, 8, 1],
#                [6, 8, 2, 5, 7, 1, 4, 9, 3],
#                [1, 9, 7, 8, 3, 4, 5, 6, 2],
#                [8, 2, 6, 1, 9, 5, 3, 4, 7],
#                [3, 7, 4, 6, 8, 2, 9, 1, 5],
#                [9, 5, 1, 7, 4, 3, 6, 2, 8],
#                [5, 1, 9, 3, 2, 6, 8, 7, 4],
#                [2, 4, 8, 9, 5, 7, 1, 3, 6],
#                [7, 6, 3, 4, 1, 8, 2, 5, 9]
#                ]

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




numberOfMissingNumbers = -1

for line in originalBoard:
    for block in line:
        for number in block:
            if number == 0:
                numberOfMissingNumbers += 1

checksum = 0
efficiencyCounter = 0
solution = [0] * (numberOfMissingNumbers + 1)

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
                #print("lines", checksum, uniqueNumber)
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
                    #print("rows")
                    return 0
                elif checksum < 1:
                    stateOfBoard = 1
                checksum = 0

    #Blocks
    checksum = 0
    uniqueCounter = 0
    for lineBlock in range(0, 9, +3):
        for y in range(3):
            for uniqueNumber in range(1, 10):
                for line in range(lineBlock, (lineBlock + 3)):
                    uniqueCounter += temporaryBoard[line][y].count(uniqueNumber)
                if uniqueCounter > 1:
                    return 0
                
                elif uniqueCounter < 1:
                    stateOfBoard = 1
                uniqueCounter = 0

    return stateOfBoard


#Function to check if the board is either unsolvabel (0), unfinished (1) or already solved(2)
def explore (level, me):
    global efficiencyCounter
    efficiencyCounter += 1

    if level == 0:
        print(level, " percent")
    if level != -1:
        #if me in solution:
        #    return 1
        solution[level] = me
        
    state = checkBoard()

    if state == 2:
        print("solution found")
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
                print("solution found")
                return 2
            
    solution[level] = 0
    return 1

print(solution)
explore (-1, 1)
print(solution)
solutionIterator = 0
for line in range(0, 9):
    for block in range(0, 3):
        for numberInBlock in range (0, 3):
            if originalBoard[line][block][numberInBlock] == 0:
                temporaryBoard[line][block][numberInBlock] = solution[solutionIterator]
                solutionIterator += 1
            else:
                temporaryBoard[line][block][numberInBlock] = originalBoard[line][block][numberInBlock]
  
print(temporaryBoard)