"""
Listas em Python:

List é do tipo Mutável          []
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - índices e fatiamento 
Métodos úteis: 
    append - adiciona um item ao final
    insert - adiciona um item no índice escolhido
    pop    - remove do final ou do índice escolhido 
    del    - apaga um índice 
    clear  - limpa a lista 
    extend - estende a lista 
    +      - concatena listas 
create, read, update, delete 
criar, ler, alterar, deletar = lista [i] CRUD
"""


#  +01234                                                                                   # Acessar indices ex: [2]
#  -54321


# string = 'ABCDE'                                                                          # 5 caracteres (len)
# lista = []
# print(bool(lista))                                                                        # List vazio é False


# lista = [123, True, 'Roger', 1.2, ['Renato Augusto',8]]                                   # Suporta valores de qualquer tipo 
# lista[2] = 'GUEDES'
# print(lista)                                                                              # Alterando valor da lista
# print(lista[2], type(lista[2]))


lista = [10, 20, 30, 40]
# lista[2] = 300                                                                            # Alternando valor da lista
# del lista[2]                                                                              # Apagando valor da lista e reorganiza
# print(lista)
# print(lista[2])


# lista.append(50)                                                                          # Acrescenta algo no final
# lista.pop()                                                                               # Pop remove o último índice no momento
# ultimo_valor = lista.pop()
# print('Removido', ultimo_valor)
# lista.pop(1)                                                                              # Removendo por índices com Pop
# lista.append(60)                                                                              


# lista.append('Roger Guedes')
# nome = lista.pop()                                                                        # Removendo último indice
# lista.append(123)
# del lista [-1]                                                                            # Removendo último com índice invertido 
# lista.clear()                                                                             # Limpar a lista


# lista.insert(0, 'Renato Augusto')                                                         # Insert insere um valor em um índice específico.
                                                                                            # 1 é a posição do índice, 2 é o valor a ser passado
# print(f'{lista}')

# lista_a = [1,2,3]
# lista_b = [4,5,6]
# lista_c = lista_a + lista_b                                                                # + é usado para concatenar listas
# lista_d = lista_a.extend(lista_b)                                                          # Estende uma lista a outra no próprio objeto
#                                                                                            # Não retorna valor

# print(lista_a)


"""
Cuidados com dados mutáveis: 
= Quando é imútável copia-se o valor                    (imutáveis)  Strings
= Quando é mutável aponta para o mesmo valor na memória  (mutável)    Listas
"""

# nome = 'Roger'
# outra_variavel = nome
# nome = 'Renato'
# print(nome)
# print(outra_variavel)

lista_a = ['Roger Guedes', 'Renato Augusto']
lista_b = lista_a.copy()                                                                     # Método para copiar listas

lista_a[0] = "qualquer coisa"
print(lista_b)