possible_move=('Head', 'Tail')
import random
num = random.randint (0,1)
credit = int(input('Uang: '))
i= 0

while i!= credit:
    a = str(input('head or tail: ')).casefold().capitalize()
    if a in possible_move and credit > i:
        if num> 0.5:
            print('head')
            if a== 'Head':
                print('GACOR KANGG\n')
                break
            else:
                credit -= 1000
                print(f'AWOKAWOK NT\nUang: {credit}\n')
        elif num<0.5:
            print('tail')
            if a== 'Tail':
                print('GACOR KANGG\n')
                break
            else:
                credit -= 1000
                print(f'AWOKAWOK NT\nUang: {credit}\n')
    elif credit == i:
            print('UANGMU HABIS')
    else:
        print('HAH MNGSD??!!')
else: 
    print('\nKAMU TIDAK PUNYA UANG')