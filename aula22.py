# Operadores Lógicos
#        OR

# Qualquer condição verdadeira torna toda a expressão verdadeira
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada como verdadeira.


entrada = input(' Para entrar pressione [E]:  \n Para sair pressione   [S]: \n ')
senha_digitada = input(' Senha: ')
senha_permitida = '123456'

# if condição
# 
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print(' Entrar')
else:
    print(' Sair')