""" SIMPLE DFA CREATOR """
""" BY BRET BLACK 2015 """

#####################
#   START PROGRAM   #
#####################

import stateMachine

# define variables
states = []
activeState = 0

# READ STATES
# add states from input to the state array
stateToAdd = stateMachine.setStateName("A")

while True:
    stateToAddStr = stateMachine.getStateName(stateToAdd)
    inp = raw_input ("Add state " + stateToAddStr +" by entering its outputs AB or type \"end\".  \n* indiciates an accepting state.\n").lower()
    if inp == "end":
        break
    else:
        #split
        inp.split()

        #define the converted states
        stateArray = []

        # turn characters into letters
        for i in range(0,2):
            stateArray.append(stateMachine.setStateName(inp[i]))

        # check to see if it is an accepting state
        accept = False
        if (len(inp) > 2):
            if (inp[2] == "*"):
                accept = True

        newState = stateMachine.State(stateArray,accept)
        states.append(newState)

        #increment state counter
        stateToAdd += 1
# READ INSTRUCTIONS
while (True):
    # read instructions
    inst = raw_input("Input your instructions, or type \"quit\": ").lower()

    # see if the user is quitting
    if (inst == "quit"):
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
    else :
        print "This is NOT an accepting state."