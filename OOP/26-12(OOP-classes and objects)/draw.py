class Triangle:

    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def calc_area(self):
        area = self.b * self.h / 2
        return area

    def calc_parameter(self):
        parameter = self.b + self.a + self.c
        return parameter

    def __str__(self):
        return f'a : {self.a}  b : {self.b}  c:  {self.c}  h :{self.h}'


t1 = Triangle(3, 4, 5, 5)  # __init__
print(t1)  # get __str__
print(t1.calc_area())  # calc_area
print(t1.calc_parameter())  # calc_parameter

t2 = Triangle(199, 202, 25, 15)
print(t2)
print(t2.calc_area())
print(t2.calc_parameter())
