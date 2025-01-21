G= 0
R= 0
H= 0
S= 0

print('Q1) Do you like Dawn or Dusk?')
print('   1) Dawn')
print('   2) Dusk')
A= int(input('Answer: '))

if A== 1:
  R +=1
  G +=1
elif A== 2:
  S +=1
  H +=1
else:
  print('Wrong input')
  StopIteration

print('\nQ2) When I’m dead, I want people to remember me as? ')
print('   1) The Good')
print('   2) The Great')
print('   3) The Wise')
print('   4) The Bold')
A= int(input('Answer: '))

if A== 1:
  H +=2
elif A== 2:
  S +=2
elif A== 3:
  R +=2
elif A== 4:
  G +=2
else:
  print('Wrong input')

print('\nQ3) Which kind of instrument most pleases your ear? ')
print('   1) The Violin')
print('   2) The Trumpet')
print('   3) The Piano')
print('   4) The Drum')
A= int(input('Answer: '))

if A== 1:
  S +=4
elif A== 2:
  H +=4
elif A== 3:
  R +=4
elif A== 4:
  G +=4
else:
  print('Wrong input')

if S> H and S> R and S> G:
  print('\nKAMU ADALAH SLYTHERINE🐍')
  print('NILAI AKHIR:',S)
  print('Griffindor:',G, 'Ravenclaw:',R, 'Hufflepuff:',H)
elif H> S and H> R and H> G:
  print('\nKAMU ADALAH HUFFLEPUFF🦡')
  print('NILAI AKHIR:',H)
  print('Griffindor:',G, 'Ravenclaw:',R, 'Slytherin',S)
elif R> H and R> S and R> G:
  print('\nKAMU ADALAH RAVENCLAW🦅')
  print('NILAI AKHIR:',R)
  print('Griffindor:',G, 'Slytherin',S, 'Hufflepuff:',H)
elif G> S and G> H and G> R:
  print('\nKAMU ADALAH GRIFFYNDOR🦁')
  print('NILAI AKHIR:',G)
  print('Hufflepuff:',H, 'Ravenclaw:',R, 'Slytherin',S)
else:
  print('Wrong input')








