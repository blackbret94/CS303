""" A TREE CLASS """
""" BY BRET BLACK """

class Tree:
	def __init__(self):
		head = None

	def setHeadNewNode(self, data):
		head = Node(data)

	def setHead(self, node):
		head = node;

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = list()

    def add_child(self, obj):
        self.children.append(obj)