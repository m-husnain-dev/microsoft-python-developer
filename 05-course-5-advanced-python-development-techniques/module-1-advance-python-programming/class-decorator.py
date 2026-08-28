def add_repr(cls):
    def __repr__(self):
        return f"<{cls.__name__} Object: {self.__dict__}>"
    cls.__repr__ = __repr__
    return cls

@add_repr
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Hamza", 22)
print(s)