# class Shape is the main classe here
# in order to declare the class we use 'class'
import math


# class Shape:
#     # parameter = None
#     # __area = None
#
#     def __init__(self, parameter, area):
#         self.parameter = parameter
#         self.set_area(area)
#
#     def get_area(self):
#         return self.__area
#
#     def set_area(self, area):
#         if area > 0:
#             self.__area = area
#
#
# s1 = Shape(2, 4)
# s2 = Shape(5, 10)
# print(s1)
# print(s1.parameter)
# print(s1.get_area())


# class FifoList:
#     def __init__(self):
#         self.__data = []
#
#     def add(self, item):
#         self.__data.append(item)
#
#     def remove(self):
#         return self.__data.pop(0)
#
#
# l1 = list()
# f1 = FifoList()
#
# f1.add(77)
# f1.add(11)
# f1.add('hodi')
# f1.add('michael')
# print(f1.remove())
# print(f1.remove())
# print(f1.remove())


class Helper:  # PascalCase
    def sperator(self):  # snake_case
        print('------------------')

    @staticmethod
    def rectangle():
        print('-----------')
        print('-----------')
        print('-----------')

    @staticmethod
    def triangle():
        print('   *  ')
        print(' * * *')
        print('* * * *')


# import math, random, datetime
#
# math.ceil(33)
# datetime.datetime.now()
# Helper.triangle()

Helper.rectangle()
