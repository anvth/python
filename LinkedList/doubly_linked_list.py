from node import BaseNode

class Node(BaseNode):
	def __init__(self, value):
		super(Node, self).__init__(value)
		self.prev = None

	def get_prev(self):
		return self.prev

	def set_prev(self, new_prev):
		self.prev = new_prev


class DoubleLinkedList(object):
	def __init__(self):
		self.head = None
		self.length = 0
	

	def add(self, data):
		node = Node(data)

		if self.head is None:
			self.head = node
			self.length += 1
		else:
			self.head.set_prev(node)
			node.set_next(self.head)
			self.head = node
			self.length += 1


	def add_at(self, data, position):		
		if position > self.length:
			print("Invalid position")
			return
		elif position == self.length:
			self.append(data)
		elif position == 0:
			self.add(data)
		else:
			node = Node(data)
			temp = self.head
			for ite in range(1, position):
				temp = temp.get_next()
			
			new_next = temp.get_next()
			temp.set_next(node)
			node.set_prev(temp)
			node.set_next(new_next)
			new_next.set_prev(node)
			self.length += 1


	def append(self, data):
		node = Node(data)

		if self.head is None:
			self.head = node
			self.length += 1
		else:
			temp = self.head
			while temp.get_next() is not None:
				temp = temp.get_next()
			temp.set_next(node)
			node.set_prev(temp)
			self.length += 1


	def remove(self):
		if self.head is None:
			print("Nothing to remove")
			return
		else:
			self.head = self.head.get_next()
			self.length -= 1


	def detach(self):
		if self.head is None:
			print("Nothing to remove")
			return
		else:
			temp = self.head
			prev = None
			while temp.get_next() is not None:
				prev = temp
				temp = temp.get_next()
			prev.set_next(None)
			self.length -= 1


	def remove_at(self, position):
		if position > self.length:
			print("Invalid position")
			return
		elif position == 0:
			self.remove()
		elif position == self.length:
			self.detach()
		else:
			temp = self.head
			prev_node = None
			next_node = None
			for ite in range(1, position):
				prev_node = temp
				temp = temp.get_next()

			next_node = temp.get_next()
			prev_node.set_next(next_node)
			next_node.set_prev(prev_node)


	def display(self):
		if self.head is None:
			print("Nothing to display")
			return
		else:
			temp = self.head
			while temp is not None:
				print(temp.get_data())
				temp = temp.get_next()
		print("---------------------------")

	def clear_list(self):
		self.head = None
		self.length = 0


if __name__ == '__main__':
	obj = DoubleLinkedList()
	obj.display()
	obj.add(3)
	obj.display()
	obj.add(2)
	obj.display()
	obj.append(5)
	obj.display()
	obj.add_at(1, 0)
	obj.display()
	obj.add_at(4, 3)
	obj.display()
	obj.add_at(6, 5)
	obj.display()
	obj.add(7)
	obj.display()
	obj.remove()
	obj.display()
	obj.detach()
	obj.display()
	obj.remove_at(0)
	obj.display()
	obj.remove_at(4)
	obj.display()
	obj.remove_at(2)
	obj.display()