# coffee = ['black', None, 'latte', 'instant']
#
#
# for c in coffee:
#     length = len(c)
#     new_c = c.title()
#     print(f'[{new_c}] coffee price is: {length} ')
#
# print('yaba daba dooo')


# for i in range(0, 1000, 7):
#     print(i)

# print(list(range(0,1000,7)))


# while condition:

# while True:
#     print('hello')
# while False:
#     print('hello')

# print all the numbers between 0 and 9
# x = 0
#
# while x < 10:
#     print(x)
#     x += 1

# print all the numbers between 0 and 9
# x = 0
#
# while x <= 10:
#     print(x)
#     x += 1

# changing the var must be in logical way to get to the false block and out of the loop
# x = 0
#
# while x < 10:
#     print(x)
#     x -= 1


# import datetime
# import time
#
# while True:
#     # counter seconds of a spec minute
#     while datetime.datetime.now().second > 30:
#         print(datetime.datetime.now().second)
#         time.sleep(1)


# while True:
#     print('64 bytes from 8.8.8.8: icmp_seq=22 ttl=117 time=40.515 ms')
#     if user==ctrlz :
#         break
# print('''--- 8.8.8.8 ping statistics ---
# 34 packets transmitted, 34 packets received, 0.0% packet loss
# round-trip min/avg/max/stddev = 10.539/174.095/1158.453/247.270 m''')


# ask the user to enter his PIN code till the right guess
# the PIN must contain 3 digits


# pin = '321'
#
# while True: # do while
#     guess = input('enter your PIN code : ')
#     if len(guess) != 3:
#         continue
#     if guess == pin:
#         break
#     print('wrong pin')
#
# print('welcome boss')

# while True:
#     guess = input('enter your PIN code : ')
#     f =True if guess == pin else False if len(guess) !=3 else None
#     if f:
#


# write a python script to create4 and fill a list with 100 random numbers between (0,5)
# iterate over the list
#   declare a new list named uniques and enter each value one time only
#   write every and each value with his count in the list
#   [1,1,1,1,2,2,2,3,3]
#    1-> 4,
#    2 -> 3,
#    3-> 2

import random

random_numbers = []  # declaration

for i in range(1000):
    rnd = random.randrange(0, 6)
    random_numbers.append(rnd)

jaja(random_numbers)

uniques = list(
    set(random_numbers))  # delete all the duplicates by casting the list to set      convert the set to list so we can mod
jaja(uniques)

for un in uniques:
    un_count = random_numbers.count(un)
    jaja(f'the count of the {un} is {un_count} ')