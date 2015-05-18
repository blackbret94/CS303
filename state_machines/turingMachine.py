""" SIMPLE TURING MACHINE CREATOR """
"""       BY BRET BLACK 2015      """

#####################
#   START PROGRAM   #
#####################

# note that this machine uses -1 as a blank input

import stateMachine
import re
import tree

print
print
print
print "***********************************************"
print "// // // SIMPLE TURING MACHINE CREATOR // // //"
print "// // //        by Bret Black          // // //"
print "***********************************************"
print ""

# define variables
tape = list()
states = list()
activeState = 0
#nextState = [0]
#stack = [-1] # starts with -1 unless otherwise specified
langSize = 0 # this will be read in as input later
tapePos = 0

# add states from input to the state array
stateToAdd = stateMachine.setStateName("A")

# open text file
#machFileName = raw_input("What is the name of the file you would like to run?\n")
machFileName = "Examples/input_turing.txt"
machFile = open(machFileName,'r')

### READ SETUP INFORMATION ###
# read language size
langSize = int(machFile.readline())

# read state count
stateCount = int(machFile.readline())

# create states
for i in range(0,stateCount):
    # create state with empty array
    states.append(stateMachine.State(list(),False))

    # add array
    for j in range(0,langSize):
        # -1 is the blank input
        states[i].links.append(-1)

# read accepting states
statesAccepting = machFile.readline().split()

# set states to accepting
print "Accepting States: " + str(statesAccepting)

for i in statesAccepting:
    # convert to number
    ss = stateMachine.setStateName(i.lower())

    # set to accepting
    states[ss].isAccepting(True)

### ADD TRANSITION FUNCTIONS ###
while True:
    inputState = machFile.readline().rstrip('\n').lower()

    #interpret input
    if inputState == "end":
        break
    else:
        # split along commas
        split = inputState.strip().split(",")

        # read each value
        startState = stateMachine.setStateName(split[0])
        endState = stateMachine.setStateName(split[1])
        consumed = int(split[2])
        newSymbol = int(split[3])
        moveDir = int(split[4])

        # create new arc
        newArc = stateMachine.TuringArc(newSymbol,endState,moveDir)

        # add arc
        states[startState].links.insert(int(consumed),newArc)

### TEST INPUTS ###
while (True):
    # reset vars
    tapePos = 0
    activeState = 0

    # read instructions
    inst = machFile.readline().rstrip('\n').lower()

    # see if the user is quitting
    if (inst == ""):
        break

    print "*********************************"
    print "START NEW INSTRUCTION SET  "
    print "*********************************"
    print ""
        
    # split string into array
    inst = list(inst)

    # print ins to tape
    tape = inst

    print "Instructions: " + str(inst)
    #print "Stack: " + str(stack)
    print ""

    print "TRAVERSING THE TURING MACHINE:"

    # run the machine until halt
    while True:
        # expand tape if neccessary
        while(len(tape) <= tapePos):
            tape.append(-1)

        # find match
        if(states[activeState].links[int(tape[tapePos])] != -1):
            # handle match
            print "Match found!"
            # save link
            thisLink = states[activeState].links[int(tape[tapePos])]

            # write to tape
            tape[tapePos] = thisLink.newSymbol

            # change state
            activeState = int(thisLink.nextState)

            # move along tape
            if(thisLink.moveDir == 0):
                # move left
                if(tapePos > 0):
                    tapePos -= 1
                else:
                    print "Error! Tried to move left of the start"

            elif(thisLink.moveDir == 1):
                # move right
                tapePos += 1
        else:
            # no match found, halt
            print "halting"

            if(states[activeState].acceptingState):
                print "**********************************************************"
                print "AN ACCEPTING STATE WAS FOUND: " + stateMachine.getStateName(int(activeState)).upper() + "  //**//**//**//**//**//**"
                print "**********************************************************"
                print ""
            else:
                print "*******************************************"
                print "TERMINATED AT: " + stateMachine.getStateName(int(activeState)).upper() + "  //"
                print "*******************************************"
                print ""

            print "Tape: " + str(tape) + " Position: " + str(tapePos) + " State: " + str(activeState)
            break

        print "Tape: " + str(tape) + " Position: " + str(tapePos) + " State: " + str(activeState)