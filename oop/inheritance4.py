class Human(object):
    def __init__(self, **kwargs):
        self.alive = True
        self.name = kwargs.setdefault('name', None)  # kwargs is a dictionary, so you can use its supported methods like `setdefault()`
        self.birthday = kwargs.setdefault('birthday', None)
        self.hobby=kwargs.setdefault('hobby', None)

class Man(Human):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Woman(Human):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__dict__.update(kwargs)  # new attributes based on kwargs

ian = Man(name='Madyan', birthday=1995)
olive = Woman(name='Olivia', hobby='singing', address='Australia', status='married')

##################################################

print(vars(ian))  # {'alive': True, 'name': 'Madyan', 'birthday': 1995, 'hobby': None}
print(vars(olive))  # {'alive': True, 'name': 'Olivia', 'birthday': None, 'hobby': 'singing', 'address': 'Australia', 'status': 'married'}
