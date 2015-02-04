""" SIMPLE NFA CREATOR """
""" BY BRET BLACK 2015 """

# get the nth letter of the alphabet
def getStateName(n):
    return chr(ord('a')+n)

#get numerical value of the nth letter of the alphabet
def setStateName(n):
    return ord(n)-ord('a')

# define variables
states = []
activeState = []
nextState = [0]
endState = 0
doesEnd = False

# read instructions
inst = raw_input("Input your instructions: ")

# add states from input to the state array
stateToAdd = setStateName("A")

while True:
    # setup and get input
    stateToAddStr = getStateName(stateToAdd)
    inp = raw_input ("Add state " + stateToAddStr +" by entering its outputs A,BC or type \"end\" \n").lower()

    #interpret input
    if inp == "end":
        break
    else:
        #split along spaces
        split = inp.strip().split(",")

        #split individual states
        for i in range(0,len(split)):
            split[i].split

        #define the converted states
        inpp = []

        # turn characters into letters
        for i in range(0,len(split)):
            # create new array space
            newArr = []
            inpp.append(newArr)

            # fill nested array
            for j in range(0,len(split[i])):
                inpp[i].append(setStateName(split[i][j]))

        # append
        states.append(inpp)

        #increment state counter
        stateToAdd += 1

# split string into array
inst.split()

# get name of the end state
end = raw_input("What is the final state?\n").lower()
endState = setStateName(end)

print "TRAVERSING THE NFA:"

print states

# loop through instructions
for i in range(0,len(inst)):
    # update active state
    activeState = nextState
    nextState = []

    # get the ith instruction
    thisInst = int(inst[i])

    # add to next states
    for j in range(0,len(activeState)):
        for k in range(0,len(states[activeState[j]][thisInst])):
            # check for end
            if (states[activeState[j]][thisInst][k] == endState):
                # the end has been reached, exit the loop
                doesEnd = True
                i = len(inst)

            else:
                # add to queue
                nextState.append(states[activeState[j]][thisInst][k])

# print result
if (doesEnd):
    print "This instruction set reaches the end"
else:
    print "This instruction set does NOT reach the end"