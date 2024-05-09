tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
         'MERCADO', 'PROGRAMADOR', 'FUTURO')
'''for p in tupla:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra.lower(), end=' ')'''


a = 'A'
e = 'E'
i = 'I'
o = 'O'
u = 'U'
cont = 0
#for p in range(0, 5):
for po in range(0, len(list(tupla))):
    print(f'Na palavra {tupla[po]} temos: ', end='')
    co = list(tupla[po]).count(a)
    print('a '*co, end='')
    co = list(tupla[po]).count(e)
    print('e ' * co, end='')
    co = list(tupla[po]).count(i)
    print('i '* co, end='')
    co = list(tupla[po]).count(o)
    print('o ' * co, end='')
    co = list(tupla[po]).count(u)
    print('u ' * co)







