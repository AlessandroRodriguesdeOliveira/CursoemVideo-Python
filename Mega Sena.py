lista = []
palpites = []
p = 0
from random import randint
from time import sleep
print('-'*30)
print('JOGA NA MEGA SENA'.center(30))
print('-'*30)
vq = int(input('Você quer que eu sorteie quantos palpites: '))
'''tot = 1'''
'''while tot <= cont:'''
'''cont = 0'''
'''while True:'''
for jogos in range(0, vq):
    for nume in range(0, 6):
        num = randint(1, 60)
        if num not in palpites:
            palpites.append(num)
            palpites.sort()
        else:
            '''if cont >=6:'
             break'''
            for tu in range(0, 6):
                num = randint(1, 60)
                if num not in palpites:
                    palpites.append(num)
                    palpites.sort()
                    break
    lista.append(palpites[:])
    palpites.clear()
print('-=-'*3, end='')
print(f' Sorteando {vq} jogos ',end='')
print('-=-'*2)
for item in lista:
    print(f'jogo {lista.index(item)+1}: {item}')
    sleep(1)
print('-=-'*4, end='')
print(' Boa sorte '.center(5),end='')
print('-=-'*4)
