def contagem(inicio, fim, passo):
    st = inicio
    d = fim
    if passo > 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        if inicio < fim:
            for i in range(inicio, fim+1):
                while not st == d+passo:
                    print(st, end=' ')
                    st = st + passo
                    break
        elif inicio > fim:
            for g in range(fim, inicio+1):
                while not st == d-passo:
                    print(st, end=' ')
                    st = st - passo
                    break
    elif passo == 0:
        print(f'Contagem de {inicio} até {fim} de {passo+1} em {passo+1}')
        if inicio < fim:
            for i in range(inicio, fim+1):
                while not st == d+1:
                    print(st, end=' ')
                    st = st + 1
                    break
        elif inicio > fim:
            for g in range(fim, inicio+1):
                while not st == d-1:
                    print(st, end=' ')
                    st = st - 1
                    break
    else:

        if inicio < fim:
            for i in range(inicio, fim-passo):
                while not st == d-passo:
                    print(st)
                    st = st - passo
                    break
        elif inicio > fim:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
            for g in range(fim, inicio+passo):
                while not st == d+passo:
                    print(st, end=' ')
                    st = st + passo
                    break


def li():
    print('-=-'*10)

li()
contagem(1,10, 1)
print('')
li()
contagem(10,0,2)
print('')
li()

print('Agora a sua vez!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contagem(i,f,p)

