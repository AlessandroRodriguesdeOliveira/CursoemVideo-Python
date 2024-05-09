a = float(input('Digite o preço:'))
b = a*0.9
c = a*0.95
d = a
e = a*1.2
print('''Forma de pagamento:
[1]Á vista 
[2]Cheque
[3]Á vista no cartão
[4]2x no cartão
[5]3x no cartão''')
g = input('Opção:')

if '1' in g:
    print('O preço do produto é:',b)
elif '2' in g:
    print('O preço do produto é:',b)
elif '3' in g:
    print('O preço do produto é:',c)
elif '4' in g:
    print('O preço do produto é:',d)
elif '5'in g:
    print('O preço do produto é:',e)
else:
    print('\033[1;31mInválido\033[m')