""" SIMPLE NFA CREATOR """
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

# add states from input to the state array
stateToAdd = stateMachine.setStateName("A")

while True:
    # setup and get input
    stateToAddStr = stateMachine.getStateName(stateToAdd)
    inp = raw_input ("Add state " + stateToAddStr +" by entering its outputs A,BC or type \"end\" \n").lower()

    #interpret input
    if inp == "end":
        break
    else:
        # check to see if it is an accepting state
        accept = False
        if (re.match(r"[*]",inp)):
            accept = True

        #split along commas
        split = inp.strip().split(",")

        #split individual states
        for i in range(0,len(split)):
            split[i].split

        #define the converted states
        stateArray = []

        # turn characters into letters
        for i in range(0,len(split)):
            # create new array space
            newArr = []
            stateArray.append(newArr)

            # fill nested array
            for j in range(0,len(split[i])):
                stateArray[i].append(stateMachine.setStateName(split[i][j]))

        # append
        newState = stateMachine.State(stateArray,accept)
        states.append(newState)

        #increment state counter
        stateToAdd += 1


while (True):
    # read instructions
    inst = raw_input("Input your instructions: ")

    # see if the user is quitting
    if (inst == "quit"):
        break
        
    # split string into array
    inst.split()

    # get name of the end state
    #end = raw_input("What is the final state?\n").lower()
    #endState = stateMachine.setStateName(end)

    print "TRAVERSING THE NFA:"

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
                nextState.append(states[activeState[j]].links[thisInst][k])

    # check if it is accepting
    resultAccepted = False
    for i in range(0,len(activeState)):
        if (activeState[i] == True):
            resultAccepted = True
            break

    # print result
    if (resultAccepted):
        print "This is an accepting state." 
    else :
        print "This is NOT an accepting state."