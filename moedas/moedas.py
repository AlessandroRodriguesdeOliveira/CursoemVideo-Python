
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