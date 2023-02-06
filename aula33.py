"""
https://docs.python.org/pt-br/3/library/stdtypes.html

Imutáveis que vimos até agora: str, int, float, bool 
"""

string = 'renato Augusto'
# outra_variavel = f'{string[:3]}ABC{string[4:]}'     # "Mudando string imutável"
# # string[3] = 'ABC'
# print(outra_variavel)
print(string.capitalize()) #Deixa a primeira letra maiúscula
print(string.zfill(50)) 