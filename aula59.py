"""
Desempacotamento em chamadas 
de métodos e funções 
"""

string = 'ABC'
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0,        1 
    ['Maria', 'Helena'],                #0

    # 0     
    ['Elaine'],                         #1

    # 0,     1,      2
    ['Luiz','João','Eduarda']           #2
]

# p,s,*_,ap, u = lista                             # O que fica depois de '*_' é o último item
# print(p,s,ap,u)                                  # Cada variável criada na linha acima, vira um item da lista 


# for nome in lista:                               # Aqui o 'for' percorre cada item da lista 
#     print(nome, end=' ')                         # E o 'end' está separando por espaço 


# print(*lista)                                    # Passa sobre cada um dos itens da lista  | * = all 
# print(*string)
# print(*tupla)


print(*salas, sep='\n')



"""
'sep' e 'end' são parâmetros opcionais que podem ser passados para a função print() em Python.

sep é usado para definir o separador entre os valores que serão impressos. Por padrão, o separador é um espaço em branco. Por exemplo, o código
print("a", "b", "c") produzirá a saída "a b c". Se quisermos usar outro separador, podemos passá-lo como argumento para sep. 
Por exemplo, print("a", "b", "c", sep="-") produzirá a saída "a-b-c".

end é usado para definir o caractere que será adicionado ao final da saída impressa. Por padrão, end é uma nova linha ("\n"). Por exemplo, o código
print("hello") produzirá a saída "hello\n". Se quisermos usar outro caractere final, podemos passá-lo como argumento para end. 
Por exemplo, print("hello", end="!") produzirá a saída "hello!".
"""