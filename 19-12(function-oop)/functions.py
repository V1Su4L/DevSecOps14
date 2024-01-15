# # def <function_name>():
# # block
#
#
# # def greet(name):  # ->> function
# #     print(f'hello {name}')  # hard coded
#
#
# # def greet_with_age(name: str, age):  # , -> another argument  : the type of the argument
# #     print(f'my name is {name} , and im {age} years old')
# #
# #
# #
#
#
# # greet_with_age('hodi', 22)
# # greet_with_age('jackson', 11)
# # greet_with_age(44, 11)
#
# # greet('yaacov')
# # greet('benny')
# # x = 'johny'
# # greet(x)
#
#
# # ================= arguments
#
#
# # def arg_print(a, b, c, d=1, e='knafeh'):
# #     print(f'a={a}')
# #     print(f'b={b}')
# #     print(f'c={c}')
# #     print(f'd={d}')
# #     print(f'e={e}')
# #
# # # arg_print(1)  # error
# # # arg_print(1, 2, 3, 4, 5)  # Pass
# # # arg_print(b=2, c=1, a=100, e=1, d=55) # pass
# # # print('live what you love', end='@hodicompany.ltd\n')
# # # 'joey dosent share food'.split(sep='o')
# # # print('live what you love')
# # # [s,s,s].sort(reverse=True)
# # # print('gaga')
# # arg_print(1, 2, 3, 4, 5)
# # arg_print( 2, 3, 4)
#
#
# # print(max(1,2,3))
# # print(max(1,2,3,4,5,6,7,8,9))
# # print(max(1,2))
#
#
# # def odd_sum(*args):
# #     for n in args:
# #         print(n if n % 2 == 1 else 'naaah')
# #         # if n%2 ==1:
# #         #     print(n)
# #         # else:
# #         #     print('naaaah')
# #
# #
# # odd_sum(1, 23, 4)
# # odd_sum(1, 2, 3, 4, 4, 5, 6, 7, 7)
#
# # def foo(**kwargs):
# #     print(kwargs)
# #
# #
# # foo(x=4, reverse=True, color='hodi')
#
#
# # build a function that receives from the user n numbers
# # and print the sum of the odd numbers
#
# # build a function that receives from the user n numbers
# # and print the sum of the even numbers
#
#
# # def odds(*args):
# #     sum = 0
# #     for n in args:
# #         if n % 2 == 1:
# #             sum += n
# #     print(sum)
# #
# #
# # def even(*args):
# #     sum = 0
# #     for n in args:
# #         if n % 2 == 0:
# #             sum += n
# #     print(sum)
# def my_sum(*args, **kwargs):
#     '''
#         print the sum of the even numbers in default
#         by sending the flag odd we sum the odd numbers
#     '''
#     print(args)
#     print(kwargs)
#     sum = 0
#     x = 0
#     if kwargs.get('odd'):
#         x = 1
#     for n in args:
#         if n % 2 == x:
#             sum += n
#     print(sum)
#
#
# # odds(1, 2, 3, 4, 5, 6, 7)
# # even(1, 2, 3, 4, 5, 6, 7)
#
# my_sum(1, 2, 3, 4, 5, 6, 7, odd=True)
# my_sum(1, 2, 3, 4, 5, 6, 7, te=1)


# define a function in python to calc the area of triangle
# the function must receive from the user 2 arguments base and height
# the function must return the area

def calc_area(b, h):
    area = b * h / 2
    return area


area1 = calc_area(1, 212)  # 106.0
area2 = calc_area(42, 3)  # 63.0
area3 = calc_area(551, 4)  # 1102.0

print(max(area3, area2, area1))
