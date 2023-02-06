"""
Introdução ao try/except

try -> tentar executar o código
except -> ocorreu um erro ao tentar executar 
"""

numero = input('Vou dobrar o número que você digitar: ')

try:
    print(f'String {numero}')                                   #String
    numero_float = float(numero)                                #convertendo p float
    print(f'Float {numero_float}')                              #float
    print(f'O dobro de {numero} é {numero_float*2:.2f}')        #execução 
except:
    print('Isso não é um número')



# if numero.isdigit():                    #isdigit verifica se os dígitos são apenas números 
#     numero_float = float(numero)
#     print(f'O dobro de {numero} é {numero_float*2:.2f}')
# else:
#     print('Isso não é um número')