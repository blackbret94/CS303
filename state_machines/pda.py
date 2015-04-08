""" SIMPLE PDA CREATOR """
""" BY BRET BLACK 2015 """

#####################
#   START PROGRAM   #
#####################

import stateMachine
import re

# define variables
states = []
activeState = []
nextState = [0]
langSize = 0; # this will be read in as input later

# add states from input to the state array
stateToAdd = stateMachine.setStateName("A")

# open text file
machFileName = raw_input("What is the name of the file you would like to run?\n")
machFile = open(machFileName,'r')

# read language size
langSize = int(machFile.readline())

while True:
    # setup and get input
    stateToAddStr = stateMachine.getStateName(stateToAdd)
    #inputState = raw_input ("Add state " + stateToAddStr +" by entering its outputs A,BC or type \"end\" \n").lower()
    inputState = machFile.readline().rstrip('\n').lower()
    print inputState

    #interpret input
    if inputState == "end":
        break
    else:
        # check to see if it is an accepting state
        accept = False
        #print re.match(r".*[*]",inputState)
        if (re.match(r".*[*]",inputState) != None):
            accept = True

        #split along commas
        split = inputState.strip().split(",")

        #split individual states
        for i in range(0,len(split)):
            split[i].split

        #define the converted states
        stateArray = []

        # turn characters into letters
        #for i, string in enumerate(split):
        for i in range(0,len(split)):
            # create new array space
            newArr = []
            stateArray.append(newArr)

            # fill nested array
            for j in range(0,len(split[i])):
                # make sure the state is not an end-state marker
                if (split[i][j] != "*"):
                    stateArray[i].append(stateMachine.setStateName(split[i][j]))

        # append
        newState = stateMachine.State(stateArray,accept)
        states.append(newState)

        #increment state counter
        stateToAdd += 1


while (True):
    # reset vars
    activeState = []
    nextState = [0]

    # read instructions
    inst = machFile.readline().rstrip('\n').lower()

    # see if the user is quitting
    if (inst == ""):
        break
        
    # split string into array
    inst.split()

    print "TRAVERSING THE PDA:"

    # loop through instructions
    for i in range(0,len(inst)):
        # update active state
        activeState = nextState
        nextState = []

        # get the ith instruction
        thisInst = int(inst[i])

        # add to next states
        for j in range(0,len(activeState)):
            for k in range(0,len(states[activeState[j]].links[thisInst])):
                # add state tied to instruction
                nextState.append(states[activeState[j]].links[thisInst][k])

                # add epsilon state
            if (len(states[activeState[j]].links) > langSize):
                for k in range(0,len(states[activeState[j]].links[langSize])):
                    nextState.append(states[activeState[j]].links[langSize][k])


    # check if it is accepting
    resultAccepted = False
    activeState = nextState
    for i in range(0,len(activeState)):
        if (states[activeState[i]].acceptingState):
            resultAccepted = True
            print "THE FINAL STATE IS: "
            print stateMachine.getStateName(int(activeState[i]))
            break

    # print result
    if (resultAccepted):
        print "This is an accepting state." 
    else :
        print "This is NOT an accepting state."