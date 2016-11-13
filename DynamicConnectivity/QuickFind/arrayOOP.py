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
class QuickFind(object):
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
			self._make_union(int(index_left), int(index_right))

	def _make_union(self, index_left, index_right):
		val = self.arr[index_left]
		self.arr[index_left] = self.arr[index_right]
		for temp in self.arr:
			if temp == val:
				self.arr[self.arr.index(temp)] = self.arr[index_right]
		print "After joining {} and {}: ".format(index_left, index_right) + str(self.arr)


	def check_connected(self):
		for ite in range(0, int(self.connected_checks)):
			line = self.f.readline()
			index_left, index_right = line.split(' ')
			if self._connected(int(index_left), int(index_right)):
				print "Connected!"
			else:
				print "Not Connected!"

	def _connected(self, index_left, index_right):
		return self.arr[index_left] == self.arr[index_right]

obj = QuickFind()
obj.make_union()
obj.check_connected()	







