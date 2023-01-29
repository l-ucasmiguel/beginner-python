# FORMATAÇÃO DE STRING
# INTRODUÇÃO f-strings

# Formatação de casas decimais :.2f = número é a quantidade de casas aṕos o ponto
# Ou :,.2f, exemplo de formatação neste caso 100050.4 vira 100,050.40

nome = 'Renato Augusto'
altura = 1.85
peso = 85.00
imc = peso/(altura**2)

linha_1 =  f'O {nome} tem {altura} de altura e pesa {peso} quilos seu imc é {imc:.2f}'

print(linha_1)




# IMC = PESO / (ALTURA X ALTURA)

# Renato Augusto tem 1.85 de altura 
# Pesa 1.85 quilos e seu imc é 
# 29.320987654320987

# ... se chama Ellipsis, é um placeholder 