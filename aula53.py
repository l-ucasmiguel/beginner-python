"""
enumerate - enumera iteráveis (índices)
númera cada índice da sua lista
\t tab
"""


lista = ['Renato Augusto', 'Roger Guedes', 'Yuri Alberto']
lista.append('Giuliano')


# lista_enumerada = enumerate(lista)                                
# Geralmente quando o enumerate é usado, não vamos jogar ele em uma variável, como está acima, vamos usar ele direto, 
# porque desta forma ele não esgota.

# lista_enumerada = list(enumerate(lista, start=10))                             # Convertendo para lista e começando do 10 
# print(lista_enumerada)


# for item in enumerate(lista):                                                                
#   indice, nome = item                                                      
#    print(indice,nome) 


# Para cada valor ele separa o índice e o nome                                   # Mais simples
for indice, nome in enumerate(lista):                                            # Método que enumera os iteráveis                                                                        
    print(indice,nome)                                                           # Separando o índice e o nome em variáveis

