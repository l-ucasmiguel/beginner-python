"""
Exercício:

1- Peça ao usuário para digitar o seu nome
2- Peça ao usuário para digitar sua idade 
3- Se o nome e a idade forem digitados:
4- Exiba: 
        Seu nome é {nome}
        Seu nome invertido é {nome-invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba:
        Desculpe, você deixou campos vazios.
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
print (60*'-')

if nome and idade:
    print(f'{nome}')                                        #nome
    print(nome[::-1])                                       #nome ao contrário                                         

    if ' ' in nome:                                         #se tem espaço ou não
        print('Seu nome contem espaço')
    else:
        print('Seu nome não contem espaço')

    print(f'Seu nome tem {len(nome)} letras')               #quantidade de caracteres, espaço é contado como caractere 
    print(f'A primeira letra do seu nome é {nome[0:1]}')    #primeira letra
    print(f'A última letra do seu nome é {nome[-1:]}')      #última letra
elif not nome or not idade:
      print('Desculpe, você deixou campos vazios.')

