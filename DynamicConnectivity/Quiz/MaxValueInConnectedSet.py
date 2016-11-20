class WeightedQuickUnionWithPC(object):
	def __init__(self):
		n = 6
		self.parent = []
		self.size = []
		self.max = []
		for i in range(0, n):
			self.parent.append(i)
			self.max.append(i)
			self.size.append(1)

		print "Initial Parent Array: " + str(self.parent)
		print "Initial Max Array: " + str(self.max)
		print "Initial Size Array: " + str(self.size)

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
			if self.max[index_right_root] <= index_left_root:
				self.max[index_right_root] = index_left_root			
		else:
			self.parent[index_right_root] = index_left_root
			self.size[index_left_root] += self.size[index_right_root]
			if self.max[index_left_root] <= index_right_root:
				self.max[index_left_root] = index_right_root

		print "Array after union of {} and {}: ".format(index_left, index_right) + str(self.parent)
		print "Max in connected set Array: " + str(self.max)

	def check_connected(self, index_left, index_right):
		pass

	def find_max(self, node):
		print "Max Value of the connected set containing {}: ".format(node) + str(self.max[self.find_root(node)])


obj = WeightedQuickUnionWithPC()
obj.make_union(0, 1)
obj.make_union(1, 2)
obj.find_max(0)
		
