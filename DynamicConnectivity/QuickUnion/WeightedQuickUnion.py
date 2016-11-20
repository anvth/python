class WeightedQuickUnion(object):
	def __init__(self):
		n = 6
		self.parent = []
		self.size = []
		for i in range(0, n):
			self.parent.append(i)
			self.size.append(1)

		print "Initial Parent Array: " + str(self.parent)
		print "Initial Size Array: " + str(self.size)

	def find_root(self, node):
		while node != self.parent[node]:
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

		print "Array after union of {} and {}: ".format(index_left, index_right) + str(self.parent)

	def check_connected(self, index_left, index_right):
		if self.find_root(index_left) == self.find_root(index_right):
			print "Nodes {} and {} are connected".format(index_left, index_right)



obj = WeightedQuickUnion()
obj.make_union(0, 1)
obj.make_union(1, 2)
obj.check_connected(0, 2)
		
