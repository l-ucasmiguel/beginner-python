"""
Formatação básica de strings com f-strings

s       - string
d       - int
f       - float
.       - <número de dígitos>f
x ou X  - Hexadecimal
(Caractere)(><^)(quantidade)
=       - Força o número a aparecer antes dos zeros 
>       - Esquerda
<       - Direita
^       - Centro
Sinal   - + ou - 
Ex.:0>-100,.1f
Conversion flags - !r !s !a     __repr__, __str__, __ascii__
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:>10}')                    # 10 casas pra direita
print(f'{variavel:<10}')                    # 10 casas pra esquerda
print(f'{variavel:^10}')                    # centro de 10 casas
print(f'{1000.4873648123746:0=+10.1f}')     
print(f'O hexadecimal de 1500 é {1500:08X}')