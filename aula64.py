# GERADOR DE CPF 

import random                                                                   # Importando o módulo random que é uma biblioteca 
                                                                                # Que gera números aleatórios

for j in range (2):                                                             # Percorre/Repete tudo 2x, gerando 2 CPF'S 
    nove_digitos = ''                                                           # Cria variável 'nove_digitos' vazia 
    for i in range(9):                                                          # o 'i' percorre o range '0' a '8' o que gera 9 digitos
        nove_digitos += str(random.randint(0,9))                                # a variável 'nove_digitos' que estava vazia é concatenada com 
                                                                                # o número gerado pelo módulo random

    contador_regressivo_1 = 10
    resultado_digito_1 = 0
    for i in nove_digitos:                                                      # 'i' percorre a variável 'nove_digitos'
        resultado_digito_1 +=(int(i) * contador_regressivo_1)                   # a variável 'resultado_digito_1' é concatenada com o 'i' atual e * pelo 'contador_regressivo_1'
        contador_regressivo_1 -= 1                                              # contador_regressivo -1 se repete até chegar a 0

    digito_1 = ((resultado_digito_1 *10) %11)
    digito_1 = digito_1 if digito_1 <= 9 else 0                                 # se digito_1 for <= 9,recebe digito_1, se não recebe 0

    dez_digitos = nove_digitos + str(digito_1)                                  # 'dez_digitos' recebe 'nove_digitos' concatenado com 'digito_1'

    contador_regressivo_2 = 11
    resultado_digito_2 = 0
    for j in dez_digitos:                                                       # 'j' percorre a variavel 'dez_digitos'
        resultado_digito_2 += (int(j) * contador_regressivo_2)                  # a variável 'resultado_digito_2' é concatenada com o 'j' atual e * pelo 'contador_regressivo_2'
        contador_regressivo_2 -= 1                                              # contador_regressivo -1 se repete até chegar a 0

    digito_2 = ((resultado_digito_2 * 10) % 11) 
    digito_2 = digito_2 if digito_2 <= 9 else 0                                 # se digito_2 for <= 9,recebe digito_2, se não recebe 0

    cpf_gerado_calculo = f'{nove_digitos}{digito_1}{digito_2}'                  # 'cpf_gerado_calculo' recebe 'nove_digitos' concatenada com 'digito_1' e 'digito_2'
    print(cpf_gerado_calculo)














"""
O comando range em Python começa por padrão no número 0.

Se você usar a função range(n), ela irá gerar uma sequência de números inteiros de 0 até n-1.

Por exemplo, range(5) gera a sequência [0, 1, 2, 3, 4].

No entanto, você também pode especificar um valor inicial diferente para a sequência. Se você usar a função range(start, stop), ela irá gerar uma 
sequência de números inteiros começando em "start" e indo até "stop-1".

Por exemplo, range(1, 6) gera a sequência [1, 2, 3, 4, 5].

Também é possível especificar um valor de passo para a sequência, usando a função range(start, stop, step). Neste caso, o valor padrão do início da 
sequência é 0, mas você pode especificá-lo se quiser começar em um valor diferente.

"""