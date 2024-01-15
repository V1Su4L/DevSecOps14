# if 'l' in 'loop':
#     print('loop got l')
# elif 'loop'.count('o') == 2:
#     print('we got the ooo\'s')
# else:
#     print('we got nothing')


# print('l' in 'loop')


# leap year -> every year does not divide by 100 and do divide by 4
# ask the user to enter his full birth year and check if the year is leap year

birth_year = int(input('enter your birth year : '))

if birth_year % 4 == 0 and birth_year % 100 != 0:
    jaja(f'leap year indeed !{birth_year}')
else:
    jaja(f'just another year {birth_year}')