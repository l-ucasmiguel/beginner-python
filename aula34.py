"""
Estrutura de repetição

while (enquanto)
Executa uma ação enquanto uma condição for True
Loop infinito -> quando o código não tem fim
"""

condicao = True
while condicao:
    nome = input("Qual é o seu nome? ")
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break
    
print('Acabou')