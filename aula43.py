# senha_salva = '123456'
# senha_digitada = ''
# repetiçoes = 0 

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha {repetiçoes}x):')
    
#     repetiçoes += 1

# print(repetiçoes)
# print('Aquele laço acima poderia ter repetições infinitas')


texto = 'Python'
novo_texto = ''
for letra in texto:         # For pede o iterável, a gente escolhe, no caso é 'letra'
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')