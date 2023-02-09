class Human(object):
    def __init__(self, **kwargs):
        self.alive = True
        self.name = kwargs.setdefault('name', None)
        self.birthday = kwargs.setdefault('birthday', None)
        self.hobby = kwargs.setdefault('hobby', None)

class Man(Human):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gifts = ['clever', 'strong']

class Woman(Human):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__dict__.update(kwargs)
        self.gifts = ['proficient in 10 programming languages']

class Child(Human, Woman):  # TypeError: Cannot create a consistent method resolution order (MRO) for bases Human, Woman
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

##################################################

# Why the error appears?
#
# Because either the Man or Woman already inherits from `Human`.
# Python now cannot determine what class to look methods up on first; either Man, or on Woman,
# which would override things defined in Human.
# 
# https://stackoverflow.com/questions/29214888/typeerror-cannot-create-a-consistent-method-resolution-order-mro
