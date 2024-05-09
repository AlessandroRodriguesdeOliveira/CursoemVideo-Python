from random import randint
print('-=-'*8)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*8)
cont = 0
while True:
    valor = int(input('Digite o valor:'))
    p_i = ' '
    while p_i not in 'PI':
        p_i = str(input('Par ou Ímpar? [P/I]:')).strip().upper()[0]
    if p_i == 'P':
       p_i = 'PAR'
    if p_i == 'I':
       p_i = 'ÍMPAR'
    ale = randint(0, 10)
    soma = valor + ale
    res = ''
    if soma % 2 == 0:
        res = ('PAR')
    else:
        res = ('ÍMPAR')
    print('-' * 63)
    print(f'Você jogou {valor} e o Computador {ale}. O total foi {soma} que é igual a {res}.')
    print('-' * 63)
    if p_i == res:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('-=-' * 8)
        cont += 1
    else:
        print(f'GAME OVER! Você venceu {cont} vez(es).')
        print('-=-'*10)
        break

