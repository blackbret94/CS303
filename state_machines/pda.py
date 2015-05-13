""" SIMPLE PDA CREATOR """
""" BY BRET BLACK 2015 """

#####################
#   START PROGRAM   #
#####################

import stateMachine
import re
import tree

# define variables
states = []
activeState = []
nextState = [0]
stack = [-1] # starts with -1 unless otherwise specified
langSize = 0 # this will be read in as input later

# add states from input to the state array
stateToAdd = stateMachine.setStateName("A")

# open text file
#machFileName = raw_input("What is the name of the file you would like to run?\n")
machFileName = "Examples/input_pda.txt"
machFile = open(machFileName,'r')

### READ SETUP INFORMATION ###
# read language size
langSize = int(machFile.readline())

# read start stack
possibleStack = machFile.readline()
stack = list()

if(possibleStack != 'null\n'):
    stack = list(possibleStack.rstrip('\n'))

# read state count
stateCount = int(machFile.readline())

# create states
for i in range(0,stateCount):
    states.append(stateMachine.State(list(),False))

# read accepting states
statesAccepting = machFile.readline().split()

# set states to accepting
print "Accepting States: " + str(statesAccepting)

for i in statesAccepting:
    # convert to number
    ss = stateMachine.setStateName(i.lower())

    # set to accepting
    states[ss].isAccepting(True)

### ADD TRANSITION ARCS ###
while True:
    inputState = machFile.readline().rstrip('\n').lower()

    #interpret input
    if inputState == "end":
        break
    else:
        # check to see if it is an accepting state
        accept = False
        #print re.match(r".*[*]",inputState)
        if (re.match(r".*[*]",inputState) != None):
            accept = True

        # split along commas
        split = inputState.strip().split(",")
        print split

        # read each value
        startState = stateMachine.setStateName(split[0])
        endState = stateMachine.setStateName(split[1])
        consumedInput = split[2]
        consumedStack = split[3]
        newStack = split[4]

        # create new arc
        newArc = stateMachine.PDAarc(consumedInput,consumedStack,newStack,endState)

        # add arc
        states[startState].links.append(newArc)

### TEST INPUTS ###
while (True):
    # reset vars
    # read instructions
    inst = machFile.readline().rstrip('\n').lower()

    # see if the user is quitting
    if (inst == ""):
        break
        
    # split string into array
    inst = list(inst)

    print "Instructions: " + str(inst)
    print "Stack: " + str(stack)
    print ""

    # create new node
    newNode = stateMachine.PDANode(0,inst,stack)

    # create queues and append
    activeNode = list()
    nextNode = list()
    nextNode.append(newNode)

    print "TRAVERSING THE PDA:"

    # loop through instructions
    for index,i in enumerate(inst):
        # check for halt
        if len(nextNode)==0:
            print "Halt!"
            break

        # update active state and create a list of next states
        activeNode = nextNode.pop(0)

        # get the ith instruction
        thisInst = int(activeNode.remainingInput.pop())

        # match to an arc
        for j,arc in enumerate(states[activeNode.state].links):
            print "Consume Input: " + str(arc.consumeInput) + " / " + str(i) 
            print "Consume stack: " + str(arc.consumeStack) + " / " + str(stack[len(stack)-1])

            if((arc.consumeInput == i) and (arc.consumeStack == stack[len(stack)-1])):
                # consume input
                newInput = list(activeNode.remainingInput)

                # modify stack
                newStack = list(activeNode.stackContents)
                if arc.consumeStack != '':
                    newStack.pop(len(newStack)-1)

                if arc.newStack != '':
                    newStack.append(arc.newStack)

                # add node
                nextNode.append(stateMachine.PDANode(arc.nextState,newInput,newStack))
                print "New node created!"

        # add to next states
        # for j in range(0,len(activeState)):
        #     for k in range(0,len(states[activeState[j]].links[thisInst])):
        #         # add state tied to instruction
        #         nextState.append(states[activeState[j]].links[thisInst][k])

        #     # add epsilon state
        #     if (len(states[activeState[j]].links) > langSize):
        #         for k in range(0,len(states[activeState[j]].links[langSize])):
        #             nextState.append(states[activeState[j]].links[langSize][k])


    # check if it is accepting
    resultAccepted = False
    activeNode = nextNode
    for i in range(0,len(activeNode)):
        if (states[activeNode[i].state].acceptingState):
            resultAccepted = True
            print "A FINAL STATE IS: " + stateMachine.getStateName(int(activeNode[i].state)).upper()
            #break

    # print result
    if (resultAccepted):
        print "This is an accepting state." 
    else :
        print "This is NOT an accepting state."
    print ""