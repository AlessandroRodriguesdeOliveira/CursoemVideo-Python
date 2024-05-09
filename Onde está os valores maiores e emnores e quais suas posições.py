lista = []
for per in range(0, 5):
    a = (int(input('Digite um número:')))
    lista.append(a)
print(f'\no máximo: {max(lista)} está na(s) posição(ões)', end=' ')
for c, item in enumerate(lista):
    if item >= max(lista):
       print(f'{c}...', end=' ')
print(f'\no mínino: {min(lista)} está na(s) posição(ões)', end=' ')
for v, item2 in enumerate(lista):
    if item2 <= min(lista):
       print(f'{v}...', end=' ')
