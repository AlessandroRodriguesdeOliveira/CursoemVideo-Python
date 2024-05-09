lista = []
soma_id = 0
cont = 0
while True:
    dic = {}
    dic["Nome"] = input('Nome: ').capitalize()
    dic["Sexo"] = input('Sexo [M/F]: ').strip().upper()[0]
    while dic["Sexo"] != 'M' and dic["Sexo"] != 'F':
        dic["Sexo"] = input('Sexo: ').strip().upper()[0]
    dic["Idade"] = int(input('Idade: '))
    soma_id += dic["Idade"]
    lista.append(dic.copy())
    fim = input('Quer continuar [S/N]: ').strip().upper()[0]
    while fim != 'S' and fim != 'N':
        fim = input('Quer continuar [S/N]: ').strip().upper()[0]
    if fim == 'N':
        break
med = soma_id/len(lista)
print(lista)
print(f'- O grupo têm {len(lista)} pessoas.')
print(f'- A média de idade: {med:.2f}')
print(f'- As muleres cadastradas foram: ', end='')
for k, item in enumerate(lista):
    if item["Sexo"] == 'F':
        print(f'{item["Nome"]}', end=' ')
    if k == len(lista)-1 and item["Sexo"] != 'F':
        print('0')
print('\n- lista de pessoas acima da média:')
print('')
for k, item2 in enumerate(lista):
    if item2["Idade"] >= (med):
        print(f'Nome = {item2["Nome"]}; Sexo = {item2["Sexo"]}; Idade = {item2["Idade"]}')
        cont += 1
    else:
        if cont == 0:
            print('Não há pessoas pessoas acima da média')
    print('')
print('<FIM>')