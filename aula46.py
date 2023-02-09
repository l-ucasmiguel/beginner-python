for i in range(10):                                 # i contador até 10
    if i == 2:
        print('i é 2, pulando...')                  # se o contador 1 for igual a 2, vai aparecer a msg e continuar
        continue
    if i == 8: 
        print('i é 8, seu else não executará')      # se o contador 1 for igual a 8, o else não vai ser executado
        break                                       # pq vai parar quando chegar em 8
    for j in range (1, 3):                          
        print(i,j)                                  # j contador de 1 a 3, n aparece último valor
else: 
    print('For completo com sucesso')