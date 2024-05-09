
from utilidadesCeV.moeda import resumo

def leiadinheiro(num):
        e = input(num)
        b = e.split()
        c = "".join(b)
        a = c
        while a.strip() == '' or a.strip().isalpha() == True or a.isalnum()==True:
            print(f'\033[1;31mERRO: "{a}" é um preço inválido\033[m')
            a = (input(num))
        if a.find(',') != -1:
            a = a.replace(',','.')
        a = float(a)
        return a

p = leiadinheiro('Digite um preço: ')
resumo(p,35, 22)