"""
Calculo do segundo dígito do CPF

CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DIGITO, multiplicando cada um dos valores por uma contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363

Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""




# CALCULANDO O 1º DÍGITO: 

cpf_enviado_usuario = '74682489070'
nove_digitos = cpf_enviado_usuario[:9]                                              # Fatiando a string do 0 ao 9 dígito | último dígito ñ aparece
contador_regressivo_1 = 10                                                          # Contador


resultado_digito_1 = 0
for i in nove_digitos:                                                              # ler 'for' como 'para'
    resultado_digito_1 +=(int(i) * contador_regressivo_1)                           # converter o 'i' para (int)
    contador_regressivo_1 -= 1
digito_1 = ((resultado_digito_1 *10) %11)

digito_1 = digito_1 if digito_1 <= 9 else 0                                         # se digito_1 for <= 9,recebe digito_1, se não recebe 0
print(digito_1)
print(150 * '-')

"""
1- 'i' percorre os 'nove_digitos'
2- 'resultado_digito_1' recebe e soma 'i' (que é o valor atual de 'nove_digitos') e múltiplicado pelo 'contador_regressivo_1'
3- 'contador_regressivo_1' vai diminuindo 
"""




# CALCULANDO O 2º DÍGITO: 

dez_digitos = nove_digitos + str(digito_1)                                          # aproveitando a nove_digitos anterior e concatenando com digito_1
contador_regressivo_2 = 11

resultado_digito_2 = 0
for j in dez_digitos:
    resultado_digito_2 += (int(j) * contador_regressivo_2)
    contador_regressivo_2 -= 1
digito_2 = ((resultado_digito_2 * 10) %11) 

digito_2 = digito_2 if digito_2 <= 9 else 0                                         # se digito_2 for <= 9,recebe digito_2, se não recebe 0
print(digito_2)

"""
1- 'j' percorre os 'dez_digitos'
2- 'resultado_digito_2' recebe e soma 'i' (que é o valor atual de 'dez_digitos') e múltiplicado pelo 'contador_regressivo_1'
3- 'contador_regressivo_2' vai diminuindo 
"""

####################################################################################

cpf_gerado_calculo = f'{nove_digitos}{digito_1}{digito_2}'
print(150 * '-')

if cpf_enviado_usuario == cpf_gerado_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF Inválido')
