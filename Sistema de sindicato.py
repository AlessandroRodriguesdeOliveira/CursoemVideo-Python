import datetime
from datetime import datetime
dic = {}
dic['Nome'] = input('Nome: ')
dic['Ano de nascimento'] = int(input('Ano de nascimento: '))
dic['Idade'] = datetime.now().year - dic['Ano de nascimento']
dic['Carteira'] = int(input('Carteira de Trabalho (0: não tiver): '))
if dic['Carteira'] != 0:
    dic['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dic['Salário'] = float(input('Salário: '))
    dic['Aposentadoria'] = dic['Idade'] + (dic['Ano de Contratação'] + 35) - datetime.now().year

#outra forma
'''print(f'Nome: {dic["Nome"]}')
print(f'Idade: {date.today().year - dic["Ano de nascimento"]}')
if dic['Carteira'] != 0:
    print(f'Carteira: {dic["Carteira"]}')
    print(f'Contratação: {dic["Ano de Contratação"]}')
    print(f'Aposentadoria: {dic["Aposentadoria"]}')'''

'''for k, v in dic.items():
    print(f'{k}: {v}')'''

dic = list(dic.items())
for item in dic:
    print(f'{item[0]}: {item[1]}')


