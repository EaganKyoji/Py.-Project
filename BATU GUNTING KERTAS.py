import random

User_move=('Batu', 'Gunting', 'Kertas')
Computer_move=('Batu', 'Gunting', 'Kertas')
User_action= str(input('Batu/Gunting/Kertas:'))
Computer_action= random.choice(Computer_move)
print(f'Komputer memilih:{Computer_action}\n')

if Computer_action==User_action:
    print('KALIAN SERI')
elif User_action=='Batu':
      if Computer_action=='Kertas':
        print('KAMU KALAH')
      elif Computer_action=='Gunting':
        print('KAMU MENANG')
elif User_action=='Gunting':
      if Computer_action=='Kertas':
        print('KAMU MENANG')
      elif Computer_action=='Batu':
        print('KAMU KALAH')
elif User_action=='Kertas':
      if Computer_action=='Batu':
        print('KAMU MENANG')
      elif Computer_action=='GUNTING':
        print('KAMU KALAH')
else:
   print('Error')