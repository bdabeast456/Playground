# Test modifying basic tree
from bp_collections import Stack

# Constructed and raised if method in base class has yet to be
# implemented.
class MethodNotImplementedException(Exception):
	pass

# Base tree node class.
# Use only as abstract class.
#
# "Public" methods:
#
# __init__()
# Initializes a tree node
# @param item, the item to store
# @param parent, the parent of this node
# @return an object of type TreeNode
#
class TreeNode:
	def __init__(self, item, parent):
		self._item = item
		self._parent = parent

# Base tree class.
# Use only as abstract class
#
# "Public" methods:
#
# __init__()
# Initializes a Tree
# @return an object of type Tree
#
# Methods to implement:
#
# findItem()
# Finds an item within the tree and confirms if it is found
# @param item, the item to search for
# @return True if the item is found and False otherwise
#
# insertItem()
# Inserts an item into the tree and confirms if the insertion is
# successful -- item must be of a coercible type or instance of the
# same class as all other items to proceed with expected behavior
# @param item, the item to insert into the tree
# @return True if successful and False otherwise
#
# removeItem()
# Removes an item from the tree and confirms if the removal is
# successful -- item must be of a coercible type or instance of
# the same class as all other items to proceed with expected behavior
# @param item, the item to find and remove
# @return True if the item is successfully removed and False otherwise
# 
class Tree:
	def __init__(self):
		self._root = None
		self._size = 0

	def findItem(self, item):
		raise MethodNotImplementedException()

	def insertItem(self, item):
		raise MethodNotImplementedException()

	def removeItem(self, item):
		raise MethodNotImplementedException()

# Node for binary trees.
#
# "Public" methods:
#
# __init__()
# Initializes a binary tree node
# @param item, the item to store in the node
# @param parent (optional), the parent node to this one
# @param left (optional), the left branch represented by a node
# @param right (optional), the right branch represented by a node
# @return object of type BinaryTreeNode
#
# getItem()
# Returns the item stored in this node
# @return primitive or object (type can vary)
#
# getParent()
# Returns the parent of this node
# @return object of type BinaryTreeNode
#
# getLeft()
# Returns the left branch from this node
# @return object of type BinaryTreeNode
#
# getRight()
# Returns the right branch from this node
# @return object of type BinaryTreeNode
#
# setItem()
# Sets the contained by the node
# @param item, a primitive or object (type can vary)
# @return
#
# setParent()
# Sets the parent node of the current node
# @param node, None or an object of type BinaryTreeNode
# @return
#
# setLeft()
# Sets the left branch of the current node
# @param node, None or an object of type BinaryTreeNode
# @return
#
# setRight()
# Sets the right branch of the current node
# @param node, None or an object of type BinaryTreeNode
# @return
#
class BinaryTreeNode(TreeNode):
	def __init__(self, item, parent=None, left=None, right=None):
		assert (left == None or type(left) == BinaryTreeNode) and \
			   (right == None or type(right) == BinaryTreeNode) and \
			   (parent == None or type(parent) == BinaryTreeNode) \
			   , "Arguments 'parent', 'left' and 'right' must be None or of type BinaryTreeNode"
		super().__init__(item, parent)
		self.__left = left
		self.__right = right

	def getItem(self):
		return self._item

	def getParent(self):
		return self._parent

	def getLeft(self):
		return self.__left

	def getRight(self):
		return self.__right

	def setItem(self, item):
		self._item = item

	def setParent(self, node):
		assert node == None or type(node) == BinaryTreeNode \
			   , "Argument 'node' must be of type BinaryTreeNode"

	def setLeft(self, node):
		assert node == None or type(node) == BinaryTreeNode \
			   , "Argument 'node' must be of type BinaryTreeNode"
		self.__left = node
		if self.__left != None:
			self.__left.setParent(self)

	def setRight(self, node):
		assert node == None or type(node) == BinaryTreeNode \
			   , "Argument 'node' must be of type BinaryTreeNode"
		self.__right = node
		if self.__right != None:
			self.__right.setParent(self)

# Binary tree implementation. More methods may be added later.
#
# "Public" methods:
#
# __init__()
# Initializes a binary tree
# @return object of type BinaryTreeNode
#
# findItem()
# Searches for an item in the binary tree
# @param item, the item to search for
# @return True if the item is found and False otherwise
#
# insertItem()
# Inserts an item into the tree -- item must be of a coercible type or
# instance of the same class as all other items to proceed with expected
# behavior
# @param item, the primitive or object (type can vary) to insert into the tree
# @return True if insertion is successful and False if it fails or the item
#		  already exists in the tree
#
# removeItem()
# Removes an item from the tree
# @param item, the item to remove from the tree
# @return True if removal is successful and False otherwise
#
# getNthLargestItem()
# Returns the nth largest item from the tree. If n is greater than the
# size of the tree, None is returned
# @param n, an integer describing the inorder rank of the item to
# 			retrieve
# @return None, a primitive, or object (type can vary)
# 
class BinaryTree(Tree):
	def __init__(self):
		super().__init__()

	def __checkItem(self, item):
		if self._root == None:
			return True
		try:
			result = self._root.getItem() > item
			return True
		except:
			return False

	def findItem(self, item):
		assert self.__checkItem(item), "Argument 'item' must be of same type as root"

		if self._size > 0:
			currentNode = self._root
			while currentNode != None:
				if currentNode.getItem() == item:
					return True
				elif currentNode.getItem() > item:
					currentNode = currentNode.getLeft()
				else:
					currentNode = currentNode.getRight()
		return False

	def insertItem(self, item):
		assert self.__checkItem(item), "Argument 'item' must be of same type as root"

		if self._size == 0:
			self._root = BinaryTreeNode(item)
		else:
			currentNode = self._root
			while True:
				if currentNode.getItem() > item:
					if currentNode.getLeft() == None:
						currentNode.setLeft(BinaryTreeNode(item))
						break
					currentNode = currentNode.getLeft()
				elif currentNode.getItem() < item:
					if currentNode.getRight() == None:
						currentNode.setRight(BinaryTreeNode(item))
						break
					currentNode = currentNode.getRight()
				else:
					return False

		self._size += 1
		return True

	def removeItem(self, item):
		assert self.__checkItem(item), "Argument 'item' must be of same type as root"

		if self._size == 0:
			return False

		currentNode = self._root
		isLeft = False
		while currentNode != None:
			if currentNode.getItem() == item:
				currParReplace = None
				if currentNode.getParent() != None:
					if isLeft:
						currParReplace = lambda x: currentNode.getParent().setLeft(x)
					else:
						print("HI")
						currParReplace = lambda x: currentNode.getParent().setRight(x)
				else:
					def setRoot(node):
						self._root = node
					currParReplace = setRoot

				if currentNode.getLeft() != None:
					leftRoot = currentNode.getLeft()
					if leftRoot.getRight() == None:
						currParReplace(leftRoot)
						leftRoot.setLeft(leftRoot.getLeft())
					else:
						while leftRoot.getRight() != None:
							leftRoot = leftRoot.getRight()
						leftRoot.getParent().setRight(leftRoot.getLeft())
						currParReplace(leftRoot)
						leftRoot.setLeft(currentNode.getLeft())

					leftRoot.setRight(currentNode.getRight())
				elif currentNode.getRight() != None:
					rightRoot = currentNode.getRight()
					if rightRoot.getLeft() == None:
						currParReplace(rightRoot)
						rightRoot.setRight(rightRoot.getRight())
					else:
						while rightRoot.getLeft() != None:
							rightRoot = rightRoot.getLeft()
						rightRoot.getParent().setLeft(rightRoot.getRight())
						currParReplace(rightRoot)
						rightRoot.setRight(currentNode.getRight())

					rightRoot.setLeft(currentNode.getLeft())
				else:
					currParReplace(None)
				self._size -= 1
				return True		
			elif currentNode.getItem() > item:
				currentNode = currentNode.getLeft()
				isLeft = True
			else:
				currentNode = currentNode.getRight()
				isLeft = False

		return False

	def getNthLargestItem(self, n):
		assert n > 0, "Argument 'n' must be a positive integer"
		if self._size < n:
			return
		toExplore = Stack()
		currentNode = self._root
		rightExplored = (self._root.getRight() == None)
		i = n - 1
		while i > 0:
			if rightExplored:
				leftNode = currentNode.getLeft()
				if leftNode != None:
					toExplore.push((leftNode, (leftNode.getRight() == None)))
				i -= 1
			else:
				rightNode = currentNode.getRight()
				toExplore.push((currentNode, True))
				toExplore.push((rightNode, (rightNode.getRight() == None)))
			currentNode, rightExplored = toExplore.pop()

		return currentNode.getItem()
