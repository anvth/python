"""
"""
from functools import wraps


class event(object):
        def __init__(self, evt=None):
                self.event = evt


        def __call__(self, func):
                @wraps(func)
                def wrap(inst, evt, *args, **kwargs):
                        if self.event is None:
                                return func(inst, evt, *args, **kwargs)
                        else:
                                return None


                return wrap


class DBInterfaceMeta(type):
        def __init__(cls, name, bases, dict):
                if not hasattr(cls, '_registry'):
                        cls.registry= {'handlers': []}


                for member in dict.values():
                        cls._registry['handlers'].append(member)
                return super(DBInterfaceMeta, cls).__init__(name, bases, dict)


class DBInterface(object):
        __metaclass__ = DBInterfaceMeta

	_registry= {'handlers': []}
        
	def handle_event(self, evt, *args, **kwargs):
                for handler in self._registry['handlers']:
                        handler(self, evt, *args, **kwargs)


print(DBInterface._registry)




class FirstInterface(DBInterface):
        @event(None)
        def print_event(self, evt):
                if evt is not None:
                        print('=== {}'.format(evt))




obj = FirstInterface()
obj.handle_event('Hello')
