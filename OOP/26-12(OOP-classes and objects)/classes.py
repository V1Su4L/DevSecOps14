class Dog:

    def __init__(self, name, age, color, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

    def run(self):
        print('running .......')

    def bark(self, sound):
        print(f'im barking {sound}')

    def get_age_in_years(self):
        return self.age / 12

    def __str__(self):
        dog = 'Dog{\n'
        for k, v in self.__dict__.items():
            dog += f'   {k} -> {v}\n'
        dog += '}'
        return dog


d1 = Dog('gibour', 24, 'brown', 'husky ')
d2 = Dog('jojo', 18, 'white', 'pitbul ')
# print(d1.__dict__.items())
# print(d1)
d1.run()
d2.run()
d1.bark('whoooooooooooooph woooph')
d2.bark('how hoooooooow ? ')

print(d1.age)
print(d1.age_in_years())
