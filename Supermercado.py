print('-'*38)
print('          LOJA SUPER BARATÂO          ')
print('-'*38)
soma = 0
cont_val = 0
min = 0
cont = 0
cont_ex = 0
min_nom = ''
while True:
    nom = str(input('Nome do produto:')).strip().capitalize()
    val = float(input('Valor: R$'))
    cont += 1
    if val > 1000:
        cont_ex += 1
    if cont == 1:
        min = val
        min_nom = nom
    else:
       if val < min:
           min = val
           min_nom = nom
    soma += val
    bre = input('Quer continuar [S/N]:').strip().upper()
    while bre != 'S' and bre != 'N':
        bre = input('Quer continuar [S/N]:').strip().upper()
    if bre == 'N':
        break
print('{:-^38}'.format(' FIM DO PRORAMA '))
print(f'''O total da compra R${soma:.2f}
Temos {cont_ex} produto(s) que extrapola(ão) o valor de R$1000.00
O produto mais barato foi o/a {min_nom} que custou R${min:.2f}''')
