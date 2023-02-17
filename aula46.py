for i in range(10):                                 # i contador até 10
    if i == 2:
        print('i é 2, pulando...')                  # se o contador 'i' for igual a 2, vai aparecer a msg e continuar
        continue
    if i == 8: 
        print('i é 8, seu else não executará')      # se o contador 'i' for igual a 8, o else não vai ser executado
        break                                      
    for j in range (1, 3):                          # 'j' contador de 1 a 3, não aparece último valor Ex: (1,2)
        print(i,j)                                  # 'i' começa em '0' e 'j' começa em '1'
else:   
    print('For completo com sucesso')