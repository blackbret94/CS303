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
            if(states[i].getAccepting()!=states[j].getAccepting()):
                table[i-1].append(1)
            else:
                # set to zero
                table[i-1].append(0)


    # for debugging
    printTable(table)
    
    # find distinguishable states
    for i in range(1,len(states)):
        for j in range(0,i):
            # set to zero
            table[i][j]=0

    return partition(table)

# partition the states into
# equvilents
# @param table The results of the
#        table-fill algorithm
def partition(table):
    # do stuff

    return constructMinimizedMachine(state,partitionedMachine)

# MAY BE ABLE TO COMBINE WITH PREVIOUS STEP
# constructs the new machine
# @param oldMachine the original machine
# @param partition the results of the previous
#        function
def constructMinimizedMachine(oldMachine, partition):

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