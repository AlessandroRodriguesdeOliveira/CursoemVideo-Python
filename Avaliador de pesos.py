lista = []
dados = []
max = 0
min = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    for p in lista:
        if len(lista) == 1:
            max = p[1]
            min = p[1]
        else:
            cont = 0
            while cont < len(lista):
                if lista[cont][1] >= max:
                    max = lista[cont][1]
                if lista[cont][1] <= min:
                    min = lista[cont][1]
                cont += 1
    fim = input('Quer continuar [S/N]: ').strip().upper()[0]
    if fim == 'N':
        break

print(f'O número de pessoas cadastradas foi: {len(lista)}')
for po in lista:
    if max in po:
        print(f'O maior peso é {max}kg de [{po[0]}]')
    if min in po:
        print(f'O menor peso é {min}kg de [{po[0]}]')