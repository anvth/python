class BaseNode(object):
	def __init__(self, value):
		self.value = value
		self.next = None

	def get_data(self):
		return self.value

	def get_next(self):
		return self.next

	def set_data(self, new_data):
		self.value = new_data

	def set_next(self, new_next):
		self.next = new_next
