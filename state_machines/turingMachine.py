""" SIMPLE TURING MACHINE CREATOR """
"""       BY BRET BLACK 2015      """
# currently does NOT handle epsilon transitions

#####################
#   START PROGRAM   #
#####################

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

    print "*********************************"
    print "START NEW INSTRUCTION SET  "
    print "*********************************"
    print ""
        
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
    #for index,i in enumerate(inst):
    while len(nextNode) > 0:
        # bool to track if a transition match has been found
        matchFound = False

        # update active state and create a list of next states
        #oldLen = len(nextNode)
        activeNode = nextNode.pop(0)

        if(len(activeNode.remainingInput)!=0):
            # get the ith instruction
            thisInst = int(activeNode.remainingInput.pop(0))
            print "Instruction: " + str(thisInst)

            # match to an arc
            for j,arc in enumerate(states[activeNode.state].links):
                print "Consume Input: " + str(arc.consumeInput) + " / " + str(thisInst) 
                print "Consume stack: " + str(arc.consumeStack) + " / " + str(activeNode.stackContents[len(activeNode.stackContents)-1])

                # does consumeInput match? is it epsilon? does the stack match?
                if((int(arc.consumeInput) == int(thisInst) or int(arc.consumeInput)>=langSize) and (int(arc.consumeStack) == int(activeNode.stackContents[len(activeNode.stackContents)-1]))):
                    # copy input
                    newInput = list(activeNode.remainingInput)

                     # restore stack if epsilon
                    if(int(arc.consumeInput)>=langSize):
                        newInput.insert(0,str(thisInst))
                        print "Epsilon detected!"

                    # print input
                    print "Remaining input: " + str(newInput)

                    # modify stack
                    newStack = list(activeNode.stackContents)
                    if arc.consumeStack != '':
                        newStack.pop(len(newStack)-1)

                    if arc.newStack != '':
                        newStack.append(arc.newStack)
                    
                    print "Stack: " + str(newStack)

                    # add node
                    nextNode.append(stateMachine.PDANode(arc.nextState,newInput,newStack))
                    print "New node created! " + str(j)
                    matchFound = True

        # check for accepting if no matches were found
        if(matchFound == False and states[activeNode.state].acceptingState):
            print "**********************************************************"
            print "AN ACCEPTING STATE WAS FOUND: " + stateMachine.getStateName(int(activeNode.state)).upper() + "  //**//**//**//**//**//**"
            print "**********************************************************"
            print ""
        elif(matchFound == False):
            print "*******************************************"
            print "TERMINATED AT: " + stateMachine.getStateName(int(activeNode.state)).upper() + "  //"
            print "*******************************************"
            print ""
