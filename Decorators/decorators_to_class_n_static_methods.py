from functools import wraps
import time

def timethis(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(func.__name__, end-start)
		return result
	return wrapper

class Spam(object):
	@timethis
	def instance_method(self, n):
		while n > 0:
			n -= 1

	@classmethod
	@timethis
	def class_method(cls, n):
		while n > 0:
			n -= 1

	@staticmethod
	@timethis
	def static_method(n):
		while n > 0:
			n -= 1


s = Spam()
s.instance_method(10000)
Spam.class_method(10000)
Spam.static_method(10000)