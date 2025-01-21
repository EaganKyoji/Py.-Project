a = ['Banana','Apple','Coconut','Orange']
print(a)

c = input('Sell/buy/gambling? ').casefold()
if c == 'buy':
    b= input('What do you want? ' ).casefold().title()
    if b in ['Banana','Apple','Coconut','Orange']:
        print('We\'re not sale what u already have')
    elif b=='Jackfruit':
        import random
        z= random.randint(1,3)
        if z>2:
            print('Who\'s fruit? \nHow abt ask Jack instead?')
        else:
            print('We got some jackpot here, haha, got it?')
    else:
        print(f'Sure buddy! Here\'s ur {b}')
        a.append(b)
        print(a)
elif c == 'sell':
    e= input('What do you want to sell? everything? ').casefold()
    if e=='yes':
        a.clear()
        print(f"Here\'s ur change {a}, loser.")
elif c== 'gambling':
    print('HOHO, I LIKE YOU! LET\'S GO GAMBLING!!!')
    f= input('What kind of fruit u want to sacrifice? ').casefold().title()
    if f not in a:
        print('U want to trick me?')
    else:
        print('LET\'s)SEEE!!!')
        g= random.randint(1,3)
        if g==1:
            print('HMMM U GOT NOTHING, LOL')
        elif g==2:
            print('Looks like i win the bet')
            a.clear()
            print(a)
        elif g==3:
            print('I WIN AGAIN, gotta take that yours again')
            a.remove(random.choice)



else:
    print('OPO SEH?')

            






