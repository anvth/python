import time
from functools import wraps

def timethis(func):
	@wraps(func)
	def wrapper(*args, **kargs):
		start = time.time()
		result = func(*args, **kargs)
		end = time.time()
		print(func.__name__, end-start)
		return result
	return wrapper

@timethis
def countdown(n):
	while n > 0:
		n -= 1


countdown(1000)