"""
"""
class DBInterfaceMeta(type):
        def __init__(cls, name, bases, dict):
                if not hasattr(cls, 'registry'):
                        cls.registry= {}
                else:
                        interface_id = name.lower()
                        cls.registry[interface_id] = cls
                return super(DBInterfaceMeta, cls).__init__(name, bases, dict)


class DBInterface(object):
    __metaclass__ = DBInterfaceMeta


print(DBInterface.registry)




class FirstInterface(DBInterface):
    pass


class SecondInterface(DBInterface):
    pass


class SecondInterfaceModified(SecondInterface):
    pass


print(DBInterface.registry)

