# Sistema de criptografia de dados 

import IntentificaNumero 
import random
letra = 5
pos = 0
teste = 're43'
cripta = ''
caracters =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


IntentificaNumero.junta(texto)
nomeArqui = input('Qual vai ser o nome do arquivo? ')
chave1 = input('Chave 1: ')
chave2 = input('Chave 2: ')
conte = input('Qual o quenteudo que você quer colocar? \n :').upper()

for i in conte:
    for conta in range(0, 5):
        if conta >= 4:
            pos = caracters.index(i)
            pos += 5 
            cripta += caracters[pos]
            print('i', i)
            print('Cripta', cripta)
            print('>', caracters[pos])
        else:
            cripta += random.choice(caracters)

nomeArqui += '.is'
arquivo = open(nome, 'w')

arquivo.write(cripta)
arquivo.close()