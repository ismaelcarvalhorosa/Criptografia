# Sistema de descriptografia 

import random
letra = 5
pos = 0
numero = 4
cripta = ''
caracters =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nome = input('Qual vai ser o nome do arquivo? ')
arquivo = open(nome, 'r')
conteudo = arquivo.read()
print(conteudo)

for n, i in enumerate(conteudo):
    if n == numero:
        #for conta in range(0, len(conteudo), 5):
        pos = caracters.index(i)
        pos -= 5 
        cripta += caracters[pos]
        print('i', i)
        print('pos', pos)
        print('>', caracters[pos])
        numero += 5

print('Tradução: ', cripta)
arquivo.close()