# listname = [,,]

# index   0            1            2         3        4
# rindex   -5          -4           -3       -2         -1
# cars = ['cupra', 'aston martin', 'ferrari', 'BYD', 'nissan']
#
# print(cars[-2])
# print(cars[3])
# print(cars[-3::-1])
# print(cars[::-1])  # -> print(cars)

# print(cars)
# print(type(cars))
#
# print(cars[0])
# print(cars[-1])
# # print(cars[222])
# print( len(cars) )


# shoes = ['timberland', 'nike', 'adidas', 'vans', 'tommy']

# l = ['as', 22, 1.5, False, [2, 2, 2]]
# list methods

# print(shoes)
# x = shoes.pop()  # -> last item added
# shoes.pop(3)  # -> last item added index
# print(shoes)
# print(x)
# shoes.remove('nike')
# if 'tommy' in shoes:
#     shoes.remove('tommy')
# print(shoes)

# print(shoes.count('nike'))
# print(shoes.sort())  # 0 - 1
# shoes.reverse()  # -> shoes[::-1]
# print(shoes)

# shoes.append('gucci')
# shoes.insert(1, 'crocs')
# print(shoes)

# l1 = [100, 22, 441, 41, 2, 2, 2, 2]
# s1 = {100, 22, 441, 41, 2, 2, 2, 2}  # distinct
# t1 = (100, 22, 441, 41, 2, 2, 2, 2)  # readonly list
#
# s1.add(2)
# print(l1, type(l1))
# print(s1, type(s1))
# print(t1, type(t1))


names = ('naomi', 'shahar', 'hason')

# names[0] = 'adir'

names = list(names)  # tuple -> list
names.append('adir')  # append
names = tuple(names)  # list -> tuple

jaja(names)