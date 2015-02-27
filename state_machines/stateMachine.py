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

    # getter for boo acceptingState
    def getAccepting(self):
        return self.acceptingState