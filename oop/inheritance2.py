class Human():
    def __init__(self, name, birthday, *args, **kwargs):
        self.alive = True
        self.name = name
        self.birthday = birthday

class Man(Human):
    def __init__(self, hobby='Exploring', *args, **kwargs):
        super().__init__(*args, **kwargs)  # include args and kwargs to pass to the parent class (Human)
        self.hobby = hobby

ian = Man(name='Madyan', birthday=1995)

##################################################

print(vars(ian))  # {'alive': True, 'name': 'Madyan', 'birthday': 1995, 'hobby': 'Exploring'}
