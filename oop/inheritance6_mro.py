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
        self.gifts = ['proficient in 10 programming languages']  # won't be inherited to `fatimah`

class Child(Man, Woman):  # `fatimah` attributes come from ian
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

ian = Man(name='Madyan', birthday=1995)
olive = Woman(name='Olivia', hobby='singing', address='Australia', status='married')
fatimah = Child(name='Fatimah')

##################################################

print(vars(fatimah))  # {'alive': True, 'name': 'Fatimah', 'birthday': None, 'hobby': None, 'gifts': ['clever', 'strong']}
