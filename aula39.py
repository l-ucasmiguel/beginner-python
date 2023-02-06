"""
Iterando strings com while 
"""

#Indices string: -3, -2, -1, 0, 1, 2, 3
nome = input('Digite seu nome: ')     #Iteráveis
#      121110987654321 

indice = 0 
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice +=1

novo_nome +='*'
print(novo_nome)