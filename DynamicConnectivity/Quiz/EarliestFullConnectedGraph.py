class EarliestFullConnectedGraph(object):
	def __init__(self):
		self.input_size = 5
		self.parent = []
		self.size = []

		for ite in range(0, self.input_size):
			self.parent.append(ite)
			self.size.append(1)
			
		print "Initial parent array: " + str(self.parent)
		print "Initial size array: " + str(self.size)
			
			

	def find_root(self, node):
		while node != self.parent[node]:
			self.parent[node] = self.parent[self.parent[node]]
			node = self.parent[node]
		return node

	def make_union(self, index_left, index_right):
		index_left_root = self.find_root(index_left)
		index_right_root = self.find_root(index_right)

		if index_left_root == index_right_root:
			return
		
		if self.size[index_left_root] < self.size[index_right_root]:
			self.parent[index_left_root] = index_right_root
			self.size[index_right_root] += self.size[index_left_root]
		else:
			self.parent[index_right_root] = index_left_root
			self.size[index_left_root] += self.size[index_right_root]
			
		print "After union of {} and {}: ".format(index_left, index_right) + str(self.parent)
		if self.size[index_right_root] == self.input_size or self.size[index_left_root] == self.input_size:
			print "*** All are connected ***"

obj = EarliestFullConnectedGraph()
obj.make_union(0, 1)
obj.make_union(1, 2)
obj.make_union(3, 4)
obj.make_union(1, 4)
obj.make_union(2, 4)

