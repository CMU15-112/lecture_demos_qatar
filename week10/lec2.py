"""
def solveWithBacktracking(problemState):
    if isComplete(problemState):
        return problemState
    nextStep = getNextStep(problemState)
    for move in getPossibleMoves(problemState, nextStep):
        # Sometimes it's easier to make a move, then check if it's valid.
        # Sometimes it's easier to check if a move is valid first.
        # Just make sure that you always undo a move properly!
        if isValid(problemState, nextStep, move):
            problemState = makeMove(problemState, nextStep, move)
            tmpSolution = solveWithBacktracking(problemState)
            if tmpSolution != None:
                return tmpSolution
            problemState = undoMove(problemState, nextStep, move)
    return None
"""
import copy
def matchingFlights(flightList, departureCity):
    ret = []
    for f in flightList:
        if f[0] == departureCity:
            ret.append(f)
    return ret

def solveFlightItinerary(flightList, partialSolution):
    if len(flightList) == 0:
        return partialSolution
    
    #print(partialSolution)
    if len(partialSolution) == 0:
        possibleNextHops = flightList
    else:
        possibleNextHops = matchingFlights(flightList, partialSolution[-1][1])
    
    for guess in possibleNextHops:
        partialSolution.append(guess)
        tmpFlightList = copy.copy(flightList)
        tmpFlightList.remove(guess)
        sol = solveFlightItinerary(tmpFlightList, partialSolution)
        if sol != None:
            return sol
        partialSolution.pop()
    
    return None
            
    
    
def testSolveFlightItinerary():
    flights = [ ("HNL", "AKL"),
                ("YUL", "ORD"),
                ("ORD", "SFO"),
                ("SFO", "DOH")
            ]
    sol = solveFlightItinerary(flights, [])
    print(sol)