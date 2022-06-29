
originalBoard = [[0, 0, 0],
                [9, 5, 1],
                [0, 3, 0]]

temporaryBoard = [[0,0,0], [0,0,0], [0,0,0]]
numberOfMissingNumbers = -1

for line in originalBoard:
    for number in line:
        if number == 0:
            numberOfMissingNumbers += 1
checksum = 0

solution = [0] * (numberOfMissingNumbers + 1)

def checkBoard():
    #Function to check if the board is either unsolvabel (0), unfinished (1) or already solved(2)
    solutionIterator = 0
    for line in range(0, 3):
        for number in range(0, 3):
            if originalBoard[line][number] == 0:
                temporaryBoard[line][number] = solution[solutionIterator]
                solutionIterator += 1
            else:
                temporaryBoard[line][number] = originalBoard[line][number]

    checksum = 0
    stateOfBoard = 2

    #Board
    for line in temporaryBoard:
        checksum += sum(line)
    if checksum > 45:
        return 0
    elif checksum < 45:
        stateOfBoard = 1

    #Lines
    for line in temporaryBoard:
        if sum(line) > 15:
            return 0
        elif sum(line) < 15:
            stateOfBoard = 1
    

    #Rows  
    checksum = 0
    for row in range(3):
        for line in range(3):
            checksum += temporaryBoard[line][row]
        if checksum > 15:
            return 0
        elif checksum < 15:
            stateOfBoard = 1
        checksum = 0
    
    #Diagonals
    checksum = 0
    for diagonal in range(0, 3):
        checksum += temporaryBoard[diagonal][diagonal]
    if checksum > 15:
        return 0
    elif checksum < 15:
        stateOfBoard = 1
    checksum = 0
    #for diagonal in range(2, -1, 
    # -1):
    for diagonal in reversed(range(-1, 2)):
        checksum += temporaryBoard[diagonal][diagonal]
    if checksum > 15:
        return 0
    elif checksum < 15:
        stateOfBoard = 1

    return stateOfBoard

#Function to check if the board is either unsolvabel (0), unfinished (1) or already solved(2)
def explore (level, me):

    if level != -1:
        solution[level] = me

    state = checkBoard()

    if state == 2:
        print("solution found")
        return 2

    elif state == 0:
        solution[level] = 0
        return 0

    elif level < numberOfMissingNumbers:
        for neighbour in range(1, 10):
            level = level + 1
            state = explore(level, neighbour)
            if state == 2:
                print("solution found")
                return 2
            elif state == 0 and level != 0:
                break
            level = level - 1

    return 1

print(solution)
explore (-1, 1)
print(solution)

#Ende + Limit = Überprüfen von Gewinnkonditionen (Funktion wie z.B. "checkBoard") 
#Weiterführungen / "Pfad" ---> Anzahl freier Stellen, Graph (Funktion wie z.B. "BoardGraph")
#Solution Variable