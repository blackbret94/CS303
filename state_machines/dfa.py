""" SIMPLE DFA CREATOR """
""" BY BRET BLACK 2015 """

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

# define variables
states = []
activeState = 0

# read instructions
inst = raw_input("Input your instructions: ")

# add states from input to the state array
stateToAdd = setStateName("A")

while True:
    stateToAddStr = getStateName(stateToAdd)
    inp = raw_input ("Add state " + stateToAddStr +" by entering its outputs AB or type \"end\" \n").lower()
    if inp == "end":
        break
    else:
        #split
        inp.split()

        #define the converted states
        inpp = []

        # turn characters into letters
        for i in range(0,len(inp)):
            inpp.append(setStateName(inp[i]))
        states.append(inpp)

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

    activeState = states[activeState][thisInst]

# print result
print "THE FINAL STATE IS: "
print getStateName(int(activeState))