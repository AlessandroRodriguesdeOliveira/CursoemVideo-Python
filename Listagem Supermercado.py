li = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
      'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('\033[1m-\033[m'*29)
print(f'{"LISTAGEM DE PREÇOS":^29}')
print('\033[1m-\033[m'*29)
for c in range(0, len(li)):
    if type(li[c]) == str:
        print(li[c],end='')
        print('.'*(20-len(li[c])), end='')
    else:
        if type(li[c]) == float or int:
            print(f'R$ {li[c]:>6.2f}')
print('\033[1m-\033[m'*29)