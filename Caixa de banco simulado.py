print('='*29)
print('       Ale\'s Bank       ')
print('='*29)
a = int(input('Que valor você quer sacar?:'))
cont = 1
while True:
    if cont == 1:
        b = a // 50
        cont += 1
        if b != 0:
          print(f'O total de {b} cédulas de R$50')
    else:
        if cont == 2:
            c = (a - (b * 50)) // 20
            cont += 1
            if c != 0:
              print(f'O total de {c} cédulas de R$20')
        else:
            if cont == 3:
                d = (a - (b * 50) - (c * 20)) // 10
                cont += 1
                if d != 0:
                  print(f'O total de {d} cédulas de R$10')
            else:
                if cont == 4:
                    e = (a - (b * 50) - (c * 20) - (d * 10)) // 1
                    cont += 1
                    if e != 0:
                      print(f'O total de {e} cédulas de R$1')
                    break
if a < 1:
    print('Saque não realizado. Tente novamente.')
else:
    print('Saque realizado com sucesso! Volte sempre ao Ale\'s Banco.')
