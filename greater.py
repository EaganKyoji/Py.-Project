a = int(input('what is your bet (0-100): '))
user_choice = ('greater','smaller')
b = (input(f'is it greater/smaller? '))

import random

num = random.randint (0, 100)
print(f'\nthe number is: {num}\n')

if b== 'greater':
    if a>= num:
        print(f'{a} is greater than {num}')
        print('YOU WINN, KINGG!!!')
    else:
        print(f'{a} is greater than {num}')
        print('LOL')
elif b== 'smaller':
    if a<= num:
        print(f'{a} is smaller than {num}')
        print('YOU WINN, KINGG!!!')
    else:
        print(f'{a} is smaller than {num}')
        print('LOL')
else: 
    print('WHAT?')
