a = float(input('Digite um número:'))
b = float(input('Digite outro número:'))
c = ''
s = a+b
sb = a-b
m = a*b
d = a/b
while c == '':
    print('''Menu de operações:
    [1] somar
    [2] subtrair
    [3] multiplicar
    [4] dividir''')
    print('')
    c = float(input('Sua opção:'))
    if c == 1:
        print('O valor é: {}'.format(s))
    if c == 2:
        print('O valor é: {}'.format(sb))
    if c == 3:
        print('O valor é: {}'.format(m))
    if c == 4:
        print('O valor é: {}'.format(d))