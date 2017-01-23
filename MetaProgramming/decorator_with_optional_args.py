import sys
import logging
from functools import wraps, partial

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
	def decorator(func):
		if func is None:
			return partial(logged, level=level, name=name, message=message)

		logname = name if name else func.__module__
		log = logging.getLogger(logname)
		logmessage = message if message else func.__name__

		@wraps(func)
		def wrapper(*args, **kargs):
			logging.basicConfig(stream=sys.stdout, level=level)
			log.log(level, logmessage)
			return func(*args, *kargs)
		return wrapper
	return decorator


@logged(logging.INFO)
def add(x, y):
	return x + y


@logged()
def sub(x, y):
	return x - y

print(add(2, 3))
print(sub(4, 1))