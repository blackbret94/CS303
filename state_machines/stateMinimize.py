""" CLASSES AND METHODS USED    """
""" TO MINIMIZE THE # of STATES """
""" By BRET BLACK, 2015         """
"""                             """
""" This class is ONLY to be    """
""" used with DFAs.             """

import stateMachine

##########################
#   METHODS AND CLASSES  #
##########################

# minimize the number of states
# @param states The state machine
#        as a multi-dimesnional array 
def minimizeMachine(states):
    return tableFill(states)

# table-filling algorithm
# @param states The state machine
#        as a multi-dimesnional array 
def tableFill(states):
    # create 2D array
    table = []

    # fill in
    # first, identify cases where one state is accepting
    # and the other is not.
    print len(states)
    for i in range(1,len(states)):
        # the index will be i-1
        table.append([])
        for j in range(0,i):
            # create spot
            #table[i-1] = []

            # set to one
            if(states[i].acceptingState!=states[j].acceptingState):
                table[i-1].append(1)
            else:
                # set to zero
                table[i-1].append(0)


    for i in range(0,5):
        table=updateTable(states,table)

     # for debugging
    printTable(table)
    return partition(table,states)

# partition the states into equvilents
# @param table The results of the table-fill algorithm
# @param states The original state machine 
def partition(table,states):
    # declare list
    equivalentList = [];

    # iterate through table to find equivalent states
    for i in range(1,len(states)):
        for j in range(0,i):
            if table[i-1][j]==0:
                # if the states are equivalent, add to list
                equivalentList=addToEquivalenceTable(equivalentList,i,j)

    # add distinguishable states to the list
    equivalentList = finishEquivalenceTable(equivalentList,states)
    print equivalentList
    return constructMinimizedMachine(states,equivalentList)

# MAY BE ABLE TO COMBINE WITH PREVIOUS STEP
# constructs the new machine
# @param oldMachine the original machine
# @param partitioned results of the previous function  
# @return The minimized machine
def constructMinimizedMachine(oldMachine, partition):
    # create new machine 
    for i, state in enumerate(partition):
        # get equivalents for the links
        l0 = findEquivalentIndex(partition,oldMachine[i].links[0])
        l1 = findEquivalentIndex(partition,oldMachine[i].links[1])

        #newState = stateMachine.State()asdfasdfasd

        # create new state and add

    return minimizedMachine

# Prints the table in a more desirable form
# @param table The table to print
def printTable(table):
    for i, row in enumerate(table):
        # state label and row
        print stateMachine.getStateName(i+1),row

    # state row
    stateRow = []

    for i in range(0,len(table)):
        stateRow.append(stateMachine.getStateName(i))
    print " ",'[%s]' % ', '.join(map(str, stateRow))

# Finds the distinguishablity of two states, this function
# is designed to avoid index-out-of-range errors
# @param table The array table
# @param s1 The first state
# @param s2 The second state
# @return The distinguishablity of s1 and s2
def checkDistinguishable(table, s1,s2):
    # use larger state value as the row
    if s1>s2:
        return table[s1-1][s2]
    if s2>s1:
        return table[s2-1][s1]

# Runs through the table while checking for distinguishable
# states.  This step should be run several times to ensure
# accuracy.  I have not come up with a way to determine that
# it is safe.
# @param states The state array
# @param table The table array
# @return The updated table

def updateTable(states,table):
    # find distinguishable states
    for i in range(1,len(states)):
        # get the states connected to this state
        linkI0 = states[i].links[0]
        linkI1 = states[i].links[1]

        for j in range(0,i):
            # get the states connected to this state
            linkJ0 = states[j].links[0]
            linkJ1 = states[j].links[1]

            if states[linkI0].acceptingState!=states[linkJ0].acceptingState:
                # check difference in 0
                table[i-1][j]=1
            elif states[linkI1].acceptingState!=states[linkJ1].acceptingState:
                # check difference in 1
                table[i-1][j]=1
            elif checkDistinguishable(table,linkI0,linkJ0):
                # check for distinguishable states in 0
                table[i-1][j]=1
            elif checkDistinguishable(table,linkI1,linkJ1):
                # check for distinguishable states in 1
                table[i-1][j]=1

    return table

# Adds to the list of equivalent states.  Checks to see
# if an equivalent state has already been found, and adds 
# to that row if it has.  Otherwise, it creates a new row.
# @param equivalentList The current list of equvalent states
# @param s1 The first state of the equivalent pair
# @param s2 The second state of the equivalent pair
# @return The updated pairing list
def addToEquivalenceTable(equivalentList, s1, s2):
    #iterate through list looking for a match
    for i,row in enumerate(equivalentList):
        for j,state in enumerate(row):
            if s1==state:
                row.append(s2)
                return equivalentList
            if s2==state:
                row.append(s1)
                return equivalentList

    # if we are this far, then no equivlent states have been found
    # so we tack them onto a new row
    equivalentList.append([])
    equivalentList[len(equivalentList)-1].append(s1)
    equivalentList[len(equivalentList)-1].append(s2)
    return equivalentList

# Runs through the table once, and adds any states that are not included.
# To achieve this, the full set of states are placed in a seperate list.
# As states are found, they are removed from the list.  The resulting lists
# are combined and then returned.
def finishEquivalenceTable(equivalentList,states):
    # create array of states
    remainingStates = []

    for i, state in enumerate(states):
        remainingStates.append(i)

    # iterate through equivalentList removing states
    for i,row in enumerate(equivalentList):
        for j,state in enumerate(row):
            remainingStates.remove(state)

    # add remaining states
    for i, state in enumerate(remainingStates):
        equivalentList.append([])
        equivalentList[len(equivalentList)-1].append(state)

    return equivalentList

# Iterates through the equvalentList and finds the index
# of the equivalent state
# @param equivalentList The list of equivalent states
# @param index The index to search for
def findEquivalentIndex(equivalentList,index):
    # iterate through list looking for index
    for i, row in enumerate(equivalentList):
        for j, state in enumerate(row):
            if state==index:
                # return the index equivalent to the original state
                return i

    # if we got this far this is a problem
    print "An error occured in finding an equivalent state"
    return -1