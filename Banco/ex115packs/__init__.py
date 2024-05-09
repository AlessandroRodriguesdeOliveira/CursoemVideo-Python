def titulo(str):
    a = str
    print('-'*50)
    print(f'{a:^50}')
    print('-'*50)

c = ('\033[m', #sem cores - 0
     '\033[1;29;41m', #vermelho - 1
     '\033[7;29m',   #branco - 2
     '\033[1;29;42m',  #verde  - 3
     '\033[1;29;44m', #azul - 4
 )

def titulo_cor(mes, cor=0):
    print(c[cor], end='')
    print('^'*(len(mes)+4))
    print(f'  {mes}')
    print('^'*(len(mes)+4))
    print(c[0], end='')

