class Vehicle:
    def __init__(self, max_speed, make, hp):
        self.hp = hp
        self.max_speed = max_speed
        self.make = make

    def go(self):
        print(f'from 0 to {self.max_speed}')

    def stop(self):
        print('stopinggggggg. . . ')


class Truck(Vehicle):
    def __init__(self, max_speed, make, hp, wheels, allowed_weight):
        super().__init__(max_speed, make, hp)
        self.wheels = wheels
        self.allowed_weight = allowed_weight

    def stop(self):
        print('stoppppppppppppppingggggggg . .  .')

    def dump(self):
        print('dumping . . .')


class Car(Vehicle):
    def __init__(self, max_speed, make, hp, color):
        super().__init__(max_speed, make, hp)
        self.color = color

    def play_music(self, song):
        print(f'this is the {song}')


c1 = Car(299, 'aston martin', 1099, 'black')
t1 = Truck(101, 'DAF', 700, 20, 18)
v1 = Vehicle(100, 'volvo', 899)
#
# print(isinstance({}, set))
# print(isinstance({}, dict))
# print(issubclass(str, object))


li = [c1, t1, v1]

for vehicle in li:
    vehicle.stop()
