# senha_salva = '123456'
# senha_digitada = ''
# repetiçoes = 0 

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha {repetiçoes}x):')
    
#     repetiçoes += 1

# print(repetiçoes)
# print('Aquele laço acima poderia ter repetições infinitas')


#   FOR
texto = input('Digite uma palavra: ') # Iterável
novo_texto = ''

for letra in texto:                   # For pede que a gente crie um iterador, para realizar a iteração
    novo_texto += f'*{letra}'         # O Iterador te entrega um valor por vez, a gente que escolhe
    print(letra)                      # no caso é 'letra', a variável texto(iterável) tá pedindo o iterador
print('\n',novo_texto + '*')          # O iterável me entrega o objeto iterador, que não é a string