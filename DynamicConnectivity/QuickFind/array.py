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
def make_union(index_left, index_right):
	val = arr[index_left]
	arr[index_left] = arr[index_right]
	for temp in arr:
		if temp == val:
			arr[arr.index(temp)] = arr[index_right]
	print "After joining {} and {}: ".format(index_left, index_right) + str(arr)

def connected(index_left, index_right):
	return arr[index_left] == arr[index_right]	

arr = []

f = open('input.txt', 'r')
arr_size, union_calls, connected_checks = f.readline().split(' ')

for ite in range(0, int(arr_size)):
	arr.append(ite)

print "Initial Array: " + str(arr) + "\n"

for ite in range(0, int(union_calls)):
	line = f.readline()
	index_left, index_right = line.split(' ')
	make_union(int(index_left), int(index_right))

for ite in range(0, int(connected_checks)):
	line = f.readline()
	index_left, index_right = line.split(' ')
	if connected(int(index_left), int(index_right)):
		print "Connected!"
	else:
		print "Not Connected!"





