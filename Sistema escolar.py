def notas(*num, sit=False):
    """-> Função para analisar notas e situações de vários alunos.
    :param num: uma um mais notas do aluno (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informacões sobre a situação do aluno."""
    dic = {}
    dic['Total'] = len(num)
    soma = 0
    maior = 0
    menor = 0
    cont = 0
    for i in num:
        if cont == 0:
            maior = i
            menor = i
        else:
            if i > maior:
                maior = i
            if i < menor:
                menor = i
        soma += num[cont]
        cont += 1
    dic['Maior'] = maior
    dic['Menor'] = menor
    med = soma/len(num)
    dic['Média'] = (f'{med:.2f}')
    if sit == True:
        if med >= 6:
            dic['Situação'] = 'Aprovado'
        else:
            dic['Situação'] = 'Reprovado'
    return dic



#teste: print(notas(3, 5, 1, 4, 2))