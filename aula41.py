# While/Else

string = 'Valor-qualquer'

i = 0 
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1 
else:
    print('O else foi executado.')
print('Fora do while')

#Toda vez que tem um break, o else não é executado, quando segue até o final, o else é executado.