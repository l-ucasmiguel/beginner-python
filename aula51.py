"""
Introdução ao desempacotamento
"""

# nomes = ['Renato Augusto', 'Roger Guedes', 'Yuri Alberto']
# nome1, nome2, nome3 = nomes                                              # Desempacotar listas, prestando atenção na quantidade 
# print(nome2)                                                             # Sempre a mesma qtd de valor e variável 

# or 

# var1, var2, var3 = ['Renato Augusto', 'Roger Guedes', 'Yuri Alberto']
# print(var2)



# Para pegar somente um item da lista sem dar erro, usar '*nomeDoRestante', desta forma pegamos o primeiro valor 
# e criamos uma variável para o resto da lista.
nome, *restante= ['Renato Augusto', 'Roger Guedes', 'Yuri Alberto']       
print(nome, restante)


# Para pegar o 2 ou 3 valor, usar '_,' e '_, _,' no começo, ex:
_, _,nome, *restante= ['Renato Augusto', 'Roger Guedes', 'Yuri Alberto']       
print(nome, restante)


# O '*_' indica que essa variável está ali mas não vai ser usada, resto aqui não importa
nome, *_= ['Renato Augusto', 'Roger Guedes', 'Yuri Alberto']       
print(nome, _)