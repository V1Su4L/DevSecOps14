# print('hello')
#
# x = 'hello'
# print(x)  #   x ->> print ->> 'hello'
# #                     |
# #                     v
# #                  storage
# #                x ==> 'hello'
#
#
import math

# ========== variable ============
# datatypes
# int      4 , 6            whole number
# float    4.8              floating point number
# str     'hello' '2'       text
# bool     True False       boolean
# list     seq of items     list
# set      unique list      list
# tuple    readonly list    list
# dict     key:value pairs  JSON

# variable name can't start with anything but a letter or _
# the var name must have no spaces in it
# the variable must have value assigned to it
# we can declare and assign more than 1 variable in one code line

# we can change the data type of each variable by casting it to the new data type
# the casting functions :
# int()
# float()
# str()
# bool()
# list()
# set()
# tuple()
# dict()

# ============== booleans ===============

# > < >= <= !=(! =)  ==(= =)  operator

# is_valid = len('helhfafhlo') > 6
# print(is_valid)

# ============ conditions =============
#
# x = 'zaOza'
#
# if x.islower():
#     print('all the letters are lower case')
# elif x.istitle():
#     print('title')
# else:
#     print('not all the letters in lower case')

# the sort line between two points is a straight line
# write a python code that receives x,y of 2 points and
# if the points aren't equals or the same calc the distance between
# the two point
# d = sqrt( (x2-x1)^2 +(y2-y1)^2 )

# example : [5,5] [5,5]
# output : its the same point

# example : [3,4] [6,8]
# output : the distance 5

# =========================distance==============================
# sol
# - x and y as input √
# - check if the two point are equal  √
# - calculate the distance √

# p1 = input('write the x and the y of the point with a space').split()
# p2 = input('write the x and the y of the point with a space')
# p2 = p2.split()
#
# if p1 != p2:
#     d = math.sqrt((int(p2[0]) - int(p1[0])) ** 2 + (int(p2[1]) - int(p1[1])) ** 2)
#     print(f'the distance is {d}')
# else:
#     print('its the same point')

# ============== elevator ============
# in my building there is 2 elevators we call them the left and the right
# the building manager (av bayet) called and want to program the elevator
# the algorithm works like this
# we calc the abs distance and we check which of the elevators are closer
# the code will print the name of the elevator that going to pick you up

# write a python code that receives the left elevator position and the
# right position
# and the call floor and print which of the elevators coming
# abs(-1)  -1 -> 1
# example
# left 4 right 6  the call  10
# output : right
# left 6 right 6  the call  10
# output : right
# left 8 right 6  the call  10
# output : left
# left_p = int(input('left position is :'))
# right_p = int(input('right position is :'))
# call = int(input('call from :'))
#
# right_distance = abs(right_p - call)
# left_distance = abs(left_p - call)
#
# if right_distance <= left_distance :
#     print('right elevator on the way')
# else:
#     print('left elevator on the way')


# =========== loops ============
# while  עד ש   use case : unknown iteration number
# for  לכל ערך  use case : list to iterate or number of iteration

# break  stop the loop
# continue skip this iteration

#           v
cakes = ['cheese', 'nuts', 'chocolate', 'tiramisu']

# for cake in cakes:
#     print(cake.count('a'))
#     # iterate over iterable -> list set tuple dict (values items keys)

# names = []
# for _ in range(4):  # [0,1,2,3,4,5,6,7,8,9]
#     # print('hello')
#     names.append(input('please enter name'))
#     # print(names)  # 4
#
# # after all the iterations
# print(names)  # 4

# set  = distinct
# tuple = readonly ()

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# l1 = {
#     0: 'a',
#     1: 'b',
#     2: 'c',
#     3: 'd',
#     4: 'e'
# }
# print(l1[0])
# print(l[0])


d1 = {
    'id': 10,
    'number of upper cases': 20,
    'number of lower cases': 40,
    'number of strings': 30
}
jaja(d1)
jaja(type(d1))
jaja(d1['number of lower cases'])
jaja(d1.keys())
jaja(d1.values())
jaja(d1.items())
jaja(d1[1])

# key : value , key : value
