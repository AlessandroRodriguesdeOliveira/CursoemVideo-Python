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


def aumentar(num, por, fort=False):
    if fort == True:
        from moeda import moeda
        aumentado = moeda.moeda(num * (1 + (por / 100)))
        return aumentado
    else:
        aumentado = num * (1 + (por / 100))
        return aumentado


def diminuir(nume, porc, fort=False):
    if fort == True:
        from moeda import moeda
        diminuido  = moeda.moeda(nume * (1 - (porc/100)))
        return diminuido
    else:
        diminuido = nume * (1 - (porc / 100))
        return diminuido


def dobro(num, fort=False):
    if fort == True:
        from moeda import moeda
        dobrado = moeda.moeda(num * 2)
        return dobrado
    else:
        dobrado = num * 2
        return dobrado


def metade(num, fort=False):
    if fort == True:
        from moeda import moeda
        dividido = moeda.moeda(num/2)
        return dividido
    else:
        dividido = num / 2
        return dividido