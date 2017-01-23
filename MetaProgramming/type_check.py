from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kargs):
	def decorate(func):
		if not __debug__:
			return func

		sig = signature(func)
		bound_types = sig.bind_partial(*ty_args, **ty_kargs).arguments

		@wraps(func)
		def wrapper(*args, **kargs):
			bound_values = sig.bind(*args, **kargs)

			for name, value in bound_values.arguments.items():
				if name in bound_types:
					if not isinstance(value, bound_types[name]):
						raise TypeError(
							'Argument {} must be {}'.format(name, bound_types[name])
							)
			return func(*args, **kargs)
		return wrapper
	return decorate

@typeassert(int, int)
def add(x ,y):
	return x + y


print(add(2, 3))
print(add(2, 'hello'))