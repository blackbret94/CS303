"""  PDA CREATOR  """
""" BY BRET BLACK """

#####################
#   START PROGRAM   #
#####################

import stateMachine
import tree

# controls the PDA
class PDAController:
	# blank constructor
	def __init__(self):
		# get file
		file = "pdaExample.txt"

		# create tree to hold instantaneous descriptions
		instTree = Tree()

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
	def run(self,inputString,thisPDA):
		# string to array
		inputArray = list(inputString)

		# pop from string
		for i,val in inputString:
			# get top of stack and current state
			stackTop = thisPDA.stack(len(thisPDA.stack)


			# match a transition function
			for j,function in transitionFunction

			# add an InstantaneousDescription node to each live branch of the tree

	# reads a transition function
	# @param stack The list representing the stack
	# @param transFunction the instance of transitionFunction we are reading from
	def readTransitionFunction(self,stack,transFunction):
		# pop from stack
		if(transitionFunction.pairs)
		# push to stack

		# change state
			

# defines a PDA machine
class PDA:
	# blank constructor
	def __init__(self):
		# this should never be called

	# accepts seven inputs
	def __init__(self,states,inputSymbols,stackAlphabet,transitionFunction,startState,startSymbol,acceptingStates):
		# save params
		self.states = states
		self.inputSymbols = inputSymbols
		self.stackAlphabet = stackAlphabet
		self.transitionFunction = transitionFunction
		self.startState = startState
		self.startSymbol = startSymbol
		self.acceptingStates = acceptingStates
		
		self.stack = list() #empty stack


# defines a transition function
class TransitionFunction:
	# blank constructor
	def __init__(self):
		# do stuff

	# accepts four inputs 
	# @param q The start state
	# @param a Input symbol or epsilon
	# @param X stack symbol
	# @param pairs The output pairs
	def __init__(self,q,a,X,pairs):
		# save params as instance vars
		self.q = q
		self.a = a 
		self.X = X
		self.pairs = pairs

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

		# save params as instance vars
		self.q = q
		self.w = w
		self.r = r
