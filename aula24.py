# Operadores IN e NOT IN
# Strings são iteráveis
# 0 1 2 3 4 5 
# R e n a t o 
# -6-5-4-3-2-1
# Acessando string pelo índice 

nome = 'Renato'
# print(nome[0])
# print(nome[1])
# print(nome[2])
# print(nome[3])
# print(nome[4])
# print(nome[5])
# print(nome[-1])

# print('a' in nome)      # True 
# print(10*'-')
# print('a' not in nome)  # False

nome = input('Digite o seu nome: ')
encontrar = input('Digite a letra que você deseja encontrar em seu nome: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

