frase = 'aayy'                                   # \ é usado para quebrar a linha e continuar o código 

i = 0                                                   # indice/ contador                          
num_qtd_mais_vezes = 0                                  # aqui é criado uma variável para armazenar qtd_apareceu_mais_vezes
letra_mais_vezes = ''                                   # aqui é criado uma variável para armazenar a letra_apareceu_mais_vezes

while i < len(frase):                                   # enquanto i < quantidade total da frase
    letra_atual = frase[i]                              # cria uma nova variável que recebe a string e o indice atual 

    if letra_atual == ' ':                              # se a variável letra_atual for igual a um espaço vazio
        i += 1                                          # o indice recebe +1
        continue                                        # ignora e começa do topo

    qtd_atual_num = frase.count(letra_atual)            # é criado uma nova variável para receber frase.count
                                                        # count é um método pra contar quantas vezes X coisas apareceu na string 
    
    if  num_qtd_mais_vezes < qtd_atual_num:             # quando é colocado o '<=' no lugar de '<' é sempre usada a última letr se a qtd for =
        num_qtd_mais_vezes = qtd_atual_num              # aqui o qtd_apareceu_mais_vezes recebe a quantidade atual que tem mais caracteres 
        letra_mais_vezes = letra_atual                  # aqui a variável letra_apareceu_mais_vezes recebe a letra que apareceu mais vezes 
        
    i += 1
    
print(
     'A letra que apareceu mais vezes foi ' 
      f'"{letra_mais_vezes}" que apareceu '
      f'{num_qtd_mais_vezes}x'
)