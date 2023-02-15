# Calculadora com while

while True:                                            #Enquanto condição for true
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    operador = input('Digite o operador [+-/*]: ')

    num_validos = None                                 # está variável recebe valor nulo
    n1_float = 0                                       # criando variável n1 do tipo float 
    n2_float = 0                                       # criando variável n2 do tipo float 

    try:                                               # Tentar
        n2_float = float(n2)                           # "  convertendo string p/ float
        n1_float = float(n1)                           # "  se o valor inserido for convertido p/ string num_vali TRUE
        num_validos = True                             # num_validos deixa de ser nulo e se torna true 
    except:
        num_validos = None                             # exceto se os números forem nulos
    
    if num_validos is None:
        print('Um ou ambos números são inválidos')     # se num_validos for none, o programa não seguirá e vai repetir
        continue                                       # por causa do continue, ignora e recomeça

    operadores_permitidos = '+-/*'                     # define caracteres aceitaveis 
    if operador not in operadores_permitidos:          # se o que foi inserido em operador, nao for o mesmo do oper_permi
        print('Operador inválido')                     # operação inválida, por causa do continue, ignora e recomeça
        continue

    if len(operador) >1:                               # Se for inserido mais de um operador, ignora e recomeça
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
    # lower       ->  Retorna a mesma string em minúsculo
    # startswith  ->  Verifica se começa coma letra inserida e retorna um valor bool

    if sair is True:    # se sair começar com 's' BREAK
        break