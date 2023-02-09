"""
Estrutura de repetição

while (enquanto)
Executa uma ação enquanto uma condição for True
Loop infinito -> quando o código não tem fim
"""

qtd_linhas = 5 
qtd_colunas = 5 

linha = 1 
while linha <= qtd_linhas:                         # enquanto linha <= qtd_linhas
    coluna = 1                                     # cria nova variavel chamda coluna com valor 1
    while coluna <= qtd_colunas:                   # cria novo laço de repetição coluna <= qtd_colunas
        print(f'{linha=}, {coluna=}')             
        coluna+=1
    linha += 1


print('\nAcabou')