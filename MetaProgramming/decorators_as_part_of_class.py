from functools import wraps


class A(object):
	def decorator_one(self, func):
		@wraps(func)
		def wrapper(*args, **kargs):
			print("Decorator one")
			return func(*args, **kargs)
		return wrapper


class B(A):
	@classmethod
	def decorator_two(cls, func):
		@wraps(func)
		def wrapper(*args, **kargs):
			print("Decorator two")
			return func(*args, **kargs)
		return wrapper


obj = B()


@obj.decorator_one
@B.decorator_two
def add(x, y):
	return x + y


print(add(2, 3))