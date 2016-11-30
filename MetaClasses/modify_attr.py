"""
Ref: http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
"""
class InterfaceMeta(type):
    def __new__(cls, name, parents, dct):
        # create a class_id if it's not specified
        if 'class_id' not in dct:
            dct['class_id'] = name.lower()


        # open the specified file for writing
        if 'file' in dct:
            filename = dct['file']
            dct['file'] = open(filename, 'w')


        # we need to call type.__new__ to complete the initialization
        return super(InterfaceMeta, cls).__new__(cls, name, parents, dct)


class Interface(object):
        __metaclass__ = InterfaceMeta
        file = 'tmp.txt'


print(Interface.class_id)
print(Interface.file)
