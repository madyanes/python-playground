class Human():
    def __init__(self):  # initial state
        self.alive = True

class Man(Human):
    def __init__(self, name=None, birth_year=None):
        super().__init__()  # without this, the Man class won't have property `alive`
        self.name = name
        self.birth_year = birth_year

ian = Man('Madyan', 1995)

##################################################

print(isinstance(ian, Man))  # True

print(type(type))  # <class 'type'>
print(type(object))  # <class 'type'>
print(type(Man))  # <class 'type'>

print(type(Man()))  # <class '__main__.Man'>
print(type(ian))  # <class '__main__.Man'>

print(f'{ian.name} is alive = {ian.alive}')
