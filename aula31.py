"""
Flag            - Marcar um local, bandeira.
None            - Não valor 
is  e is not    - É ou não é (tipo, valor, identidade)
id              - Identidade 
"""

# v1 = 'a'
# v2 = 'a'
# print(id(v1))
# print(id(v2))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else: 
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')