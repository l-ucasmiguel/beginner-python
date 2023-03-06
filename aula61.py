"""
Calculo do primeiro dígito do CPF 

CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF                                        SOMA = 48
Multiplicando cada um dos valores por uma contagem regressiva começando de 10      

Ex: 746.824.890-70 (746824890)

    10  9   8   7   6   5   4   3   2
*   7   4   6   8   2   4   8   9   0                                               MULTIPLICANDO
   70  36  48  56  12  20  32  27   0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10
301*10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9: 
    o resultado é 0 
contrário disso
    resultado é o valor da conta

    
O primeiro dígito do CPF é 7
"""


# CALCULANDO O 1º DÍGITO: 

cpf_enviado_usuario = '74682489070'
nove_digitos = cpf_enviado_usuario[:9]                                                          # Fatiando a string do 0 ao 9 dígito
contador_regressivo_1 = 10                                                      


resultado_digito_1 = 0
for i in nove_digitos:                                                    
    resultado_digito_1 +=(int(i) * contador_regressivo_1)                 
    contador_regressivo_1 -= 1
digito_1 = ((resultado_digito_1 *10) %11)

digito_1 = digito_1 if digito_1 <= 9 else 0 
print(digito_1)

"""
1- 'i' percorre os 'nove_digitos'
2- 'resultado_digito_1' recebe e soma 'digito' (que é o dígito atual de 'nove_digitos') e múltiplica pelo 'contador_regressivo_1'
3- 'contador_regressivo_1' vai diminuindo 
"""

print(170 * '-')

# CALCULANDO O 2º DÍGITO: 

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for j in dez_digitos:
    resultado_digito_2 += (int(j) * contador_regressivo_2)
    contador_regressivo_2 -= 1
digito_2 = ((resultado_digito_2 * 10) %11) 

digito_2 = digito_2 if digito_2 <= 9 else 0 
print(digito_2)

####################################################################################

cpf_gerado_calculo = f'{nove_digitos}{digito_1}{digito_2}'
print(170 * '-')

if cpf_enviado_usuario == cpf_gerado_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF Inválido')