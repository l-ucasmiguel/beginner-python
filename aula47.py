"""
Faça um jogo para  o usuário adivinhar qual é a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário
digitar apenas uma letra.
- Quando o usuário digitar uma letra você vai conferir se a letra digitada está na 
palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra; 
    - Se a letra digitada não estiver na palavra secreta; exiba '*'.
Faça a contagem de tentativas do seu usúario.

FOR     =   PARA
WHILE   =   ENQUANTO
"""

import os

palavra_secreta = 'tomate'                     
letras_acertadas = ''
tentativas = 0                              

while True:
    letra_digitada = input('Digite uma letra: ')    # Digitar caractere 
    tentativas += 1

    if len(letra_digitada) > 1:                     # Se for digitado mais do que 01 caractere, 
        print('Digite apenas uma letra.')           # Aparece esse aviso e volta no primeiro laço
        continue

    if letra_digitada in palavra_secreta:           # Se a letra digitada estiver na palavra secreta 
        letras_acertadas += letra_digitada          # letras acertadas recebe o letra digitada 
    
    palavra_formada = ''                            # cria variável palavra formada vazio
    
    for letra_secreta in palavra_secreta:           # for vai percorrer toda palavra secreta com o letra secreta
        if letra_secreta in letras_acertadas:       # se alguma letra secreta estiver em letra acertadas
            palavra_formada += letra_secreta        # a palavra formada recebe o letra secreta 
        else:
            palavra_formada += '*'                  # caso não tenha uma letra que esteja, exiba '*'

    print('Palavra formada: ', palavra_formada)     

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print("\nVOCÊ GANHOU, PARABÉNS!")
        print('A palavra era', palavra_secreta)
        print('Tentativas:', tentativas)
        break

        
