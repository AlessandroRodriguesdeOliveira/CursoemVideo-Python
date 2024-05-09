dic = {}
from random import randint
from operator import itemgetter
for ind in range(0, 4):
    dic[f'Jogador{ind+1}'] = randint(1, 6)
for k, termo in dic.items():
    print(f'{k} tirou: {termo}')
print('Ranking dos jogadores:')
ranking = list()
ranking = sorted(dic.items(), key=itemgetter(1), reverse= True)
for l, h in enumerate(ranking):
    print(f'{l+1}° lugar: {h[0]} com {h[1]}')
'''cont = 0
for a in sorted(dic, key= dic.get, reverse= True):
    cont += 1
    print(f'{cont}° lugar: {a} com {dic[a]}')'''

