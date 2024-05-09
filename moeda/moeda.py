def moeda(num):
    return (f'R${num:.2f}').replace('.', ',')

def resumo(num, aum, red):
    from moedas import moedas
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<20}',end='')
    print(f'{moeda(num):<20}')
    print(f'{"Dobro do preço:":<20}', end='')
    print(f'{moeda(moedas.dobro(num)):<20}')
    print(f'{"Metade do preço:":<20}', end='')
    print(f'{moeda(moedas.metade(num)):<20}')
    print(f'{aum}{"% de aumento:":<18}', end='')
    print(f'{moeda(moedas.aumentar(num,aum)):<20}')
    print(f'{red}% {"de redução:":<16}', end='')
    print(f'{moeda(moedas.diminuir(num, red)):<20}')

