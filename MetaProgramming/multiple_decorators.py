from functools import wraps


def decorator_one(func):
	@wraps(func)
	def wrapper(*args, **kargs):
		print("Decorator one")
		return func(*args, *kargs)
	return wrapper


def decorator_two(func):
	@wraps(func)
	def wrapper(*args, **kargs):
		print("Decorator two")
		return func(*args, *kargs)
	return wrapper
	

@decorator_one
@decorator_two
def add(x, y):
	return x + y


add(2, 3)