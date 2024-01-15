# 1
# for row in range(1, 10):
#     # print(str(n)*n)
#     for col in range(0, row):
#         print(row, end='')
#     print()

# 2
# s = input('enter a word')
# s = s.replace(' ', '').upper()  # delete all the spaces from the word
# if s == s[::-1]: # check if the str readable from right to left
#     print(f'{s} is palindrome')
# else:
#     print(f'{s} not palindrome')

# 3
# a = 0
# b = 1
# counter = 1
#
# while True:
#     z = a + b
#     print(z)
#     a = b
#     b = z
#     counter += 1
#     if counter == 20:
#         break

# fibo = [0, 1]
# index = 2
# while len(fibo) <= 20:
#     fibo.append(fibo[index - 1] + fibo[index - 2])
#     index+=1
#
# print(fibo)

# fibo = [0, 1]
# for i in range(2, 20):
#     fibo.append(fibo[i - 1] + fibo[i - 2])
# print(fibo)


# 44
# for number in range(1, 100):
#     is_prime = True
#     for dividers in range(2, number//2):
#         if number % dividers == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(number)

# 5
strings = ['abc', 'xyz', 'aba', '12331']

c = 0
for s in strings:
    if len(s) > 2 and s[0] == s[-1]:
        c += 1
jaja(c)


strings = list(set(strings)) # remove duplicates form a list