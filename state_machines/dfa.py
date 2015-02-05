""" SIMPLE DFA CREATOR """
""" BY BRET BLACK 2015 """

##########################
#   METHODS AND CLASSES  #
##########################

# get the nth letter of the alphabet
def getStateName(n):
    return chr(ord('a')+n)

#get numerical value of the nth letter of the alphabet
def setStateName(n):
    return ord(n)-ord('a')

class State:
    # blank constructor
    def __init__(self):
        # handles the array of lists, accepting 0, 1, or epsilon
        self.links = []
        # is an accepting state?
        self.acceptingState = False

    # constructor with param
    def __init__(self,stateArray,isIt):
        # create links list
        self.links = stateArray
        # adjust accepting state
        self.acceptingState = isIt

    # add states
    def addState(self,addedState):
        self.links.append(addedState)

    # modify whether it is accepting
    def isAccepting(self,isIt):
        self.acceptingState = isIt


#####################
#   START PROGRAM   #
#####################

# define variables
states = []
activeState = 0

# read instructions
inst = raw_input("Input your instructions: ")

# add states from input to the state array
stateToAdd = setStateName("A")

while True:
    stateToAddStr = getStateName(stateToAdd)
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
            stateArray.append(setStateName(inp[i]))

        # check to see if it is an accepting state
        accept = False
        if (len(inp) > 2):
            if (inp[2] == "*"):
                accept = True

        newState = State(stateArray,accept)
        states.append(newState)

        #increment state counter
        stateToAdd += 1

# split string into array
inst.split()

print "TRAVERSING THE DFA:"

# loop through instructions
for i in range(0,len(inst)):
    #print active state
    print getStateName(int(activeState))

    # get the ith instruction
    thisInst = int(inst[i])

    activeState = states[activeState].links[thisInst]

# print result
print "THE FINAL STATE IS: "
print getStateName(int(activeState))

# check if it is accepting
resultAccepted = states[activeState].acceptingState
if (resultAccepted):
    print "This is an accepting state." 
else :
    print "This is NOT an accepting state."