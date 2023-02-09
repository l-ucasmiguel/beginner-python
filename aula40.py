# Calculadora com while

while True:
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    operador = input('Digite o operador [+-/*]: ')

    num_validos = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        num_validos = True
    except:
        num_validos = None
    
    if num_validos is None:
        print('Um ou ambos números são inválidos')
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) >1:
        print('Digite apenas um operador')
        continue
    print('Realizando a sua conta, confira o resultado abaixo: ')
    if operador == '+':
        print(f'{n1_float} + {n2_float}  = ', n1_float+n2_float)
    elif operador == '-':
        print(f'{n1_float} - {n2_float}  = ', n1_float-n2_float)
    elif operador == '/':
        print(f'{n1_float} / {n2_float}  = ', n1_float/n2_float)
    elif operador == '*':
        print(f'{n1_float} * {n2_float}  = ', n1_float*n2_float)
    else:
        print('Nunca deveria chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    # lower -> Retorna a mesma string em minúsculo/ startswith-> Verifica se começa coma letra inserida 

    if sair is True:
        break