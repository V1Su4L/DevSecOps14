class Animal:
    def __init__(self, name):
        print('initializing  animal')
        self.name = name

    def eat(self):
        print('eating ...')


class Cat(Animal):
    def __init__(self, name, color):
        print('initializing  cat')
        super().__init__(name)
        self.color = color

    def walk(self):
        print('walking ...')

    def eat(self):
        print('eating lasagna')


class Fish(Animal):
    def swim(self):
        print('swimming ....')


# animal1 = Animal()
# nemo = Fish()
# garfield = Cat()
#
# animal1.eat()
# nemo.eat()
# garfield.eat()

# an2 = Animal('shoun')
cat2 = Cat('garfield', 'Orange')
print(cat2.name)
