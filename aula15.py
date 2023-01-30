# Coletar dados do usuário

# nome = input('Qual é o seu nome? ')
# print(f'O seu nome é {nome=}')

n1 = input('Digite sua primeira nota: ')
n2 = input('Digite sua segunda nota: ')
n3 = (float(n1)+float(n2))/2
print(f'Sua média é: {n3:.2f}')
# print(f'Sua média é: {(int(n1)+int(n2))/2}')

if n3 >=5 :
    print('VOCÊ FOI APROVADO')
else:
    print('VOCÊ FOI REPROVADO')
