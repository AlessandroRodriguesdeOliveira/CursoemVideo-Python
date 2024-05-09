
#verificação do arquivo de dados
from ex115packs import *
from manipula_arq import *
print('~'*50)
perg = input('Verificar banco de dados? : ').strip().capitalize()
print('~'*50)
if perg == 'Não':
       import glob, os
       os.chdir("/Banco")
       for file in glob.glob("*.txt"):
            qual_b = file

elif perg == 'Sim':
       titulo('Banco de dados')
       qual_b = input('Qual Banco de dados será operado. [Nome do arquivo]: ')
       proc_arq(qual_b)
       print('')


#iniciando
from time import sleep
sleep(1)
titulo_cor('Iniando o programa...', 4)
sleep(1)
print('')

#menu
while True:
       titulo('MENU PRINCIPAL')
       titulo('1 - Ver pessoas cadastradas\n'
              '2 - Cadastrar nova pessoa\n'
              '3 - Sair do programa')
       op = int(input('Qual a sua opção: '))

       #visualizando menu
       if op == 1:
              titulo('PESSOAS CADASTRADAS')
              try:
                     ler_arquiv(qual_b)
              except (NameError):
                     print('\033[1;31mERRO: O arquivo dos dados não se encontra na mesma pasta do programa. '
                           'Verifique e tente novamente.\033[m')
                     break

       #cadastrando pessoas
       if op == 2:
              titulo('NOVO CADASTRO')
              nome = input('Nome: ')
              idade = input('Idade: ')
              dados = (f'{nome}, {idade} anos.')
              escrever_no_arquivo(qual_b, dados)
              print(f'Novo registro de {nome} adicionado.')

       #sair do programa
       if op == 3:
              titulo('SAINDO DO SISTEMA... ATÉ LOGO!')
              print('')
              sleep(1)
              titulo_cor('SISTEMA FINALIZADO. VOLTE SEMPRE!', 4)
              break


