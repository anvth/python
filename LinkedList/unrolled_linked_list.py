##################
##  Incomplete  ##
##################

from node import BaseNode
from circular_linked_list import CircularLinkedList

class Node(BaseNode):
	def __init__(self, data):
		super(Node, self).__init__(data)

class UnrolledLinkedList(object):
	def __init__(self):
		self.head = None
		self.max_nodes = 0
		self.circular_list = CircularLinkedList()