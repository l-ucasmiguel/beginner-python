# Operadores Lógicos
#       AND

# Quando utilizamos o (AND) todas as condições precisam ser verdadeiras 
# Se qualquer valor for considerado falso, a expressão inteira será falsa
# São considerados False 

# Também existe o tipo (NONE) que é usado para representar um valor nulo


entrada = input(' Para entrar pressione [E]:  \n Para sair pressione   [S]: \n ')
senha_digitada = input(' Senha: ')
senha_permitida = '123456'

# if condição
# só vai ser executado quando a expressão for True
if entrada == 'E' and senha_digitada == senha_permitida:
    print(' Entrar')
else:
    print(' Sair')