class Human(object):
    def __init__(self, **kwargs):
        self.alive = True
        self.name = kwargs.setdefault('name', None)
        self.birthday = kwargs.setdefault('birthday', None)
        self.hobby=kwargs.setdefault('hobby', None)

class Man(Human):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Woman(Human):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__dict__.update(kwargs)

ian = Man(name='Madyan', birthday=1995)
olive = Woman(name='Olivia', hobby='singing', address='Australia', status='married')

##################################################

# print(ian.address)  # AttributeError: 'Man' object has no attribute 'address'
#       ^^^^^^^^^^^
# why is it error? 
# because ian and olive are different objects in memory, 
# but having the same parent class
# so the properties aren't shared

print(issubclass(Man, Human))    # True
print(issubclass(Woman, Human))  # True

print(type(ian))    # <class '__main__.Man'>
print(type(olive))  # <class '__main__.Woman'>

print(isinstance(ian, Man))  # True
print(isinstance(ian, Human))  # True

print(ian)    # <__main__.Man object at 0x7f1abe099d10>
print(olive)  # <__main__.Woman object at 0x7f1abe09b810>
