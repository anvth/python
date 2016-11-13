"""
Input format:
Line 1: Size of the array<space>No. of unions<space>No. of connected checks
Line 2..n: List of nodes to be joined

Example:
5 2 1
1 4
2 3
1 2
"""
class QuickUnion(object):
	def __init__(self):
		self.arr = []

		self.f = open('input.txt', 'r')
		self.arr_size, self.union_calls, self.connected_checks = self.f.readline().split(' ')

		for ite in range(0, int(self.arr_size)):
			self.arr.append(ite)

		print "Initial Array: " + str(self.arr) + "\n"

	def make_union(self):
		for ite in range(0, int(self.union_calls)):
			line = self.f.readline()
			index_left, index_right = line.split(' ')
			index_left_root = self._find_root(int(index_left))
			index_right_root = self._find_root(int(index_right))
			self.arr[index_left_root] = self.arr[index_right_root]
			print "Array after union of {} and {}: ".format(index_left_root, index_right_root) + str(self.arr)


	def check_connected(self):
		for ite in range(0, int(self.connected_checks)):
			line = self.f.readline()
			index_left, index_right = line.split(' ')
			index_left_root = self._find_root(int(index_left))
			index_right_root = self._find_root(int(index_right))
			if index_right_root == index_left_root:
				print "Root of {} is {} and {} is {}: Connected!".format(index_left, index_left_root, index_right, index_right_root)
			else:
				print  "Root of {} is {} and {} is {}: Not Connected!".format(index_left, index_left_root, index_right, index_right_root)
			

	def _find_root(self, index):
		while index != self.arr[index]:
			index = self.arr[index]

		return index


obj = QuickUnion()
obj.make_union()
obj.check_connected()
