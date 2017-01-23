from functools import wraps
import logging
import sys


def logged(level, name=None, message=None):
	def decorator(func):
		logname = name if name else func.__module__
		logging.basicConfig(stream=sys.stdout, level=level)
		log = logging.getLogger(logname)
		logmessage = message if message else func.__name__

		@wraps(func)
		def wrapper(*args, **kargs):
			log.log(level, logmessage)
			return func(*args, **kargs)
		return wrapper
	return decorator


@logged(logging.DEBUG)
def add(x, y):
	return x + y


add(2, 3)