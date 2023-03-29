"""
Calculo do primeiro dígito do CPF 

CPF: 746.824.890-70

Multiplique cada um dos valores por uma contagem regressiva começando de 10
Colete a soma dos 9 primeiros dígitos do CPF                              

Ex: 746.824.890-70 (746824890)

    10  9   8   7   6   5   4   3   2
*   7   4   6   8   2   4   8   9   0                                               MULTIPLICANDO
   70  36  48  56  12  20  32  27   0                                               COLETANDO OS VALORES

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301                                                     SOMANDO OS VALORES COLETADOS 

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

cpf = '74682489070'
nove_digitos = cpf[:9]                                                              # Fatiando a string do 0 ao 9 dígito | último dígito ñ aparece
contador_regressivo_1 = 10                                                          # Contador

resultado_digito_1 = 0
for i in nove_digitos:                                                              # ler 'for' como 'para'
    resultado_digito_1 += int(i) * contador_regressivo_1                            # converter o 'i' para (int)
    contador_regressivo_1 -= 1

digito_1 = ((resultado_digito_1 *10) %11)

digito_1 = digito_1 if digito_1 <= 9 else 0                                         # se digito_1 for <= 9,recebe digito_1, se não recebe 0
print(digito_1)


"""
1- 'i' percorre os 'nove_digitos'
2- 'resultado_digito_1' recebe e soma 'i' (que é o valor atual de 'nove_digitos') e múltiplicado pelo 'contador_regressivo_1'
3- 'contador_regressivo_1' vai diminuindo 
"""