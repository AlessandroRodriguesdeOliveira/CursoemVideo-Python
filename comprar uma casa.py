a = float(input('Valor da casa:'))
b = float(input('Seu salário:'))
c = float(input('Tempo, em meses, para a quitação:'))
d = a/c
if d >= b*(0.3):
    print('Que pena sua solicitação foi negada!')

else:
    print('Oba! Sua solicitaçao foi confirmada com o valor de prestações do valor R${:.2f}'.format(d))