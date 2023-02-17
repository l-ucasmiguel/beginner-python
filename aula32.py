"""
Exercícios:

1) Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é ímpar ou par. Caso
o usúario não digite um número inteiro, informe que não é um número inteiro.
"""


# try:
#     num = int(input("Digite um número inteiro: "))
#     if num%2==0: 
#         print(f'O número {num} é par')
#     else :
#         print(f'O número {num} é ímpar')
# except:
#     print('O caractere digitado não é inteiro')


"""
2) "Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. 
Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


# hora = input('Digite a hora em números inteiros: ')

# try:
#     hora_int = int(hora)
#     if hora_int >= 0 and hora_int <= 11:
#         print('Bom dia')
#     elif hora_int >=12 and hora_int <= 17:
#         print('Boa tarde')
#     elif hora_int >=18 and hora_int <= 23:
#         print('Boa noite')
#     else:
#         print('Hora inválida')
# except:
#     print('Digite somente números inteiros')


"""
3) Faça um programa que peça o primeiro nome ao usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
Se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; Maior que 6 escreva "Seu nome é muito grande".
"""


nome = input('Digite seu nome: ')
nome_len = len(nome)

if nome_len >1 and nome_len <=4:
    print('Seu nome é pequeno')
elif nome_len >=5 and nome_len <=6:
    print('Seu nome é de tamanho médio')
elif len(nome) >=7:
    print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')