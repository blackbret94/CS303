"""  PDA CREATOR  """
""" BY BRET BLACK """

#####################
#   START PROGRAM   #
#####################

import stateMachine

# define tree
def tree(): return defaultdict(tree)

# controls the PDA
class PDAController:
	# blank constructor
	def __init__(self):
		# get file
		file = "pdaExample.txt"

		# create tree to hold instantaneous descriptions
		instTree = list()

		# parse input string
		inputString = "1001"

		# make PDA
		pda = makePDA(file)

		# run
		run(inputString,pda)

	# creates a PDA from a text file
	def makePDA(self,file):
		# read states and accepting states
		states = list()
		acceptingStates = list()

		# read input symbols
		inputSymbols = list()

		# read stackAlphabet
		stackAlphabet = list()

		#read transition functions
		transitionFunction = list()

		# read start state
		startState = stateMachine.State()

		# read start symbol
		startSymbol = list()

		# create PDA
		pda = PDA(states,inputSymbols,stackAlphabet,transitionFunction,startState,startSymbol,acceptingStates)

		return PDA

	# generates a tree from the PDA and input string
	def run(self,inputString,PDA):
		# string to array
		inputArray = list(inputString)

		# pop from string
		for i,val in inputString:
			# add an InstantaneousDescription node to each live branch of the tree
			

# defines a PDA machine
class PDA:
	# blank constructor
	def __init__(self):
		# do stuff

	# accepts seven inputs
	def __init__(self,states,inputSymbols,stackAlphabet,transitionFunction,startState,startSymbol,acceptingStates):
		# do stuff
		


# defines a transition function
class transitionFunction:
	# blank constructor
	def __init__(self):
		# do stuff

	# accepts four inputs 
	# @param q The start state
	# @param a Input symbol or epsilon
	# @param X stack symbol
	# @param pairs The output pairs
	def __init__(self,q,a,X,pairs):
		# do stuff

# defines an instantaneous description
class InstantaneousDescription:
	# blank constructor
	def __init__(self):
		# mark as incomplete
		complete = False

		# do stuff

	# constructor with three inputs 
	# @param q The state
	# @param w The remaining input
	# @param r The stack contents
	def __init__(self,q,w,r):
		# mark as incomplete
		complete = False

		# do stuff
