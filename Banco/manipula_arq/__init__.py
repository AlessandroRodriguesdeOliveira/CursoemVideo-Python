def escrever_no_arquivo(algo, cont):
    with open(algo, 'a') as arquivo:
        arquivo.write(f'{cont}\n')
        arquivo.close()

def ler_arquiv(algo):
        arq = open(algo, 'r')
        arquivo = arq.readlines()
        print('-'*50)
        for linha in arquivo:
            e = linha.find(' ')
            v = linha.find(',')
            p = linha.find('.')
            print(f'{linha[0:v]:<38}', end='')
            print(linha[e+1:p])
        print('-'*50)
        arq.close()



def proc_arq(nom_arq, criar=False, falso=False):
        import pathlib
        cami_arq = pathlib.Path(nom_arq)
        d = cami_arq.exists()
        if d == False:
            print('\033[0;31mERRO: Arquivo não encontrado ou inexistente. '
                  'Dessa maneira, talvez o arquivo não encontra-se '
                  'no mesmo diretório.\033[m')
            print('')
            c = input('Você quer criar um arquivo com esse nome: ').strip().capitalize()
            if c == 'Não':
                print('Tente novamente.\n'
                      'Sistema finalizado.')
            elif c == 'Sim':
                with open(nom_arq, 'x') as arquivo:
                    arquivo.write('')
                print('Arquivo criado.')
        else:
            falso = True
            print('\033[1;32mArquivo encontrado com sucesso. Prossegindo...\033[m')
        if d == False and criar == True:
            with open(nom_arq, 'x') as arquivo:
                arquivo.write('')
            print('Arquivo criado.')
