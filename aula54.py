"""
Exercício
Faça uma lista de compra com listas, O usuário deve ter a possibilidade de inserir, apagar e listar valores 
da sua lista. Não permita que o programa quebre com erros de índices inexistentes na lista.
"""

import os 

lista = []
while True:
    print('Selecione uma opção:')
    menu = input('[i]nserir, [a]pagar, [l]istar: ')

    if menu == 'i':
        os.system('clear')
        lista_valor = input('Item a ser inserido: ')
        lista.append(lista_valor)
        

    elif menu == 'a':
        apagar_str = input('Escolha o índice para apagar: ')
        try:
            apagar = int(apagar_str)
            del lista[apagar]
        except ValueError:
            print('Por favor, digite um número inteiro')
        except IndexError:
            print('Digite um índice válido, índice inexistente')
        except Exception:
            print('Erro desconhecido')
        
    elif menu == 'l':
        os.system('clear')
        if lista == []:
            print('Lista vazia')
        for i, item in enumerate(lista):
            print(i,item)

    else:
        os.system('clear')
        print('Por favor, escolha [i]nserir, [a]pagar ou [l]istar')



