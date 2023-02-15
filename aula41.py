# While/Else

string = 'Valor-qualquer'

i = 0                                   # índice/ contador
while i < len(string):                  # enquanto indice for < que o tamanho da string
    letra = string[i]                   # cria uma nova variável e recebe string +indice atual

    if letra == ' ':                    # se tiver algum espaço BREAK
        break

    print(letra)                        # se não tiver e o laço continuar, escreva a variável letra na tela
    i += 1                              # como a variável letra recebe um caractere por vez, cada vez vai aparecer uma 
                                        # letra diferente, o i+=1 é para sempre passar pra próxima, até o final

else:
    print('O else foi executado.')
print('Fora do while')



#Toda vez que tem um break, o else não é executado, quando segue até o final, o else é executado.