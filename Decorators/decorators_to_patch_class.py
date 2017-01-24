def log_attribute(cls):
	orig_getattribute = cls.__getattribute__

	def new_getattribute(self, name):
		print('Getting: ', name)
		return orig_getattribute(self, name)

	cls.__getattribute__ = new_getattribute
	return cls

@log_attribute
class A:
	def __init__(self):
		self.x = 5
	
	def spam(self):
		pass


a = A()
print(a.x)