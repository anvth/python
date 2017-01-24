from functools import wraps
import inspect

def decorator(func):
	if 'debug' in inspect.getargspec(func).args:
		raise TypeError('debug already defined')

	@wraps(func)
	def wrapper(*args, debug=False, **kwargs):
		if debug:
			print('Calling', func.__name__)
		return func(*args, **kwargs)
	
	sig = inspect.signature(func)
	params = list(sig.parameters.values())
	params.append(inspect.Parameter('debug',
		inspect.Parameter.KEYWORD_ONLY,
		default=False))
	wrapper.__signature__ = sig.replace(parameters=params)
	return wrapper

@decorator
def add(x, y):
	return x + y


print(add(2, 3))
print(add(2, 3, debug=True))