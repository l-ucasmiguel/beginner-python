"""
Fatiamento de strings
Ex:
 012345678
 Olá mundo 
-987654321

Fatiamento [i:f:p] [::]     Início-fim-passo, o passo é de quantos em quantos caracteres vão ser pulados 
Obs: A função (len) retorna a quantidade de caracteres da string 

: indica o fatiamento

Contagem de caracteres com a função (len), é diferente de posições com índice 
"""

variavel = 'Olá mundo'
# print(variavel[1:])         # Se a intenção for de ir até o final, tem que omitir o final
# print(variavel[:8])         # Podemos também omitir o começo 
# print(len(variavel[0:]))    # Len retorna a quantidade de caracteres da string
print(variavel[0:9:1])
print(variavel[::-1])         # de 0 a 9 ao contrário 
print(variavel[-1:-10:-1])    # de 0 a 9 ao contrário 
