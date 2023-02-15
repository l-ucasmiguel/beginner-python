"""
Iterável    -> str, range, etc / É um elemento que pode me entregar uma coisa por vez
               É um elemento que tem um método dentro dele chamado de (__iter__)
Iterador    -> quem sabe entregar um valor por vez  
next        -> me entregue o próximo valor 
iter        -> me entregue seu iterador 
"""


###########################################################################################################################


"""
texto = iter('Renato')                # é =  .__iter__()                 Isso acontece automaticamente, por baixo dos panos 
print(next(texto))                    # é =  .print(nome.__next__())
""" 


###########################################################################################################################


# for letra in texto
texto = 'Renato'                        #Iterável
iterador = iter(texto)                  #Iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
#OR
"""
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
"""


###########################################################################################################################

print('\n')
for letra in texto:
    print(letra)