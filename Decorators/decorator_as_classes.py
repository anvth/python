from functools import wraps
import types

class Profiled:
	def __init__(self, func):
		wraps(func)(self)
		self.ncalls = 0

	def __call__(self, *args, **kwargs):
		self.ncalls += 1
		return self.__wrapped__(*args, **kwargs)

	def __get__(self, instance, cls):
		if instance is None:
			return self
		else:
			return types.MethodType(self, instance)


@Profiled
def add(x, y):
	return x + y

print(add(1, 2))
print(add(3, 4))
print(add.ncalls)