lista = []
aluno = []
while True:
    aluno.append(input('Nome: '))
    aluno.append([float(input('Primera nota: '))])
    aluno[1].append(float(input('Segunda nota: ')))
    lista.append(aluno[:])
    aluno.clear()
    fim = input('Continuar [S/N]: ').strip().upper()[0]
    while fim != 'S' and fim != 'N':
        fim = input('Continuar [S/N]: ').strip().upper()[0]
    if fim == 'N':
        break
print('-=-'*10)
print('NO. NOME               MÉDIA')
print('-'*30)
for aluno in lista:
    med = (aluno[1][0] + aluno[1][1]) / 2
    aluno.append(med)
    print(f'{lista.index(aluno):>2}', end='  ')
    print(f'{aluno[0]:<18}', end='')
    print(f'{med:>6.1f}')
while True:
    pesso = int(input('Você quer ver a nota de qual aluno? (999 para parar) '))
    if pesso == 999:
        break
    if pesso == len(lista)-1:
        print(f'As notas de {lista[pesso][0]} são {lista[pesso][1]}')
    else:
        print('Aluno não cadastrado.')

