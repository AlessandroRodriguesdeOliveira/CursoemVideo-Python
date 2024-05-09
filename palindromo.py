a = input('Digite:').lower()
ba = a.split()
c = ''.join(ba)
d = c
for item in d:
    f = c[::-1]
if f == d:
    print('É um palíndromo')
    print('Pois \"{}\" é o mesmo que \"{}\"'.format(d, f))
else:
    print('Não é um palíndromo')
    print('Pois \"{}\" não é o mesmo que \"{}\"'.format(d, f))

