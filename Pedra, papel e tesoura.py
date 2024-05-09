print('\033[1;35mJokenpô\033[m')
print('''Suas opcões:
[1] Pedra
[2] Papel
[3] Tesoura''')
a = input('Qual a sua jogada?')
import random
b = ['Pedra', 'Papel', 'Tesoura']
c = random.choice(b)
print('Você...')
from time import sleep
sleep(2)
print('')
print('O computador escolheu:',c)
print('')
if 'Pedra' in a and 'Papel' in c:
    print('Perdeu')
elif 'Pedra' in a and 'Tesoura' in c:
    print('Ganhou')
elif 'Tesoura' in a and 'Pedra' in c:
    print('Pedra')
elif 'Tesoura' in a and 'Papel' in c:
    print('Ganhou')
elif 'Papel' in a and 'Pedra' in c:
    print('Ganhou')
elif 'Papel' in a and 'Tesoura' in c:
    print('Perdeu')
else:
    print('Empate')