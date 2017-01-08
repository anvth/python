from node import BaseNode as Node

class UnorderedList(object):
	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head == None

	def display(self):
		if self.head is None:
			print "Nothing to display!!"
			return

		current = self.head
		while current != None:
			print current.get_data()
			current = current.get_next()
		print "--------------------------------"

	def add(self, item):
		temp = Node(item)
		temp.set_next(self.head)
		self.head = temp

	def add_to_end(self, item):
		current = self.head
		while current.get_next() != None:
			current = current.get_next()
		current.set_next(Node(item))

	def delete(self):
		self.head = self.head.get_next()

	def delete_at_end(self):
		current = self.head
		while current.get_next().get_next() != None:
			current = current.get_next()
		current.set_next(None)


if __name__ == '__main__':
	obj = UnorderedList()	
	obj.add(2)
	obj.display()
	obj.add(1)
	obj.display()
	obj.add_to_end(3)
	obj.display()
	obj.delete()
	obj.display()
	obj.delete_at_end()
	obj.display()
			
