""" CLASSES AND METHODS USEFUL   """
""" IN MY STATE MACHINE SCRIPTS  """
""" By BRET BLACK, 2015          """

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
        # handles the array of lists, accepting 0, 1, or epsilon. Links can hold
        # states or transitions, depending on the machine
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

# node of a PDA
class PDANode:
    def __init__(self):
        self.remainingInput = list()
        self.stackContents = list()

    def __init__(self,remain,stack):
        self.remainingInput = remain
        self.stackContents = stack

# PDA transition
class PDAarc:
    def __init__(self):
        # should never be used 
        self.consumeInput = 0
        self.consumeStack = 0
        self.newStack = 0
        self.nextState = 0

    def __init__(self,consumeInput,consumeStack,newStack,nextState):
        # the input symbol to consume
        self.consumeInput = consumeInput

        # the stack symbol to consume (may be epsilon)
        self.consumeStack = consumeStack

        # the new head of the stack (may be epsilon)
        self.newStack = newStack

        # this is the state the arc is linked to
        self.nextState = nextState