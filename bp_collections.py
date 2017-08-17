# These objects are simple building-blocks. Should be user friendly.

# Singly Linked List Node.
#
# "Public" methods:
#
# __init__()
# Initializes a Singly Linked Node
# @param item, the item to store in this node
# @param nextNode (optional), the next node of type SLN or None
# @return an object of type SLN
#
# getItem()
# Returns the item stored in this node
# @return the stored primitive or object (type can vary)
#
# getNextNode()
# Returns the next node in the sublist starting from this node
# @return an object of type SLN
#
# setItem()
# Sets the item stored in this node
# @param item, the item to store
# @return
#
# setNextNode()
# Sets the next node in the sublist starting with this node
# to a new node
# @param node, the next node in the linked list.
# @return
#
class SLN:
	def __init__(self, item, nextNode=None):
		assert nextNode == None or type(nextNode) == SLN, \
			   "Argument 'nextNode' must be None or of type SLN"
		self.__item = item
		self.__next = nextNode

	def getItem(self):
		return self.__item

	def getNextNode(self):
		return self.__next

	def setItem(self, item):
		self.__item = item

	def setNextNode(self, node):
		assert type(node) == SLN, "Argument 'node' must be of type SLN"
		self.__next = node

# Singly Linked List with tail accessibility.
#
# "Public" methods:
#
# __init__()
# Initializes a new Singly Linked List
# @return an object of type SLL
#
# size()
# Returns the size (cardinality) of the linked list
# @return an integer corresponding to the size of the list
#
# prepend()
# Add an item to the front of the linked list
# @param item, the item to add to the list
# @return
#
# append()
# Add an item to the end of the linked list
# @param item, the item to add to the list
# @return
#
# removeItemAtIndex()
# Removes and returns the item at index within the list -- 
# index must be [0, list size - 1]
# @param index, the integer index to retrieve an item at
# @return the item store at index or None
#
class SLL:
	def __init__(self):
		self.__head = None
		self.__tail = None
		self.__size = 0

	def size(self):
		return self.__size

	def prepend(self, item):
		if self.__head == None:
			self.__head = SLN(item)
			self.__tail = self.__head
		else:
			self.__head = SLN(item, self.__head)
		self.__size += 1

	def append(self, item):
		if self.__head == None:
			self.__head = SLN(item)
			self.__tail = self.__head
		else:
			newNode = SLN(item)
			self.__tail.setNextNode(newNode)
			self.__tail = newNode
		self.__size += 1

	def getItemAtIndex(self, index):
		if self.__size == 0 or index < 0 or index >= self.__size:
			raise IndexError("index out of range or size is 0")

		currentNode = self.__head
		i = 0
		while i < index:
			currentNode = currentNode.getNextNode()
			i += 1

		return currentNode.getItem()

	def removeItemAtIndex(self, index):
		if self.__size == 0 or index < 0 or index >= self.__size:
			raise IndexError("index out of range or size is 0")

		previousNode = None
		currentNode = self.__head
		i = 0
		while i < index:
			previousNode = currentNode
			currentNode = currentNode.getNextNode()
			i += 1

		if self.__tail == currentNode:
			if self.__head == self.__tail:
				self.__tail = None
			else:
				self.__tail = previousNod
		if previousNode != None:
			previousNode.setNextNode(currentNode.getNextNode())
		else:
			self.__head = currentNode.getNextNode()

		self.__size -= 1
		return currentNode.getItem()

	def __str__(self):
		i = 0
		currentNode = self.__head
		string = "["
		while i < self.__size:
			string += str(currentNode.getItem()) + \
					  (", " if currentNode.getNextNode() != None else "")
			currentNode = currentNode.getNextNode()
			i += 1
		return string + "]"

	def __repr__(self):
		string = "Singly Linked List object with items: "
		if self.__size == 0:
			return string + "Empty"
		return string + str(self.__head.getItem()) + (", ..." if self.__size > 1 else "")

# Basic stack implementation.
#
# "Public" methods:
#
# __init__()
# Initializes the Stack object
# @return an object of type Stack
#
# push()
# Adds an item to the stack
# @param item, the item to stack
# @return
#
# pop()
# Removes and returns the item on top of the stack
# @return an item from the stack (type can vary) or None if
#		  the stack is empty
#
class Stack:
	def __init__(self):
		self.__linkedList = SLL()

	def push(self, item):
		self.__linkedList.prepend(item)

	def pop(self):
		return self.__linkedList.removeItemAtIndex(0)

# Basic queue implementation.
#
# "Public" methods:
#
# __init__()
# Initializes the Queue object
# @return an object of type Queue
#
# queue()
# Adds an item to the queue
# @param item, the item to queue
# @return
#
# dequeue()
# Removes and returns the item on top of the queue
# @return an item from the queue (type can vary) or None if
#		  the queue is empty
#
class Queue:
	def __init__(self):
		self.__linkedList = SLL()

	def queue(self, item):
		self.__linkedList.append(item)

	def dequeue(self):
		return self.__linkedList.removeItemAtIndex(0)
