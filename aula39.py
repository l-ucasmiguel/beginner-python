"""
Iterando strings com while 
"""

#Indices string: -3, -2, -1, 0, 1, 2, 3
nome = input('Digite seu nome: ')       #Iteráveis
#      121110987654321- 

indice = 0 
novo_nome = ''
while indice < len(nome):               # enquanto indice 0 < quantidade de caracteres inserido pelo usuario
    letra = nome[indice]                # cria variavel letra que recebe variavel nome [indice]
    novo_nome += f'*{letra}'            # variavel novo_nome que estava vazia concatena '*' antes de cada letra
    indice +=1                          # contador pra chegar até o final da string 

novo_nome +='*'
print(novo_nome)