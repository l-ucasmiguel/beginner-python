"""
Tipo tuples - Uma lista imutável 
"""

nomes = 'Renato Augusto', 'Roger Guedes', 'Yuri Alberto'                # Para criar uma tupla, é só não colocar os colchetes ou usar ()
print(nomes)                                                         # Tuplas são mais eficientes do que listas 


# Convertendo listas para tuples
nomes2 = ['Cassio', 'Fabio Santos', 'Fagner']
nomes2 = tuple(nomes2)
print(nomes2)

# Convertendo tuples para listas
nomes3 = 'Du Queiroz', 'Roni', 'Giuliano'
nomes3 = list(nomes3)
print(nomes3)

