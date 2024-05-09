count = 0
from random import randint
print('Vou pensar em um número entre 0 e 5 tente adivinhar!')
b = ''
a = randint(0, 10)
while not b == a:
    count += 1
    b = int(input('Em que número eu pensei ?:'))
    if not b == a:
        print('\033[1;35mErrou! \033[2;31mDe novo\033[m!')
print('Nossa você demorou {} palpites para acertar!'.format(count))
