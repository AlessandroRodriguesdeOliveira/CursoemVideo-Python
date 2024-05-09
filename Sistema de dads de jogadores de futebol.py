lista = []
while True:
    dic = {}
    dic['Jogador'] = input('Nome do jogador: ')
    quantos = int(input(f'Quantas partidas {dic["Jogador"]} jogou: '))
    dic['Gols'] = gols = list()
    soma = 0
    for a in range(0, quantos):
        gols.append(int(input(f'Quantos gols {dic["Jogador"]} fez na partida {a+1}: ')))
        soma += dic['Gols'][a]
    dic['Total'] = soma
    lista.append(dic.copy())
    fim = input('Quer continuar [S/N]: ').strip().upper()[0]
    print('-'*40)
    if fim == 'N':
        break
print('-=-'*20)
print(f'{"cod":>3} {"nome":<15} {"gols":<15} {"total":<5}')
print('-'*40)
for k, i in enumerate(lista):
     print(f'{k:>3} {i["Jogador"]:<15} {str(i["Gols"]):<15} {i["Total"]:<5}')
print('-'*20)
while True:
    pe = int(input('Mostrar dados de qual jogador [cod.]: '))
    if pe == 999:
        break
    if pe > len(lista):
        print('Cod. não identificado ou não encontra-se no sistema.')
    else:
        print(f'-- Levantamento do jogador {lista[pe]["Jogador"]}:')
        for a in range(0, len(lista[pe]["Gols"])):
            print(f'  => Na partida {a + 1}, fez {lista[pe]["Gols"][a]} gol(s).')
        print(f'Foi um total de {lista[pe]["Total"]}')

