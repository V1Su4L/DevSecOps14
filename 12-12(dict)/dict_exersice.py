#  Write a Python script to generate and print a dictionary that contains a number
#  (between 1 and n) in the form (x, x*x).
# Sample Dictionary n as input :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# num = int(input("enter num: "))
# nums = {}
# for i in range(1, num + 1):
#     nums[i] = i * i
# print(nums)

# Write a Python program to map two lists into a dictionary.
# abs = ['a', 'b', 'c', 'd']  # keys list
# nums = [1, 2, 3]  # values list
#
# dict1 = {}  # dict
# for i in range(len(abs)):  # iterate over the index of the key list
#     if i < len(nums):  # if the index accessible in the value list add it
#         dict1[abs[i]] = nums[i]  # abs[i] -> the key itself nums[i] -> the value i -> index
#     else:  # else add None as a value
#         dict1[abs[i]] = None
# print(dict1)

# Write a Python program to combine values in a list of dictionaries.
# Sample data:
# [
# {'item': 'item1', 'amount': 400},
# {'item': 'item2', 'amount': 300},
# {'item': 'item1', 'amount': 750}
# ]
# # Expected Output: {'item1': 1150, 'item2': 300}
# items = [
#     {'item': 'item1', 'amount': 400},
#     {'item': 'item2', 'amount': 300},
#     {'item': 'item1', 'amount': 750},
#     {'item': 'item2', 'amount': 950}
# ]
# counter = {}
#
# for d in items:
#     values = list(d.values())  # ['item1', 750]
#     if values[0] in counter.keys():  # [item1,item2]
#         counter[values[0]] = values[1] + counter[values[0]]
#     else:
#         counter[values[0]] = values[1]
#
# print(counter)


# x = 1
# y = 5 if x > 0 else -5  # short handed if
# print(y)


# list comprehension

# m1 = list(range(100))
# print(m1)
# m2 = [x for x in m1 if x % 2 == 1]
# m3 = [x * 2 for x in m1]
# # <list name> = [<object to append> for <iterator> in <iterable> | if <condition> ]
# # m2 = []
# # for i in m1:
# #     if i % 2 == 1:
# #         m2.append(i)
# print(m2)
# print(m3)

for i in range(40):
    x = 1
    if i == 20:
        break
else:
    print('walla')
