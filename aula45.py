"""
Iterável    -> str, range, etc / É um elemento que pode me entregar uma coisa por vez
            É um elemento que tem um método dentro dele chamado de (__iter__)

Iterador    -> quem sabe entregar um valor por vez  
next        -> me entregue o próximo valor 
iter        -> me entregue seu iterador 
"""
# Exemplo:
# nome = iter('Renato Augusto') #.__iter__()
# print(next(nome))             # print(nome.__next__())  

# for letra in texto 
texto = 'Renato Augusto'        #Iterável
# iterador = iter(texto)          #Iterador

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
