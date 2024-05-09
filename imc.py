a = float(input('Digite o seu peso:'))
b = float(input('Digite a sua altura:'))
c = a/b**2
if c < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= c <25:
    print('Peso ideal.')
elif 25 <= c <30:
    print('Sobrepeso.')
elif 30 <= c >40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')