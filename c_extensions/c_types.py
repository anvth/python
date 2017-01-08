import ctypes
import os


_file = 'libsample.so'
_path = os.getcwd() + '/' + _file
_mod = ctypes.cdll.LoadLibrary(_path)


gcd = _mod.gcd
gcd.argtypes = (ctypes.c_int, ctypes.c_int)
gcd.restype = ctypes.c_int

_divide = _mod.divide
_divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
_divide.restype = ctypes.c_int

def divide(x, y):
	reminder = ctypes.c_int()
	quotient = _divide(x, y, reminder)
	return quotient, reminder.value


class DoubleArrayType:
	def from_param(self, params):
		type_name = type(params).__name__
		if hasattr(self, 'from_' + type_name):
			return getattr(self, 'from_' + type_name)(params)
		elif isinstance(params, ctypes.Array):
			return params
		else:
			raise TypeError("Cannot convert")

	def from_array(self, params):
		if params.typecode != 'd':
			raise TypeError('Must be a array of type Double')
		ptr, _ = params.buffer_info()
		return ctypes.cast(ptr, ctypes.POINTER())

	def from_list(self, params):
		val = ((ctypes.c_double)*len(params))(*params)
		return val

	from_tuple = from_list

double_array = DoubleArrayType()
_avg = _mod.avg
_avg.argtypes = (double_array, ctypes.c_int)
_avg.restype = ctypes.c_double

def avg(values):
	return _avg(values, len(values))


class Point(ctypes.Structure):
	_fields_ = [('x', ctypes.c_double),
				('y', ctypes.c_double)]

distance = _mod.distance
distance.argtypes = (ctypes.POINTER(Point), ctypes.POINTER(Point))
distance.restype = ctypes.c_double