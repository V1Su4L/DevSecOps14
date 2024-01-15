import math

# x = int(input('please enter a number '))
# y = int(input('please enter a number '))

# print(math.pow(4, 2))  # -> 4**2
# print(math.sqrt(81))
# print(math.pi)  # 3.14151
# print(math.factorial(1000))    #5! = 5*4*3*2*1
# print(math.floor(1.9))
# print(math.ceil(1.1))
# print(round(1.5))

# x = 15
# y = 3
# b = True
# print(x == y)
# print(x > y)
# print(x < y)
# print(x != y)
# print(x >= y)
# print(x <= y)
#
# print(b and b == 0) # False
# print(b or b == 0) # True

# age = 17

# if condition :
#     # true block\
# =========== if ===========
# if age >= 18:
#     # true block
#     print('welcome')
# else:
#     # false block
#     print('come back in few years')
#
# print('thank you')

# class exercise
# 1 get the salary from the user if its above 14 K then tax it 34% otherwise 13 %
# salary = float(input('enter your salary : '))
#
# if salary > 14000:
#     tax = 0.66
# else:
#     tax = 0.87
#
# print(f'the taxed salary is {salary * tax}')
# 2 receive 2 numbers from the user and print the greatest
# number1 = int(input('please enter a number : '))
# number2 = int(input('please enter a number : '))
#
# if number1 > number2:
#     print(number1)
# elif number1 == number2:
#     print('equals')
# else:
#     print(number2)
# 3
#
# sales by the user total :
# if the user total is greater than 5000 -> discount 20 %
# if the user total is between 1000 ni and 5000 i -> discount 10%
# write a python code to calc the new total after the sale :

# total = float(input('please enter total : '))
#
# if total > 5000:
#     print(total * 0.8)
# elif total > 1000:
#     print(total * 0.9)
# else:
#     print(total)

# discount = 0
# if 1000 < total < 5000:
#     discount = 0.1
# elif total > 5000:
#     discount = 0.2
#
# print(total * (1 - discount))
# if c < a > b:
# if c > a < b:
# if c > a == b<z:

# food1 = 'shawarma'
# food2 = '55'

# print(food2 == food1)
#
# if food2.isdigit():
#     x = int(food2)
#     print(x)
#
# if 't' in food1:
#     print('we got Tt')

# sen = input('please enter a sen : ')
#
# if len(sen.replace(' ', '')) >= 8:
#     print(sen)
# else:
#     print('please try again')

a = int(input('enter a number : '))
b = int(input('enter a number : '))

if a > b:
    jaja(a)
else:
    jaja(b)

jaja(a if a > b else b)

avg = (a+b)/2 if a > b else -(a+b)/2

jaja(avg)

# print( trueblock if condition else flaseblock )
