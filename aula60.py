"""
Operação ternária (condição de uma linha)
<valor> if <condicao> else <outro valor>
"""

# variavel = 'Valor' if False else 'Outro valor'          # variavel recebe 'valor' se for verdadeira, se for falsa recebe 'outro valor'
# print(variavel)


# digito = int(input('Digite um dígito: '))
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

print('TESTE 01' if True else 'TESTE 02' if True else 'TESTE 03')       # Não recomendado 
# Se a 1º condição for verdadeira, o print vai mostrar o 'TESTE 01'
# Se a 1º condição for falsa, e a 2º verdadeira o print vai mostrar o 'TESTE 02'
# Se a 1º condição for falsa, e a 2º falsa o print vai mostrar o 'TESTE 03'