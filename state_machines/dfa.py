""" SIMPLE DFA CREATOR """
""" BY BRET BLACK 2015 """

#####################
#   START PROGRAM   #
#####################

import stateMachine

# define variables
states = []
activeState = 0
langSize = 0
#instructionsList = []

# READ STATES
# add states from input to the state array
stateToAdd = stateMachine.setStateName("A")

# open text file
machFileName = raw_input("What is the name of the file you would like to run?\n")
machFile = open(machFileName,'r')

# read language size
langSize = int(machFile.readline())

# read states
while True:
    stateToAddStr = stateMachine.getStateName(stateToAdd)
    inputState = machFile.readline().rstrip('\n').lower()
    print inputState

    if inputState == "end":
        break
    else:
        #split
        inputState.split()

        #define the converted states
        stateArray = []

        # turn characters into letters
        for i in range(0,langSize):
            stateArray.append(stateMachine.setStateName(inputState[i]))

        # check to see if it is an accepting state
        accept = False
        if (len(inputState) > langSize):
            if (inputState[langSize] == "*"):
                accept = True

        newState = stateMachine.State(stateArray,accept)
        states.append(newState)

        #increment state counter
        stateToAdd += 1

# read instructions
while (True):
    # reset vars
    activeState = 0

    # read instructions
    inst = machFile.readline().rstrip('\n').lower()

    # see if EOF has been reached
    if (inst == ""):
        break

    # otherwise, continue
    # split string into array
    inst.split()

    print "TRAVERSING THE DFA:"

    # loop through instructions
    for i in range(0,len(inst)):
        #print active state
        print stateMachine.getStateName(int(activeState))

        # get the ith instruction
        thisInst = int(inst[i])

        activeState = states[activeState].links[thisInst]

    # print result
    print "THE FINAL STATE IS: "
    print stateMachine.getStateName(int(activeState))

    # check if it is accepting
    resultAccepted = states[activeState].acceptingState
    if (resultAccepted):
        print "This is an accepting state." 
    else:
        print "This is NOT an accepting state."