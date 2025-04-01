from functools import wraps
from types import FunctionType


def document_wrapper(method):
    @wraps(method)
    def wrapped(*args, **kwargs):
        class_name = args[0].__class__.__name__
        func_name = method.__name__
        print('calling {}.{}()... '.format(class_name, func_name))
        return method(*args, **kwargs)
    return wrapped


class MetaClass(type):
    def __new__(meta, classname, bases, classDict):
        newClassDict = {}
        for attributeName, attribute in classDict.items():
            if isinstance(attribute, FunctionType):
                # replace it with a wrapped version
                attribute = document_wrapper(attribute)
            newClassDict[attributeName] = attribute
        return type.__new__(meta, classname, bases, newClassDict)

class SimpleList(object, metaclass=MetaClass):
    def __init__(self):
        super().__init__()
        self.list_elem = list(range(1))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        this_index = self.index
        if this_index >= len(self.list_elem):
            raise StopIteration()
        self.index += 1
        return self.list_elem[this_index]


simple_list = SimpleList()
print(simple_list)
for element in simple_list:
    pass