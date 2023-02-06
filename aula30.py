"""
Constante  = "Variáveis" que não vão mudar 
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

Não existe constante em python
Convenção usada 
Letras maiúsculas para variáveis que não vão mudar no código (constantes)
"""

velocidade = 61             # velocidade atual do carro
local_carro = 101           # km que o carro está na estrada 

RADAR_1 = 60                # velocidade máxima permitida pelo radar 1
LOCAL_1 = 100               # km onde está o radar 1 
RADAR_RANGE = 1             # alcance que o radar pega 


velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1


if velocidade_carro_passou_radar_1:
    print('O carro passou da velocidade do radar 01 ')

if carro_passou_radar_1:
    print('Carro passou pelo radar 01')

if carro_passou_radar_1 and velocidade_carro_passou_radar_1:
    print('Carro multado no Radar 01 ')