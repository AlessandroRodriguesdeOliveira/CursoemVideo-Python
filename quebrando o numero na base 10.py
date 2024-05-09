a = int(input('Número:'))
b = a // 1 % 10
c = a // 10 % 10
d = a // 100 % 10
f = a // 1000 % 10
print('unidade: {} \ndezena: {} \ncentena: {} \nmilhar {}'.format(b,c,d,f))
