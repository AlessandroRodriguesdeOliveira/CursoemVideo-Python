perg = input('Digite a expressão:')
if not perg.count('(') == perg.count(')'):
    print('Sua expressão está errada!')
else:
    print('Sua expressão está certa.')