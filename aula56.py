"""
SPLIT E JOIN COM LIST E STRING 

split - Divide uma string | Se no split não for passado nenhum parâmetro, ele cria uma lista com separação 
a cada espaço, o caractere que for passado dentro como parâmetro vai ser usado na quebra em tal ponto. 

join  - une uma string 

strip, rstrip e lstrip - corta os espaços, da direita, da esquerda, ou dos dois.
"""




# Split

frase = '    Olha só que   , coisa interessante     '                         # É criado uma string.
lista_frases = frase.split(',')                                               # Aqui a string é dividida em 2 usando ',' como separador.

lista_frases_certa = []                                                       # É criado uma variável vazia do tipo list, que será usada para armazenar a frase correta

for i, frase in enumerate(lista_frases):                                      # Aqui iniciamos um 'for' que usa a função 'enumerate' para obter o índice 'i' e o 
    lista_frases_certa.append(lista_frases[i].strip())                        # valor 'frase' de cada elemento da 'lista_frases', que no caso está dividido em 2 


# Dentro do loop for, adiciona a string atual, sem espaços em branco no início e no final, à lista lista_frases_certa usando o método strip() da classe string. 
# 1º Ele vai pegar o 'i' 0 de 'lista_frases', que depois de dividido usando spli(',') é 'olha só que'
# 2º Ele vai pegar o 'i' 1 de 'lista_frases', que depois de dividido usando spli(',') é 'coisa interessante'
# É importante que você não altere os valores de um valor direto, porque pode ser que no futuro você queria voltar nos valores originais 

# print(lista_frases_certa)




# Join

frases_join = ' # '.join(lista_frases_certa)           # Com 'Join' primeiro temos que passar o separador a ser usado entre ' ', e depois a string ou lista a ser unida 

print(frases_join)
