# class Person:
#     # data
#     gender = 'female'
#     age = 20
#     skin_color = 'navy'
#     weight = 93.1
#     name = 'koki'
#     # functionality
#
#
# # class Human:
# #     # data
# #     # functionality
# #     pass
#
#
# # h= Human()
# p1 = Person()
# p2 = Person()
# # # print(type(p2))
# # # print(type(p1))
# # # print(p1)
# # # print(p2)
# # print(p1.name)
# # print(p2.name)
# #
# # p1.name = 'adele'
# #
# # print(p1.name)
# # print(p2.name)
#
# # p1.title = 'Dr'
# #
# # print(p1.title)
# # print(p2.title)
#
# del p1.name
# print(p1.name)


class Person(object):
    # data

    def __init__(self, name, gender, age, skin_color):
        self.name = name
        self.gender = gender
        self.age = age
        self.skin_color = skin_color

        # p4.name = name
        # p4.gender = gender

    def __len__(self):
        return len(self.__dict__.keys())  # number of variables or attributes

    def __add__(self, other):
        return self.name + other.name

    def __gt__(self, other):  # >
        # gt ge le lt eq nq
        return self.age > other.age

    # def __le__(self, other):
    #     return self.age <= other.age

    # def __str__(self):
    #     return f'the object name is {self.name}'

    def __int__(self):
        return self.age

    def __float__(self):
        return float(self.age)

    def __bool__(self):
        return True if len(self.name) > 4 else False

    def __repr__(self):
        '''

        :return: print a look alike object code
        '''
        return "Person('hodi', 'male', 11, 'white') "


p3 = Person('hodi', 'male', 11, 'white')  # class name ()
p4 = Person('kokiiiiii', 'female', 100, 'black')
p4.k = 11
# p5 = Person('costa', 'male', 99, 'white')
# p6 = Person('', '', 0, '')

# p3.__dict__ = {'username': 'go'} # change the structure of the object
# print(p3.__dict__)  # it's the way to extract a dict of attributes and there values
#
# print(p4.__dict__)
# print(p5.__dict__)
# print(p6.__dict__)

# print(p3)
# print(bool(p4))
# print(len(p4))

# s = str(p3) + '5'
# print(s)

print(p3 > p4)
print(p4 < p3)
print(p3)

# print(f'{p3.__class__} object at 0x{p3.__hash__()}')
