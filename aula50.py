"""
Exercício
Exiba os índices da lista 
"""

lista = ['Renato Augusto', 'Roger Guedes', 'Yuri Alberto']
lista.append('Giuliano')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])