# DRY - don't repeat yourself

# loop

# while

# for -each
# iterable -> [] {} () str
# -------- for --------

# movies = ['rush hour 3', 'leap year', 'it', 'euro trip', 'matrix']

# print(movies[0].upper())
# print(movies[1].upper())
# print(movies[2].upper())
# print(movies[3].upper())
# print(movies[4].upper())

# for movie in movies:
#     print(movie.upper())

# numbers = [66, 51, 762, 100, 61, 56, 34, 73, 84, 874, 25, 2]
#
# for n in numbers:
#     if n == 56:
#         continue # break
#     print(n)
#
# print('end of the loop')

#

# range(5)  # -> [0,1,2,3,4] range(end)
# range(2, 7)  # -> [2,3,4,5,6] range(start,end)
# range(0, 10, 3)  # -> [0,3,6,9] range(start,end,step)
# print(list(range(5)))

# for i in range(5):
#     print(f'{i} pizza')

# print the even numbers between 0 and 20:

# for i in range(21):
#     if i % 2 == 0:
#         print(i)
#
# for i in range(21):
#     if not i % 2:
#         print(i)
#
# for i in range(0, 21, 2):
#     print(i)


# books = ['antichrist', '5am club', 'python for dummies', 'bible']
#
# # for(i=0;i<10;i++)
#
# for i in range(len(books)): # [0,1,2,3]
#     print(books[i])
#
# for i in books: # [0,1,2,3]
#     print(i)


# get from the user  a number
# and print the following pattern

# *
# **
# ***
# ****
# *****
# ******

# n = int(input('enter a nuber'))
#
# for i in range(1,n+1):
#     print(f'{" "*(n-i)}{"* "*i}')
# for i in range(1,n+1):
#     print(f'{" "*(i)}{"* "*(n-i)}')
