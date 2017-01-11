from node import BaseNode

class Node(BaseNode):
	def __init__(self, value):
		super(Node, self).__init__(value)
		self.next = self

class CircularLinkedList(object):
	def __init__(self):
		self.head = None

	def add(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
			self.head.set_next(self.head)
		else:
			temp = self.head
			if temp.get_next() is self.head:
				self.head.set_next(node)
				node.set_next(self.head)
				self.head = node
			else:
				while temp.get_next() is not self.head:
					temp = temp.get_next()
				temp.set_next(node)
				node.set_next(self.head)
				self.head = node


	def append(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
			self.head.set_next(self.head)
		else:
			temp = self.head
			if temp.get_next() is self.head:
				self.head.set_next(node)
				node.set_next(self.head)
			else:
				while temp.get_next() is not self.head:
					temp = temp.get_next()
				temp.set_next(node)
				node.set_next(self.head)


	def remove(self):
		if self.head is None:
			print("Nothing to remove")
		else:
			temp = self.head
			if temp.get_next() is self.head:
				self.head = None
			else:
				while temp.get_next() is not self.head:
					temp = temp.get_next()
				self.head = self.head.get_next()
				temp.set_next(self.head)


	def detach(self):
		if self.head is None:
			print("Nothing to detach")
		else:
			temp = self.head
			while temp.get_next() is not self.head:
				prev_node  = temp
				temp = temp.get_next()
			prev_node.set_next(self.head)


	def display(self):
		temp = self.head
		if self.head is None:
			print("Nothing to display")
			return
		print(temp.get_data())
		while temp.get_next() is not self.head:
			temp = temp.get_next()
			print(temp.get_data())
		print("-------------------------")


	def clear_list(self):
		self.head = None


if __name__ == '__main__':
	obj = CircularLinkedList()
	obj.add(3)
	obj.display()
	obj.add(2)
	obj.display()
	obj.add(1)
	obj.display()
	obj.append(4)
	obj.display()
	obj.remove()
	obj.display()
	obj.detach()
	obj.display()