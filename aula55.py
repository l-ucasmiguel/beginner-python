"""
Imprecisão de ponto flutuante 
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal                # d minúsculo | Módulo

n1 = decimal.Decimal('0.1')   # Usando a classe "Decimal" dentro do módulo "decimal", Neste caso precisamos passar uma string     1º
n2 = decimal.Decimal('0.7')   # Geralmente é usado para números de pontos flutuantes muito grandes
n3 = n1 + n2 
print(n3)
print(f'{n3:.2f}')            # Arredondando com f'strings, escolhendo quantas casas decimais, aqui é retornado uma STRING        2º
print(round(n3,2))            # Arredondando com round, se depois da ',' for 0, não aparece, aqui é retornado em FLOAT            3º