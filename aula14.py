# Usando . após as aspas da string ''.
# Conseguimos acessar os métodos do objeto
# Uma das funções é o format()

a = 'AAA'
b = 'BBB'
c = 1.1

# PEGANDO POR POSIÇÃO

# string ='a={} b={} c={:.2f}'
# formato = string .format(a,b,c)

# PEGANDO POR ÍNDICES 
string = 'a={nome1} a={nome1} b={nome2} c={nome3:.2f}'   # nome3= PARÂMETRO NOMEADO
formato = string.format(nome1=a,nome2=b,nome3=c)         # Valor de C, é chamado de argumento 

# Tudo que vem após um parâmetro nomeado, precisa também estar nomeado, antes não tem problema 

print(formato)