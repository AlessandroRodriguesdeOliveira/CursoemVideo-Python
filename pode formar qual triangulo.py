a = int(input('Reta 1:'))
b = int(input('Reta 2:'))
c = int(input('Reta 3:'))
d =  a < b + c
e = b < c + a
f = c < a + b
g =  a == b == c
h =  a == b != c or a == c != b or c == b != a
i = a != b and a !=c and c != b

if d and e and f and g:
    print('Pode formar um triângulo equilátero.')
elif d and e and f and h:
    print('Pode formar um triângulo isóscele')
elif d and e and f and i:
    print('Pode formar um triângulo escaleno')
else:
    print('Não pode formar um triângulo')
