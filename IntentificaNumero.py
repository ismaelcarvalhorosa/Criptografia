numeros=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
retorno=[]
junta=0

texto=input('Fale! :) ')

for pos, caracter in enumerate(texto):
    if caracter in numeros:
        retorno.append(caracter)
 
junta = ''.join(retorno)





'''
def validaNumero (texto):
    numeros=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lista=[]
    nStr = '' # string nesesaria para tranformar uma string em numero 
    n = 0

    for i in texto:
        if i in numeros:
            lista.append(i)
            junta = ''.join(lista)
            n = int(junta)
            #print('N:' n )
        else:
            print('.', i)
    return n 
'''