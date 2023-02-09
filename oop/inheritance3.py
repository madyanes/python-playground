class Human(object):
    def __init__(self, **kwargs):
        self.alive = True
        self.name = kwargs.setdefault('name', None)  # kwargs is a dictionary, so you can use its supported methods like `setdefault()`
        self.birthday = kwargs.setdefault('birthday', None)
        self.hobby=kwargs.setdefault('hobby', None)

class Man(Human):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

ian = Man()

##################################################

print(vars(ian))  # {'alive': True, 'name': None, 'birthday': None, 'hobby': None}
