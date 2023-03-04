# Lista dentro de listas e seus índices
# Ou tuplas dentro de listas, e vice-versa 
# [] - List     - Mutáveis
# () - Tuples   - Imutáveis

salas = [
    # 0,        1 
    ['Maria', 'Helena'],              #0

    # 0     
    ['Elaine'],                     #1

    # 0,     1,      2
    ['Luiz','João','Eduarda']       #2
]

# print(salas[0][1])                  # Acessando o índice da lista, e o índice interno da lista 
# print(salas[1][1][2])
# print(salas[2][2])

for sala in salas:                  # Sempre depois do for é criado uma variável para percorrer a variável depois do 'in'
    print(f'A sala é: {sala}')
    for i in sala:
        print(i)